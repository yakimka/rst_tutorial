..
   _Chapter: 2. Basic Text Formatting (Inline Markup)
..
   _Next: 2_4_inline_literals

============================
Lesson 2.3: Strong Emphasis
============================

In reStructuredText, **strong emphasis** is used to give text more prominence than regular emphasis,
typically rendering it in a **bold** font. This is another fundamental form of inline markup.

The syntax for strong emphasis is to surround the text with double asterisks: ``**text**``.

Key points for using strong emphasis:

*   **No Spaces:** Like regular emphasis, the double asterisks must be directly adjacent to the
    text being strongly emphasized. There should be no space between the asterisks and the
    word(s) they mark up. For example, ``**this is correct**``, but ``** this is not **``.
*   **Inline:** Strong emphasis is an inline markup, applying to text within block-level
    elements such as paragraphs.
*   **Recognition:** The parser follows
    `inline markup recognition rules <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#inline-markup-recognition-rules>`_
    to distinguish strong emphasis from literal asterisks. Generally, if double asterisks
    are surrounded by whitespace or are part of a word without matching closing double
    asterisks, they won't be treated as strong emphasis.

For more details, you can refer to the official documentation on
`Strong Emphasis <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#strong-emphasis>`_
and the `:strong: role <https://docutils.sourceforge.io/docs/ref/rst/roles.html#strong>`_.

**Your Task:**

The editor below contains a few paragraphs of text. Your goal is to apply strong
emphasis to make certain words or phrases stand out significantly.

1.  **Identify and Strongly Emphasize:**

    * Read through the provided text in the interactive section.
    * Choose at least three different words or short phrases that you believe require
      strong emphasis (e.g., warnings, key commands, or very important notes).
    * Apply strong emphasis to them using the double asterisk syntax (e.g., ``**word**``).
2.  **Observe Correct Usage:**

    * Ensure that your strongly emphasized text is rendered in bold in the output panel.
    * Try strongly emphasizing a phrase that spans multiple words, like ``**a very critical warning**``.
3.  **Distinguish from Regular Emphasis:**

    * If you completed the previous lesson on emphasis, consider when you would use
      strong emphasis (``**text**``) versus regular emphasis (``*text*``). Strong
      emphasis is for a higher level of prominence.

# Lesson Example

This paragraph contains some important information.
Sometimes, you need to make a statement **unmistakably clear**.
For instance, the command **sudo rm -rf /** is **extremely dangerous** and should
**never** be run without understanding its full implications.

Another use case for strong emphasis is to highlight **critical warnings** or **safety notices**.
This helps the reader to immediately recognize the significance of the message.
Remember that reStructuredText aims for readability in both raw and rendered forms.
Proper use of strong emphasis contributes to this by making **vital information** pop out.
Make sure you understand how to apply it effectively.
It is **crucial** to use strong emphasis sparingly to maintain its impact.
