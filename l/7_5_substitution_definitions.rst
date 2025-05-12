..
   _Chapter: 7. Directives, Roles & Comments
..
   _Next: 8_1_configuration_settings

========================================
Lesson 7.5: Substitution Definitions
========================================

Substitution definitions in reStructuredText allow you to define a piece of text or
an inline element that can be reused throughout your document. They are similar to
macros or named entities in other markup languages. This is particularly useful for
frequently used terms, inline images, or complex inline markup that you want to
keep out of the main text flow for readability.

Syntax
------
A substitution definition starts with ``..`` (explicit markup start), followed by
a vertical bar ``|``, the substitution text (the "name" you'll use to refer to it),
another vertical bar, whitespace, and then an inline-compatible directive.

.. code-block:: rst

    .. |substitution_text| directive_type:: directive_data
       :directive_options: ...

The ``directive_type`` is one of the directives that can produce inline content,
such as ``image``, ``replace``, ``unicode``, or ``date``.

A substitution reference is used in your text by enclosing the substitution text
in vertical bars: ``|substitution_text|``.

Common Inline-Compatible Directives for Substitutions
-----------------------------------------------------

1.  **replace**:

    Used for simple text replacement. The content of the ``replace`` directive
    will substitute the reference. It can also contain inline markup.

    .. code-block:: rst

        .. |RST| replace:: reStructuredText
        .. |myemph| replace:: *really important*

        I am learning |RST|. This is |myemph|.

2.  **image**:

    Used to define an inline image.

    .. code-block:: rst

        .. |logo| image:: /img/company_logo.png
           :alt: Company Logo
           :height: 32px

        Check out our |logo|!

3.  **unicode**:

    Converts Unicode character codes (decimal or hexadecimal) to characters.

    .. code-block:: rst

        .. |copy| unicode:: 0xA9  .. copyright sign
        .. |mdash| unicode:: U+2014 .. em dash

        Copyright |copy| 2025. This is an em dash |mdash|.

4.  **date**:

    Generates the current local date. The format can be specified.

    .. code-block:: rst

        .. |today| date::
        .. |isotime| date:: %Y-%m-%dT%H:%M

        Document generated on |today| at |isotime|.

Benefits of Substitutions
-------------------------
*   **Reusability**: Define once, use many times.
*   **Maintainability**: If something needs to change (e.g., a logo path, an abbreviation's full form),
    you only need to update the definition in one place.
*   **Readability**: Keeps complex inline markup (like image options or styled text)
    separate from the main flow of your document.

Substitution references can also be combined with hyperlink references:

.. code-block:: rst

       .. |Python| replace:: *Python*
       .. _Python: https://www.python.org

       Learn more about |Python|_.


References:
-----------
*   `Substitution Definitions <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#substitution-definitions>`_
*   `Substitution References <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#substitution-references>`_
*   Inline-compatible directives:

    *   `image <https://docutils.sourceforge.io/docs/ref/rst/directives.html#image>`_
    *   `replace <https://docutils.sourceforge.io/docs/ref/rst/directives.html#replace>`_
    *   `unicode <https://docutils.sourceforge.io/docs/ref/rst/directives.html#unicode>`_
    *   `date <https://docutils.sourceforge.io/docs/ref/rst/directives.html#date>`_

**Your Task:**

In the editor below, practice creating and using substitution definitions.

1.  **Text Replacement**:

    *   Define a substitution called ``|docutils|`` that replaces with "Docutils Project".
    *   Use ``|docutils|`` in a sentence.
2.  **Inline Image**:

    *   Define a substitution called ``|warningicon|`` using the ``image`` directive.
    *   Use the path ``/img/warning.png`` for the image.
    *   Add an ``:alt:`` text like "Warning!" and a ``:height:`` of ``18px``.
    *   Use ``|warningicon|`` next to some text.
3.  **Unicode Character**:

    *   Define a substitution called ``|euro|`` using the ``unicode`` directive for the Euro currency symbol (€).
        (Hint: its hexadecimal code is ``U+20AC``).
    *   Write a sentence that includes the ``|euro|`` symbol.
4.  **Date**:

    *   Define a substitution called ``|updated|`` using the ``date`` directive.
    *   Format it to show as "Month Day, Year" (e.g., ``%B %d, %Y``).
    *   Write a sentence indicating when the document was last updated using ``|updated|``.

Observe how the substitutions are rendered in the output panel.

# Lesson Example

.. Substitution definitions are usually placed at the beginning or end of a document,
.. or in a separate included file, for better organization.

.. Define your substitutions here:


.. Now use your substitutions in the text below:

This document discusses the ... project.
Please pay attention to this important note: ...
The price is 100 ...
This page was last updated on ...
