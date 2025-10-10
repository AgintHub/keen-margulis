# calculate_influence_scores PRD

## Description
Calculates a list of influence scores (between 0 and 1) for each cultural factor provided.


## Conceptual Info

This shim evaluates the relative importance of each cultural factor by producing a normalized score between 0 and 1, enabling downstream modules to assess significance and rank factors.

## Docstring

### Summary
Calculate influence scores for a list of cultural factors.

### Parameters

- **factors** (List[str]): A list of cultural factor names to evaluate.

### Returns

List[float]: A list of influence scores, one per input factor, ranging from 0 (no influence) to 1 (maximum influence).

### Raises

- ValueError: Raised if the factors list is empty or contains non-string elements.
- TypeError: Raised if the input is not a list of strings.

### Examples

```python
>>> calculate_influence_scores(['religion', 'artistic_movement'])
[0.85, 0.42]
```

```python
>>> calculate_influence_scores(['language_trend'])
[0.92]
```
