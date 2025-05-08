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
        # Ensure that publish_parts doesn't fail on completely empty or whitespace-only rst_text
        # It should be handled by the initial check, but as a safeguard for direct calls:
        if not rst_text.strip():
            output_div.innerHTML = ""
            return

        parts = publish_parts(
            source=rst_text,
            writer_name='html5',
            settings_overrides=settings_overrides
        )
        output_div.innerHTML = parts['html_body']
    except Exception as e:
        # Catching all exceptions might be too broad for docutils,
        # but for now, this ensures some error message is shown.
        output_div.innerHTML = f"<pre style='color: red;'>Error rendering reStructuredText:\n{str(e)}</pre>"

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
