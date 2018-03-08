# Introduction
This document covers the code standards for the project

This project (mostly) follows the [PEP 8 style guide](https://www.python.org/dev/peps/pep-0008)

# Specifics
These are guidelines not specified by the PEP 8 standard

- Indent using 4 spaces
- __Do not__ exceed 80 characters on a single line
- Use camelCase for local variables
- Use UpperCamelCase for class names
- Use an \_underscore before 'internal use' class properties and methods
  these shouldn't be accessed by other classes
  for internal properties, use provided public methods for getting/setting instead of directly
accessing them

- When breaking up arguments onto several lines, __do not__ provide an argument on the same line as
the function call:
  ```python
  foo = myFunc(
      arg1,
      arg2)
  # not
  foo = myFunc(arg1,
               arg2)
  ```

# PEP 8 exceptions
- _multiple-imports_ (C0410):
  Multiple imports __may be__ performed on a single

- Where __absolutely unavoidable__, the PEP 8 standard may be broken.
  In these cases, a Pylint ignore comment should be added so Pylint does not
take it into account
  On the line after this ignore comment, explain why the standard must be
broken
  For example:
  ```python
  # pylint: disable=(error code),(error code 2)
  # The above comment disables the given error codes for the entire file
  constant = 20 # pylint: disable=(error code)
  # The above comment disables the given error code for just that line
  ```
