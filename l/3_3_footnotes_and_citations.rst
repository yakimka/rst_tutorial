..
   _Chapter: 3. Document Structure
..
   _Next: 4_1_bulleted_and_enumerated_lists

======================================
Lesson 3.3: Footnotes and Citations
======================================

Footnotes and citations are used to provide additional information, references, or
comments without disrupting the main flow of the document. reStructuredText
offers distinct syntax for both.

Footnotes
---------
Footnotes provide supplementary information or comments related to a specific
part of the text. They are typically numbered and appear at the bottom of the
page or end of the document.

Syntax:
~~~~~~~
A footnote reference is placed in the text where the note applies, and the
footnote content is defined elsewhere using an explicit markup block.

.. code-block:: rst

    This is some text that needs a footnote [1]_.
    Another point might need an auto-numbered footnote [#]_.
    You can also label auto-numbered footnotes for multiple references [#label]_.

    .. [1] This is the content of the first manually numbered footnote.
    .. [#] This is the content of the first auto-numbered footnote.
           It will be numbered sequentially.
    .. [#label] This is an auto-numbered footnote with a label.
                It can be referenced again using [#label]_.

Key points for Footnotes:

*   **Reference**: ``[label]_`` where `label` can be:

    *   A number (e.g., ``[1]_``) for manual numbering.
    *   A ``#`` (e.g., ``[#]_``) for automatic numbering (footnotes are numbered in the order they are defined).
    *   A ``#`` followed by a simple reference name (e.g., ``[#myfootnote]_``) for an
        "autonumber label", allowing multiple references to the same auto-numbered footnote.
    *   A ``*`` (e.g., ``[*]_``) for auto-symbol footnotes (e.g., ``*``, ``†``, ``‡``).
*   **Definition**: An explicit markup block starting with ``.. [label]`` followed by the footnote content, indented.
*   **Placement**: Footnote definitions can appear anywhere in the document, but are often grouped at the end.
*   **Automatic Hyperlinking**: Each footnote reference automatically links to its definition, and vice-versa.

Citations
---------
Citations are similar to footnotes but are typically used for bibliographic
references. They use non-numeric labels.

Syntax:
~~~~~~~
Citation references are placed in the text, and citation content is defined
elsewhere using an explicit markup block, similar to footnotes.

.. code-block:: rst

    This claim is supported by research [Author2023]_.
    Another study also confirms this [AnotherRef]_.

    .. [Author2023] Author, A. N. (2023). *Title of Work*. Publisher.
    .. [AnotherRef] Other, S. O. (2022). *Different Article*. Journal Name.

Key points for Citations:

*   **Reference**: ``[Label]_`` where `Label` is a simple reference name (e.g., ``[CIT2002]_``, ``[Author2023]_``).
    Labels are case-insensitive and typically alphanumeric with internal hyphens or underscores.
*   **Definition**: An explicit markup block starting with ``.. [Label]`` followed by the citation content, indented.
*   **Rendering**: Citations are often rendered differently from footnotes, e.g., in a bibliography section.
*   **Automatic Hyperlinking**: Like footnotes, citation references link to their definitions.

References:
-----------
*   `Footnotes <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#footnotes>`_
*   `Citations <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#citations>`_

**Your Task:**

The editor below contains some text. Your task is to add footnotes and citations
to it.

1.  **Manual Footnote**:

    *   In the first paragraph, add a manually numbered footnote reference (e.g., ``[1]_``)
        to explain the term "reStructuredText".
    *   Define the content for this footnote ``.. [1]`` at the bottom of the example.
2.  **Auto-Numbered Footnote**:

    *   In the second paragraph, add an auto-numbered footnote reference (e.g., ``[#]_``)
        to comment on the "Zen of Python".
    *   Define the content for this auto-numbered footnote ``.. [#]`` below the first footnote definition.
3.  **Labeled Auto-Numbered Footnote**:

    *   In the second paragraph, add another auto-numbered footnote reference, but this time
        give it a label (e.g., ``[#zen_source]_``).
    *   Define its content ``.. [#zen_source]``, perhaps mentioning where to find the Zen of Python.
    *   Add a second reference to this same labeled footnote later in the text.
4.  **Citation**:

    *   In the third paragraph, add a citation reference (e.g., ``[PEP20]_``) related to "PEP 20".
    *   Define the content for this citation ``.. [PEP20]`` at the end, providing a brief
        description or source for PEP 20.
5.  **Auto-Symbol Footnote (Optional)**:

    *   If you're feeling adventurous, add an auto-symbol footnote (``[*]_``) somewhere and define its content.

Observe how the footnotes and citations are rendered and how they link to their definitions.

# Lesson Example

reStructuredText is a powerful markup language used for technical documentation.
It allows for clear and readable source text.

The "Zen of Python" by Tim Peters offers guiding principles for Python's design.
It's a collection of 19 aphorisms. One can often find it by typing ``import this``
in a Python interpreter.

PEP 20 is the official designation for the Zen of Python.
Understanding these principles can be very insightful for developers.

.. Footnote and Citation definitions will go here
