# Plan for reStructuredText Interactive Tutorial Exercises

## 1. Introduction to reStructuredText
    - 1.1. What is reStructuredText?
    - 1.2. Basic Syntax: Paragraphs, Blank Lines, and Indentation
    - 1.3. The Escaping Mechanism (`\`)

## 2. Basic Text Formatting (Inline Markup)
    - 2.1. Paragraphs (recap)
    - 2.2. Emphasis (`*text*`)
    - 2.3. Strong Emphasis (`**text**`)
    - 2.4. Inline Literals (````text````)
    - 2.5. Inline Markup Recognition Rules (Conditions and Character-level markup)
    - 2.6. Recognition Order for Inline Markup

## 3. Lists
    - 3.1. Bulleted Lists (Markers, Indentation, and Continuation)
    - 3.2. Enumerated Lists (Sequences, Formatting, Auto-enumeration, and Rules)
    - 3.3. Definition Lists (Term, Definition, and Classifiers)
    - 3.4. Field Lists (Syntax, Bibliographic Fields, and RCS Keywords)
    - 3.5. Option Lists (Syntax, Arguments, and Synonyms)
    - 3.6. Nesting Lists

## 4. Blocks
    - 4.1. Literal Blocks (`::` marker, Indented, and Quoted)
    - 4.2. Line Blocks (`|` prefix, Nesting, and Continuation Lines)
    - 4.3. Block Quotes (Indentation and Attribution)
    - 4.4. Doctest Blocks (`>>>` prefix and Usage)

## 5. Document Structure
    - 5.1. Sections (Titles, Adornments, Hierarchy, and Implicit Targets)
    - 5.2. Document Title and Subtitle (using unique section adornments)
    - 5.3. Transitions (horizontal lines for thematic breaks)

## 6. Hyperlinks
    - 6.1. Hyperlink Targets (External, Internal, Indirect, and Anonymous)
    - 6.2. Hyperlink References (Simple, Phrase, and Anonymous)
    - 6.3. Embedded URIs and Aliases (``` `text <URL or alias_>`_ ```)
    - 6.4. Inline Internal Targets (`_`target name```)
    - 6.5. Standalone Hyperlinks (automatic recognition of URIs and email addresses)
    - 6.6. Reference Name Normalization (whitespace, case-insensitivity)

## 7. Footnotes and Citations
    - 7.1. Footnotes (Manual, Auto-numbered, Auto-labeled, and Auto-symbol)
    - 7.2. Footnote References (Manual, Auto-numbered, Auto-labeled, and Auto-symbol)
    - 7.3. Citations (`.. [citekey] text`)
    - 7.4. Citation References (`[citekey]_`)
    - 7.5. Implicit hyperlink targets from footnotes and citations

## 8. Images and Figures
    - 8.1. Image Directive (`.. image:: path/to/image.png`, Common Options, and HTML5 Loading)
    - 8.2. Figure Directive (`.. figure:: path/to/image.png`, Caption, Legend, and Options)
    - 8.3. Inline Images (using substitution definitions with the `image` directive)

## 9. Tables
    - 9.1. Grid Tables (Drawing, Spans, and Headers)
    - 9.2. Simple Tables (Borders, Headers, Spans, and Multi-line Rows)
    - 9.3. Table Directive (`.. table:: [Caption]` and Options)
    - 9.4. CSV Table Directive (`.. csv-table:: [Caption]`, Inline/External Data, and Options)
    - 9.5. List Table Directive (`.. list-table:: [Caption]`, Data Source, and Options)

## 10. Directives (General Concepts and Common Directives)
    - 10.1. Directive Syntax: `.. directivename:: [arguments]`
    - 10.2. Directive Parts: Arguments, Options (field lists), Content
    - 10.3. Admonitions (Specific and Generic)
    - 10.4. Body Elements Directives (topic, sidebar, parsed-literal, code, math, rubric, epigraph/highlights/pull-quote, compound, container)
    - 10.5. Document Parts Directives (contents, sectnum, header/footer, target-notes)
    - 10.6. Helper/Meta Directives (include, raw, class, role, default-role, meta, title)

## 11. Interpreted Text Roles (General Concepts and Common Roles)
    - 11.1. Role Syntax: ```:role:`text` ``` or ``` `text`:role: ```
    - 11.2. Default Interpreted Text Role (and how to change it with `default-role`)
    - 11.3. Standard Roles (abbreviation, acronym, code, emphasis, literal, math, pep-reference, rfc-reference, strong, subscript, superscript, title-reference)
    - 11.4. Specialized Roles (`:raw:` defined via `.. role::`)
    - 11.5. Custom Roles (defining new roles using `.. role::`)

## 12. Substitution Definitions
    - 12.1. Syntax: `.. |name| directive:: data`
    - 12.2. Substitution References: `|name|`
    - 12.3. Substitution with Hyperlink: `|name|_` or `|name|__`
    - 12.4. Common Inline-Compatible Directives for Substitutions (image, replace, unicode, date)
    - 12.5. Case sensitivity in matching

## 13. Comments
    - 13.1. Syntax: `.. comment text` (explicit markup not matching other constructs)
    - 13.2. Empty Comments: `..` (used to terminate preceding constructs or separate blocks)

## 14. Advanced Topics & Miscellaneous
    - 14.1. Whitespace and Indentation Rules (comprehensive review)
    - 14.2. Reference Names (Simple, Phrase, Normalization, and Namespace Sharing)
    - 14.3. Implicit Hyperlink Targets (Sources and Conflict Resolution)
    - 14.4. Error Handling (system messages, problematic elements)
    - 14.5. Measures and Units (Length and Percentage)
    - 14.6. Identifier Normalization (for class names, etc.)
    - 14.7. Configuration Settings (brief mention of relevant ones like `tab_width`, `footnote_references`, etc.)
