..
   _Chapter: 2. Basic Text Formatting (Inline Markup)
..
   _Next: 2_6_recognition_order_for_inline_markup

===============================================
Lesson 2.5: Inline Markup Recognition Rules
===============================================

In reStructuredText, inline markup constructs like *emphasis*, **strong emphasis**,
and ``inline literals`` use special characters (\* and \`).
To avoid confusing these with ordinary text (multiplication signs, pointers, code ticks),
reST applies precise rules to decide when to interpret these sequences as markup.

Core Rules
----------

1. **Adjacency at start**: The opening marker ("*", "**", or "``") must be followed immediately
   by a non-whitespace character (e.g., ``*word``, not ``* word``).
2. **Adjacency at end**: The closing marker must be preceded immediately by a non-whitespace character
   (e.g., ``word*``, not ``word *``).
3. **Non-empty content**: There must be at least one character between the opening and closing
   markers (so ``**`` alone is not valid strong emphasis).
4. **No escaping**: The marker must not be preceded by an unescaped backslash (``\``).
   (Inline literals are an exception: their closing backticks can be escaped.)
5. **Punctuation context**: If the opening marker is preceded by an opening punctuation
   character (one of ``(``, ``[``, ``{``, ``<``, ``'``, ``"``),
   it must not be followed by the matching closing punctuation (so ``(*text*)``
   works but ``(*)`` does not count as emphasis).

Surrounding Context (Default)
-----------------------------

By default (unless you enable character-level inline markup), additional restrictions apply
to what can appear around the markers:

- **Before opening marker**: start of line, whitespace, or one of ``- : / ' " < ( [ {``.
- **After closing marker**: end of line, whitespace, or one of ``- . , : ; ! ? \ / ' " ) ] } >``.

These prevent applying emphasis in the middle of words without explicit enabling of
character-level inline markup.

Character-Level Inline Markup
-----------------------------

Enabling `character-level inline markup` in configuration relaxes the surrounding context rules above,
allowing emphasis inside words (e.g., ``em*pha*sis``).
However, this can lead to accidental markup if your text contains stray markers.

Escaping Markup Characters
--------------------------

Use a backslash (``\*`` or ``\````) to treat markup characters literally. For example:

- Write ``5*3=15`` to show "5*3=15".
- Write ``He said \`\`hello\`\` to her.`` to show double backticks literally.

References
----------

- `Inline markup recognition rules <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#inline-markup-recognition-rules>`_
- `Character-Level Inline Markup <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#character-level-inline-markup>`_

# Lesson Example

Below are examples. Edit them to see how the rules apply in practice.

This is *correctly emphasized text*.
This is **correctly strong text**.
This is ``correctly literal text``.

The expression (a*b) + c should show literal asterisks.
The file is named report.*.txt.
Is this * a single asterisk? Or this one*?

Consider the C code: char* ptr = NULL;

And a Python docstring: """This is a ````docstring````."""

Can you make *part*ofaword* emphasized?  (tries inline without enabling character-level)
