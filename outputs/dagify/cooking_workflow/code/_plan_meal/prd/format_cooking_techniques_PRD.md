# format_cooking_techniques PRD

## Description
Formats a list of cooking techniques into a string representation.


## Conceptual Info

This shim node is responsible for taking a list or string of cooking techniques and formatting it into a human-readable string format.

## Docstring

### Summary
Formats cooking techniques into a string.

### Parameters

- **techniques** (str): A list or comma-separated string of cooking techniques to be formatted.

### Returns

str: A formatted string representation of the cooking techniques, potentially comma-separated or bulleted.

### Raises

- ValueError: If the input techniques are not in an expected format (e.g., not a list or comma-separated string).
- TypeError: If the input techniques are not of type string or list.

### Examples

```python
>>> format_cooking_techniques(techniques='grilling,roasting,boiling')
'grilling, roasting, boiling'
```

```python
>>> format_cooking_techniques(techniques=['grilling', 'roasting', 'boiling'])
'grilling, roasting, boiling'
```
