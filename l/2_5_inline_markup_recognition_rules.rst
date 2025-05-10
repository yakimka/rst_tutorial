..
   _Chapter: 2. Basic Text Formatting (Inline Markup)
..
   _Next: 2_6_recognition_order_for_inline_markup

==============================================
Lesson 2.5: Inline Markup Recognition Rules
==============================================

You've learned about emphasis (``*text*``), strong emphasis (``**text**``), and
inline literals (````text````). These constructs use special characters (asterisks
and backticks) to define their boundaries. However, these characters are also
common in everyday text (e.g., for multiplication, pointers, or as part of
code).

To avoid ambiguity, reStructuredText has a precise set of **inline markup
recognition rules**. These rules determine when a sequence of characters is
treated as markup and when it's treated as literal text.

Core Recognition Rules:

Inline markup start-strings (like ``*``, ``**``, or :literal:\`\`) and end-strings are
generally recognized if:

1.  **Start-string Adjacency:** The start-string is immediately followed by
    non-whitespace. (e.g., ``*word``, not ``* word``)
2.  **End-string Adjacency:** The end-string is immediately preceded by
    non-whitespace. (e.g., ``word*``, not ``word *``)
3.  **Non-empty Content:** The end-string is separated by at least one character
    from the start-string. (e.g., ``**`` is not strong emphasis)
4.  **No Escaping (Usually):** Neither the start-string nor the end-string is
    preceded by an unescaped backslash (``\``). (The end-string of inline
    literals is an exception to this part of the rule regarding backslashes).
5.  **Context with Punctuation:** If a start-string is immediately preceded by
    an opening punctuation character (like ``(``, ``[``, ``{``, ``<``, ``'``, ``"``),
    it must not be immediately followed by the corresponding closing punctuation.
    (e.g., ``(*text*)`` is fine, but ``(*)`` would not be emphasis).

Additional Rules (Default Behavior):

By default (when
`character-level inline markup <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#character-level-inline-markup>`_
is not enabled), there are
stricter rules about the characters surrounding the markup:

6.  **Preceding Context:** The start-string must either start a text block or be
    immediately preceded by whitespace or one of the characters:
    ``- : / ' " < ( [ {``.
7.  **Following Context:** The end-string must either end a text block or be
    immediately followed by whitespace or one of the characters:
    ``- . , : ; ! ? \ / ' " ) ] } >``.

These rules (6 and 7) mean that, by default, you cannot easily apply inline
markup to parts of words without using `character-level inline markup`_ techniques.
For example, ``em*pha*sis`` would not typically work to emphasize "pha".

Character-Level Inline Markup:

reStructuredText allows for
`character-level inline markup <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#character-level-inline-markup>`_
using backslash-escapes to separate the markup from adjacent text if needed (e.g., ``*word*\s``).
This can be useful but is often less readable in the raw text.
There's also a configuration setting
(`character_level_inline_markup <https://docutils.sourceforge.io/docs/user/config.html#character-level-inline-markup>`_)
that can relax rules 6 and 7, making it easier to mark up parts of words but potentially
leading to more false positives if not careful.

Understanding these rules helps you predict how your text will be rendered and
how to use escaping (``\``) when you need to use markup characters literally.

For a comprehensive explanation, refer to the official documentation on
`Inline markup recognition rules <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#inline-markup-recognition-rules>`_
and `Character-Level Inline Markup <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#character-level-inline-markup>`_.

**Your Task:**

The editor below contains various examples. Your goal is to observe how the inline
markup recognition rules apply and to experiment with them.

1.  **Observe Existing Examples:**

    * Examine the pre-filled text in the interactive section.
    * Identify which instances of ``*text*``, ``**text**``, or ````text````
      are correctly rendered as emphasis, strong emphasis, or literals.
    * Identify which of these are not.
    * Try to explain *why* some are not rendered as markup, based on the
      rules above.
2.  **Test the Rules:**

    * Modify some of the "incorrect" examples to make them valid markup.
    * For instance, if ``* text *`` doesn't work, change it to ``*text*``.
    * Try to apply emphasis to only part of a word, like making "pha"
      italic in "emphasis".
    * See if it works by default.
    * Then, try to make it work using a backslash escape (e.g.,
      ``em\*pha*\sis`` - this might be tricky and is just for
      experimentation with the concept).
3.  **Experiment with Escaping:**

    * In a sentence like "The result is 5*3=15.", ensure the asterisk is
      treated literally and not as emphasis.
    * If it's being misinterpreted, use a backslash (``\*``) to escape it.
    * Try to write a sentence that includes literal double backticks, e.g.,
      ``He said ````hello```` to her.``
    * You might need to think about how inline literals are defined.

# Lesson Example

This is *correctly emphasized text*.
This is **correctly strong text**.
This is ``correctly literal text``.

However, * this is not emphasized* due to leading/trailing spaces.
And *this is also not * emphasized.
What about *this*one? (Rule 7: no following whitespace/punctuation)
Or this*one*? (Rule 6: no preceding whitespace/punctuation)

The expression (a*b) + c should show literal asterisks.
The file is named report.*.txt.
Is this * a single asterisk? Or this one*?

Consider the C code: char* ptr = NULL;
And a Python docstring: """This is a ````docstring````."""

Can you make *part*ofaword* emphasized?
Try to write a literal asterisk: \*.
What about a literal backslash before an asterisk: \\\*?

The function call is ``my_func(*args, **kwargs)``.
He said (``hello``) to her.
This should be ``literal with *asterisks* inside``.
