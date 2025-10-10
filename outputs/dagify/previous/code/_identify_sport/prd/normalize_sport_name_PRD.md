# normalize_sport_name PRD

## Description
Normalizes a raw sport name string into a canonical form suitable for further processing.


## Conceptual Info

The `normalize_sport_name` shim standardizes user-provided sport names, ensuring consistent downstream handling by trimming whitespace, validating content, and applying a canonical capitalization rule.

## Docstring

### Summary
Normalize a raw sport name string to a canonical form.

### Parameters

- **sport_name** (str): The raw sport name string to be normalized.

### Returns

str: Normalized sport name string following canonical conventions.

### Raises

- ValueError: Raised when the input is empty, contains only whitespace, or includes invalid characters.
- TypeError: Raised when the input is not of type str.

### Examples

```python
>>> normalize_sport_name('soccer')
'Soccer'
```

```python
>>> normalize_sport_name('  baseball ')
'Baseball'
```
