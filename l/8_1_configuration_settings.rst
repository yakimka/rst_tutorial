..
   _Chapter: 8. Configuration & Best Practices
..
   _Next: 8_2_style_and_readability_tips

======================================
Lesson 8.1: Configuration Settings
======================================

reStructuredText itself defines a markup syntax, but the way this syntax is processed
into a final document (like HTML or PDF) can be influenced by various **configuration settings**.
These settings are typically part of the Docutils processing system (or other systems like Sphinx
that use reStructuredText).

What are Configuration Settings?
--------------------------------
Configuration settings allow you to customize the behavior of the reStructuredText parser
and the output writers. They can affect:

*   How certain markup is interpreted (e.g., tab width).
*   How elements are rendered in the output (e.g., footnote style).
*   Whether certain features are enabled or disabled (e.g., stripping comments, syntax highlighting).
*   Security-related options (e.g., enabling file inclusion).

How are Settings Applied?
-------------------------
Configuration settings are usually applied outside of the ``.rst`` document itself. Common methods include:

*   **Command-line options**: When running a Docutils tool (like ``rst2html.py``),
    you can pass options.
*   **Configuration files**: Docutils can read settings from a configuration file
    (e.g., ``docutils.conf``).
*   **Programmatically**: If you're using Docutils as a library in your own Python
    code, you can set these options in your script.

**Note**: In this interactive tutorial environment, you cannot change these settings directly.
The purpose of this lesson is to make you aware that they exist and can influence the final output
when you use reStructuredText in other contexts.

Examples of Common Configuration Settings
-----------------------------------------
Here are a few examples of settings mentioned in the reStructuredText documentation:

*   **tab_width**:
    Determines how many spaces a tab character is converted to. Default is usually 8.
    Affects indentation and literal block formatting if tabs are used.
*   **footnote_references**:
    Controls how footnote references are displayed. Options might include "superscript"
    or "brackets". Example: ``[1]_`` could become a superscript ¹ or remain as [1].
*   **trim_footnote_reference_space**:
    If true, removes the space preceding a footnote reference when it's not needed
    (e.g., if the reference is already superscripted).
*   **character_level_inline_markup**:
    If true, relaxes the rules for inline markup recognition, allowing markup
    within words without explicit escaping.
    The default is usually false, requiring whitespace or punctuation around inline markup.
*   **strip_comments**:
    If true (often the default), comments are removed from the processed output.
    If false, they might be preserved (e.g., as HTML comments).
*   **syntax_highlight**:
    Used with the ``code`` directive and role. It can specify whether to use a syntax
    highlighter (like Pygments)
    and which style to apply. Common values are ``long`` (use Pygments) or ``short`` (no highlighting).
*   **file_insertion_enabled**:
    A security setting that controls whether directives like ``.. include::`` or ``.. raw::`` with the ``:file:`` option
    are allowed to read external files. Default is usually true, but can be disabled for security.
*   **raw_enabled**:
    A security setting that controls whether the ``.. raw::`` directive and ``:raw:`` role are enabled.
    Default is usually true, but can be disabled.

This is just a small sample. Docutils has many more settings that control various aspects of parsing and rendering.

Why Are They Important?
-----------------------
Understanding that configuration settings exist helps you:

*   Troubleshoot why your reStructuredText might render differently in different environments.
*   Customize the output to better suit your needs when you have control over the processing pipeline.
*   Be aware of security implications for certain features.

References:
-----------
*   `Docutils config <https://docutils.sourceforge.io/docs/user/config.html>`_
*   For a comprehensive list, you would typically consult the documentation of the
    specific Docutils tool or library you are using, often via ``--help`` or the
    Docutils website's configuration section.

# Lesson Example
