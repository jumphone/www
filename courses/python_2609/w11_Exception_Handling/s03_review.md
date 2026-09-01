# Python Exception Handling

* Common error types: `SyntaxError`, `NameError`, `TypeError`, `FileNotFoundError`, `IndentationError`.

* `SyntaxError`: violates Python syntax rules, e.g., `while True` without colon.

* `NameError`: uses undefined variable, e.g., `print(new_variable)`.

* `TypeError`: unsupported operation between types, e.g., `1+'a'`.

* `FileNotFoundError`: attempts to open non-existent file.

* `IndentationError`: improper code block indentation.

* Error message structure: **Traceback** (error roadmap), **File** (location), **Line** (line number), **ErrorType**, and **details**.

* Basic exception handling: `try:` (risky code) + `except ErrorType:` (handler).

* Catch specific errors: `except ZeroDivisionError:`, `except FileNotFoundError:`.

* Catch-all errors: `except Exception as e:` stores error details in `e`.

* Provide user-friendly messages in except blocks to help users understand mistakes.

* Multiple except blocks handle different errors; only the first matching block executes.

* Tuple-style catching: `except (Error1, Error2):` handles multiple errors together.

* `else` clause: runs only when try block succeeds, separates success logic.

* `finally` block: always executes, used for cleanup like closing files.

* Manual exception raising: `raise ValueError("message")` for validation.

* Resource management pattern: `try` → `except` → `else` → `finally`.
