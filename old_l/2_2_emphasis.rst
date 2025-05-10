..
   _Chapter: 2. Basic Text Formatting (Inline Markup)
..
   _Next: 2_3_strong_emphasis

======================
Lesson 2.2: Emphasis
======================

In reStructuredText, **emphasis** is used to highlight text, typically rendering it in an *italic* font.
This is one of the most common forms of inline markup.

The syntax for emphasis is to surround the text with single asterisks: ``*text*``.

Key points for using emphasis:

*   **No Spaces:** The asterisks must be directly adjacent to the text being emphasized.
    There should be no space between the asterisk and the word(s) it's marking up.
    For example, ``*this is correct*``, but ``* this is not *``.
*   **Inline:** Emphasis is an inline markup, meaning it applies to text within a block-level
    element like a paragraph.
*   **Recognition:** The parser follows specific
    `inline markup recognition rules <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#inline-markup-recognition-rules>`_
    to distinguish emphasis from literal asterisks (e.g., in multiplication or pointers). Generally,
    if an asterisk is surrounded by whitespace or is part of a word without a matching
    closing asterisk, it won't be treated as emphasis.

For more details, you can refer to the official documentation on
`Emphasis <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#emphasis>`_
and the `:emphasis: role <https://docutils.sourceforge.io/docs/ref/rst/roles.html#emphasis>`_.

**Your Task:**

The editor below contains a few paragraphs of text. Your goal is to apply emphasis
to make certain words or phrases stand out.

1.  **Identify and Emphasize:**

    * Read through the provided text in the interactive section.
    * Choose at least three different words or short phrases that you think would benefit from emphasis.
    * Apply emphasis to them using the single asterisk syntax (e.g., ``*word*``).
2.  **Observe Correct Usage:**

    * Ensure that your emphasized text is rendered in italics in the output panel.
    * Try emphasizing a phrase that spans multiple words, like ``*a very important point*``.
3.  **Experiment with Incorrect Usage (Optional):**

    * Try putting a space between an asterisk and the word (e.g., ``* word*`` or ``*word *``).
    * Notice how it's likely not rendered as emphasis. This helps understand the "no spaces" rule.

# Lesson Example

This is a paragraph that contains some regular text.
Sometimes, you want to make certain words stand out.
For instance, the word 'important' is often a good candidate for emphasis.
Using emphasis correctly can greatly improve the readability of your document.

Another common use case is to highlight a specific term or concept the first time it is introduced.
This helps the reader to pay special attention to it.
Remember that reStructuredText aims to be both readable in its raw form and when rendered.
Proper use of inline markup like emphasis contributes to this goal.
Make sure you understand how to apply it.
