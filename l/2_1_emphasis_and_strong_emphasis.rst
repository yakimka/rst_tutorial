..
   _Chapter: 2. Basic Text Formatting (Inline Markup)
..
   _Next: 2_2_inline_literals

====================================================
Lesson 2.1: Emphasis (*) and Strong Emphasis (**)
====================================================

In reStructuredText, you can highlight text in two main ways: *emphasis* and **strong emphasis**.
These are fundamental forms of inline markup, used to draw attention to specific words or phrases.

Emphasis (Italics)
------------------
Emphasis is typically rendered as *italic text*. It's used for gentle highlighting,
like when introducing a new term or for subtle stress.

The syntax for emphasis is to surround the text with single asterisks: ``*text*``.

Key points for emphasis:

*   **No Spaces**: The asterisks must be directly adjacent to the text being emphasized.
    There should be no space between the asterisk and the word(s) it's marking up.
    For example, ``*this is correct*``, but ``* this is not *``.
*   **Inline**: Emphasis applies to text within a block-level element like a paragraph.

Strong Emphasis (Bold)
----------------------
Strong emphasis is used for a higher level of prominence, typically rendering text in a
**bold font**. Use it for important warnings, key terms that need to stand out significantly,
or any text that requires strong visual weight.

The syntax for strong emphasis is to surround the text with double asterisks: ``**text**``.

Key points for strong emphasis:

*   **No Spaces**: Similar to regular emphasis, the double asterisks must be directly
    adjacent to the text. For example, ``**this is correct**``, but ``** this is not **``.
*   **Inline**: Strong emphasis is also an inline markup.
*   **Sparing Use**: Use strong emphasis judiciously. Overuse can diminish its impact and
    make text harder to read.

Recognition Rules
-----------------
The parser follows specific `inline markup recognition rules`_ to distinguish emphasis
and strong emphasis from literal asterisks (e.g., in multiplication or pointers).
Generally, if asterisks are surrounded by whitespace or are part of a word without
matching closing asterisks, they won't be treated as markup. We'll cover these rules
in more detail in a later lesson.

References:
-----------
*   `Emphasis <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#emphasis>`_
*   `Strong Emphasis <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#strong-emphasis>`_
*   `Inline markup recognition rules <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#inline-markup-recognition-rules>`_
*   Standard roles: `:emphasis: <https://docutils.sourceforge.io/docs/ref/rst/roles.html#emphasis>`_
    and `:strong: <https://docutils.sourceforge.io/docs/ref/rst/roles.html#strong>`_

**Your Task:**

Your task is to modify text in interactive editor and apply both
emphasis and strong emphasis to make certain words or phrases stand out appropriately.

1.  **Apply Emphasis**:

    *   Read through the provided text.
    *   Choose at least two different words or short phrases that you think would benefit
        from *gentle emphasis* (italics).
    *   Apply emphasis to them using the single asterisk syntax (e.g., ``*word*``).
2.  **Apply Strong Emphasis**:

    *   Identify at least two different words or short phrases that require **strong emphasis**
        (bold), such as a critical point or an important term.
    *   Apply strong emphasis to them using the double asterisk syntax (e.g., ``**word**``).
3.  **Observe Correct Usage**:

    *   Ensure that your emphasized text is rendered in italics and your strongly
        emphasized text is rendered in bold in the output panel.
    *   Try emphasizing a phrase that spans multiple words, like ``*a very important point*``
        or ``**a critical warning**``.
4.  **Experiment (Optional)**:

    *   Try putting a space between an asterisk and a word (e.g., ``* word*`` or ``** word **``).
        Notice how it's likely not rendered as emphasis. This helps understand the "no spaces" rule.

# Lesson Example

This is a paragraph that contains some regular text.
Sometimes, you want to make certain words stand out.
For instance, the word 'important' is often a good candidate for emphasis.
Using emphasis correctly can greatly improve the readability of your document.

Another common use case is to highlight a specific term or concept the first time it is introduced.
This helps the reader to pay special attention to it.
Remember that reStructuredText aims to be both readable in its raw form and when rendered.
Proper use of inline markup like emphasis contributes to this goal.

Sometimes, you need to make a statement unmistakably clear.
For instance, the command sudo rm -rf / is extremely dangerous and should
never be run without understanding its full implications.
This is a crucial piece of information.
Make sure you understand how to apply these styles effectively.
It is vital to use strong emphasis sparingly to maintain its impact.
