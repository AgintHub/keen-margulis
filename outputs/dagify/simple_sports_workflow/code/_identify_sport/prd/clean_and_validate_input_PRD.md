# clean_and_validate_input PRD

## Description
Cleans and validates a raw string input, returning a trimmed, whitespace‑normalised, alphanumeric‑only string or raising an error if validation fails.


## Conceptual Info

The shim normalises user input by stripping surrounding whitespace, collapsing internal spaces, removing non‑alphanumeric characters (except single spaces), and ensuring the result is non‑empty and contains at least one alphabetic or numeric character. It is used before further processing such as sport name normalization.

## Docstring

### Summary
Return a cleaned, validated string from a raw input or raise an error if the input is invalid.

### Parameters

- **raw_input** (str): The raw string supplied by the user, which may contain leading/trailing whitespace, extra internal spaces, punctuation, or be empty.

### Returns

str: The cleaned string: stripped of leading/trailing spaces, internal spaces collapsed to single spaces, only alphanumeric characters and spaces retained, and guaranteed to be non‑empty.

### Raises

- ValueError: If the cleaned string is empty or contains no alphanumeric characters.
- TypeError: If the input is not a string.

### Examples

```python
>>> clean_and_validate_input('  Hello   World  ')
'Hello World'
```

```python
>>> clean_and_validate_input('!!!@@@')
'ValueError: Input must contain alphanumeric characters'
```
