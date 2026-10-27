# Reflection: Static Code Analysis

## 1. What types of issues were found?

The original `maintenance_system.py` contained several code-quality, security, reliability, and style issues.

Pylint identified missing docstrings, a mutable default argument, a bare exception handler, an unused import, a global-variable modification, and file-handling concerns.

Bandit initially identified the use of `tempfile.mktemp()` and an assertion used for validation. The original program also lacked consistent input validation for asset IDs, service dates, and inspection intervals.

Flake8 reported formatting issues, including missing blank lines, an excessively long line, an unused import, and a missing final newline.

## 2. Which issue was the most important to fix, and why?

The unsafe temporary-file creation was an important issue because `tempfile.mktemp()` generates a filename without securely creating the corresponding file. Another process could potentially create a file at that path before the application opens it.

The implementation was changed to use `tempfile.NamedTemporaryFile()`, which securely creates the temporary file. The application also uses a context manager to ensure that the file is closed appropriately.

## 3. How did static analysis improve the code?

Static analysis provided a repeatable way to identify problems before delivering the application.

Pylint highlighted maintainability and code-quality issues. Bandit helped identify potentially unsafe operations, while Flake8 identified style violations.

The original Pylint score was 6.55/10. After the improvements, the score reached 9.86/10 before the final formatting correction. Bandit subsequently reported no issues, and the final Flake8 report was empty.

These results demonstrate that static analysis can help improve code quality, security, consistency, and maintainability.

## 4. What did you learn from this exercise?

This exercise demonstrated that code can execute successfully while still containing weaknesses that automated analysis tools can detect.

I learned the importance of avoiding mutable default arguments, catching specific exceptions, validating input, using context managers for file operations, and following Python naming and formatting conventions.

I also learned that static analysis findings must be interpreted rather than blindly accepted. Some warnings can be false positives, so the code and the tool's explanation must be examined before deciding how to respond.

Finally, comparing baseline and final reports provides measurable evidence of improvement and helps make code-review decisions more systematic.