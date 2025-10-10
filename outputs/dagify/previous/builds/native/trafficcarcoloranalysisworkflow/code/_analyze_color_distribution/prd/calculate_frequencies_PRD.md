# calculate_frequencies PRD

## Description
Calculates the frequency of occurrences based on given counts and total.


## Conceptual Info

This shim node is responsible for calculating frequencies from given counts and a total, typically used in statistical analysis or data processing pipelines.

## Docstring

### Summary
Calculates frequencies of occurrences based on input counts and total, returning a list of float values.

### Parameters

- **counts** (str): String representation of a list of integers where each integer represents the count of occurrences.
- **total** (str): String representation of an integer that represents the total count of all occurrences.

### Returns

List[float]: A list of float values representing the frequency of each count relative to the total.

### Raises

- ValueError: If the input counts or total cannot be properly parsed into integers, or if total is zero.
- TypeError: If the input counts or total are not strings that can be interpreted as integers or lists of integers.

### Examples

```python
>>> counts = '[1, 2, 3]'
>>> total = '6'
>>> calculate_frequencies(counts=counts, total=total)
[0.16666666666666666, 0.3333333333333333, 0.5]
```

```python
>>> counts = '[4, 5, 6]'
>>> total = '15'
>>> calculate_frequencies(counts=counts, total=total)
[0.26666666666666666, 0.3333333333333333, 0.4]
```
