import io
import js  # To access URL parameters
import re # For regular expression matching
from pyscript import document, fetch
from docutils.core import publish_parts

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


def handle_keydown(event):
    """
    Handles custom keyboard shortcuts for the rst-input textarea.
    - Tab: Inserts 4 spaces.
    - Ctrl+E: Deletes the current line.
    - Ctrl+D: Duplicates the current line.
    """
    target = event.target
    if target.id != "rst-input":
        return

    text = target.value
    cursor_pos = target.selectionStart
    lines = text.split('\n')

    char_count_so_far = 0
    current_line_idx = 0
    cursor_offset_in_line = 0
    # Find current line index based on cursor_pos
    # This loop correctly identifies the line index even if the cursor is at the very end of the text
    # or at the end of a line (before a newline character).
    temp_cursor_pos = cursor_pos
    for i, line_content in enumerate(lines):
        line_start_char_pos = char_count_so_far
        # +1 to handle cursor at the very end of a line (right before \n or end of text)
        line_end_char_pos_inclusive = line_start_char_pos + len(line_content)
        if temp_cursor_pos <= line_end_char_pos_inclusive: # Cursor is on this line or at its end
            current_line_idx = i
            cursor_offset_in_line = temp_cursor_pos - line_start_char_pos
            break
        char_count_so_far += len(line_content) + 1 # +1 for the \n
    else: # Cursor is at the very end of the text
        current_line_idx = len(lines) - 1
        cursor_offset_in_line = len(lines[current_line_idx])


    if event.key == "Tab" and not event.shiftKey:
        event.preventDefault()
        start = target.selectionStart
        end = target.selectionEnd
        target.value = text[:start] + "    " + text[end:]
        target.selectionStart = target.selectionEnd = start + 4
    elif event.key == "Tab" and event.shiftKey:
        event.preventDefault()
        if not lines:
            return

        current_line_content = lines[current_line_idx]
        if current_line_content.startswith(" "):
            leading_spaces_count = len(current_line_content) - len(current_line_content.lstrip())
            spaces_to_remove = min(4, leading_spaces_count)
            lines[current_line_idx] = current_line_content[spaces_to_remove:]
            new_text = '\n'.join(lines)
            target.value = new_text

            # Adjust cursor position
            # Calculate the character position of the start of the current line
            line_start_char_pos = 0
            for i in range(current_line_idx):
                line_start_char_pos += len(lines[i] if i < current_line_idx else "") +1 # length of previous lines + newline

            # New cursor position will be current line's start + original offset in line - 4
            # (or 0 if offset was < 4)
            new_cursor_offset_in_line = max(0, cursor_offset_in_line - spaces_to_remove)
            new_cursor_char_pos = line_start_char_pos + new_cursor_offset_in_line

            # Ensure cursor is not out of bounds
            if new_cursor_char_pos > len(new_text):
                new_cursor_char_pos = len(new_text)
            if new_cursor_char_pos < 0: # Should not happen with max(0, ...)
                new_cursor_char_pos = 0

            target.selectionStart = target.selectionEnd = new_cursor_char_pos


def render_rst(rst: str) -> str:
    if not rst.strip():
        return ""

    error_stream = io.StringIO() # To catch any stray messages
    settings_overrides = {
        'warning_stream': error_stream,  # Redirects some messages
        # 'report_level': 5,  # Report WARNING_LEVEL (1) and above
        # 'halt_level': 5,  # Do not halt on any reported message (NONE_LEVEL is 5)
        'traceback': True  # Do not include Python tracebacks in docutils messages
    }
    try:
        parts = publish_parts(
            source=rst,
            writer_name='html5',
            settings_overrides=settings_overrides
        )
    except Exception as e:
        return f"<pre style='color: red;'>Error rendering reStructuredText:\n{str(e)}</pre>"

    return parts['html_body']


async def load_text_file(url_path: str) -> str:
    """
    Asynchronously loads a text file from the given URL path.
    Returns the file content as a string, or an error message if fetching fails.
    """
    try:
        response = await fetch(url_path)
        if response.ok:
            return await response.text()
        else:
            return f"Error: Could not load file {url_path}. Status: {response.status}"
    except Exception as e:
        return f"Error: Exception while fetching {url_path}. {str(e)}"


async def load_exercise_from_url():
    """
    Loads exercise content from an .rst file specified by the 'id' URL parameter
    and renders it into the exercise panel.
    """
    params = js.URLSearchParams.new(js.window.location.search)
    exercise_id = params.get("id")
    exercise_div = document.querySelector("#exercise-content-area")
    rst_input_element = document.querySelector("#rst-input")
    rst_output_div = document.querySelector("#rst-output")
    page_main_title_element = document.querySelector("#page-main-title")
    next_button_element = document.querySelector("#next-lesson-button")
    page_loader_element = document.querySelector("#page-loader")
    # Also get direct references to the main content containers to show them
    body_h1_element = document.querySelector("body > h1#page-main-title") # More specific selector
    body_container_element = document.querySelector("body > div.container")


    EXAMPLE_DELIMITER = "# -Example-"
    DEFAULT_PAGE_TITLE = "reStructuredText Live Editor"

    if exercise_id:
        file_path = f"/l/{exercise_id}.rst"
        full_rst_content = await load_text_file(file_path)
        
        chapter_title_from_meta = None
        next_lesson_id_from_meta = None

        if not full_rst_content.startswith("Error:"):
            # Extract _Chapter metadata
            chapter_pattern = re.compile(r"^\.\.\s*\n\s*_Chapter:\s*(.*)", re.MULTILINE)
            chapter_match = chapter_pattern.search(full_rst_content)
            if chapter_match:
                chapter_title_from_meta = chapter_match.group(1).strip()

            # Extract _Next metadata
            next_pattern = re.compile(r"^\.\.\s*\n\s*_Next:\s*(.*)", re.MULTILINE)
            next_match = next_pattern.search(full_rst_content)
            if next_match:
                extracted_next_id = next_match.group(1).strip()
                if extracted_next_id: # Ensure it's not empty after stripping
                    next_lesson_id_from_meta = extracted_next_id
        
        # Update page title
        if page_main_title_element:
            page_main_title_element.textContent = chapter_title_from_meta if chapter_title_from_meta else DEFAULT_PAGE_TITLE
        
        # Update Next button
        if next_button_element:
            if next_lesson_id_from_meta:
                next_button_element.href = f"?id={next_lesson_id_from_meta}"
                next_button_element.style.display = "inline-block"
            else:
                next_button_element.style.display = "none"

        # Process exercise content
        exercise_rst_part = ""
        example_rst_part = ""

        if full_rst_content.startswith("Error:"):
            exercise_div.innerHTML = f"<p style='color: red;'>{full_rst_content}</p>"
            rst_input_element.value = ""
            rst_output_div.innerHTML = ""
            # Ensure button is hidden on error too
            if next_button_element: next_button_element.style.display = "none"
            if page_main_title_element: page_main_title_element.textContent = DEFAULT_PAGE_TITLE

        else:
            if EXAMPLE_DELIMITER in full_rst_content:
                parts = full_rst_content.split(EXAMPLE_DELIMITER, 1)
                exercise_rst_part = parts[0].strip() # Comments like .. _Chapter will be ignored by render_rst
                if len(parts) > 1:
                    example_rst_part = parts[1].strip()
            else:
                exercise_rst_part = full_rst_content.strip()
            
            exercise_div.innerHTML = render_rst(exercise_rst_part)
            rst_input_element.value = example_rst_part
            render_rst_on_input() 
            
    else: # No exercise_id in URL
        # Reset to default state
        exercise_div.innerHTML = "<p>Select a lesson or start typing reStructuredText in the input area.</p>"
        rst_input_element.value = ""
        rst_output_div.innerHTML = ""
        if page_main_title_element:
            page_main_title_element.textContent = DEFAULT_PAGE_TITLE
        if next_button_element:
            next_button_element.style.display = "none"
        pass
    
    # Hide loader and show content, regardless of outcome
    if page_loader_element:
        page_loader_element.style.display = "none"
    if body_h1_element:
        body_h1_element.style.display = "block" # Or "flex" or whatever its original display was if needed
    if body_container_element:
        body_container_element.style.display = "flex"


async def main_app_setup():
    """Main function to run on script load to set up the application."""
    await load_exercise_from_url()
    # Other initial setup tasks can be added here in the future.

# Call the main setup function. PyScript will handle running this async function.
main_app_setup()
