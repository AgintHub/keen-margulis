# calculate_strategy_scores PRD

## Description
Calculates a numeric score for each trading strategy based on its evaluation text and associated risk value.


## Conceptual Info

This shim computes a quantitative score for each trading strategy by combining the textual evaluation of the strategy with its associated risk level, enabling downstream selection of the optimal strategy.

## Docstring

### Summary
Compute strategy scores from evaluation texts and risk values.

### Parameters

- **evaluations** (List[str]): A list of textual evaluations for each trading strategy.
- **risks** (List[float]): A list of risk values (between 0 and 1) corresponding to each strategy.

### Returns

List[float]: A list of float scores, one for each strategy.

### Raises

- ValueError: Raised if evaluations and risks lists have different lengths.
- TypeError: Raised if evaluations is not a list of strings or risks is not a list of floats.

### Examples

```python
>>> calculate_strategy_scores(['Buy', 'Sell'], [0.1, 0.3])
[0.9, 0.7]
```

```python
>>> calculate_strategy_scores(['Long', 'Short', 'Hold'], [0.05, 0.2, 0.15])
[0.95, 0.8, 0.85]
```
