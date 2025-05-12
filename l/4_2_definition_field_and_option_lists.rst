..
   _Chapter: 4. Lists and Blocks
..
   _Next: 4_3_literal_line_and_doctest_blocks

==================================================
Lesson 4.2: Definition, Field, and Option Lists
==================================================

Beyond simple bulleted and enumerated lists, reStructuredText provides specialized list
formats for presenting specific types of information: definition lists for term-definition
pairs, field lists for metadata or record-like data, and option lists for command-line
options.

Definition Lists
----------------
Definition lists are used to associate terms with their definitions, much like a
glossary or dictionary.

Syntax:
~~~~~~~
Each item in a definition list consists of:

*   **Term**: A one-line word or phrase.
*   **Definition**: One or more paragraphs or other body elements, indented relative
    to the term. There should be no blank line between the term and its definition block.

.. code-block:: rst

    Term 1
        Definition of term 1.
        It can span multiple lines and include multiple paragraphs.

        Another paragraph for term 1's definition.

    Term 2 : classifier
        Definition of term 2. Classifiers can be used to provide
        additional context for the term (e.g., part of speech, data type).
        Classifiers are separated from the term by " : " (space, colon, space).

    Another Term : Classifier One : Classifier Two
        Definitions can also have multiple classifiers.

Key points for definition lists:

*   **No Blank Line**: Crucially, there must not be a blank line between a term
    and the start of its definition block. This distinguishes it from a block quote.
*   **Indentation**: The definition block must be indented relative to the term.
*   **Classifiers**: Optional classifiers follow the term on the same line,
    separated by " : " (space, colon, space).
*   **Separation**: Blank lines are required before the first definition list item
    and after the last, but are optional between items.

Field Lists
-----------
Field lists are used for presenting data in a "field name: field body" format,
similar to RFC 822 headers or database records. They are often used for document
metadata (like author, version) or as part of directive syntax.

Syntax:
~~~~~~~
Each field consists of:

*   **Field Marker**: ``:FieldName:`` (a colon, the field name, and another colon).
*   **Field Body**: One or more body elements, indented relative to the field marker.
    The first line of the field body determines its indentation.

.. code-block:: rst

    :Author: J. R. R. Tolkien
    :Version: 1.0
    :Status: Draft
    :Dedication:
        To my children.
        And to all who love a good story.
    :Abstract:
        This field body can contain multiple paragraphs,
        lists, or other reStructuredText elements.
        The indentation is key.

Key points for field lists:

*   **Field Names**: Can contain most characters. Colons within field names must be
    backslash-escaped if followed by whitespace (e.g., ``:Field\: Name:``).
*   **Bibliographic Fields**: When a field list is the first element in a document
    (or after the title), certain registered field names (like Author, Version,
    Copyright, Abstract, etc.) are transformed into specific document metadata.
*   **Indentation**: The field body's indentation is relative to the entire field marker.

Option Lists
------------
Option lists are specifically designed for documenting command-line program options.

Syntax:
~~~~~~~
Each item describes one or more command-line options and their meaning.

*   **Option Marker**: The option itself (e.g., ``-a``, ``--long-option``, ``/V``).
    Multiple synonymous options can be listed, separated by a comma and a space.
*   **Description**: Text explaining the option. There must be at least two spaces
    between the option marker (and its argument, if any) and the description.
    The description can span multiple lines and contain multiple paragraphs, indented
    relative to the start of the description.

.. code-block:: rst

    -a            Output all items.
    -b FILE       Specify the input file.
                  The description can be on multiple lines.
    --long-option, -l
                  A long option with a short alias.
                  This also has a multi-line description.
    --input=PATH  Long option with an argument using "=".
    /V            A DOS/VMS style option.

Key points for option lists:

*   **Spacing**: At least two spaces are required between the option (and its
    optional argument placeholder) and the description.
*   **Argument Placeholders**: Arguments can be indicated (e.g., ``FILE``, ``PATH``).
    If an argument placeholder starts with a letter, it can contain letters,
    numbers, underscores, and hyphens. If it contains other characters or spaces,
    it should be enclosed in angle brackets (e.g., ``<file name>``).
*   **Option Types**: Supports POSIX-style short (``-o``) and long (``--option``)
    options, and DOS/VMS-style (``/O``) options.

References:
-----------
*   `Definition Lists <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#definition-lists>`_
*   `Field Lists <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#field-lists>`_
*   `Bibliographic Fields <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#bibliographic-fields>`_
*   `Option Lists <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#option-lists>`_

**Your Task:**

The editor below provides a starting point. Your task is to expand upon it by
creating examples for each of the list types discussed.

1.  **Definition Lists**:

    *   Add at least two more term-definition pairs to the "Glossary" section.
    *   For one of your new terms, add a classifier (e.g., ``: (noun)``).
    *   Ensure one of your definitions spans multiple paragraphs.
2.  **Field Lists**:

    *   Complete the "Document Metadata" field list by adding fields for
        `:Copyright:` and `:Abstract:`.
    *   Make the `:Abstract:` field body contain at least two paragraphs.
3.  **Option Lists**:

    *   Add at least three more options to the "Command-Line Help" section.
    *   Include one option that has both a short and a long form (e.g., ``-v, --verbose``).
    *   Include one option that takes an argument (e.g., ``--output <filename>``).
    *   Ensure the description for one of your options is multi-lined.

Observe the rendered output in the HTML panel to see how these specialized lists
are formatted.

# Lesson Example

--Glossary--

IP
    Internet Protocol. A set of rules governing the format of data sent over the Internet.


--Document Metadata--

:Name: PEP 8


--Command-Line Help--

--help              Print this help message and exit.
