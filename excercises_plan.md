# Plan for reStructuredText Interactive Tutorial Exercises

## 1. Introduction to reStructuredText
    - 1.1. What is reStructuredText?
    - 1.2. Basic Syntax:
        - 1.2.1. Paragraphs
        - 1.2.2. Blank Lines
        - 1.2.3. Indentation (its significance)
    - 1.3. The Escaping Mechanism (`\`)

## 2. Basic Text Formatting (Inline Markup)
    - 2.1. Paragraphs (recap)
    - 2.2. Emphasis (`*text*`)
    - 2.3. Strong Emphasis (`**text**`)
    - 2.4. Inline Literals (````text````)
    - 2.5. Inline Markup Recognition Rules
        - 2.5.1. Conditions for recognition
        - 2.5.2. Character-level inline markup (and its caveats)
    - 2.6. Recognition Order for Inline Markup

## 3. Lists
    - 3.1. Bulleted Lists
        - 3.1.1. Markers: `*`, `+`, `-`
        - 3.1.2. Indentation and continuation
    - 3.2. Enumerated Lists
        - 3.2.1. Enumeration sequences: arabic numerals, alphabet (upper/lower), Roman numerals (upper/lower)
        - 3.2.2. Formatting: `.`, `()`, `)`
        - 3.2.3. Auto-enumeration (`#`)
        - 3.2.4. List start and sequence rules
    - 3.3. Definition Lists
        - 3.3.1. Term
        - 3.3.2. Definition
        - 3.3.3. Optional Classifiers (`: classifier :`)
    - 3.4. Field Lists
        - 3.4.1. Syntax: `:field name: field body`
        - 3.4.2. Bibliographic Fields (e.g., Author, Version, Date, Abstract)
            - 3.4.2.1. RCS Keywords
    - 3.5. Option Lists
        - 3.5.1. Syntax for command-line options (POSIX short/long, DOS/VMS)
        - 3.5.2. Option arguments
        - 3.5.3. Multiple option synonyms
    - 3.6. Nesting Lists

## 4. Blocks
    - 4.1. Literal Blocks
        - 4.1.1. `::` marker
        - 4.1.2. Indented literal blocks
        - 4.1.3. Quoted literal blocks (per-line quoting)
    - 4.2. Line Blocks
        - 4.2.1. `|` prefix for preserving line breaks
        - 4.2.2. Indentation for nesting
        - 4.2.3. Continuation lines
    - 4.3. Block Quotes
        - 4.3.1. Indentation
        - 4.3.2. Attribution (`-- text`)
    - 4.4. Doctest Blocks
        - 4.4.1. `>>>` prefix
        - 4.4.2. For Python interactive sessions

## 5. Document Structure
    - 5.1. Sections
        - 5.1.1. Titles
        - 5.1.2. Underlines and Overlines (adornment characters, consistency)
        - 5.1.3. Section hierarchy (order of appearance)
        - 5.1.4. Implicit hyperlink targets from section titles
    - 5.2. Document Title and Subtitle (using unique section adornments)
    - 5.3. Transitions (horizontal lines for thematic breaks)

## 6. Hyperlinks
    - 6.1. Hyperlink Targets
        - 6.1.1. External Hyperlink Targets (`.. _name: URL`)
        - 6.1.2. Internal Hyperlink Targets (`.. _name:`)
        - 6.1.3. Indirect Hyperlink Targets (`.. _name1: name2_`)
        - 6.1.4. Anonymous Hyperlink Targets (`.. __: URL` or `__ URL`)
    - 6.2. Hyperlink References
        - 6.2.1. Simple named references (`name_`)
        - 6.2.2. Phrase named references (``` `phrase name`_ ```)
        - 6.2.3. Anonymous references (`text__` or ``` `phrase name`__ ```)
    - 6.3. Embedded URIs and Aliases (``` `text <URL or alias_>`_ ```)
    - 6.4. Inline Internal Targets (`_`target name```)
    - 6.5. Standalone Hyperlinks (automatic recognition of URIs and email addresses)
    - 6.6. Reference Name Normalization (whitespace, case-insensitivity)

## 7. Footnotes and Citations
    - 7.1. Footnotes
        - 7.1.1. Manual numbering (`.. [1] text`)
        - 7.1.2. Auto-numbered footnotes (`.. [#] text`)
        - 7.1.3. Auto-numbered with label (`.. [#label] text`)
        - 7.1.4. Auto-symbol footnotes (`.. [*] text`)
    - 7.2. Footnote References
        - 7.2.1. Manual (`[1]_`)
        - 7.2.2. Auto-numbered (`[#]_`)
        - 7.2.3. Auto-numbered with label (`[#label]_`)
        - 7.2.4. Auto-symbol (`[*]_`)
    - 7.3. Citations (`.. [citekey] text`)
    - 7.4. Citation References (`[citekey]_`)
    - 7.5. Implicit hyperlink targets from footnotes and citations

## 8. Images and Figures
    - 8.1. Image Directive (`.. image:: path/to/image.png`)
        - 8.1.1. Common Options: `alt`, `height`, `width`, `scale`, `align`, `target`, `class`, `name`
        - 8.1.2. HTML5 specific: `loading`
    - 8.2. Figure Directive (`.. figure:: path/to/image.png`)
        - 8.2.1. Figure Caption (paragraph after options)
        - 8.2.2. Figure Legend (body elements after caption)
        - 8.2.3. Figure-specific Options: `figclass`, `figname`, `figwidth` (plus image options)
    - 8.3. Inline Images (using substitution definitions with the `image` directive)

## 9. Tables
    - 9.1. Grid Tables
        - 9.1.1. Drawing with `+`, `-`, `|`, `=`
        - 9.1.2. Row and column spans
        - 9.1.3. Header rows
    - 9.2. Simple Tables
        - 9.2.1. Borders with `=`
        - 9.2.2. Header row separation with `=`
        - 9.2.3. Column spans with `-`
        - 9.2.4. Multi-line rows and continuation lines
    - 9.3. Table Directive (`.. table:: [Caption]`)
        - 9.3.1. Options: `widths`, `width`, `align`, `class`, `name`
    - 9.4. CSV Table Directive (`.. csv-table:: [Caption]`)
        - 9.4.1. Inline CSV data
        - 9.4.2. External CSV data (`:file:`, `:url:`)
        - 9.4.3. Options: `header`, `header-rows`, `widths`, `delim`, `quote`, `escape`, `encoding`, `stub-columns`, `align`, `class`, `name`
    - 9.5. List Table Directive (`.. list-table:: [Caption]`)
        - 9.5.1. Data from a uniform two-level bullet list
        - 9.5.2. Options: `header-rows`, `stub-columns`, `widths`, `width`, `align`, `class`, `name`

## 10. Directives (General Concepts and Common Directives)
    - 10.1. Directive Syntax: `.. directivename:: [arguments]`
    - 10.2. Directive Parts: Arguments, Options (field lists), Content
    - 10.3. Admonitions
        - 10.3.1. Specific: `attention`, `caution`, `danger`, `error`, `hint`, `important`, `note`, `tip`, `warning`
        - 10.3.2. Generic: `.. admonition:: User-Defined Title`
    - 10.4. Body Elements Directives
        - 10.4.1. `.. topic:: Title`
        - 10.4.2. `.. sidebar:: Title` (options: `subtitle`, `class`, `name`)
        - 10.4.3. `.. parsed-literal::`
        - 10.4.4. `.. code:: [language]` (options: `number-lines`, `class`, `name`)
        - 10.4.5. `.. math::`
        - 10.4.6. `.. rubric:: Title`
        - 10.4.7. `.. epigraph::`, `.. highlights::`, `.. pull-quote::`
        - 10.4.8. `.. compound::`
        - 10.4.9. `.. container:: [classes]` (option: `name`)
    - 10.5. Document Parts Directives
        - 10.5.1. `.. contents:: [Title]` (Table of Contents; options: `depth`, `local`, `backlinks`, `class`)
        - 10.5.2. `.. sectnum::` or `.. section-numbering::` (options: `depth`, `prefix`, `suffix`, `start`)
        - 10.5.3. `.. header::` and `.. footer::`
        - 10.5.4. `.. target-notes::`
    - 10.6. Helper/Meta Directives
        - 10.6.1. `.. include:: path` (options: `start-after`, `end-before`, `start-line`, `end-line`, `literal`, `code`, `encoding`, `tab-width`, `number-lines`, `class`, `name`, `parser`)
        - 10.6.2. `.. raw:: format1 [format2 ...]` (options: `file`, `url`, `encoding`, `class`)
        - 10.6.3. `.. class:: class-name(s)`
        - 10.6.4. `.. role:: new_role_name [(base_role_name)]` (options: `class`, `language`, `format`)
        - 10.6.5. `.. default-role:: role_name`
        - 10.6.6. `.. meta::` (using a field list for metadata)
        - 10.6.7. `.. title:: Document Title As Metadata` (overrides document-supplied title)

## 11. Interpreted Text Roles (General Concepts and Common Roles)
    - 11.1. Role Syntax: ```:role:`text` ``` or ``` `text`:role: ```
    - 11.2. Default Interpreted Text Role (and how to change it with `default-role`)
    - 11.3. Standard Roles:
        - 11.3.1. `:abbreviation:` (or `:ab:`)
        - 11.3.2. `:acronym:` (or `:ac:`)
        - 11.3.3. `:code:` (customizable with `language` and `class` options via `.. role::`)
        - 11.3.4. `:emphasis:` (equivalent to `*text*`)
        - 11.3.5. `:literal:` (equivalent to ````text````)
        - 11.3.6. `:math:` (for inline math)
        - 11.3.7. `:pep-reference:` (or `:PEP:`)
        - 11.3.8. `:rfc-reference:` (or `:RFC:`)
        - 11.3.9. `:strong:` (equivalent to `**text**`)
        - 11.3.10. `:subscript:` (or `:sub:`)
        - 11.3.11. `:superscript:` (or `:sup:`)
        - 11.3.12. `:title-reference:` (or `:title:`, `:t:`)
    - 11.4. Specialized Roles:
        - 11.4.1. `:raw:` (must be defined via `.. role::` with `format` option)
    - 11.5. Custom Roles (defining new roles using `.. role::`)

## 12. Substitution Definitions
    - 12.1. Syntax: `.. |name| directive:: data`
    - 12.2. Substitution References: `|name|`
    - 12.3. Substitution with Hyperlink: `|name|_` or `|name|__`
    - 12.4. Common Inline-Compatible Directives for Substitutions:
        - 12.4.1. `image` (for inline images)
        - 12.4.2. `replace` (for text replacement, macros)
        - 12.4.3. `unicode` (for inserting Unicode characters by code)
        - 12.4.4. `date` (for inserting current date/time)
    - 12.5. Case sensitivity in matching

## 13. Comments
    - 13.1. Syntax: `.. comment text` (explicit markup not matching other constructs)
    - 13.2. Empty Comments: `..` (used to terminate preceding constructs or separate blocks)

## 14. Advanced Topics & Miscellaneous
    - 14.1. Whitespace and Indentation Rules (comprehensive review)
    - 14.2. Reference Names
        - 14.2.1. Simple reference names
        - 14.2.2. Phrase references (backquoted)
        - 14.2.3. Normalization (whitespace, case)
        - 14.2.4. Namespace sharing (hyperlinks, footnotes, citations)
    - 14.3. Implicit Hyperlink Targets (from sections, footnotes, citations)
        - 14.3.1. Conflict resolution with explicit targets
    - 14.4. Error Handling (system messages, problematic elements)
    - 14.5. Measures and Units
        - 14.5.1. Length units (em, px, cm, in, etc.)
        - 14.5.2. Percentage unit (%)
    - 14.6. Identifier Normalization (for class names, etc.)
    - 14.7. Configuration Settings (brief mention of relevant ones like `tab_width`, `footnote_references`, etc.)
