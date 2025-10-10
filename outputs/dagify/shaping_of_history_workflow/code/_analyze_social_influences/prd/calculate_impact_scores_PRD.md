# calculate_impact_scores PRD

## Description
Calculates a normalized impact score for each provided social factor.


## Conceptual Info

This shim provides a mechanism to quantify the relative importance of social factors within a historical analysis, producing a score per factor that can be aggregated or compared.

## Docstring

### Summary
Compute impact scores for each social factor.

### Parameters

- **social_factors** (list of str): A list of social factor names to evaluate.

### Returns

list of float: A list of impact scores between 0.0 and 1.0, one per input factor.

### Raises

- ValueError: If the input list is empty.
- TypeError: If any element of the input is not a string.

### Examples

```python
>>> scores = calculate_impact_scores(['media coverage', 'public protest', 'policy change'])
>>> print(scores)
[0.78, 0.65, 0.92]
```

```python
>>> try:
...     calculate_impact_scores([])
>>> except ValueError as e:
...     print(e)
Input list of social factors must contain at least one element.
```
