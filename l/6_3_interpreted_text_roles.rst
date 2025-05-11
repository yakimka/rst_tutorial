..
   _Chapter: 6. Directives and Roles
..
   _Next: 6_4_substitution_definitions

======================================
Lesson 6.3: Interpreted Text Roles
======================================

Interpreted text is a versatile feature in reStructuredText that allows you to semantically
mark up small pieces of inline text. The interpretation of this text depends on its "role."
Roles provide specific meaning or formatting instructions for the enclosed text.

Syntax
------
Interpreted text is enclosed in single backticks (\`).
A role can be specified explicitly or a default role can be used.

**Default Role**:
If you just write ``` `text` ```, it uses the default role.
The standard default role in reStructuredText is ``:title-reference:`` (often rendered as italics,
suitable for book titles, etc.). This default can be changed within a document using the
``.. default-role::`` directive.

.. code-block:: rst

    This is `interpreted text` using the default role.

**Explicit Roles**:
You can specify a role explicitly using a role marker, which consists of a colon,
the role name, and another colon, either as a prefix or a suffix:

.. code-block:: rst

    This is :rolename:`interpreted text` using an explicit role.
    This is `interpreted text`:rolename: using an explicit role (suffix style).

Role names are single words (alphanumerics plus isolated internal hyphens, underscores, etc.)
and are case-insensitive.

Standard Roles
--------------
reStructuredText comes with a set of predefined standard roles. Here are some common ones:

*   **Emphasis (:emphasis:)**: Equivalent to ``*text*``.
    Example: ``:emphasis:`italic text``` renders as *italic text*.

*   **Strong Emphasis (:strong:)**: Equivalent to ``**text**``.
    Example: ``:strong:`bold text``` renders as **bold text**.

*   **Literal (:literal:)**: Equivalent to ````text````. For inline code or text that
    should not be further interpreted.
    Example: ``:literal:`<tag> & entity;``` renders as ``<tag> & entity;``.

*   **Code (:code:)**: Similar to ``:literal:``, but specifically intended for code snippets.
    It can optionally be configured with a language for syntax highlighting (usually via custom roles).
    Example: ``:code:`print("Hello")``` renders as ``print("Hello")``.

*   **Math (:math:)**: For inline mathematical notation using LaTeX syntax.
    Example: ``:math:`A_\text{c} = (\pi/4) d^2``` renders as an inline math formula.

*   **Title Reference (:title-reference: or :title: or :t:)**: For titles of books,
    periodicals, etc. This is often the default role.
    Example: ``Read :title:`The reStructuredText Guide`.``

*   **Subscript (:sub:)** and **Superscript (:sup:)**: For subscript and superscript text.
    Example: ``H :sub:`2` O`` or ``E = mc :sup:`2```.
    (Note: Often requires escaping spaces for readability: ``H\ :sub:`2`\ O``)

*   **PEP Reference (:PEP:)** and **RFC Reference (:RFC:)**: For linking to Python
    Enhancement Proposals and Requests for Comments.
    Example: ``See :PEP:`8` and :RFC:`2616`.``

Custom Roles
------------
You can define your own custom roles using the ``.. role::`` directive. This allows you to
create new semantic meanings or apply specific styling (often in conjunction with CSS if
rendering to HTML). Custom roles can be based on standard roles.

.. code-block:: rst

    .. role:: custom-warning(strong)
       :class: red-text

    This is a :custom-warning:`serious alert`.

This creates a role ``custom-warning`` based on ``:strong:`` and applies a CSS class ``red-text``.

References:
-----------
*   `Interpreted Text <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#interpreted-text>`_
*   `Standard Interpreted Text Roles <https://docutils.sourceforge.io/docs/ref/rst/roles.html>`_
*   `Custom Interpreted Text Roles (role directive) <https://docutils.sourceforge.io/docs/ref/rst/directives.html#role>`_
*   `Setting the Default Interpreted Text Role <https://docutils.sourceforge.io/docs/ref/rst/directives.html#default-role>`_

**Your Task:**

In the editor below, practice using different interpreted text roles.

1.  **Default Role**:

    *   Write a sentence using the default interpreted text role for a book title, e.g., \`My Awesome Book\`.
2.  **Explicit Standard Roles**:

    *   Use the ``:emphasis:`` role for some text.
    *   Use the ``:strong:`` role for other text.
    *   Use the ``:literal:`` role to display a snippet like ``*not* emphasized``.
    *   Use the ``:code:`` role for a simple code example like ``x = 10``.
    *   Use the ``:math:`` role for a simple formula like ``e = mc^2``
3.  **Subscript/Superscript**:

    *   Write "H2O" with the "2" as a subscript using the ``:sub:`` role.
        Remember you might need to escape spaces around it for it to look right.
4.  **PEP Reference**:

    *   Create a reference to PEP 20 (The Zen of Python) using the ``:PEP:`` role.

Observe how each role affects the rendering in the output panel.

# Lesson Example

Interpreted text roles add semantic meaning to your inline text.

Let's start with the default role. If the default is :title-reference:,
then `The Hitchhiker's Guide to the Galaxy` should appear as a title.

Now, let's try some explicit roles:
- This text can be :emphasis:`emphasized`.
- This text can be :strong:`made strong`.
- This shows :literal:`verbatim text with * and _`.
- A code snippet: :code:`def func(): pass`.
- A simple formula: :math:`a^2 + b^2 = c^2`.

Practicing subscript and superscript:
Water is H2O. (Fix this to use :sub:)
Energy is E=mc2. (Fix this to use :sup:)

Linking to standards:
Python Enhancement Proposals like PEP 8. (Fix this to use :PEP:)
Requests for Comments like RFC 123. (Fix this to use :RFC:)
