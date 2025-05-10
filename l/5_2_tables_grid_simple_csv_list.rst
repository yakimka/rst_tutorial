..
   _Chapter: 5. Multimedia
..
   _Next: 6_1_directive_syntax_and_options

=======================================================
Lesson 5.2: Tables - Grid, Simple, CSV, and List Tables
=======================================================

Tables are a powerful way to present structured data. reStructuredText offers
several syntaxes for creating tables, from simple to complex, and also allows
importing data from CSV files.

Grid Tables
-----------
Grid tables are the most versatile type, allowing for complex structures including
row and column spans. They are drawn using a grid of hyphens (``-``), equals signs (``=``),
vertical bars (``|``), and plus signs (``+``).

Syntax:
~~~~~~~
.. code-block:: rst

    +------------------------+------------+----------+
    | Header 1               | Header 2   | Header 3 |
    +========================+============+==========+
    | body row 1, column 1   | column 2   | column 3 |
    +------------------------+------------+----------+
    | body row 2             | Cells may span columns|
    +------------------------+------------+----------+
    | body row 3             | Cells may  | - Cells  |
    +------------------------+ span rows. | - contain|
    | body row 4             |            | - blocks.|
    +------------------------+------------+----------+

Key points for Grid Tables:

*   **Structure**: ``+`` for intersections, ``|`` for vertical lines, ``-`` for horizontal lines.
    ``=`` is used to separate header rows from the body.
*   **Spans**: Cells can span multiple rows or columns.
*   **Content**: Cells can contain arbitrary body elements (paragraphs, lists, etc.).
*   **Complexity**: Can be cumbersome to write by hand for large tables.

Writing grid tables can be tedious, especially for large tables. But you can use table generators,
just search online for "reStructuredText table generator". For example, you can use
`this one <https://www.tablesgenerator.com/text_tables>`_ to create grid tables easily
(check "Use reStructuredText syntax" checkbox).

Simple Tables
-------------
Simple tables are easier to write but have limitations: they support column spans
but not row spans. Cells in the first column cannot be blank (unless using a workaround)
and are limited to a single line of text.

Syntax:
~~~~~~~
.. code-block:: rst

    =====  =====  ======
     In           Out
    -----  -----  ------
      A      B    A or B
    =====  =====  ======
    False  False  False
    True   False  True
    False  True   True
    True   True   True
    =====  =====  ======

Key points for Simple Tables:

*   **Borders**: ``=`` for top/bottom borders and header row separation.
    ``-`` can be used for column spans or visual row separation.
*   **Columns**: Must have at least two columns. Column boundaries
    are marked by spaces in the border lines.
*   **Continuation Lines**: A blank cell in the first column indicates
    a continuation of the previous row's cell in the subsequent columns.

``csv-table`` Directive
-----------------------
This directive allows you to create a table from Comma-Separated Values (CSV) data,
either embedded directly or from an external file.

Syntax:
~~~~~~~
.. code-block:: rst

    .. csv-table:: Frozen Delights Price List
       :header: "Treat", "Quantity", "Price"
       :widths: 15, 10, 10

       "Albatross", 2.99, "$1,000,000"
       "Crunchy Frog", 1.49, "$2.50"
       "Gannet Ripple", 1.99, "$3.00"

Key options for ``csv-table``:

*   ``:header: "col1", "col2", ...``: Defines header row(s).
*   ``:widths: N, M, ...`` or ``auto``: Relative column widths.
*   ``:file: path/to/file.csv``: Specifies an external CSV file.
*   ``:delim: character``: Specifies a delimiter other than comma.
*   ``:stub-columns: N``: Number of leading columns to be treated as stub (row header) columns.

``list-table`` Directive
------------------------
This directive creates a table from a uniform two-level bullet list. Each item in the
outer list becomes a table row, and items in the inner lists become cells in that row.

Syntax:
~~~~~~~
.. code-block:: rst

    .. list-table:: My List Table
       :widths: 25 25 50
       :header-rows: 1

       * - Column A Title
         - Column B Title
         - Column C Title
       * - Item A1
         - Item B1
         - Item C1 can be longer.
       * - Item A2
         - Item B2
         - Item C2

Key options for ``list-table``:

*   ``:widths: N, M, ...`` or ``auto``: Relative column widths.
*   ``:header-rows: N``: Specifies the number of initial list items to use as header rows.
*   ``:stub-columns: N``: Number of initial cells in each row to be treated as stub columns.

General Table Directive (``.. table::``)
-----------------------------------------
The ``.. table::`` directive can be used to provide a title (caption) for any
reStructuredText table (grid or simple) that immediately follows it, or to specify
options like column widths for these table types.

.. code-block:: rst

    .. table:: An Important Table
       :widths: auto

       ===== =====
       Col1  Col2
       ===== =====
       Val1  Val2
       Val3  Val4
       ===== =====

References:
-----------
*   `Grid Tables <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#grid-tables>`_
*   `Simple Tables <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#simple-tables>`_
*   `CSV Table directive <https://docutils.sourceforge.io/docs/ref/rst/directives.html#csv-table>`_
*   `List Table directive <https://docutils.sourceforge.io/docs/ref/rst/directives.html#list-table>`_
*   `Table directive <https://docutils.sourceforge.io/docs/ref/rst/directives.html#table>`_

**Your Task:**

The editor below is empty. Your task is to create examples for each type of table.

1.  **Grid Table**:

    *   Create a small grid table with 2 columns and 3 rows (including a header row).
    *   Make one cell in the body span both columns.
2.  **Simple Table**:

    *   Create a simple table with 3 columns and 4 rows (including a header row).
    *   Use a column span in the header row for the first two columns.
3.  **CSV Table**:

    *   Create a ``.. csv-table::`` with a title.
    *   Include a ``:header:`` option with 3 column names.
    *   Provide 2-3 rows of CSV data directly in the directive's content.
    *   Specify ``:widths:``.
4.  **List Table**:

    *   Create a ``.. list-table::`` with a title.
    *   Set ``:header-rows: 1``.
    *   Define a table with 2 columns and 3 data rows (plus the header row).
    *   Specify ``:widths:``.
5.  **Table with Caption (using ``.. table::`` directive)**:

    *   Create a simple table.
    *   Above it, use the ``.. table:: Your Caption Here`` directive to give it a title.

Observe how each table type is rendered.

# Lesson Example

.. Start your table examples here.
