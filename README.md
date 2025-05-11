# Interactive reStructuredText Tutorial

This project provides a hands-on learning experience for reStructuredText (reST), an easy-to-read,
what-you-see-is-what-you-get plaintext markup syntax and parser system. reStructuredText is commonly
used for technical documentation, including Python's official documentation, and is a core component
of the [Docutils](https://docutils.sourceforge.io/) project.

Through these interactive lessons, you'll learn the fundamentals and more advanced features of
reStructuredText, enabling you to write clear, well-structured documents. Each lesson includes an
interactive editor where you can practice the concepts immediately.

## Features

* **Interactive Lessons:** Step-by-step tutorials covering various aspects of reStructuredText.
* **Live Preview:** See the rendered output of your reStructuredText as you type.
* **reStructuredText Playground:** A dedicated page to experiment with reST syntax freely.

## Technologies Used

* **PyScript:** Enables running Python code directly in the browser.
* **Python:** For reStructuredText parsing (via Docutils) and application logic.
* **HTML, CSS, JavaScript:** For the frontend structure, styling, and interactivity.
* **Pico.css:** A minimalist CSS framework for styling.
* **Split.js:** For creating draggable split views.
* **indent-textarea.js:** For enabling tab indentation in textareas.

## Getting Started

To run this project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/yakimka/rst_tutorial.git
   ```
2. Navigate to the project directory:
   ```bash
   cd rst_tutorial
   ```
3. Open the `index.html` file in your web browser.
   Alternatively, you can serve the project directory using a local web server. For example, using
   Python's built-in HTTP server:
   ```bash
   python -m http.server
   ```
   Then open `http://localhost:8000` (or the port specified by the server) in your browser.

## Official Docutils Documentation

For more comprehensive information, refer to the official Docutils and reStructuredText
documentation:

* [reStructuredText Quickref](https://www.docutils.org/docs/user/rst/quickref.html)
* [reStructuredText Markup Specification](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html)
* [reStructuredText Directives](https://docutils.sourceforge.io/docs/ref/rst/directives.html)
* [reStructuredText Interpreted Text Roles](https://docutils.sourceforge.io/docs/ref/rst/roles.html)
