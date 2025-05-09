import asyncio
import io
import logging
import re
from typing import NamedTuple

from docutils.core import publish_parts
from pyscript import document, fetch

import js

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger("lesson_page")


# ===== Global State =====
_current_lesson_id: str | None = None
_preloaded_lesson_cache: dict[str, "Lesson"] = {}


# ===== Logic =====


def render_rst(rst: str) -> str:
    if not rst.strip():
        return ""

    error_stream = io.StringIO()  # To catch any stray messages
    settings_overrides = {
        "warning_stream": error_stream,
        "traceback": True,
    }
    try:
        parts = publish_parts(
            source=rst, writer_name="html5", settings_overrides=settings_overrides
        )
    except Exception as e:
        return (
            "<pre style='color: red;'>"
            f"Error rendering reStructuredText:\n{str(e)}</pre>"
        )

    return parts["html_body"]


class Lesson(NamedTuple):
    main_chapter: str
    description: str
    interactive: str
    next_lesson_id: str | None


_chapter_pattern = re.compile(r"^\.\.\s*\n\s*_Chapter:\s*(.*)", re.MULTILINE)
_next_pattern = re.compile(r"^\.\.\s*\n\s*_Next:\s*(.*)", re.MULTILINE)


def parse_lesson(rst: str) -> Lesson | None:
    example_delimiter = "# Lesson Example"

    chapter_match = _chapter_pattern.search(rst)
    if not chapter_match or example_delimiter not in rst:
        return None
    chapter_title_from_meta = chapter_match.group(1).strip()
    next_lesson_id_from_meta = None
    if next_match := _next_pattern.search(rst):
        if extracted_next_id := next_match.group(1).strip():
            next_lesson_id_from_meta = extracted_next_id

    parts = rst.split(example_delimiter, 1)
    return Lesson(
        main_chapter=chapter_title_from_meta,
        description=parts[0].strip(),
        interactive=parts[1].strip(),
        next_lesson_id=next_lesson_id_from_meta,
    )


async def load_text_file(url_path: str) -> str | None:
    """
    Asynchronously loads a text file from the given URL path.
    Returns the file content as a string, or an error message if fetching fails.
    """
    try:
        response = await fetch(url_path)
        if response.ok:
            return await response.text()
        else:
            logger.warning(
                "Error: Could not load file %s. Status: %s", url_path, response.status
            )
            return None
    except Exception as e:
        logger.warning("Error: Exception while fetching %s. %s", url_path, str(e))
        return None


async def fetch_and_parse_lesson(lesson_id: str) -> Lesson | None:
    """Fetches, parses, and returns a lesson by its ID."""
    file_path = f"/l/{lesson_id}.rst"
    full_rst_content = await load_text_file(file_path)
    if not full_rst_content:
        logger.warning(
            f"Failed to fetch content for lesson {lesson_id} from {file_path}"
        )
        return None
    lesson_data = parse_lesson(full_rst_content)
    if not lesson_data:
        logger.warning(f"Failed to parse content for lesson {lesson_id}")
        return None
    return lesson_data


async def preload_lesson(lesson_id: str) -> None:
    """Preloads a lesson and stores it in the cache if successful."""
    if not lesson_id or lesson_id in _preloaded_lesson_cache:
        return  # No ID or already preloaded/being preloaded

    logger.info(f"Attempting to preload lesson: {lesson_id}")
    lesson_data = await fetch_and_parse_lesson(lesson_id)
    if lesson_data:
        _preloaded_lesson_cache[lesson_id] = lesson_data
        logger.info(f"Successfully preloaded lesson: {lesson_id}")
    else:
        logger.warning(f"Failed to preload lesson: {lesson_id}")
        # If preload fails, button click will fallback to standard navigation.


# ===== UI =====


def render_rst_on_input(event=None):
    """
    Renders reStructuredText from the input textarea to the output div.
    Called on every input event in the textarea.
    Manages a list of recent docutils errors and displays up to MAX_ERRORS_TO_DISPLAY.
    """
    input_element = document.querySelector("#rst-input")
    rst_text = input_element.value
    output_div = document.querySelector("#rst-output")
    output_div.innerHTML = render_rst(rst_text)


async def handle_next_lesson_click(event) -> None:
    """Handles clicks on the 'Next Lesson' button for client-side navigation."""
    event.preventDefault()
    next_button_href = event.target.href

    # Extract lesson_id from the button's href
    try:
        url_object = js.URL.new(next_button_href, js.window.location.origin)
        params = js.URLSearchParams.new(url_object.search)
        next_lesson_id = params.get("id")
    except Exception as e:
        logger.error(f"Error parsing next lesson URL '{next_button_href}': {e}")
        js.window.location.href = next_button_href  # Fallback
        return

    if not next_lesson_id:
        logger.warning(
            "Next lesson ID not found in href, falling back to full navigation."
        )
        js.window.location.href = next_button_href  # Fallback
        return

    if next_lesson_id in _preloaded_lesson_cache:
        logger.info(f"Rendering preloaded lesson: {next_lesson_id}")
        await set_current_lesson(next_lesson_id, push_to_history=True)
    else:
        logger.info(
            "Next lesson %s not preloaded. Falling back to full navigation.",
            next_lesson_id,
        )
        # Fallback to full page navigation
        js.window.location.href = next_button_href


def display_lesson(lesson_data: Lesson, lesson_id: str) -> None:
    """Updates the DOM to display the given lesson."""
    lesson_div = document.querySelector("#lesson-content-area")
    rst_input_element = document.querySelector("#rst-input")
    page_main_title_element = document.querySelector("#page-main-title")
    next_button_element = document.querySelector("#next-lesson-button")
    toc_button_element = document.querySelector("#toc-button")

    page_main_title_element.textContent = lesson_data.main_chapter
    toc_button_element.href = "/index.html"  # Ensure ToC always points to index

    if lesson_data.next_lesson_id:
        next_button_element.href = f"?id={lesson_data.next_lesson_id}"
        next_button_element.style.display = "inline-block"
        # Remove old listener before adding a new one to prevent duplicates
        next_button_element.removeEventListener("click", handle_next_lesson_click)
        next_button_element.addEventListener("click", handle_next_lesson_click)
    else:
        next_button_element.style.display = "none"

    lesson_div.innerHTML = render_rst(lesson_data.description)
    rst_input_element.value = lesson_data.interactive
    render_rst_on_input()  # Render the initial interactive content


async def set_current_lesson(lesson_id: str, push_to_history: bool) -> None:
    """Loads, displays, and sets up the next preload for a lesson."""
    global _current_lesson_id

    # Show loader while content is being fetched/rendered, if not initial load
    # For initial load, loader is handled by initial_load itself.
    # This simple check might need refinement for complex scenarios.
    if push_to_history:  # Indicates a navigation, not the very first page load
        page_loader_element = document.querySelector("#page-loader")
        if page_loader_element:
            page_loader_element.style.display = "flex"

    lesson_data: Lesson | None = None
    if lesson_id in _preloaded_lesson_cache:
        lesson_data = _preloaded_lesson_cache.pop(lesson_id)  # Use and remove
        logger.info("Using preloaded lesson: %s", lesson_id)
    else:
        logger.info("Fetching lesson directly: ", lesson_id)
        lesson_data = await fetch_and_parse_lesson(lesson_id)

    if lesson_data:
        _current_lesson_id = lesson_id
        display_lesson(lesson_data, lesson_id)

        if push_to_history:
            js.history.pushState({"lesson_id": lesson_id}, "", f"?id={lesson_id}")
            logger.info("Pushed lesson %s to browser history.", lesson_id)

        document.body.scrollTop = 0  # Scroll to top for new lesson
        document.documentElement.scrollTop = 0

        if lesson_data.next_lesson_id:
            # Schedule preloading of the next lesson
            asyncio.ensure_future(preload_lesson(lesson_data.next_lesson_id))
    else:
        logger.error(
            "Failed to load or parse lesson %s. Redirecting to main page.", lesson_id
        )
        go_to_main_page()  # Fallback if lesson loading fails

    if push_to_history:  # Hide loader after navigation content is ready
        hide_loader()


async def handle_popstate(event) -> None:
    """Handles browser back/forward button navigation."""
    params = js.URLSearchParams.new(js.window.location.search)
    lesson_id_from_url = params.get("id")

    logger.info(
        "Popstate event. URL lesson ID: %s, Current lesson ID: %s",
        lesson_id_from_url,
        _current_lesson_id,
    )

    if lesson_id_from_url and lesson_id_from_url != _current_lesson_id:
        await set_current_lesson(lesson_id_from_url, push_to_history=False)
    elif (
        not lesson_id_from_url and _current_lesson_id
    ):  # Navigated to a URL without lesson ID (e.g. base page)
        go_to_main_page()


def go_to_main_page() -> None:
    js.window.location.href = "/index.html"


def hide_loader() -> None:
    page_loader_element = document.querySelector("#page-loader")
    body_header_element = document.querySelector("body > header")
    body_container_element = document.querySelector("body > div.container")

    if page_loader_element:
        page_loader_element.style.display = "none"
    if body_header_element:
        body_header_element.style.display = "flex"
    if body_container_element:
        body_container_element.style.display = "flex"


async def initial_load() -> None:
    """Loads the initial lesson based on URL and sets up the page."""
    params = js.URLSearchParams.new(js.window.location.search)
    lesson_id = params.get("id")

    if not lesson_id:
        logger.info("No lesson ID in URL, redirecting to main page.")
        go_to_main_page()
        return

    await set_current_lesson(lesson_id, push_to_history=False)
    hide_loader()  # Hide loader after the first lesson is fully processed


async def main_app_setup():
    # Add popstate listener to handle browser navigation buttons
    # Wrap lambda in asyncio.ensure_future for async event handlers
    js.window.addEventListener(
        "popstate", lambda event: asyncio.ensure_future(handle_popstate(event))
    )
    await initial_load()


# Call the main setup function.
#   PyScript will handle running this async function.
main_app_setup()
