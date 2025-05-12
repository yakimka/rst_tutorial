..
   _Chapter: 7. Directives, Roles & Comments
..
   _Next: 7_3_admonitions_and_layout_directives

=========================================
Lesson 7.2: Directive Syntax and Options
=========================================

Directives are a powerful extension mechanism in reStructuredText. They allow you
to introduce more complex elements and functionalities into your documents without
altering the core syntax of the language. Think of them as special commands that
tell the reStructuredText parser to do something specific.

Basic Directive Syntax
----------------------
A directive generally follows this structure:

.. code-block:: rst

    .. directive-type:: [arguments]
       :option1: value1
       :option2: value2

       Content of the directive.

Let's break this down:

1.  **Explicit Markup Start**: All directives begin with ``..`` (two periods followed by a space).
    This signals to the parser that an explicit markup block is starting.

2.  **Directive Type**: This is the name of the directive (e.g., ``image``, ``note``, ``table``).
    It must be a single word (alphanumerics plus isolated internal hyphens, underscores, etc.)
    and is case-insensitive.

3.  **Double Colons (::)**: Two colons follow the directive type, separating it from the
    directive's arguments, options, and content.

4.  **Directive Block**: This is everything that follows the ``::`` and belongs to the directive.
    It consists of three optional parts, in this order:

    *   **Arguments**: Text that appears on the same line as the directive marker, or on
        subsequent indented lines if the arguments are long. Not all directives take arguments.
        The meaning of arguments is specific to each directive (e.g., a file path for an
        ``image`` directive).
    *   **Options**: Specified as a field list (e.g., ``:option-name: value``) indented
        under the directive. Options provide additional configuration for the directive.
        If arguments are present, options must follow them. If there are no arguments,
        options can start on the line after the directive marker. A blank line must
        separate options from the content block if content is present.
    *   **Content**: An indented block of text or other reStructuredText elements that
        form the body of the directive. A blank line must precede the content block if
        arguments or options are present.

Not all directives use all three parts. Some might only have content, some only arguments and options, etc.

Example Breakdown:
~~~~~~~~~~~~~~~~~~
Consider an ``image`` directive:

.. code-block:: rst

    .. image:: /img/cat.png
       :alt: This is the alternate text for the image
       :align: center

*   ``.. image::`` is the directive marker and type.
*   ``/img/cat.png`` is the **argument** (the image path).
*   ``:alt: ...`` and ``:align: ...`` are **options**.
*   This particular ``image`` directive doesn't typically have **content** in the same way a ``note`` directive would.

Another example, a ``note`` admonition:

.. code-block:: rst

    .. note::
       This is the **content** of the note.
       It can span multiple lines and include other reStructuredText markup.

*   ``.. note::`` is the directive marker and type.
*   It has no arguments or explicit options shown here (though some admonitions can take options like ``:class:``).
*   The indented block is its **content**.

And a ``figure`` directive, which uses all three:

.. code-block:: rst

    .. figure:: /img/company_logo.png
       :alt: Company Logo

       This is the caption for the figure. It serves as the content.

*   ``.. figure::`` is the directive marker and type.
*   ``/img/company_logo.png`` is the **argument**.
*   ``This is the caption...`` is the **content** (the figure's caption).

The specific arguments, options, and content interpretation depend entirely on the
directive itself. This lesson focuses on the general syntax. Future lessons will
cover specific directives like admonitions, images, tables, etc., in more detail.

References:
-----------
*   `Directives <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#directives>`_
*   `reStructuredText Directives (overview of standard directives) <https://docutils.sourceforge.io/docs/ref/rst/directives.html>`_

# Lesson Example

.. image:: /img/cat.png
   :alt: This is the alternate text for the image
   :align: center

----

.. note::
   This is the **content** of the note.
   It can span multiple lines and include other reStructuredText markup.

----


.. figure:: /img/company_logo.png
   :alt: Company Logo

   This is the caption for the figure. It serves as the content.
