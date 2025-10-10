# extract_leadership_figures PRD

## Description
Extracts a list of leadership figures from a string containing political factors.


## Conceptual Info

This shim identifies key political leaders from a textual description of political factors, producing a structured list that can be consumed by downstream analysis nodes.

## Docstring

### Summary
Extracts a list of leadership figures from a string containing political factors.

### Parameters

- **political_factors** (str): A string representation of political factors, which may include narrative text, bullet points, or comma‑separated names of political leaders.

### Returns

List[str]: A list of names (strings) of leadership figures found in the input. The list may be empty if no leaders are detected.

### Raises

- ValueError: Raised when the input string is empty, contains only whitespace, or does not contain any recognisable leadership names.
- TypeError: Raised when the input is not of type `str`.

### Examples

```python
>>> extract_leadership_figures('Key leaders: John Doe, Jane Smith, and Alan Turing')
['John Doe', 'Jane Smith', 'Alan Turing']
```

```python
>>> extract_leadership_figures('No leaders mentioned in this political analysis.')
[]
```
