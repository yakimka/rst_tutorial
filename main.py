from pyscript import document
from docutils.core import publish_parts


def parse_rst():
    parts = publish_parts(source=RST_STRING,
                          writer_name='html5')

    return parts['html_body']
    with open("out.html", "w") as f:
        f.write(parts['html_body'])


def translate_english(event):
    input_text = document.querySelector("#english")
    # english = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = parse_rst()




RST_STRING = """
. _picodi_documentation:

####################
Picodi Documentation
####################

**Picodi** is a straightforward and powerful Dependency Injection (DI) library for Python,
designed to simplify managing dependencies in both synchronous and asynchronous applications.

`Dependency Injection <https://en.wikipedia.org/wiki/Dependency_injection>`_ is a
design pattern where an object receives its dependencies from an external source rather than creating them itself.
Picodi helps you implement this pattern effectively, making your code more modular, testable, and maintainable.

Inspired by FastAPI's DI system but usable in any Python project (framework-agnostic), Picodi offers:

*   **Simplicity:** Easy-to-understand API.
*   **Flexibility:** Works seamlessly in sync and async code.
*   **Zero Dependencies:** Lightweight and requires only Python.
*   **Lifecycle Management:** Control over dependency creation and cleanup using scopes and lifespans.
*   **Testability:** Built-in support for overriding dependencies in tests.

Whether you're building a web application with FastAPI, a CLI tool, or any other Python project,
Picodi can help you manage your dependencies cleanly.
"""


# if __name__ == "__main__":
#     main()
