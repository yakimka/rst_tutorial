..
   _Chapter: 1. Introduction to reStructuredText
..
   _Next: 1_3_the_escaping_mechanism

===================================================================
Lesson 1.2: Basic Syntax - Paragraphs, Blank Lines, and Indentation
===================================================================
In reStructuredText, the fundamental building blocks of a document are paragraphs.
Understanding how they are formed and separated, along with the role of indentation,
is key to creating well-structured documents.

Paragraphs
----------
A paragraph is a simple block of text. Paragraphs are separated from each other by one or more
blank lines. The text within a paragraph should typically have the same level of indentation
(usually, meaning it's not indented at all, or it's part of an indented block like a quote).

.. code-block:: rst

   This is the first paragraph.
   It can span multiple lines.

   This is the second paragraph.
   It is separated from the first by a blank line.

Blank Lines
-----------
Blank lines are crucial in reStructuredText. They serve as the primary way to separate
different elements, not just paragraphs. Using more than one blank line between
elements has the same effect as using a single blank line.

Indentation
-----------
Indentation is significant in reStructuredText. While many elements start at the
left margin, indenting a block of text usually means something specific.
One common use of indentation is to create a **block quote**.
If a paragraph is indented relative to the preceding text, it becomes a block quote.

.. code-block:: rst

   This is a normal paragraph.

       This paragraph is indented,
       so it will be treated as a block quote.
       It can also span multiple lines.

   This paragraph is back at the original indentation level.

We will explore more uses of indentation for lists and other constructs in later lessons.

**Your Task:**

The editor below contains some initial text. Your task is to modify and add to it:

1.  Currently, there are a few paragraphs and an indented block.
    Identify them. Add at least one **new** distinct paragraph of your own.
    For example, you could add it after the first paragraph or at the very end.
2.  Experiment with the blank lines between the existing paragraphs and your new paragraph.
    Try using one, two, or even three blank lines. Notice how the rendered output
    separates paragraphs regardless of the exact number of blank lines (as long as there's at least one).
3.  The example already contains an indented block (a block quote).
    Modify this existing block quote by adding another line of text to it.
    Then, add a **new** block quote after one of your normal paragraphs.
    Ensure your new block quote also contains at least two lines of text.
4.  After your new block quote, add a final paragraph, making sure it returns to the
    normal (non-indented) indentation level.

# Lesson Example

This is an initial paragraph to get you started.
You can add more text to it, or create new paragraphs below.

Remember, a blank line is needed to start a new paragraph.

   And indentation is used for things like block quotes.
   Try to make this quote longer!

This text follows the initial indented block.
Try adding more content here.
