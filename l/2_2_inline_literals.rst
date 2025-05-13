..
   _Chapter: 2. Basic Text Formatting (Inline Markup)
..
   _Next: 2_3_inline_markup_recognition_rules_and_order

==================================
Lesson 2.2: Inline Literals (``)
==================================

In reStructuredText, **inline literals** are used to represent text that should be
displayed exactly as it is written, typically in a fixed-width (monospaced) font.
This is very useful for short code snippets, commands, filenames, or any text
where special characters (like ``*``, ``_``, or ``|``) should not be interpreted as markup.

The syntax for inline literals is to surround the text with double backticks:
````text````.

Key points for using inline literals:

*   **Double Backticks**: The text is enclosed by two backtick characters (\`\`) at the
    start and two at the end.
*   **No Markup Interpretation**: Within inline literals, no reStructuredText markup
    is processed. This means characters like ``*``, ``_``, or ``|`` will be
    displayed literally and will not trigger emphasis, hyperlinks, or
    substitutions. Even backslash-escapes (``\``) are treated as literal characters.
*   **Whitespace Handling**: While the reStructuredText parser preserves whitespace
    (like multiple spaces) within inline literals in its internal representation,
    the final rendering in an output format like HTML might collapse multiple spaces
    into one. Line breaks within inline literals are generally not preserved in the
    final output. For critical whitespace preservation, especially line breaks,
    `Literal Blocks <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#literal-blocks>`_
    are more suitable.
*   **Use Cases**: Ideal for showing variable names (e.g., ``my_variable``),
    function names (e.g., ``calculate_value()``), file paths (e.g.,
    ``/etc/hosts``), or short commands (e.g., ``ls -l``).

References:
-----------
*   `Inline Literals <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#inline-literals>`_
*   Standard role: `:literal: <https://docutils.sourceforge.io/docs/ref/rst/roles.html#literal>`_
*   Related role: `:code: <https://docutils.sourceforge.io/docs/ref/rst/roles.html#code>`_ (often used for semantic highlighting of code)

**Your Task:**

The editor below contains several sentences with text that would be more appropriately
represented as inline literals. Your task is to identify these and apply the correct
markup.

1.  **Identify and Mark Up**:

    *   Read through the provided text in the interactive section.
    *   Identify at least three instances where text should be an inline literal.
        This could be a filename, a command, a piece of code, a special symbol sequence,
        or a variable name.
    *   Apply the inline literal syntax (e.g., ````text````) to these instances.
2.  **Observe Literal Rendering**:

    *   Ensure that your marked-up text is rendered in a monospaced font in the
        output panel.
    *   Notice that any special characters you included within the double backticks
        (like ``*`` or ``_``) are displayed literally and not interpreted as
        reStructuredText markup.
3.  **Experiment with Special Characters**:

    *   Try including text like ````*this_is_not_italic*```` or ````not_a_link_````
        within double backticks.
    *   Observe that it is rendered as ``*this_is_not_italic*`` and ``not_a_link_``
        respectively, not as emphasized text or a hyperlink.

# Lesson Example

To list files in a directory, you can use the command ls -a.
The configuration file is often named config.json or settings.yaml.
In Python, a common way to define a function is def my_function():.
Be careful with wildcards like * when deleting files.
The special sequence __init__.py is important in Python packages.
You might see a variable named _internal_variable.
The pipe character | can be used for shell command redirection.
Consider the reStructuredText markup for emphasis: *text*.
How would you show that literally?
