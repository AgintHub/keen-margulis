# sanitize_and_normalize_text PRD

## Description
Sanitizes and normalizes raw input text into a clean, consistent string suitable for downstream processing.


## Conceptual Info

This shim normalizes raw user input by trimming whitespace, collapsing consecutive spaces, removing non-printable characters, and standardizing line breaks into a single space, producing a clean, consistent string ready for further processing.

## Docstring

### Summary
Sanitize and normalize a text string, ensuring it is trimmed, single-spaced, printable, and line breaks are standardized.

### Parameters

- **text** (str): Raw input text that may contain irregular spacing, line breaks, or non-printable characters.

### Returns

str: The cleaned text string with uniform spacing and line breaks.

### Raises

- TypeError: Raised if the input is not a string.
- ValueError: Raised if the input is an empty string or contains only whitespace after sanitization.

### Examples

```python
>>> sanitize_and_normalize_text('  Hello   world  ')
'Hello world'
```

```python
>>> sanitize_and_normalize_text('Line1\nLine2')
'Line1 Line2'
```
