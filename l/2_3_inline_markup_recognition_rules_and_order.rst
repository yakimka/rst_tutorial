..
   _Chapter: 2. Basic Text Formatting (Inline Markup)
..
   _Next: 2_4_escaping_markup_characters

=========================================================
Lesson 2.3: Inline Markup Recognition Rules and Order
=========================================================

In reStructuredText, inline markup constructs like *emphasis*, **strong emphasis**,
and ``inline literals`` use special characters (``*``, ``**``, ``````).
To avoid confusing these with ordinary text (like multiplication signs, pointers, or literal backticks),
reStructuredText applies precise rules to decide when to interpret these sequences as markup.
Additionally, there's a specific order in which these rules are applied.

Core Recognition Rules
----------------------

For a sequence to be recognized as inline markup, generally:

1.  **Adjacency at Start**: The opening marker (e.g., ``*``, ``````) must be immediately
    followed by a non-whitespace character (e.g., ``*word``, not ``* word``).
2.  **Adjacency at End**: The closing marker must be immediately preceded by a
    non-whitespace character (e.g., ``word*``, not ``word *``).
3.  **Non-empty Content**: There must be at least one character between the opening
    and closing markers (so ``**`` alone is not valid strong emphasis).
4.  **No Escaping**: The marker must not be preceded by an unescaped backslash (``\``).
    (Inline literals are an exception for their closing backticks).
5.  **Punctuation Context**: If an opening marker is preceded by an opening punctuation
    character (like ``(``, ``[``, ``{``, ``'``, ``"``), it must not be immediately
    followed by the matching closing punctuation (so ``(*text*)`` works, but ``(*)``
    does not become emphasis).

Surrounding Context (Default Behavior)
--------------------------------------
By default, additional restrictions apply to what can appear around the markers,
preventing markup in the middle of words unless `character-level inline markup`_
is explicitly enabled (which is an advanced topic and can lead to accidental markup).

*   **Before opening marker**: Must be the start of a line, whitespace, or one of
    ``- : / ' " < ( [ {``.
*   **After closing marker**: Must be the end of a line, whitespace, or one of
    ``- . , : ; ! ? \ / ' " ) ] } >``.

Recognition Order
-----------------
When multiple interpretations are possible, reStructuredText follows a specific order:

1.  **Asterisks (*)**:

    *   `Strong emphasis`_ (``**text**``) is recognized before `emphasis`_ (``*text*``).
        So, ``***text***`` is usually parsed as strong emphasis around ``*text*`` or vice-versa,
        resulting in bold italic.
2.  **Backquotes (``)**:

    *   `Inline literals`_ (````text````) and `Inline internal targets`_ (``_`target```)
        are checked first and are independent of each other.
    *   Then, phrase `hyperlink references`_ (``` `Link text`_ ```).
    *   Finally, `interpreted text`_ (``` `text` ``` or ``` :role:`text` ```).
3.  **Trailing Underscores (_)**:

    *   `Footnote references`_ (``[label]_``) and simple `hyperlink references`_ (``name_``)
        are distinct due to the brackets in footnotes.
4.  **Vertical Bars (|)**:

    *   `Substitution references`_ (``|text|``) are recognized independently.
5.  **Standalone Hyperlinks**:

    *   `Standalone hyperlinks`_ (like ``https://example.com``) are recognized last.

Understanding these rules and the order helps predict how reStructuredText will interpret
your text and how to use escaping (covered in the next lesson) when you need literal characters.

References:
-----------
*   `Inline markup recognition rules <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#inline-markup-recognition-rules>`_
*   `Recognition order <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#recognition-order>`_
*   `Character-Level Inline Markup <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#character-level-inline-markup>`_

**Your Task:**

1.  **Predict Rendering**: Examine each line in the interactive section.
    Based on the rules and order discussed, predict how reStructuredText will render it.
2.  **Test Adjacency & Context Rules**:

    *   In the "Rule Testing: Adjacency & Context" part of the example:

        *   Why do the lines under "Invalid due to spacing" (e.g., ``Try: * spaced emphasis *``)
            fail to produce the intended markup? Correct one of them by removing the internal spaces.
        *   Why aren't the asterisks in ``report.*.txt`` treated as markup?
        *   In the "Experiment Zone", try to make the ``*`` in ``report.*.txt`` emphasized.
            (Hint: you might need to use escaping)
3.  **Test Recognition Order**:

    *   In the "Recognition Order Testing" part:

        *   How is ``***bold***`` and  ``**``not code``**`` rendered?
4.  **Use the Experiment Zone**:

    *   Add your own examples to test other rules. For instance, try ``(*text*)`` versus ``(*)``.
    *   Can you create a situation where ``word*`` (an asterisk directly after a word without
        following whitespace) is *not* markup, and then make it markup?

.. _emphasis: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#emphasis
.. _strong emphasis: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#strong-emphasis
.. _inline literals: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#inline-literals
.. _inline internal targets: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#inline-internal-targets
.. _hyperlink references: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#hyperlink-references
.. _interpreted text: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#interpreted-text
.. _footnote references: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#footnote-references
.. _substitution references: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#substitution-references
.. _standalone hyperlinks: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#standalone-hyperlinks

# Lesson Example

--- Rule Testing: Adjacency & Context ---

Valid examples:

- This is *emphasized*.
- This is **strong**.
- This is ````literal````.

Invalid due to spacing (Rule 1 & 2 - non-whitespace adjacency):

- Try: * spaced emphasis *
- Try: ** spaced strong **
- Try: `` spaced literal ``

Default surrounding character restrictions:

- Filename: report.*.txt (Is ``*`` emphasized here?)
- Math: 2*3=6 (Is ``*`` emphasized?)
- Thisis*not*emphasis. (Markup in middle of word)

--- Recognition Order Testing ---

- This is ***bold***.
- This is **``not code``**

--- Experiment Zone ---

Add your own tests below.
For example:

- Try to make part of "report.*.txt" italic using escaping.
- Test word* (no space after asterisk).
