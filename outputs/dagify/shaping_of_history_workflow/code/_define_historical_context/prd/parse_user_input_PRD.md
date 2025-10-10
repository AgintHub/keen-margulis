# parse_user_input PRD

## Description
Parse and normalize user input by trimming whitespace, converting to lowercase, and stripping extraneous punctuation.


## Conceptual Info

This shim receives raw user input, performs basic cleaning such as whitespace trimming, case normalization, and punctuation removal, and outputs a sanitized string for downstream processing.

## Docstring

### Summary
Clean and normalize a raw user input string.

### Parameters

- **input_text** (str): Raw user input text to be parsed and cleaned.

### Returns

str: Normalized user input string ready for downstream processing.

### Raises

- ValueError: Raised when the cleaned input string is empty.
- TypeError: Raised when input_text is not of type str.

### Examples

```python
>>> parse_user_input('  Hello, World!  ')
'hello world'
```

```python
>>> parse_user_input('  2021-05-10  ')
'2021-05-10'
```
