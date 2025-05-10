..
   _Chapter: 1. Introduction to reStructuredText
..
   _Next: 1_2_basic_syntax

=====================================
Lesson 1.1: What is reStructuredText?
=====================================

Welcome to the interactive reStructuredText tutorial!

reStructuredText (often abbreviated as RST, ReST, or reST) is a lightweight markup language.
It's designed to be easy to read in its plain text form, which means you can understand the
structure even before it's converted into other formats like HTML or PDF. Tools like Docutils_
are used for this conversion.

Think of it as a way to write structured documents (like articles, documentation, or even books)
using simple text conventions that you can type in any basic text editor.

Key Characteristics:
--------------------

*   **Plain Text First**: The raw reStructuredText you write should be easily readable on its own.
    The markup symbols are chosen to be unobtrusive.
*   **Simple Syntax**: It uses straightforward patterns for common formatting needs.
    For example, blank lines separate paragraphs, and asterisks are used for *emphasis*.
*   **Extensible**: For more complex needs, reStructuredText uses "directives" – special
    commands that can create things like tables, images, or specially formatted blocks of text.
*   **Widely Used**: It's a popular choice for software documentation
    (including Python's own documentation), project README files, and any situation where
    you need to create well-structured documents from plain text.

The Goal of reStructuredText:
-----------------------------

The main idea behind reStructuredText is to offer a markup system that is:

1.  **Readable**: Both in its raw source form and in its processed form.
2.  **Unobtrusive**: The markup symbols should blend in with the text as much as possible.
3.  **Intuitive**: The syntax should be easy to learn and remember.
4.  **Powerful**: Capable of representing complex document structures.

In this tutorial, we'll explore these features step by step, starting with the very basics.

References:
-----------

*   `A ReStructuredText Primer <https://docutils.sourceforge.io/docs/user/rst/quickstart.html>`_
*   `reStructuredText Markup Specification <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html>`_
*   `Docutils Project <https://docutils.sourceforge.io/>`_

**Your Task:**

Your task is to modify text in interactive editor to get comfortable with the basics. Try the following:

1.  **Add a new paragraph**: After the existing paragraphs, write a short sentence about
    what you hope to learn from this tutorial. Remember, paragraphs are separated by blank lines.
2.  **Apply emphasis**: In one of the original paragraphs, choose some words and make them
    *emphasized* (italic) using single asterisks (e.g., ``*text*``).
3.  **Apply strong emphasis**: In another original paragraph, select different words and make them
    **strongly emphasized** (bold) using double asterisks (e.g., ``**text**``).
4.  **Use inline literal text**: Add a new sentence to any paragraph (or your new paragraph) that
    includes ``inline literal text``. This is done with double backticks. For example,
    ````text```` is often used for code or commands. For instance, you could write:
    "I want to learn how to use the \`\`.. image::\`\` directive."

Observe how your changes are rendered in the HTML output panel as you type. Don't worry about
making mistakes; that's part of learning!

.. _Docutils: https://docutils.sourceforge.io/

# Lesson Example

This is a simple paragraph in reStructuredText.
It's written in plain text, and designed to be readable.

This is another paragraph.
Paragraphs are separated by one or more blank lines.
Notice how the structure is clear even without any special rendering.

You can easily create *emphasized text* (usually shown as italics)
or **strongly emphasized text** (usually shown as bold).
For code snippets or to show text exactly as it is, without interpreting
any special characters, you can use ``inline literal text``.

Feel free to modify this example and see the results instantly!
This interactive editor is here to help you learn.
Try adding a new paragraph below this one.
