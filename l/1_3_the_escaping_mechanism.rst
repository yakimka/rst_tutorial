..
   _Chapter: 1. Introduction to reStructuredText
..
   _Next: 2_1_paragraphs_recap

=======================================
Lesson 1.3: The Escaping Mechanism (\\)
=======================================

Sometimes, you'll want to use characters that normally have a special meaning in
reStructuredText (like `*` for emphasis, or ``` `` ``` for inline literals) as
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
*   If you write `\``this`\``, it will appear as \`this\` (with literal backticks)
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

**Your Task:**

In the example editor below:

1.  Write a sentence that includes the phrase "literal \*asterisks\* around a word"
    where the asterisks are visible.
2.  Write a sentence that displays "a literal \`backtick\` character".
3.  Write a sentence that shows how to represent "a single literal backslash: \\".
4.  Try to write the text `*emphasized*` without it being emphasized, and then
    write \`\`literal\`\` without it being treated as an inline literal.

# Lesson Example

Sometimes you want to talk about markup characters themselves.
For example, to show a literal asterisk, you type \\\* like this: \*.
To show a literal backtick, you type \\\` like this: \`.

What if you want to show a backslash? You type \\\\ like this: \\.

Try to modify the text below to use escaping:
This text should show *stars* not emphasis.
This text should show ``backticks`` not literal code.
This text should show a path like C:\\Users\\YourName.
