# count_wins PRD

## Description
Counts the number of wins from a list of parsed game scores.


## Conceptual Info

This shim node is designed to count the number of wins from a given list of parsed game scores, playing a crucial role in analyzing team performance.

## Docstring

### Summary
Counts the number of wins from a list of parsed game scores.

### Parameters

- **parsed_scores** (List[str]): A list of strings representing parsed game scores (e.g., '74-68').

### Returns

int: The total count of wins based on the provided game scores.

### Raises

- ValueError: If the input scores are not in the expected format.
- TypeError: If the input is not a list of strings.

### Examples

```python
>>> count_wins(parsed_scores=['74-68', '60-70', '80-75'])
2
```

```python
>>> count_wins(parsed_scores=['50-60', '70-65', '60-70'])
1
```
