# extract_opponent_scores PRD

## Description
Extracts opponent scores from a list of parsed score tuples into a list of integers.


## Conceptual Info

This shim function is designed to extract opponent scores from a list of parsed score tuples, which are derived from game score strings.

## Docstring

### Summary
Extract opponent scores from a list of parsed score tuples.

### Parameters

- **parsed_scores** (List[tuple[int, int]]): List of tuples containing team and opponent scores

### Returns

List[int]: List of opponent scores as integers

### Raises

- TypeError: If parsed_scores is not a list of tuples or if tuple elements are not integers
- ValueError: If parsed_scores list is empty or contains tuples without exactly two elements

### Examples

```python
>>> parsed_scores = [(100, 90), (80, 95), (70, 85)]
>>> opponent_scores = extract_opponent_scores(parsed_scores=parsed_scores)
[90, 95, 85]
```

```python
>>> parsed_scores = [(75, 80), (90, 85)]
>>> opponent_scores = extract_opponent_scores(parsed_scores=parsed_scores)
[80, 85]
```
