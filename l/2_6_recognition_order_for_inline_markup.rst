..
   _Chapter: 2. Basic Text Formatting (Inline Markup)
..
   _Next: 3_1_bulleted_lists

===================================================
Lesson 2.6: Recognition Order for Inline Markup
===================================================

Inline markup delimiter characters like asterisks (``*``), backquotes (``` ``),
underscores (``_``), and vertical bars (``|``) are used for multiple constructs.
To avoid ambiguity and ensure predictable parsing, reStructuredText defines a
specific recognition order for these characters. Understanding this order is
crucial for correctly applying and interpreting inline markup.

The inline markup recognition order is as follows:

-   **Asterisks**: `Strong emphasis`_ (``**text**``) is recognized before `emphasis`_
    (``*text*``). This means if you write ``***text***``, it will typically be
    interpreted as strong emphasis around ``*text*`` (i.e., ``**\*text***``) or
    ``*text*`` inside strong emphasis (i.e. ``***text***`` renders as bold italic).

-   **Backquotes**:

    1.  `Inline literals`_ (````text````)
    2.  `Inline internal targets`_ (``_`target name```)
        These two are mutually independent and are recognized *before*:
    3.  Phrase `hyperlink references`_ (``` `Link text`_ ```)
    4.  `Interpreted text`_ (``` `text` ``` or ``` :role:`text` ```)

-   **Trailing underscores**: `Footnote references`_ (``[label]_``) and simple
    `hyperlink references`_ (``name_``) are mutually independent. Their specific
    syntax (brackets for footnotes) differentiates them.

-   **Vertical bars**: `Substitution references`_ (``|text|``) are independently
    recognized.

-   **Standalone hyperlinks**: `Standalone hyperlinks`_ (like ``https://example.com``)
    are the last to be recognized. This means if a URL could also be interpreted as
    another markup construct (which is rare), the other construct would take
    precedence if its rules are met.

**Your Task:**

1.  Examine the examples provided in the editor. Predict how each will be rendered
    before looking at the HTML output.
2.  Modify the examples. For instance, how does ``**word***`` differ from ``*word**``?
3.  Try to create a text snippet that uses ``**strong**``, then immediately
    a ``` `hyperlink`_ ```, and then an ````inline literal````. Observe if the
    recognition order helps in parsing them correctly next to each other.
4.  What happens if you try to make an inline literal that looks like a hyperlink,
    e.g., `````` `NotALink`\_ ``````?

References:

- `Recognition order <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#recognition-order>`_
- `Emphasis <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#emphasis>`_
- `Strong Emphasis <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#strong-emphasis>`_
- `Inline Literals <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#inline-literals>`_
- `Inline Internal Targets <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#inline-internal-targets>`_
- `Hyperlink References <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#hyperlink-references>`_
- `Interpreted Text <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#interpreted-text>`_
- `Footnote References <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#footnote-references>`_
- `Substitution References <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#substitution-references>`_
- `Standalone Hyperlinks <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#standalone-hyperlinks>`_

# Lesson Example

.. This section preloads for the student. Provide a starting point:

Observe the following examples. How are they parsed based on recognition order?

This is ``***triple asterisks***``.
Is it *emphasis* within **strong** or **strong** around *emphasis*?

This is ``**word***`` (strong, then literal asterisk).
This is ``*word**`` (emphasis, then literal asterisk).

Consider backquotes:
This is ``` `a phrase link`_ ```. (Hyperlink)
This is ````a literal with backquotes````. (Literal)
This is also ```an interpreted text```. (Interpreted Text, default role)

What about `literal_with_underscore`_? (Hyperlink, name is "literal_with_underscore")
And ````literal_with_underscore_````? (Literal text "literal_with_underscore_")

.. _literal_with_underscore: https://example.com/this_is_a_test_target

A footnote [1]_ and a link_ share the underscore suffix.

.. [1] This is a footnote.

.. _link: https://docutils.sourceforge.io/

A substitution |subst| and a |subst|_ with a link.

.. |subst| replace:: example substitution

.. _subst: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#substitution-references

A standalone link: https://docutils.sourceforge.io/
An email: user@example.com
