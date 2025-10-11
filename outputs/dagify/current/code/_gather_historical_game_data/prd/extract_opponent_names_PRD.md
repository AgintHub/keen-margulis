# extract_opponent_names PRD

## Description
Extracts a list of opponent names from the provided games data.


## Conceptual Info

This shim function is designed to extract opponent names from a given string of games data, playing a crucial role in data processing for historical game analysis.

## Docstring

### Summary
Extracts opponent names from the provided games data string.

### Parameters

- **games** (str): A string representing the games data from which opponent names will be extracted.

### Returns

List[str]: A list of strings representing the names of opponents extracted from the input games data.

### Raises

- ValueError: If the input games data is not in the expected format or is empty.
- TypeError: If the input games data is not a string.

### Examples

```python
>>> extract_opponent_names(games='[{\"opponent\": \"Team A\"}, {\"opponent\": \"Team B\"}]')
['Team A', 'Team B']
```

```python
>>> extract_opponent_names(games='[{\"opponent\": \"Team C\"}]')
['Team C']
```
