# calculate_average_score PRD

## Description
Calculates the average score from a list of scores.


## Conceptual Info

This shim calculates the average score from a given list of scores, playing a crucial role in analyzing team performance by providing a key metric.

## Docstring

### Summary
Calculates the average score from a list of scores provided as input.

### Parameters

- **scores** (List[int]): A list of integer scores for which the average needs to be calculated.

### Returns

float: The average score calculated from the input list of scores.

### Raises

- ValueError: If the input list is empty or contains non-numeric values.
- TypeError: If the input is not a list or if the list contains non-integer values.

### Examples

```python
>>> calculate_average_score(scores=[10, 20, 30])
20.0
```

```python
>>> calculate_average_score(scores=[15, 25, 35, 45])
30.0
```
