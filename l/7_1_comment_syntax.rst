..
   _Chapter: 7. Comments and Configuration
..
   _Next: 7_2_configuration_settings

=============================
Lesson 7.1: Comment Syntax
=============================

Comments are parts of your reStructuredText document that are ignored by the parser
and do not appear in the final rendered output. They are useful for leaving notes
to yourself or other authors within the source text.

Standard Comments
-----------------
A comment block is an explicit markup block that isn't recognized as any other
explicit markup construct (like a footnote, citation, hyperlink target, directive,
or substitution definition).

The syntax for a comment is:

.. code-block:: rst

    .. This is a comment.
       It can span multiple lines, as long as subsequent lines
       are indented relative to the initial '.. '.

    .. Another comment block.

Key points for standard comments:

*   They begin with ``..`` (two periods followed by a space).
*   The content of the comment can be any text.
*   If the comment spans multiple lines, all subsequent lines must be indented
    relative to the initial ``..``.
*   To ensure a block is treated as a comment and not mistaken for another
    explicit markup construct (like a directive with a typo), it's often safest
    to leave the ``..`` on a line by itself if the following text might be ambiguous:

    .. code-block:: rst

        ..
           This is clearly a comment because the '..' is alone.
           _this_is_not_a_target::
           [this]_is_not_a_footnote_reference::

Empty Comments
--------------
An "empty comment" is a special type of comment that consists only of the
explicit markup start (``..``) followed by a blank line (or end of file)
and nothing else on the line with ``..``.

.. code-block:: rst

           This is block quote

       ..

           This is another block quote.
           The empty comment above separates them
           but doesn't produce any output.

Empty comments are particularly useful for:

*   **Terminating a preceding construct**: Sometimes, an indented block (like a
    list item's content or a directive's content) might unintentionally consume
    a following indented block (like a block quote). An unindented empty comment
    can explicitly separate these.

    .. code-block:: rst

       *   This is a list item.
           It has some indented content.

       ..

           This is a block quote, not part of the list item.

*   **Separating adjacent explicit markup blocks** where the parser might otherwise
    get confused.

Comments are generally stripped from the document during processing and do not
affect the rendered output, though some tools might offer options to preserve them
in certain output formats (e.g., as HTML comments).

References:
-----------
*   `Comments <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#comments>`_
*   `Empty Comments <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#empty-comments>`_

**Your Task:**

In the editor below, practice adding comments to a reStructuredText document.

1.  **Standard Comment**:

    *   Add a standard comment above the first paragraph, explaining what the document is about.
        Make it a multi-line comment.
2.  **Another Standard Comment**:

    *   Add a comment between the first and second paragraph.
3.  **Empty Comment for Separation**:

    *   The example has a list item followed by an indented paragraph that should be a block quote.
        Use an empty comment to correctly separate the list item from the block quote.
4.  **Comment out a Directive**:

    *   There's an ``.. image::`` directive in the example. Temporarily "disable" it by
        turning it into a comment. (Hint: How can you make the parser treat the whole
        directive block as comment content?)

Observe how comments do not appear in the rendered output, and how empty comments
can affect the parsing of subsequent blocks.

# Lesson Example

This is the first paragraph of our example document.
It discusses various interesting topics.

This is the second paragraph. It continues the discussion.

*   A list item.
    This text is part of the list item.

    This indented paragraph should be a block quote,
    but it might be parsed as part of the list item above.
    Fix this using an empty comment.

Here is an image that we might want to temporarily remove using comments:

.. image:: /img/cat.png
   :alt: A cute cat
   :width: 100px

This is the final paragraph.
