# extract_liquid_type PRD

## Description
Extracts the liquid type from a given input string, ignoring any volume or additional information.


## Conceptual Info

This shim encapsulates the logic for parsing a liquid type from arbitrary input strings, providing a standardized, validated output that other nodes can rely upon.

## Docstring

### Summary
Extracts the liquid type from a general input string, returning a standardized lowercase string.

### Parameters

- **general_input** (str): The raw input string that may contain a liquid type followed by additional descriptors such as volume or units.
- **kwargs** (str): Additional keyword arguments in string form; currently unused but retained for API compatibility.

### Returns

str: The liquid type extracted from the input, lowercased. Example: 'water', 'coffee', 'milk'.

### Raises

- ValueError: Raised when the liquid type cannot be determined from the input.
- TypeError: Raised when either `general_input` or `kwargs` is not a string.

### Examples

```python
>>> print(extract_liquid_type('Water 500ml', {}))
'water'
```

```python
>>> print(extract_liquid_type('Coffee 300ml', {}))
'coffee'
```
