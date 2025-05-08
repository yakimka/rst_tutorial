.. default-role:: literal

=====================================
Lesson 1.1: What is reStructuredText?
=====================================

Welcome to the first lesson!

reStructuredText (often abbreviated as RST, ReST, or reST) is a lightweight markup language designed to be both:

1.  **Readable by humans** in its raw, plain text form.
2.  **Processable into various formats** (like HTML, PDF, etc.) by software, most notably the Docutils_ library.

Key Characteristics
-------------------

*   **Plain Text**: You write reStructuredText in any plain text editor.
*   **Simple Constructs**: It uses simple and intuitive patterns (like asterisks for emphasis,
    or blank lines to separate paragraphs) to indicate the structure of a document.
*   **Extensible**: While the core syntax is simple, reStructuredText can be extended with
    "directives" to support more complex structures like tables, images, and code blocks.
*   **Widely Used**: It's commonly used for technical documentation (including Python's official documentation),
    README files, and anywhere structured plain text is needed.

The Goal
--------

The goal of reStructuredText is to provide a markup syntax that is easy to write and read without
any special tools, yet powerful enough to create well-structured documents.
The markup should be as unobtrusive as possible.

This tutorial will guide you through the various features of reStructuredText,
starting with the basics.

.. _Docutils: https://docutils.sourceforge.io/

# -Example-
This is a simple paragraph in reStructuredText.

This is another paragraph. Notice the blank line separating them.

You can use *emphasis* (italics) or **strong emphasis** (bold).
You can also write ``inline literal text``, which is often used for code snippets.
