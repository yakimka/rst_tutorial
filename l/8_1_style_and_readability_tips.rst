..
   _Chapter: 8. Practice and Best Practices
..
   _Next: 8_2_common_pitfalls_and_validation_checks

=========================================
Lesson 8.1: Style and Readability Tips
=========================================

Writing reStructuredText is not just about getting the syntax right; it's also about
creating documents that are easy to read and maintain in their raw plain text form.
Clear, consistent source text leads to fewer errors and a more pleasant experience
for authors and collaborators.

Key Readability Tips
--------------------

1.  **Consistent Section Adornments**:
    While reStructuredText allows you to choose your section adornment characters
    (e.g., ``= - ` : ' " ~ ^ _ * + #``), be consistent within a document.
    Use the same character for the same level of heading throughout.
    For example, always use ``=`` for chapter titles, ``-`` for sections,
    and ````` for subsections. Overlines and underlines should also be used
    consistently for their respective levels.
2.  **Appropriate Line Lengths**:
    Keep your lines of reStructuredText at a reasonable length, typically between
    80 and 120 characters. This makes the raw text easier to read in text editors
    without excessive horizontal scrolling. Most text editors can be configured
    to wrap lines automatically or show a ruler.
3.  **Strategic Use of Blank Lines**:
    Blank lines are fundamental for separating paragraphs and other block-level
    elements. Use them consistently:

    *   One blank line between paragraphs.
    *   One blank line before and after lists, block quotes, literal blocks,
        directives, etc.
    *   Optionally, use blank lines between list items or definition list items
        if it improves readability, especially for multi-paragraph items.
4.  **Clear Indentation**:
    Use consistent indentation (typically 4 spaces, though 2 or 3 are also common)
    for the content of lists, directives, block quotes, etc. This visual structure
    is key to understanding the document's hierarchy in its raw form. Avoid using
    tabs or mixing tabs and spaces for indentation, as tab width can vary across
    editors.
5.  **Readable Hyperlink Targets**:
    For external hyperlinks, place the target definitions (e.g., ``.. _Link Name: URL``)
    in a logical place, often at the end of a section or the document. This keeps
    the main text flow cleaner. Use meaningful link names.
6.  **Logical Use of Inline Markup**:

    *   Use emphasis (``*text*``) and strong emphasis (``**text**``) purposefully.
        Overuse can make text harder to read.
    *   Use inline literals (````text````) for code snippets, commands, or any text
        that should be represented verbatim and stand out visually.
7.  **Comments for Clarity**:
    Use comments (``.. This is a comment``) to explain complex markup, leave notes
    for future editors, or temporarily remove sections of text.
8.  **Substitution Definitions for Reusability**:
    If you have frequently repeated text, symbols, or inline images, use
    substitution definitions (e.g., ``.. |name| replace:: Replacement Text``)
    to improve maintainability and readability.

Example of Good Style:
----------------------
.. code-block:: rst

    My Document Title
    =================

    Introduction
    ------------
    This is the first paragraph. It's kept to a reasonable line length
    for easy reading in a text editor.

    This is the second paragraph, clearly separated by a blank line.

    Key Features
    ~~~~~~~~~~~~
    Here are some important features:

    *   **Feature One**:
        Description of the first feature. This list item
        contains multiple lines, all consistently indented.

    *   **Feature Two**:
        Description of the second feature.

    .. note::
       This is an important note, clearly marked and indented.
       Its content is also kept to a readable line length.

    For more information, see the `Official Website`_.

    .. _Official Website: https://example.com

Bad Style (Exaggerated for Effect):
-----------------------------------
.. code-block:: rst

    MY DOC TITLE
    ***********************
    Intro
    -----
    This paragraph is way too long and just keeps going and going without any breaks, making it very difficult to read in a plain text editor because you have to scroll horizontally all the time, which is annoying.
    Another paragraph but with inconsistent section titles.

    Features
    ++++++
    * Feature 1: description.
    * Feature 2: another description.
                .. warning:: A warning that is indented too much and hard to associate.
    See `here <https://example.com>`_ for details.

Adhering to good style conventions makes your reStructuredText documents more professional,
easier to manage, and more accessible to others (and your future self!).

References:
-----------
*   `A ReStructuredText Primer (Style Guide section implicitly) <https://docutils.sourceforge.io/docs/user/rst/quickstart.html>`_
*   Many style points are derived from general best practices for writing plain text and code.

**Your Task:**

The editor below contains a short reStructuredText document with several style and
readability issues. Your task is to refactor it according to the tips discussed.

1.  **Section Adornments**:

    *   Make the section adornments consistent. For example, use ``=`` for
        the main title, ``-`` for the "Overview" section, and ````` for
        the "Details" subsection. Ensure overlines/underlines are the
        correct length.
2.  **Line Lengths**:

    *   Break up the very long line in the first paragraph into multiple
        shorter lines (aim for under 80-100 characters).
3.  **Blank Lines**:

    *   Ensure proper blank lines between paragraphs and before/after the list and the directive.
4.  **Indentation**:

    *   Correct the indentation of the list items and the ``.. tip::`` directive's content.
5.  **Hyperlink Target**:

    *   Move the hyperlink target for "Docutils Website" to the end of the document for better organization.
6.  **Inline Markup**:

    *   The phrase "very important" is bolded. Consider if simple
        emphasis (italics) might be more appropriate, or if it's
        fine as is. (This is subjective, make a choice).
    *   The command ``rst2html`` should be an inline literal.

Review your changes and see how they improve the readability of the raw text.

# Lesson Example
.. code-block::

    A Document About reStructuredText
    #################################
    This is the first paragraph and it's extremely long, stretching out far beyond what is considered good practice for readability in a plain text editor, forcing users to scroll horizontally which is generally a bad experience for anyone trying to read or edit the source file.
    The **very important** tool for processing reStructuredText is rst2html.
    Overview
    ========
    Here are some points:
        * Point one, not indented correctly.
    * Point two, also not quite right.
    .. tip::
      This tip is also not indented properly and lacks a blank line before it.
    For more info, see `Docutils Website`_. .. _Docutils Website: https://docutils.sourceforge.io/
    Final thoughts.
