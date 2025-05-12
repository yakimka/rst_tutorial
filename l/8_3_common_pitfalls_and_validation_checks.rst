..
   _Chapter: 8. Configuration & Best Practices
..
   _Next:

====================================================
Lesson 8.3: Common Pitfalls and Validation Checks
====================================================

As you've learned, reStructuredText relies on subtle cues like indentation and blank
lines. While this makes the raw text readable, it can also lead to common errors,
especially for beginners. Understanding these pitfalls and knowing how to validate
your documents can save you a lot of time and frustration.

Common Pitfalls
---------------

1.  **Incorrect Indentation**:

    *   **Problem**: Inconsistent indentation for list items, directive content,
        block quotes, or literal blocks. reStructuredText is very strict about this.
    *   **Symptom**: Content may not be associated with the intended parent element,
        or system messages (warnings/errors) might appear.
    *   **Solution**: Use a consistent number of spaces (e.g., 3 or 4) for each
        level of indentation. Ensure all lines of a multi-line block are indented
        to the same level.

2.  **Missing Blank Lines**:

    *   **Problem**: Forgetting the required blank line(s) before or after block-level
        elements like lists, directives, literal blocks, tables, or between paragraphs.
    *   **Symptom**: Elements might merge unexpectedly, or markup might not be recognized.
        For example, a list following a paragraph without a blank line might not be
        parsed as a list.
    *   **Solution**: Always ensure block elements are separated by at least one blank line.

3.  **List Formatting Issues**:

    *   **Problem**: Incorrect spacing after bullets/enumerators, inconsistent
        enumerator types in an enumerated list, or improper indentation of
        multi-paragraph list items.
    *   **Symptom**: Lists may not render correctly or might be broken into multiple lists.
    *   **Solution**: Ensure a space after the bullet/enumerator (e.g., ``* item``, not ``*item``).
        Align subsequent lines of a list item's content with the text of the first line.

4.  **Directive Syntax Errors**:

    *   **Problem**: Typos in directive names (e.g., ``.. imge::`` instead of ``.. image::``),
        incorrect number/type of arguments, malformed options (e.g., missing colon,
        incorrect indentation), or missing blank line before content.
    *   **Symptom**: The directive might not be processed, or it might be rendered as a
        literal block with an error message.
    *   **Solution**: Double-check directive names and syntax against the documentation.
        Pay close attention to colons, spacing, and indentation for options and content.

5.  **Hyperlink Target Issues**:

    *   **Problem**: Mismatched hyperlink reference names and target names (case or
        whitespace differences, though normalization helps), or malformed target URLs.
        Forgetting the underscore after a reference (e.g., ```Link Text`_``).
    *   **Symptom**: Links might not work, or "undefined reference" errors may occur.
    *   **Solution**: Ensure reference names match target names precisely (after normalization).
        Verify URLs. Make sure hyperlink references end with an underscore (or two for anonymous).

6.  **Inline Markup Recognition**:

    *   **Problem**: Inline markup (like ``*emphasis*`` or ````code````) not rendering as
        expected because of surrounding characters or lack of whitespace, as per
        `inline markup recognition rules <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#inline-markup-recognition-rules>`_.
    *   **Symptom**: Asterisks or backticks appear literally instead of applying formatting.
    *   **Solution**: Ensure inline markup is surrounded by whitespace or appropriate
        punctuation, or use backslash escapes for character-level markup if absolutely necessary.

Validation Checks
-----------------
Most reStructuredText processing tools, like Docutils (which powers this tutorial's
rendering) or Sphinx, include a validation mechanism. When they parse your ``.rst``
file, they will output system messages (information, warnings, or errors) if they
encounter problems.

*   **Level-1 (Info)**: Minor issues or suggestions.
*   **Level-2 (Warning)**: Potential problems that might lead to unexpected output.
*   **Level-3 (Error)**: Serious problems that prevent proper parsing or rendering.
*   **Level-4 (Severe)**: Critical errors.

Tools like ``doc8`` (a style checker for reStructuredText) can also be used to
enforce style consistency (like line length, trailing whitespace) and catch some
common syntax errors. This tutorial uses ``doc8`` as part of its linting process.

**Tips for Debugging**:

*   **Read System Messages Carefully**: They often pinpoint the line number and type of error.
*   **Isolate the Problem**: If you get an error, try commenting out recent changes or
    sections of your document to find the problematic markup.
*   **Check Indentation and Blank Lines First**: These are the most common sources of errors.
*   **Refer to Documentation**: When unsure about syntax, consult the reStructuredText
    specifications or examples.

References:
-----------
*   `Error Handling (System Messages) <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#error-handling>`_
*   `Inline markup recognition rules <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#inline-markup-recognition-rules>`_
*   `doc8 (external tool) <https://pypi.org/project/doc8/>`_

**Your Task:**

The editor below contains several common reStructuredText errors. Your task is to
identify and fix them. The goal is to make the document parse correctly and render
as intended.

1.  **Paragraph Separation**: The first two "paragraphs" are not separated correctly.
2.  **List Indentation**: The bullet list items are not indented correctly.
3.  **Directive Syntax**: The ``.. note::`` directive has an issue with its content indentation.
4.  **Hyperlink**: The hyperlink reference "Example Link" is missing its trailing underscore.
5.  **Inline Literal**: The inline literal for ``my-variable`` is not correctly formed.
6.  **Section Title Adornment**: The "Conclusion" section title's underline is too short.

After making corrections, observe the output. If there were system messages (though
you won't see them directly here), they would ideally disappear or lessen.

# Lesson Example
.. code-block::

    My Document Title
    =================
    This is the first paragraph.This should be a second paragraph.

    Some points to consider:

    * Item one
    *Item two (this one has an issue with the bullet)
      * Sub-item A (this sub-item's indentation is off)

    .. note::
    This note's content is not properly indented.
    And this line is also part of the note.

    This is an `Example Link` to https://www.example.com.
    And here is an inline variable: `my-variable`.

    Conclusion
    ----------
    This is the end.
