..
   _Chapter: 2. Basic Text Formatting (Inline Markup)
..
   _Next: 3_1_bulleted_and_enumerated_lists

========================================
Lesson 2.4: Escaping Markup Characters
========================================

In reStructuredText, certain characters like ``*``, ``````, and ``_`` have special
meanings for inline markup. But what if you want to use these characters literally
in your text, without them triggering emphasis, inline literals, or hyperlinks?
This is where the **escaping mechanism** comes in.

The Backslash (``\``) as an Escape Character
--------------------------------------------
The primary way to escape a character in reStructuredText is by preceding it
with a backslash (``\``). When the parser encounters a backslash followed by
a character that normally has a markup meaning, it treats that character as a
literal character instead of interpreting it as markup.

Common Scenarios:
-----------------

1.  **Literal Asterisks**:
    If you want to write \*this\* and have the asterisks appear literally,
    you would type ``\*this\*``. Without the backslashes, it would become
    *this* (emphasized).

2.  **Literal Backticks**:
    To display literal double backticks, like \`\`this\`\`, you would type
    \\`\\`this\\`\\`. Without escaping, ``this`` would be an inline literal.
    For a single literal backtick, use \`.

3.  **Literal Underscores for Hyperlinks**:
    If you have a word that ends with an underscore but it's not meant to be
    a hyperlink, like my_variable\_, you would write my_variable\\_.

4.  **Displaying a Literal Backslash**:
    To show an actual backslash character in your output, you need to escape
    it with another backslash. So, \\\\ in your source text will render as
    a single \\ in the output.

When to Use Escaping:
---------------------
You generally need to use escaping when:

*   A character with markup significance appears in a context where it could be
    interpreted as markup (e.g., an asterisk at the start/end of a word that
    you don't want to be emphasis).
*   You explicitly want to show the markup character itself.
*   You want to display a literal backslash.

reStructuredText is often smart enough to figure out when a character isn't
intended as markup (e.g., an asterisk in example*word or in 5 * 3 = 15).
However, when in doubt, or if the parser is misinterpreting your text,
escaping is the solution.

Whitespace and Escaping:
------------------------
Backslash-escaped whitespace characters are removed from the output. This can be
used for `character-level inline markup`_ (joining marked-up text directly to
surrounding text without spaces), but this is an advanced and often less readable
technique.

References:
-----------
*   `Escaping Mechanism <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#escaping-mechanism>`_
*   `Character-Level Inline Markup <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#character-level-inline-markup>`_

**Your Task:**

The editor below contains text with several instances where characters should be
displayed literally but might be misinterpreted as markup. Your task is to apply
the escaping mechanism correctly.

1.  **Literal Asterisks**:

    *   Modify the line ``This text should show *stars* around words.`` so that the
        asterisks appear literally around "stars".
    *   In the sentence ``The C code uses a pointer like *ptr.``, ensure the asterisk
        is literal.
2.  **Literal Backticks**:

    *   Change ``Show these ``as literal backticks``.`` so the double backticks are
        displayed.
3.  **Literal Underscores**:

    *   The variable ``temp_value_`` should not be a hyperlink. Fix it.
4.  **Literal Backslashes**:

    *   Correct the Windows path ``C:\Users\Default`` to display the backslashes.
5.  **Add New Examples**:

    *   Add a new sentence that demonstrates how to write the literal sequence ``**not bold**``.
    *   Add a new sentence showing how to display a single literal backslash character.

Observe how your changes are rendered in the HTML output panel.

# Lesson Example
.. code-block::

    This text should show *stars* around words.
    The C code uses a pointer like *ptr.

    Show these ``as literal backticks``.

    The variable temp_value_ is important.

    A common Windows path is C:\Users\Default.

    Sometimes you need to write about reStructuredText itself, like how an _`internal target` looks.
    Or maybe you want to show a multiplication: 5 * 3 = 15. (This usually works fine!)
