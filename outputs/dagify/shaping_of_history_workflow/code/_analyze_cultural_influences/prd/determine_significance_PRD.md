# determine_significance PRD

## Description
Determines the significance of each cultural factor based on its influence score.


## Conceptual Info

This shim evaluates a list of influence scores and flags each factor as significant or not, allowing downstream analysis to filter or prioritize factors.

## Docstring

### Summary
Determines the significance of cultural factors by thresholding influence scores.

### Parameters

- **scores** (List[float]): Influence scores for each cultural factor, values expected to be in the range [0, 1].

### Returns

List[bool]: A list of booleans where True indicates the factor's score meets or exceeds the significance threshold.

### Raises

- ValueError: Raised if any score is outside the [0, 1] range or if the input list is empty.
- TypeError: Raised if the input is not a list or if any element is not a float.

### Examples

```python
>>> determine_significance([0.8, 0.3, 0.95])
[True, False, True]
```

```python
>>> determine_significance([0.4, 0.6])
[False, True]
```
