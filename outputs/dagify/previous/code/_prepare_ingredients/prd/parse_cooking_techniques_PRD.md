# parse_cooking_techniques PRD

## Description
Parses a string containing cooking techniques into a list of individual techniques.


## Conceptual Info

This shim node is responsible for parsing a string that contains cooking techniques and returning a list of individual techniques.

## Docstring

### Summary
Parses a string of cooking techniques into a list of strings.

### Parameters

- **techniques_str** (str): A string containing one or more cooking techniques, potentially comma-separated or listed in some format.

### Returns

List[str]: A list of individual cooking techniques extracted from the input string.

### Raises

- ValueError: If the input string is malformed or cannot be parsed into a list of techniques.
- TypeError: If the input is not a string.

### Examples

```python
>>> parse_cooking_techniques(techniques_str='roasting, sautéing, boiling')
['roasting', 'sautéing', 'boiling']
```

```python
>>> parse_cooking_techniques(techniques_str='grilling')
['grilling']
```
