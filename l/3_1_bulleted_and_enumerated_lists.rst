..
   _Chapter: 3. Lists and Blocks
..
   _Next: 3_2_definition_field_and_option_lists

===========================================
Lesson 3.1: Bulleted and Enumerated Lists
===========================================

Lists are a fundamental way to organize and present information in a clear,
structured manner. reStructuredText offers two main types of lists:
bulleted (unordered) and enumerated (ordered).

Bulleted Lists
--------------
Bulleted lists are used when the order of items is not important.
Each list item begins with a bullet character followed by a space and the item's text.

Syntax:
~~~~~~~
The bullet characters can be ``*`` (asterisk), ``+`` (plus), or ``-`` (minus).

.. code-block:: rst

    * This is the first list item.
    * This is the second item, using a different bullet.
    * And this is the third.

.. code-block:: rst

    + Different bullet style.

    - Mean different lists

    * In this example items MUST be separated by blank lines.

Key points for bulleted lists:

*   **Indentation**: The text of a list item must be left-aligned and indented
    relative to the bullet. If a list item spans multiple lines or contains
    nested elements (like paragraphs or other lists), they must be aligned
    with the text of the first line of the item, not the bullet itself.
*   **Blank Lines**: A blank line is required before the first list item and
    after the last. Blank lines between list items are optional but can
    improve readability.
*   **Nested Lists**: To create a nested list, simply indent further and start a
    new list. The nested list must be separated from the parent item's content
    by a blank line.

Example with a multi-line item and a nested list:

.. code-block:: rst

    * First item.
      This line is a continuation of the first item.

      This paragraph also belongs to the first item.
    * Second item.

      - A nested item, first level.
      - Another nested item.

        * A nested item, second level.

Enumerated Lists
----------------
Enumerated lists are used when the order of items is significant. Each item
begins with an enumerator followed by a space.

Syntax:
~~~~~~~
Enumerators can be:

*   Arabic numerals: ``1.``, ``2.``, ``3.``
*   Uppercase alphabet characters: ``A.``, ``B.``, ``C.``
*   Lowercase alphabet characters: ``a.``, ``b.``, ``c.``
*   Uppercase Roman numerals: ``I.``, ``II.``, ``III.``
*   Lowercase Roman numerals: ``i.``, ``ii.``, ``iii.``

The enumerator format can also include a period (``1.``), a right-parenthesis (``1)``),
or be surrounded by parentheses (``(1)``).

Like in bulleted lists, you can't mix different enumerator formats in the same list.

reStructuredText also supports auto-enumeration using the ``#`` symbol:

.. code-block:: rst

    #. First auto-enumerated item.
    #. Second auto-enumerated item.
    #. Third auto-enumerated item.

Auto-enumerated lists may begin with explicit enumeration, which sets the sequence.

.. code-block:: rst

    42. First auto-enumerated item.
    #. Second auto-enumerated item.
    #. Third auto-enumerated item.


Key points for enumerated lists:

*   **Sequence**: Enumerators should be in sequence (e.g., ``1.``, ``2.``, ``3.``).
    If the sequence is broken (e.g., ``1.``, ``3.``), a new list is started.
*   **Format and Type**: A new list will also start if the format (e.g., from ``1.`` to ``(a)``)
    or sequence type changes.
*   **Recommendation**: It's recommended to start lists with ordinal-1
    (``1``, ``A``, ``a``, ``I``, or ``i``).
*   **Ambiguity**: Ordinary paragraphs starting with text identical to an enumerator
    (e.g., ``A. Einstein was...``) can be misinterpreted as list items if they
    consist of only one line. Use escaping in such cases.

Example of an enumerated list:

.. code-block:: rst

    1. First step.
    2. Second step.
       a. Sub-item for the second step.
       b. Another sub-item.
    3. Third step.

General Rules for Lists:
------------------------
*   The content of a list item (including nested paragraphs, lists, etc.) must be
    left-aligned with the text of the first line of that item.
*   Lists must be separated from surrounding text by blank lines (above and below).

References:
-----------
*   `Bulleted Lists <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#bullet-lists>`_
*   `Enumerated Lists <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#enumerated-lists>`_

**Your Task:**

The editor below contains initial examples. Your task is to practice creating
and modifying bulleted and enumerated lists.

1.  **Bulleted Lists**:

    *   Add a new item to the existing "Shopping List".
    *   Create a new bulleted list titled "Features of reStructuredText" with at
        least three items.
    *   In one of the items of "Features of reStructuredText", add a second paragraph of text.
    *   Create a nested bulleted list within one of the "Features of reStructuredText" items.
2.  **Enumerated Lists**:

    *   Add another step to the existing "Instructions" list.
    *   Create a new enumerated list titled "Project Phases" using letters for
        enumeration (e.g., ``A.``, ``B.``).
    *   In one of the project phases, create a nested enumerated list using
        Roman numerals (e.g., ``i.``, ``ii.``).
    *   Experiment with auto-enumeration (``#.``) in a new list.
    *   Try creating an enumerated list using a different enumerator format,
        such as ``(1)`` or ``A)``.

Observe how your changes are rendered in the HTML output panel.

# Lesson Example

Example of a bulleted list:

Shopping List:

* Milk
* Bread
* Eggs

  * A dozen, large

Example of an enumerated list:

Instructions:

1. Open the package.
2. Remove the contents.
   This is an important step, don't miss it.
3. Follow further directions.

   a. Sub-point for step three.
   b. Another sub-point.

Auto-enumeration:

#. First item
#. Second item

   #. Nested auto-item
#. Third item
