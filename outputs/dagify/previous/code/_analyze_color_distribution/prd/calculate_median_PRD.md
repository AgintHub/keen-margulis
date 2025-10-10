# calculate_median PRD

## Description
Calculates the median of a list of confidence scores.


## Conceptual Info

This shim node is responsible for computing the median value from a list of confidence scores provided as input. It plays a crucial role in statistical analysis within the larger system.

## Docstring

### Summary
Calculates the median of a list of confidence scores.

### Parameters

- **scores** (str): A string representation of a list of confidence scores.

### Returns

float: The median value of the confidence scores.

### Raises

- ValueError: If the input string cannot be converted to a list of numbers.
- TypeError: If the input is not a string or if the list contains non-numeric values.

### Examples

```python
>>> calculate_median(scores='[0.8, 0.9, 0.7]')
0.8
```

```python
>>> calculate_median(scores='[0.5, 0.6, 0.4, 0.7]')
0.55
```
