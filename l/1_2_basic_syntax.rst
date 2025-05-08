..
   _Chapter: 1. Introduction to reStructuredText

==================================================================
Lesson 1.2: Basic Syntax - Paragraphs, Blank Lines, & Indentation
==================================================================

In reStructuredText, the structure of your document is largely defined by how you arrange text,
blank lines, and indentation. Let's explore these fundamental concepts:

**1. Paragraphs:**
   Paragraphs are the most basic block of text. They are simply chunks of text separated by one or more blank lines. There's no special markup needed to indicate a paragraph.

**2. Blank Lines:**
   Blank lines are crucial in reStructuredText. They are not just for visual spacing; they are significant for parsing.
   - A single blank line separates paragraphs.
   - Multiple blank lines are treated the same as a single blank line between paragraphs.
   - Blank lines are also used to separate other block-level elements like lists, block quotes, section titles, etc., from surrounding content.

**3. Indentation:**
   Indentation is also very significant. Consistent indentation is key.
   - Most of the time, your text will have no indentation (it will start at the left margin).
   - Indentation is used to indicate block quotes. Any text indented relative to the current paragraph level will be treated as a block quote.
   - Indentation is also essential for nested lists and definition list items.

**Your Task:**

Examine the example provided in the input area.

1.  Observe how paragraphs are formed and separated by blank lines.
2.  Notice the use of indentation to create a block quote.
3.  Experiment by:
    a. Removing a blank line between two distinct ideas to see how they merge into one paragraph.
    b. Adding or removing indentation from the block quote to see how it affects the rendering.
    c. Try to create a new paragraph and then indent a part of it to make it a block quote.

# -Example-

This is the first paragraph. It's a block of text that stands on its own.
We can write multiple sentences here, and they will all be part of the same paragraph.

This is a second paragraph. Notice the blank line above it? That's what separates it from the first paragraph. Without that blank line, it would just be a continuation of the first.

Let's introduce a block quote:

    This text is indented.
    Therefore, it becomes a block quote.
    All lines in this quote share the same level of indentation.

    A blank line within an indented block still maintains the block quote,
    but creates a new paragraph *within* that quote.

This paragraph is back at the main indentation level, so it's not part of the block quote above.
Indentation matters!
Try removing the blank line between this paragraph and the block quote, or change the indentation of the quote.
