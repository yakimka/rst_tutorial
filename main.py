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
    pass


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


async def load_lesson_from_url():
    """
    Loads lesson content from an .rst file specified by the 'id' URL parameter
    and renders it into the lesson panel.
    """
    params = js.URLSearchParams.new(js.window.location.search)
    lesson_id = params.get("id")
    lesson_div = document.querySelector("#lesson-content-area")
    rst_input_element = document.querySelector("#rst-input")
    rst_output_div = document.querySelector("#rst-output")
    page_main_title_element = document.querySelector("#page-main-title")
    next_button_element = document.querySelector("#next-lesson-button")
    page_loader_element = document.querySelector("#page-loader")
    # Also get direct references to the main content containers to show them
    body_header_element = document.querySelector("body > header") # Updated selector
    body_container_element = document.querySelector("body > div.container")


    EXAMPLE_DELIMITER = "# Lesson Example"
    DEFAULT_PAGE_TITLE = "reStructuredText Live Editor"

    if lesson_id:
        file_path = f"/l/{lesson_id}.rst"
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

        # Process lesson content
        lesson_rst_part = ""
        example_rst_part = ""

        if full_rst_content.startswith("Error:"):
            lesson_div.innerHTML = f"<p style='color: red;'>{full_rst_content}</p>"
            rst_input_element.value = ""
            rst_output_div.innerHTML = ""
            # Ensure button is hidden on error too
            if next_button_element: next_button_element.style.display = "none"
            if page_main_title_element: page_main_title_element.textContent = DEFAULT_PAGE_TITLE

        else:
            if EXAMPLE_DELIMITER in full_rst_content:
                parts = full_rst_content.split(EXAMPLE_DELIMITER, 1)
                lesson_rst_part = parts[0].strip() # Comments like .. _Chapter will be ignored by render_rst
                if len(parts) > 1:
                    example_rst_part = parts[1].strip()
            else:
                lesson_rst_part = full_rst_content.strip()
            
            lesson_div.innerHTML = render_rst(lesson_rst_part)
            rst_input_element.value = example_rst_part
            render_rst_on_input() 
            
    else: # No lesson_id in URL
        # Reset to default state
        lesson_div.innerHTML = "<p>Select a lesson or start typing reStructuredText in the input area.</p>"
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
    if body_header_element: # Updated variable name
        body_header_element.style.display = "flex" # header is now a flex container
    if body_container_element:
        body_container_element.style.display = "flex"


async def main_app_setup():
    """Main function to run on script load to set up the application."""
    await load_lesson_from_url()
    # Other initial setup tasks can be added here in the future.

# Call the main setup function. PyScript will handle running this async function.
main_app_setup()
