..
   _Chapter: 2. Basic Text Formatting (Inline Markup)
..
   _Next: 2_2_emphasis

================================
Lesson 2.1: Paragraphs (Recap)
================================

In reStructuredText, a **paragraph** is one of the most fundamental building
blocks. It's simply a chunk of text separated from other blocks by one or more
blank lines.

Key things to remember about paragraphs:

*   **Separation:** Paragraphs are separated by at least one blank line.
    Multiple blank lines are treated as a single blank line for separation.
*   **Alignment:** Lines within the same paragraph must have the same level of
    indentation (usually, this means they all start at the left margin).
*   **Indentation:** If a paragraph is indented, it's typically interpreted as
    a block quote, not just an indented paragraph in the typical word-processing
    sense. Consistent indentation is crucial.

Paragraphs can contain various inline markup elements, which we'll cover in
upcoming lessons (like emphasis, strong emphasis, inline literals, etc.). For now,
let's focus on creating simple text paragraphs.

**Your Task:**

In the editor below:

1.  Create at least three distinct paragraphs.
2.  Make one of your paragraphs consist of multiple lines of text.
3.  Try indenting one of your paragraphs (e.g., by 4 spaces) and observe how
    it's rendered (it should look like a block quote).
4.  Ensure there's at least one blank line separating each paragraph and the
    indented block.

# Lesson Example

This is the first paragraph. It's a simple block of text.
Remember that paragraphs are separated by blank lines.

This is a second paragraph. It can contain multiple sentences
and will continue as long as the text is contiguous and shares
the same indentation level. If you want to start a new line
within the same paragraph, just hit enter and keep typing.

    This paragraph is indented.
    In reStructuredText, an indented paragraph like this
    is usually treated as a block quote.

And this is a third paragraph, back at the main indentation level.
It appears after the block quote because there's a blank line
above it and it's not indented.
