..
   _Chapter: 4. Document Structure
..
   _Next: 4_2_hyperlinks_external_internal_anonymous

=============================================
Lesson 4.1: Sections, Titles, and Transitions
=============================================

Structuring a document logically is crucial for readability and organization.
reStructuredText uses titles with adornments to create sections and subsections,
and transitions to mark thematic breaks.

Sections and Titles
-------------------
Sections form the hierarchical structure of a document. Each section is identified
by its title, which is adorned with underline characters, or both overlines and
underlines.

Syntax for Titles:
~~~~~~~~~~~~~~~~~~
A title is a single line of text. The adornment line(s) must be made of the same
non-alphanumeric printable 7-bit ASCII character (e.g., ``= - ` : ' " ~ ^ _ * + #``)
and must be at least as long as the title text.

.. code-block:: rst

    =================
    Document Title
    =================
    (Typically for the main document title, uses overline and underline)

    Section Title
    =============
    (Underline-only style)

    Another Section Title
    ---------------------
    (Different underline character for a different level or style)

    Subsection Title
    ~~~~~~~~~~~~~~~~
    (Yet another style for a deeper level)

Key points for Sections and Titles:

*   **Hierarchy by Order**: reStructuredText determines the hierarchy of sections by
    the order in which different adornment styles are encountered. The first style
    encountered becomes the outermost section (like H1 in HTML), the second style
    encountered becomes a subsection (H2), and so on.
*   **Consistency**: Once a style is used for a certain level, it should consistently
    represent that level throughout the document. You cannot use the same style for
    both a main section and a subsection if another style has already established
    a different level between them.
*   **Overlines and Underlines**: If an overline is used, it must match the underline
    character and length. Underline-only styles are distinct from overline-and-underline
    styles using the same character.
*   **Blank Lines**: A blank line is optional after a title. All text blocks up to the
    next title of the same or higher level are included in a section.
*   **Implicit Hyperlink Targets**: Each section title automatically creates a hyperlink
    target with the same name as the title text, allowing you to link to sections.

Document Title and Subtitle:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A unique adornment style at the very beginning of a document can mark the document title.
A second unique adornment style immediately following the document title can mark the
document subtitle.

.. code-block:: rst

    My Awesome Document
    ###################
    An Amazing Subtitle
    *******************

    First Section
    =============
    ...

Transitions
-----------
Transitions are used to indicate a thematic break or a shift in topic within a
section, without creating a new section. They are often rendered as a horizontal line.

Syntax for Transitions:
~~~~~~~~~~~~~~~~~~~~~~~
A transition is a horizontal line of 4 or more repeated punctuation characters
(e.g., ``----``, ``******``, ``++++``). It must be preceded and followed by a blank line.

.. code-block:: rst

    This is a paragraph.

    ----------

    This paragraph follows the transition, indicating a shift in topic.

    ********

    Another transition using different characters.

Key points for Transitions:

*   **Separation**: Requires blank lines before and after.
*   **No Hierarchy**: Unlike section titles, there's no hierarchy of transition styles.
    All transition markers are treated equally. It's recommended to use a consistent
    style for transitions within a document.
*   **Placement**: Should not begin or end a section or document, nor should two
    transitions be immediately adjacent.

References:
-----------
*   `Sections <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#sections>`_
*   `Document Title/Subtitle <https://docutils.sourceforge.io/docs/user/rst/quickstart.html#document-title-subtitle>`_
    (from the Primer, also see `Markup Spec <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#document-title>`_)
*   `Transitions <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#transitions>`_

**Your Task:**

The editor below contains a basic structure. Your task is to expand and refine it
using sections, titles, and transitions.

1.  **Document Title and Subtitle**:

    *   The example has a placeholder for a document title. Choose a suitable title
        and adorn it with overlines and underlines using a character like ``=``.
    *   Add a subtitle immediately after the document title, using a *different*
        overline/underline style (e.g., ``-``).
2.  **Sections and Subsections**:

    *   The example has "Chapter 1" and "Chapter 2". Ensure their title adornments
        are consistent and represent the top level of sections (e.g., underline with ``=``).
    *   Under "Chapter 1", create at least two subsections (e.g., "Section 1.1", "Section 1.2").
        Use a consistent underline style for these subsections, different from the chapter
        titles (e.g., underline with ``-``).
    *   Under "Section 1.1", create a sub-subsection (e.g., "Subsection 1.1.1"). Use yet
        another different underline style (e.g., underline with ``~``).
3.  **Transitions**:

    *   Within the content of "Section 1.2", add a transition marker to separate
        two distinct ideas or paragraphs.
    *   Add another transition marker within "Chapter 2".
4.  **Content**:

    *   Add a short paragraph of placeholder text under each section, subsection,
        and sub-subsection you create or modify.

Observe how the document structure takes shape in the HTML output panel. Pay attention
to how different adornment styles create different levels of headings.

# Lesson Example
.. code-block::

    Document Title
    ==============

    Chapter 1

    Chapter 2
