# validate_input_lists PRD

## Description
Checks that the provided lists of titles and texts are non-empty, of equal length, and contain only strings, returning a success message or raising an error.


## Conceptual Info

This shim serves as a guardrail before downstream processing, ensuring that article titles and corresponding texts are aligned and ready for further analysis.

## Docstring

### Summary
Validates that the supplied `titles` and `texts` lists are non-empty, equal in length, and contain only string elements. Returns a success message or raises a descriptive error.

### Parameters

- **titles** (List[str]): List of article titles to validate.
- **texts** (List[str]): List of article texts to validate.

### Returns

str: A message confirming successful validation.

### Raises

- ValueError: Raised when `titles` and `texts` are empty or have different lengths.
- TypeError: Raised when either `titles` or `texts` is not a list of strings.

### Examples

```python
>>> titles = ['Title 1', 'Title 2']
>>> texts = ['Text 1', 'Text 2']
>>> validate_input_lists(titles=titles, texts=texts)
'Validation successful.'
```

```python
>>> titles = ['Title 1']
>>> texts = ['Text 1', 'Text 2']
>>> validate_input_lists(titles=titles, texts=texts)
ValueError: Titles and texts must have the same non‑zero length.
```
