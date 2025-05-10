..
   _Chapter: 4. Document Structure
..
   _Next: 4_3_footnotes_and_citations

=======================================================
Lesson 4.2: Hyperlinks - External, Internal, Anonymous
=======================================================

Hyperlinks are essential for connecting documents and navigating within them.
reStructuredText provides a flexible system for creating various types of hyperlinks.

Hyperlink Basics
----------------
Hyperlinks generally consist of two parts:

1.  **Reference**: Text in your document that will become clickable (e.g., ``Python_`` or ```Visit our website`_``).
    It's marked with a trailing underscore (``_``) for named links, or double underscore (``__``) for anonymous links.
2.  **Target**: Defines where the link points. This can be an external URL, another location
    within the same document, or an indirect reference.

External Hyperlinks
-------------------
External hyperlinks point to resources outside your document, like websites.

Syntax:
~~~~~~~
.. code-block:: rst

    Visit the `Python official website`_.

    .. _Python official website: https://www.python.org/

    You can also embed the URL directly (less readable for long URLs):
    `Google <https://www.google.com>`_

    This is also will be rendered as a link:
    https://example.com

Key points for External Hyperlinks:

*   **Target Definition**: An explicit target is defined starting with ``.. _Reference Name: URL``.
    The "Reference Name" must match the text used in the hyperlink reference (case-insensitive, whitespace-normalized).
*   **Embedded URIs**: For convenience, you can embed the URL directly in the reference: ``` `Link Text <URL>`_ ```.
    This creates a named hyperlink. Using ``` `Link Text <URL>`__ ``` (double underscore)
    creates an anonymous one-off link.
*   **Standalone Hyperlinks**: Simple URLs like ``https://example.com`` in text are often automatically converted to links.

Internal Hyperlinks
-------------------
Internal hyperlinks point to other locations within the same document.
Section titles automatically become internal hyperlink targets. You can also define explicit internal targets.

Syntax for Explicit Internal Targets:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: rst

    See the `Conclusion`_ section for a summary.

    .. _Conclusion:

    (The target `Conclusion` points to the element immediately following it)

    You can also create inline internal targets:
    This is an _`important point` that I want to reference later.

    Now we can refer to the `important point`_.

Key points for Internal Hyperlinks:

*   **Implicit Targets**: Every section title (e.g., ``My Section Title``) automatically
    creates an internal target named ``My Section Title``.
    You can link to it using ```My Section Title`_``.
*   **Explicit Targets**: Defined with ``.. _Target Name:`` (note the empty link block).
    The target points to the element that follows it.
*   **Inline Internal Targets**: Defined within text using ``_`Target Name```.
    This creates a target at that specific point.
*   **Reference Matching**: Link text must match the target name (case-insensitive, whitespace-normalized).

Anonymous Hyperlinks
--------------------
Anonymous hyperlinks are useful when you don't want to name a target, especially for
one-off links where the link text itself is descriptive.

Syntax:
~~~~~~~
.. code-block:: rst

    Read more on `this interesting topic`__.

    .. __: https://example.com/interesting-topic

    Or, for an embedded anonymous link:
    `Another page <https://example.com/another>`__

Key points for Anonymous Hyperlinks:

*   **Double Underscore**: References use a double underscore (``__``) at the end.
*   **Target Definition**: Targets start with ``.. __: URL`` (no name).
*   **Order Matters**: Anonymous references are matched to anonymous targets in the order they appear in the document.
    The first ``__`` reference links to the first ``.. __:`` target, and so on.
*   **Readability**: Best used when the target is close to the reference or for very short documents.

Indirect Hyperlinks
-------------------
An indirect hyperlink target refers to another hyperlink target.

Syntax:
~~~~~~~
.. code-block:: rst

    .. _actual_target: https://www.python.org
    .. _alias_target: actual_target_

    Now, `Python site`_ will point to the URL defined in `actual_target`.

    .. _Python site: alias_target_

This can be useful for creating aliases or centralizing link definitions.

References:
-----------
*   `Hyperlink Targets <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#hyperlink-targets>`_
*   `Hyperlink References <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#hyperlink-references>`_
*   `Embedded URIs and Aliases <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#embedded-uris-and-aliases>`_
*   `Anonymous Hyperlinks <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#anonymous-hyperlinks>`_
*   `Inline Internal Targets <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#inline-internal-targets>`_
*   `Implicit Hyperlink Targets <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#implicit-hyperlink-targets>`_ (covers section title links)

**Your Task:**

The editor below provides a basic document structure. Your task is to add various types of hyperlinks.

1.  **External Hyperlink**:

    *   In the "Introduction" section, add a sentence that links to an external website.
        Use an explicit target definition for this link (e.g., link to ``https://www.wikipedia.org/`` with link text "Wikipedia").
2.  **Embedded URI Hyperlink**:

    *   In the "Introduction" section, add another sentence with an external link,
        but this time use the embedded URI syntax
        (e.g., link to ``https://www.eff.org/`` with link text "Electronic Frontier Foundation").
3.  **Internal Hyperlink to a Section**:

    *   In the "Introduction" section, add a sentence that links to the "Methods" section.
        Remember that section titles are implicit targets.
4.  **Explicit Internal Hyperlink**:

    *   In the "Methods" section, add an explicit internal target named ``data_collection``.
    *   In the "Results" section, add a sentence that links to this ``data_collection`` target.
5.  **Inline Internal Target**:

    *   Within a paragraph in the "Methods" section, create an inline internal target named ``key_assumption``.
    *   In the "Discussion" section, add a sentence that links to this ``key_assumption`` target.
6.  **Anonymous Hyperlink**:

    *   In the "Discussion" section, add a sentence with an anonymous hyperlink to an external site
        (e.g., ``https://docutils.sourceforge.io/``). Define the anonymous target nearby.

Observe how the links are rendered and ensure they point to the correct locations.

# Lesson Example
.. code-block::

    My Research Paper
    =================

    Introduction
    ------------
    This paper explores various concepts.
    (Add external link to Wikipedia here)
    (Add embedded URI link to EFF here)
    (Add a sentence that links to the "Methods" section)

    Methods
    -------
    We used several methods for this study.
    (Add explicit internal target "data_collection" here)
    (Add an inline internal target named key_assumption.)
    Our data collection process was rigorous.

    Results
    -------
    The results were significant.
    (Add link to "data_collection" target here)

    Discussion
    ----------
    The implications of these findings are broad.
    (Add link to "key_assumption" target here)
    (Add anonymous link to Docutils here)

    .. (Define anonymous target for Docutils here)

    Conclusion
    ----------
    In conclusion, this research opens new avenues.
