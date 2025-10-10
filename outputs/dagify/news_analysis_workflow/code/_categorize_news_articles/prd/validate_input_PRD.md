# validate_input PRD

## Description
Validate the list of article identifiers, ensuring each is a non-empty string and return a status message.


## Conceptual Info

This shim centralizes validation logic for article identifiers used throughout the news processing pipeline, ensuring that downstream nodes receive clean, well‑formed input.

## Docstring

### Summary
Validate the list of article identifiers, ensuring that each element is a non-empty string and return a status message.

### Parameters

- **filtered_article_ids** (List[str]): A list of article identifiers (IDs or titles) that must be validated.

### Returns

str: A confirmation string indicating that validation succeeded.

### Raises

- TypeError: Raised when `filtered_article_ids` is not a list.
- ValueError: Raised when the list is empty, contains non-string elements, or any string element is empty.

### Examples

```python
>>> validate_input(['id1', 'id2', 'id3'])
'Validation succeeded.'
```

```python
>>> try:
...     validate_input(['id1', '', 'id3'])
>>> except ValueError as e:
...     print(e)
'Article ID at index 1 is empty or not a string.'
```
