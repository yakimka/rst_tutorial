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

1.  **Examine the Examples**: Look at the text in the interactive section.
    Try to predict how each line will be rendered based on the rules and order described above.
    Pay attention to spacing and surrounding characters.
2.  **Test the Rules**:

    *   Modify "This is *correctly emphasized text*." by adding a space after the
        opening asterisk (e.g., ``* correctly...``). What happens?
    *   In "The file is named report.*.txt.", try to make ``*`` emphasized. What do you
        need to do if the default rules prevent it? (Hint: escaping might be needed,
        or this might illustrate a case where it's hard without character-level markup).
3.  **Test Recognition Order**:

    *   How does ``***triple asterisks***`` render? Try to make it ``**bold**`` around ``*italic*``
        and then ``*italic*`` around ``**bold**``.
    *   What happens if you write `````` ````NotALink`_```` ``````? Is it a literal or a hyperlink?
        How can you force it to be one or the other if the default isn't what you want?
4.  **Experiment**: Try creating your own examples that test the boundaries of these rules.
    For example, can you create a situation where an intended inline literal is
    misinterpreted as a hyperlink or interpreted text?

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

This is *correctly emphasized text*.
This is **correctly strong text**.
This is ````correctly literal text````.

The expression (a*b) + c should show literal asterisks.
The file is named report.*.txt.
Is this * a single asterisk?

Consider the C code: char* ptr = NULL;
And a Python docstring: """This is a ````docstring````."""

--- Recognition Order Examples ---

This is ``***triple asterisks***``.

This is ``` `a phrase link`_ ```.
This is ````a literal with backquotes````.
This is also ```an interpreted text```. (Uses the default role)

What about `literal_with_underscore`_?
And ````literal_with_underscore_````?

A footnote [1]_ and a link_ use trailing underscores.

A substitution |subst| and a linked substitution |subst_link|_.

A standalone link: https://docutils.sourceforge.io/
An email: user@example.com

.. _a phrase link: https://example.com/phrase
.. _literal_with_underscore: https://example.com/target1
.. [1] This is a footnote.
.. _link: https://docutils.sourceforge.io/
.. |subst| replace:: example text
.. |subst_link| replace:: linked example
.. _subst_link: https://example.com/subst_target
