import asyncio
import io
import logging
import re
from textwrap import dedent
from typing import NamedTuple

from docutils.core import publish_parts

import js
from pyscript import document, fetch, ffi, window

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger("lesson_page")

_current_lesson_id = ""
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
    id: str
    main_chapter: str
    description: str
    interactive: str
    next_lesson_id: str | None


_chapter_pattern = re.compile(r"^\.\.\s*\n\s*_Chapter:\s*(.*)", re.MULTILINE)
_next_pattern = re.compile(r"^\.\.\s*\n\s*_Next:\s*(.*)", re.MULTILINE)


def parse_lesson(rst: str, lesson_id: str) -> Lesson | None:
    if not rst:
        return None
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
    description, interactive = parts[0].strip(), parts[1].strip()
    if interactive.startswith(".. code-block::"):
        # thi is hack for linters, we need to remove the first line and dedent the rest
        interactive = dedent(interactive.split("\n", 1)[1])

    return Lesson(
        id=lesson_id,
        main_chapter=chapter_title_from_meta,
        description=description,
        interactive=interactive,
        next_lesson_id=next_lesson_id_from_meta,
    )


class LoadError(Exception):
    def __init__(self, message: str, status: int | None):
        super().__init__(message)
        self.status = status


async def load_text_file(url_path: str) -> str | None:
    """
    Asynchronously loads a text file from the given URL path.
    Returns the file content as a string, or an error message if fetching fails.
    """
    try:
        response = await fetch(url_path)
    except Exception as e:
        raise LoadError(str(e), status=None) from None
    if response.ok:
        return await response.text()

    raise LoadError(await response.text(), status=response.status)


async def fetch_and_parse_lesson(lesson_id: str) -> tuple[Lesson | None, str]:
    """Fetches, parses, and returns a lesson by its ID."""
    file_path = f"/l/{lesson_id}.rst"
    try:
        full_rst_content = await load_text_file(file_path)
    except LoadError as exc:
        if exc.status == 404:
            return None, "not_found"
        else:
            return None, "network"
    lesson = parse_lesson(full_rst_content, lesson_id)
    if lesson is None:
        return None, "invalid_lesson"
    return lesson, ""


async def preload_lesson(lesson_id: str) -> None:
    if lesson_id in _preloaded_lesson_cache:
        return

    lesson, _ = await fetch_and_parse_lesson(lesson_id)
    if lesson:
        _preloaded_lesson_cache[lesson_id] = lesson
        logger.info("Successfully preloaded lesson: %s", lesson_id)
        return

    logger.warning("Failed to preload lesson: %s", lesson_id)


# ===== UI =====


async def set_current_lesson(lesson_id: str, push_to_history: bool) -> None:
    global _current_lesson_id
    _current_lesson_id = lesson_id

    if push_to_history:
        set_load_lesson_loader()

    if lesson_id in _preloaded_lesson_cache:
        lesson = _preloaded_lesson_cache.get(lesson_id)
        logger.info("Using preloaded lesson: %s", lesson_id)
    else:
        lesson, err = await fetch_and_parse_lesson(lesson_id)
        if push_to_history:
            set_lesson_id_in_url(lesson_id)
        if err:
            display_error(is404=err == "not_found")
            return

    assert lesson is not None

    display_lesson(lesson)

    if push_to_history:
        set_lesson_id_in_url(lesson_id)

    document.body.scrollTop = 0
    document.documentElement.scrollTop = 0

    if lesson.next_lesson_id:
        asyncio.create_task(preload_lesson(lesson.next_lesson_id))

    if push_to_history:
        reset_load_lesson_loader()


def display_lesson(lesson: Lesson) -> None:
    lesson_div = document.querySelector("#lesson-content-area")
    rst_input_element = document.querySelector("#rst-input")
    page_main_title_element = document.querySelector("#page-main-title")
    next_button_element = document.querySelector("#next-lesson-button")

    page_main_title_element.textContent = lesson.main_chapter
    lesson_div.innerHTML = render_rst(lesson.description)
    rst_input_element.value = lesson.interactive
    render_rst_on_input()
    if lesson.next_lesson_id:
        next_button_element.setAttribute("data-next-lesson-id", lesson.next_lesson_id)
        next_button_element.style.display = "inline-block"
    else:
        next_button_element.style.display = "none"

    lesson_div.scrollTop = 0
    rst_input_element.scrollTop = 0
    output_element = document.querySelector("#rst-output")
    output_element.scrollTop = 0


def display_error(is404: bool = False) -> None:
    lesson_div = document.querySelector("#lesson-content-area")
    rst_input_element = document.querySelector("#rst-input")
    next_button_element = document.querySelector("#next-lesson-button")
    output_div = document.querySelector("#rst-output")

    message = "Error loading lesson. Please try again later."
    if is404:
        message = "Lesson not found. Please check the URL."
    lesson_div.innerHTML = message

    rst_input_element.value = ""
    output_div.innerHTML = ""
    next_button_element.style.display = "none"


def go_to_main_page() -> None:
    window.location.href = "/"


def get_current_lesson_id() -> str:
    url = js.URL.new(window.location.href)
    last_path_segment = url.pathname.split("/")[-1]
    if last_path_segment.startswith("playground"):
        return "playground"
    return url.searchParams.get("id") or ""


def set_lesson_id_in_url(lesson_id: str) -> None:
    url = js.URL.new(window.location.href)
    url.searchParams.set("id", lesson_id)
    window.history.pushState(None, "", url.href)


def set_load_lesson_loader() -> None:
    next_button_element = document.querySelector("#next-lesson-button")
    if next_button_element:
        next_button_element.setAttribute("aria-busy", "true")
        next_button_element.setAttribute("disabled", "true")


def reset_load_lesson_loader() -> None:
    next_button_element = document.querySelector("#next-lesson-button")
    if next_button_element:
        next_button_element.removeAttribute("aria-busy")
        next_button_element.removeAttribute("disabled")


def hide_main_loader() -> None:
    page_loader_element = document.querySelector("#page-loader")
    body_header_element = document.querySelector("body > header")
    body_container_element = document.querySelector("body > div.container")

    if page_loader_element:
        page_loader_element.style.display = "none"
    if body_header_element:
        body_header_element.style.display = "flex"
    if body_container_element:
        body_container_element.style.display = "flex"


# ===== Event Handlers =====


def render_rst_on_input(event=None):
    input_element = document.querySelector("#rst-input")
    rst_text = input_element.value
    output_div = document.querySelector("#rst-output")
    output_div.innerHTML = render_rst(rst_text)


async def handle_next_lesson_click(event) -> None:
    event.preventDefault()
    next_lesson_id = event.target.getAttribute("data-next-lesson-id")
    await set_current_lesson(next_lesson_id, push_to_history=True)


async def on_history_change(event):
    lesson_id = get_current_lesson_id()
    if lesson_id and lesson_id != _current_lesson_id:
        await set_current_lesson(lesson_id, push_to_history=False)


# ===== Main Setup =====


async def main_app_setup():
    if lesson_id := get_current_lesson_id():
        if lesson_id == "playground":
            render_rst_on_input()
            hide_main_loader()
            return

        proxy = ffi.create_proxy(on_history_change)
        window.addEventListener("popstate", proxy)
        await set_current_lesson(lesson_id, push_to_history=False)
        hide_main_loader()
        return

    go_to_main_page()


# Call the main setup function.
#   PyScript will handle running this async function.
main_app_setup()
