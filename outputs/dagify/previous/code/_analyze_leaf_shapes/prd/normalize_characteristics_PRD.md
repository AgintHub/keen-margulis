# normalize_characteristics PRD

## Description
Normalizes a list of leaf characteristics into a standardized format.


## Conceptual Info

This shim function takes a string of leaf characteristics, normalizes it, and returns a list of normalized characteristic descriptions.

## Docstring

### Summary
Normalizes a string of leaf characteristics into a list of standardized format.

### Parameters

- **characteristics** (str): Input string containing leaf characteristics to be normalized

### Returns

List[str]: List of normalized characteristic descriptions for each leaf

### Raises

- ValueError: When the input string is empty or contains invalid characters
- TypeError: When the input is not a string

### Examples

```python
>>> normalize_characteristics(characteristics='large, green, oval-shaped')
>>> normalize_characteristics(characteristics='small, yellow, heart-shaped')
['large', 'green', 'oval-shaped']
['small', 'yellow', 'heart-shaped']
```

```python
>>> normalize_characteristics(characteristics='')
[]
```
