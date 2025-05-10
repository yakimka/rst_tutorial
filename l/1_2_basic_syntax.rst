..
   _Chapter: 1. Introduction to reStructuredText
..
   _Next: 2_1_emphasis_and_strong_emphasis

===================================================================
Lesson 1.2: Basic Syntax - Paragraphs, Blank Lines, and Indentation
===================================================================

In reStructuredText, the fundamental building blocks of a document are paragraphs.
Understanding how they are formed and separated, along with the role of indentation
and how to use special characters literally, is key to creating well-structured documents.

Paragraphs
----------
A paragraph is a simple block of text. Paragraphs are separated from each other by one or more
blank lines. The text within a paragraph should typically have the same level of indentation
(usually, this means it's not indented at all, or it's part of an indented block like a quote).

.. code-block:: rst

    This is the first paragraph.
    It can span multiple lines.

    This is the second paragraph.
    It is separated from the first by a blank line.

Blank Lines
-----------
Blank lines are crucial in reStructuredText. They serve as the primary way to separate
different elements, not just paragraphs. Using more than one blank line between
elements has the same effect as using a single blank line.

Indentation
-----------
Indentation is significant in reStructuredText. While many elements start at the
left margin, indenting a block of text usually means something specific.
One common use of indentation is to create a **block quote**.
If a paragraph is indented relative to the preceding text (typically by 4 spaces), it becomes a block quote.

.. code-block:: rst

    This is a normal paragraph.

        This paragraph is indented,
        so it will be treated as a block quote.
        It can also span multiple lines.

    This paragraph is back at the original indentation level.

The Escaping Mechanism (``\``)
------------------------------
Sometimes, you'll want to use characters that normally have a special meaning in
reStructuredText (like ``*`` for emphasis, or \`\` for inline literals) as
literal characters in your text.

The backslash (``\``) is used as an escape character.
When you place a backslash before a character that has a special markup meaning,
it tells the reStructuredText parser to treat that character as a literal character.

For example:

*   ``\*this\*`` will appear as \*this\* (with literal asterisks).
*   \\`\\`this\\`\\` will appear as \`\`this\`\` (with literal backticks).
*   To display a literal backslash, you escape it with another backslash: ``\\`` renders as ``\``.

References:
-----------
*   `Paragraphs <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#paragraphs>`_
*   `Blank Lines <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#blank-lines>`_
*   `Indentation <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#indentation>`_
*   `Block Quotes <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#block-quotes>`_
*   `Escaping Mechanism <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#escaping-mechanism>`_

**Your Task:**

Your task is to modify text in interactive editor and add to it:

1.  **Paragraphs and Blank Lines**:

    *   Add at least one **new** distinct paragraph of your own.
        For example, you could add it after the first paragraph or at the very end.
    *   Experiment with using one, two, or even three blank lines between paragraphs.
        Notice how the rendered output separates paragraphs consistently as long as there's at least one blank line.
2.  **Indentation and Block Quotes**:

    *   The example already contains an indented block (a block quote).
        Modify this existing block quote by adding another line of text to it.
    *   Add a **new** block quote after one of your normal paragraphs.
        Ensure your new block quote also contains at least two lines of text and is properly indented.
    *   After your new block quote, add a final paragraph, making sure it returns to the
        normal (non-indented) indentation level.
3.  **Escaping**:

    *   Modify the line "This text should show *stars* not emphasis."
        so that the asterisks (``*``) are displayed literally.
    *   Modify the line "This text should show ``backticks`` not literal code."
        so that the backticks (\`\`) are displayed literally.
    *   Ensure the file path "C:\\Users\\YourName." correctly displays literal backslashes.
    *   Add a new sentence that includes the exact phrase "my *word* here" but
        with the asterisks displayed literally.

# Lesson Example

This is an initial paragraph to get you started.
You can add more text to it, or create new paragraphs below.

Remember, a blank line is needed to start a new paragraph.

    And indentation is used for things like block quotes.
    This quote has one line.

This text follows the initial indented block.

Now, let's practice escaping:

- This text should show *stars* not emphasis.
- This text should show ``backticks`` not literal code.
- This text should show a path like C:\\Users\\YourName.
