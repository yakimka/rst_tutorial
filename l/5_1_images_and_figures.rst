..
   _Chapter: 5. Multimedia
..
   _Next: 5_2_tables_grid_simple_csv_list

=================================
Lesson 5.1: Images and Figures
=================================

Images and figures are essential for enriching documents, providing visual context,
and illustrating concepts. reStructuredText uses directives to embed images and
create figures with captions and legends.

The ``image`` Directive
-----------------------
The ``image`` directive is used to insert a simple image into the document.

Syntax:
~~~~~~~
.. code-block:: rst

    .. image:: path/to/your/image.png

The path to the image is relative to the document, or it can be an absolute path
or a URL.

Key options for the ``image`` directive:

*   ``:alt: text`` - provides alternative text for the image, crucial for
    accessibility (e.g., for screen readers or if the image fails to load).
*   ``:height: length`` - specifies the desired height of the image (e.g., ``100px``, ``5cm``).
*   ``:width: length or percentage`` - specifies the desired width (e.g., ``200px``, ``50%``).
*   ``:scale: percentage`` - scales the image by a percentage (e.g., ``50%`` for half size).
    If width or height are also specified, scale is applied to them.
*   ``:align: "top" | "middle" | "bottom" | "left" | "center" | "right"``
    - aligns the image. "left", "center", and "right" are for block images,
    allowing text to flow around for "left" and "right". "top", "middle",
    "bottom" are for inline images (used in substitutions).
*   ``:target: URI or reference_name_`` - makes the image a clickable hyperlink.

Example with options:

.. code-block:: rst

    .. image:: /img/company_logo.png
       :alt: Our Company Logo
       :width: 150px
       :align: center

Will render as:

.. image:: /img/company_logo.png
   :alt: Our Company Logo
   :width: 150px
   :align: center

----------

Inline Images:
~~~~~~~~~~~~~~
Images can also be used inline within text through substitution definitions:

.. code-block:: rst

    |warning_icon| some text here.

    .. |warning_icon| image:: /img/warning.png
       :alt: Warning!
       :height: 16px

Will render as:

|warning_icon| some text here.

.. |warning_icon| image:: /img/warning.png
   :alt: Warning!
   :height: 16px

----------

The ``figure`` Directive
------------------------
The ``figure`` directive is used when you want to include an image along with a
caption and an optional legend. Figures are block-level elements and can sometimes
float to a suitable position in paged output.

Syntax:
~~~~~~~
.. code-block:: rst

    .. figure:: /img/cat.png
       :alt: A descriptive caption for the image

       This is the caption for the figure. It's a single paragraph.

       This is the first paragraph of the legend.
       The legend can contain multiple body elements, like lists:

       * Point one
       * Point two

Will render as:

.. figure:: /img/cat.png
   :alt: A descriptive caption for the image

   This is the caption for the figure. It's a single paragraph.

   This is the first paragraph of the legend.
   The legend can contain multiple body elements, like lists:

   * Point one
   * Point two

----------

Key points for Figures:

*   **Image Path**: The first argument is the path to the image, same as the ``image`` directive.
*   **Options**: Supports all options of the ``image`` directive (like ``alt``, ``width``, ``scale``, ``target``).
    These options apply to the image within the figure.
*   **Figure-Specific Options**:

    *   ``:figwidth: "image" | length | percentage``
        - sets the width of the entire figure block. "image" makes the figure as wide as the image itself.
    *   ``:figclass: classname`` - adds a CSS class to the figure element.
    *   ``:align: "left" | "center" | "right"`` - aligns the entire figure block.
*   **Caption**: A single paragraph immediately following the directive options (after a blank line).
*   **Legend**: Any body elements following the caption (after another blank line).
    If there's no caption but you want a legend, use an empty comment (``..``) as a placeholder for the caption.

Supported Image Formats
-----------------------
Common web formats like PNG, JPEG, GIF, and SVG are generally well-supported,
especially for HTML output. Support for other formats or in other output types (like PDF via LaTeX)
can vary. Always test with your target output format.

References:
-----------
*   `Image directive <https://docutils.sourceforge.io/docs/ref/rst/directives.html#image>`_
*   `Figure directive <https://docutils.sourceforge.io/docs/ref/rst/directives.html#figure>`_
*   `Image formats table <https://docutils.sourceforge.io/docs/ref/rst/directives.html#image-formats>`_

**Your Task:**

The editor below is empty. Your task is to create a document that demonstrates
the use of images and figures.

1.  **Simple Image**:

    *   Add an ``.. image::`` directive.
2.  **Image with Options**:

    *   Add another ``.. image::`` directive.
    *   Include ``:alt:`` text, a ``:width:`` (e.g., ``200px``), and ``:align: center``.
3.  **Figure with Caption**:

    *   Add a ``.. figure::`` directive.
    *   Provide ``:alt:`` text for the image within the figure.
    *   Add a concise, single-paragraph caption below the directive options.
4.  **Figure with Caption and Legend**:

    *   Add another ``.. figure::`` directive.
    *   Include ``:alt:`` text and perhaps a ``:scale: 50%`` option.
    *   Add a caption.
    *   After the caption, add a legend consisting of at least one paragraph and a short bullet list.
5.  **Clickable Image (Optional)**:

    *   Modify one of your ``image`` or ``figure`` directives to include the ``:target:``
        option, making the image link to an external URL (e.g., ``https://www.example.com``).

# Lesson Example

.. Start your examples here.
.. For image paths, you can use placeholders like: /img/cat.png
