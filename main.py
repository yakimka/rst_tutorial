import io
import logging
import re
from typing import NamedTuple

from docutils.core import publish_parts
from pyscript import document, fetch

import js

logger = logging.getLogger("lesson_page")


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


async def load_lesson_from_url():
    """
    Loads lesson content from an .rst file specified by the 'id' URL parameter
    and renders it into the lesson panel.
    """
    params = js.URLSearchParams.new(js.window.location.search)
    lesson_id = params.get("id")
    if not lesson_id:
        go_to_main_page()

    file_path = f"/l/{lesson_id}.rst"
    full_rst_content = await load_text_file(file_path)
    if not full_rst_content:
        go_to_main_page()
        return
    lesson = parse_lesson(full_rst_content)
    if not lesson:
        go_to_main_page()
        return

    render_lesson(lesson)
    render_rst_on_input()

    hide_loader()


def go_to_main_page() -> None:
    raise ValueError(f"Error: {type}")


def render_lesson(lesson: Lesson) -> None:
    lesson_div = document.querySelector("#lesson-content-area")
    rst_input_element = document.querySelector("#rst-input")
    page_main_title_element = document.querySelector("#page-main-title")
    next_button_element = document.querySelector("#next-lesson-button")

    page_main_title_element.textContent = lesson.main_chapter
    if lesson.next_lesson_id:
        next_button_element.href = f"?id={lesson.next_lesson_id}"
        next_button_element.style.display = "inline-block"
    else:
        next_button_element.style.display = "none"

    lesson_div.innerHTML = render_rst(lesson.description)
    rst_input_element.value = lesson.interactive


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


async def main_app_setup():
    await load_lesson_from_url()


# Call the main setup function.
#   PyScript will handle running this async function.
main_app_setup()
