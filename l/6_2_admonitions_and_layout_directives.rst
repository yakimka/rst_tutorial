..
   _Chapter: 6. Directives and Roles
..
   _Next: 6_3_interpreted_text_roles

================================================
Lesson 6.2: Admonitions and Layout Directives
================================================

In the previous lesson, we learned the general syntax for directives. Now, let's explore
two important categories of directives: **Admonitions** and **Layout Directives**.

Admonitions
-----------
Admonitions are special blocks of text designed to draw the reader's attention to
a particular point. They are often rendered with a distinct style, like a colored
box or an icon.

**Specific Admonitions**:
reStructuredText provides several predefined admonition types. The syntax is simple:

.. code-block:: rst

    .. <admonition-type>::
       Content of the admonition, indented.
       It can span multiple lines and include other markup.

Common admonition types include:

*   ``attention``
*   ``caution``
*   ``danger``
*   ``error``
*   ``hint``
*   ``important``
*   ``note``
*   ``tip``
*   ``warning``

Example of a ``warning`` admonition:

.. code-block:: rst

    .. warning::
       Be careful with this command, as it can delete files permanently.

**Generic Admonition**:
If none of the specific types fit your needs, you can use the generic ``admonition``
directive. This directive requires a title as an argument:

.. code-block:: rst

    .. admonition:: My Custom Title for this Block
       :class: my-custom-style

       This is a generic admonition. You provide the title.
       You can also add options like ``:class:`` for custom styling.

Layout Directives
-----------------
Layout directives help control the structure and presentation of content blocks
within your document.

**Topic**:
The ``topic`` directive creates a self-contained block of text, like a block quote
with a title, that is separate from the main flow of the document.

Syntax:

.. code-block:: rst

    .. topic:: The Title of Your Topic
       :class: special-topic

       This is the content of the topic. It can include paragraphs,
       lists, or other body elements.

**Sidebar**:
A ``sidebar`` is for information that is somewhat separate from the main text flow,
often rendered to the side or in a distinct block. It's like a mini-document
within your document.

Syntax:

.. code-block:: rst

    .. sidebar:: Interesting Aside
       :subtitle: A little extra detail
       :class: fancy-sidebar

       This content appears in the sidebar. It might be
       related material, definitions, or references.

Other layout directives like ``container`` (a generic block-level container, similar to HTML's ``<div>``)
and ``compound`` (for creating a single logical paragraph from multiple physical elements)
offer more fine-grained control over document structure, but are more advanced.

References:
-----------
*   `Specific Admonitions <https://docutils.sourceforge.io/docs/ref/rst/directives.html#specific-admonitions>`_
*   `Generic Admonition <https://docutils.sourceforge.io/docs/ref/rst/directives.html#admonition>`_
*   `Topic <https://docutils.sourceforge.io/docs/ref/rst/directives.html#topic>`_
*   `Sidebar <https://docutils.sourceforge.io/docs/ref/rst/directives.html#sidebar>`_
*   `Compound Paragraph <https://docutils.sourceforge.io/docs/ref/rst/directives.html#compound-paragraph>`_
*   `Container <https://docutils.sourceforge.io/docs/ref/rst/directives.html#container>`_

**Your Task:**

In the editor below, practice creating various admonitions and layout directives.

1.  **Note Admonition**:

    *   Create a ``.. note::`` admonition with a short message (e.g., "This is an important piece of information.").
2.  **Warning Admonition**:

    *   Create a ``.. warning::`` admonition with a cautionary message.
3.  **Generic Admonition**:

    *   Create a ``.. admonition::`` directive.
    *   Give it a custom title like "Key Takeaway".
    *   Add some content to it.
4.  **Topic Directive**:

    *   Create a ``.. topic::`` directive.
    *   Title it "Core Concept".
    *   Write a short paragraph as its content.
5.  **Sidebar Directive**:

    *   Create a ``.. sidebar::`` directive.
    *   Title it "Further Reading".
    *   Add a bullet list to its content, perhaps listing some related (fictional) document titles.

Observe how each directive is rendered in the output panel.

# Lesson Example

This document is a place for you to practice admonitions and layout directives.

Start by adding a 'note' admonition below this paragraph.
Remember to indent its content.

Then, try creating a 'warning' admonition.

You can also experiment with a generic 'admonition:: My Special Title'.

----

Now, let's try some layout directives.

Create a 'topic' directive here, perhaps summarizing a key idea.

And finally, add a 'sidebar' to present some tangential information.
Make sure to include a title for your sidebar.
