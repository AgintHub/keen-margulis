# count_losses PRD

## Description
Counts the number of losses from a list of parsed game scores.


## Conceptual Info

This shim node is designed to count the number of losses from a given list of parsed game scores, playing a crucial role in analyzing team performance.

## Docstring

### Summary
Counts the number of losses from a list of parsed game scores represented as a string.

### Parameters

- **parsed_scores** (str): A string representation of parsed game scores, expected to be in a format that can be interpreted to determine wins or losses.

### Returns

int: The total count of losses derived from the input parsed scores.

### Raises

- ValueError: If the input string cannot be parsed into a recognizable score format.
- TypeError: If the input is not a string.

### Examples

```python
>>> count_losses(parsed_scores='10-5,8-7,3-10')
1
```

```python
>>> count_losses(parsed_scores='15-20,25-30,10-15')
3
```
