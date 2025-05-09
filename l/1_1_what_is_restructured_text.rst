..
   _Chapter: 1. Introduction to reStructuredText
..
   _Next: 1_2_basic_syntax

=====================================
Lesson 1.1: What is reStructuredText?
=====================================

Welcome to the interactive reStructuredText tutorial!

reStructuredText (often abbreviated as RST, ReST, or reST) is a lightweight markup language.
It's designed to be easy to read in its plain text form and can be converted into various other
formats like HTML or PDF using tools like Docutils_.

Think of it as a way to write structured documents (like articles, documentation, or even books)
using simple text conventions that you can type in any basic text editor.

Key Characteristics:
--------------------

*   **Plain Text First**: The raw reStructuredText you write should be easily readable on its own.
*   **Simple Syntax**: It uses straightforward patterns for common formatting needs.
    For example, blank lines separate paragraphs, and asterisks are used for emphasis.
*   **Extensible**: For more complex needs, reStructuredText uses "directives" – special
    commands that can create things like tables, images, or specially formatted blocks of text.
*   **Widely Used**: It's a popular choice for software documentation
    (including Python's own documentation), project README files, and any situation where
    you need to create well-structured documents from plain text.

The Goal of reStructuredText:
-----------------------------

The main idea behind reStructuredText is to offer a markup system that is:

1.  **Unobtrusive**: The markup symbols should blend in with the text as much as possible.
2.  **Intuitive**: The syntax should be easy to learn and remember.
3.  **Powerful**: Capable of representing complex document structures.

In this tutorial, we'll explore these features step by step.

.. _Docutils: https://docutils.sourceforge.io/

**Your Task:**

The example text below is pre-loaded in the interactive editor.
Your task is to modify this existing text. Try the following:

1.  Add a new paragraph of your own after the existing paragraphs.
    For example, write a short sentence about what you hope to learn.
2.  In one of the original paragraphs (like the first or second one),
    select some words and make them *emphasized* (italic).
    Then, select different words in another original paragraph and make them
    **strongly emphasized** (bold).
3.  Add a new sentence to any paragraph (or your new paragraph) that
    includes ``inline literal text``. For instance, you could write:
    "I want to learn how to use the ``.. code-block::`` directive."

Observe how your changes are rendered in the HTML output panel as you type.

# Lesson Example

This is a simple paragraph in reStructuredText.
It's written in plain text.

This is another paragraph.
Paragraphs are separated by one or more blank lines.

You can easily create *emphasized text* (usually shown as italics)
or **strongly emphasized text** (usually shown as bold).
For code snippets or to show text exactly as it is, you can use ``inline literal text``.

Feel free to modify this example and see the results instantly!
This interactive editor is here to help you learn.
