# calculate_average_impact PRD

## Description
Calculates the mean of a list of individual impact scores and returns the result as a float.


## Conceptual Info

This shim provides a simple, reusable routine for computing the average impact of a set of social factors, ensuring consistent validation and error handling across the analytics pipeline.

## Docstring

### Summary
Computes the mean of a list of individual impact scores, validating the input and raising informative errors for malformed data.

### Parameters

- **scores** (List[float]): A list of float values representing individual impact scores (expected range 0.0–1.0).

### Returns

float: The average of the provided impact scores.

### Raises

- ValueError: Raised when the input list is empty.
- TypeError: Raised when the input is not a list or contains non‑float elements.

### Examples

```python
>>> calculate_average_impact([0.2, 0.5, 0.8])
0.5
```

```python
>>> calculate_average_impact([1.0, 0.9])
0.95
```
