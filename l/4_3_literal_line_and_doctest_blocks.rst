..
   _Chapter: 4. Lists and Blocks
..
   _Next: 5_1_tables_grid_simple_csv_list

================================================
Lesson 4.3: Literal, Line, and Doctest Blocks
================================================

reStructuredText offers several ways to include blocks of text where formatting,
especially whitespace and line breaks, is significant. These are literal blocks,
line blocks, and doctest blocks.

Literal Blocks
--------------
Literal blocks are used for displaying code examples, preformatted text, or any
text where markup should not be processed and whitespace should be preserved.

Syntax:
~~~~~~~
A literal block is indicated by ending the preceding paragraph with a double colon
(``::``). The literal block itself must be indented relative to the preceding paragraph.

.. code-block:: rst

    This is a normal paragraph::

        This is a literal block.
        All whitespace (spaces, newlines) is preserved.
        *No* markup is interpreted here.

    This paragraph follows the literal block.

The paragraph containing only :: will be completely removed from the output; no empty paragraph will remain.

.. code-block:: rst

    This is a typical paragraph.  An indented literal block follows.

    ::

        This is a literal block.

Key points for literal blocks:

*   **Double Colon**: The ``::`` marker is key. If it's at the end of a line with
    other text, it will be rendered as a single colon. If it's on a line by itself,
    it will be invisible in the output.
*   **Indentation**: The literal block must be indented. The minimum indentation common
    to all lines in the block is removed.
*   **No Markup Processing**: Text inside a literal block is not parsed for reStructuredText
    markup.
*   **Quoted Literal Blocks**: Alternatively, lines can be prefixed with a quoting
    character (e.g., ``>``) if the block is not indented. This is less common.

Line Blocks
-----------
Line blocks are useful for text where line breaks are significant, such as poetry,
addresses, or unadorned lists. Inline markup is supported within line blocks.

Syntax:
~~~~~~~
Each line in a line block starts with a vertical bar (``|``) followed by a space.
Indentation of the vertical bars creates nested line blocks. Continuation lines
(for long lines that wrap) start with a space instead of a vertical bar and must
be indented.

.. code-block:: rst

    | This is the first line of a line block.
    | This is the second line.
    |   This line is indented, creating a nested structure.
    | A very long line can be continued on the next line
      by indenting the continuation and starting it with a space.

Key points for line blocks:

*   **Vertical Bar**: Each new line intended to be preserved starts with "| ".
*   **Preserved Line Breaks**: Line breaks are rendered as they appear.
*   **Indentation for Nesting**: Indenting the text after "|" creates nested structures.
*   **Inline Markup**: Markup like ``*emphasis*`` or ``**strong**`` works within line blocks.

Doctest Blocks
--------------
Doctest blocks are specifically for including interactive Python sessions, often
used in documentation to show examples that can be automatically tested by Python's
`doctest` module.

Syntax:
~~~~~~~
A doctest block starts with ``>>>`` (the Python interactive prompt) and ends with
a blank line. They are treated as a special kind of literal block.

.. code-block:: rst

    >>> print("Hello, reStructuredText!")
    Hello, reStructuredText!
    >>> a = 5
    >>> b = 3
    >>> a * b
    15

Key points for doctest blocks:

*   **Python Prompt**: Must begin with ``>>>``.
*   **Literal**: Content is treated as literal text; no reStructuredText markup is processed.
*   **Testing**: Designed to be copy-pasted into documentation and verified by the
    `doctest` tool.

References:
-----------
*   `Literal Blocks <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#literal-blocks>`_
*   `Line Blocks <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#line-blocks>`_
*   `Doctest Blocks <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#doctest-blocks>`_

**Your Task:**

The editor below contains placeholders for each type of block. Your task is to
fill them in with appropriate examples.

1.  **Literal Block**:

    *   After "Python code example::", create a literal block.
    *   Inside, write a small, simple Python code snippet (e.g., a function definition
        or a loop). Ensure it's properly indented.
    *   Include some Python comments (``# like this``) and perhaps a string with
        asterisks (e.g., ``"*" * 5``) to demonstrate that markup is not processed.
2.  **Line Block**:

    *   After "A short poem:", create a line block.
    *   Write a short, 2-4 line poem or an address.
    *   Use indentation for at least one line in your line block to show nesting or
        continuation.
    *   Apply ``*emphasis*`` to at least one word within your line block.
3.  **Doctest Block**:

    *   After "Python interactive session:", create a doctest block.
    *   Include a sequence of at least 2-3 Python commands and their expected output,
        as if typed into an interactive Python shell. For example, define a variable,
        perform a calculation, and print a result.

Observe how each block type is rendered in the HTML output panel.

# Lesson Example

Python code example::
    .. Add your Python code snippet here

A short poem:
    .. Add your line block example here (e.g., a poem or address)

Python interactive session:
    .. Add your doctest block example here
