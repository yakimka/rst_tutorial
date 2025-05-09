..
   _Chapter: 1. Introduction to reStructuredText
..
   _Next: 2_1_paragraphs_recap

=======================================
Lesson 1.3: The Escaping Mechanism (\\)
=======================================

Sometimes, you'll want to use characters that normally have a special meaning in
reStructuredText (like `*` for emphasis, or \`\` for inline literals) as
literal characters in your text. For example, you might want to write about
an asterisk itself, or show a command that uses backticks.

This is where the **escaping mechanism** comes in.

The Backslash (``\``)
---------------------
In reStructuredText, the backslash (``\``) is used as an escape character.
When you place a backslash before a character that has a special markup meaning,
it tells the reStructuredText parser to treat that character as a literal character,
not as markup.

For example:

*   If you write ``\*this\*``, it will appear as \*this\* (with literal asterisks)
    instead of *this* (emphasized).
*   If you write \\`\\`this\\`\\`, it will appear as \`\`this\`\` (with literal backticks)
    instead of ``this`` (inline literal).

Displaying a Literal Backslash
------------------------------
What if you want to display an actual backslash character? You escape it with
another backslash: ``\\`` will render as a single ``\``.

When to Use Escaping:
---------------------
You need to use the escaping mechanism when:

1.  You want to use a markup character (like ``*``, ``_``, ``|``) literally,
    and it's in a position where it might be interpreted as markup.
2.  You want to display a literal backslash character.

reStructuredText is often smart enough to know when a character isn't intended
as markup (e.g., an asterisk in the middle of a word like "example*word").
However, when in doubt, or when a character is at the beginning/end of a word
or surrounded by spaces in a way that could trigger markup, escaping is the way to go.

For further details, consult the `Escaping Mechanism <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#escape>`_
section in the official reStructuredText documentation.

**Your Task:**

The editor below contains text demonstrating escaping, along with some lines for you to modify.
Your task is to:

1.  **Modify the existing lines** at the end of the example as instructed by the comments within the example text:

    *   Change the line "This text should show *stars* not emphasis."
        so that the asterisks (``*``) are displayed literally and the text is not emphasized.
    *   Change the line "This text should show ``backticks`` not literal code."
        so that the backticks (\`\`) are displayed literally and the text is not treated as an inline literal.
    *   Ensure the file path "C:\\Users\\YourName." correctly displays literal backslashes.
2.  After modifying the existing lines, **add new sentences** to the example to further practice escaping:

    *   Add a new sentence that includes the exact phrase "my *word* here" but
        with the asterisks displayed literally (e.g., "This is my \*word\* here.").
    *   Add a new sentence that displays the characters "``literal_text``" including the literal backticks.
    *   Add a new sentence that explicitly shows how to represent a single literal backslash character,
        for example: "To show one backslash, you type two: \\\\".

Observe how your changes are rendered in the HTML output panel.

# Lesson Example

Sometimes you want to talk about markup characters themselves.
For example, to show a literal asterisk, you type \\\* like this: \*.
To show a literal backtick, you type \\\` like this: \`.

What if you want to show a backslash? You type \\\\ like this: \\.

Try to modify the text below to use escaping:

- This text should show *stars* not emphasis.
- This text should show ``backticks`` not literal code.
- This text should show a path like C:\\Users\\YourName.
