import io
from pyscript import document
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

    if not rst_text.strip():
        output_div.innerHTML = ""
        return

    # Configure docutils to report errors as text, not via stderr or exceptions
    # for parsing issues.
    error_stream = io.StringIO() # To catch any stray messages
    settings_overrides = {
        'warning_stream': error_stream,  # Redirects some messages
        # 'report_level': 5,  # Report WARNING_LEVEL (1) and above
        # 'halt_level': 5,  # Do not halt on any reported message (NONE_LEVEL is 5)
        'traceback': True  # Do not include Python tracebacks in docutils messages
    }

    try:
        parts = publish_parts(
            source=rst_text,
            writer_name='html5',
            settings_overrides=settings_overrides
        )
        output_div.innerHTML = parts['html_body']
    except Exception as e:
        output_div.innerHTML = f"<pre style='color: red;'>Error rendering reStructuredText:\n{str(e)}</pre>"
