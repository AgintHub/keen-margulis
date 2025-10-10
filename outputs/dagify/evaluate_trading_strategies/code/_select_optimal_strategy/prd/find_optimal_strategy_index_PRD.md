# find_optimal_strategy_index PRD

## Description
Returns the index of the highest score in a list of strategy scores.


## Conceptual Info

Determines which strategy has the highest score among a list of computed strategy scores.

## Docstring

### Summary
Return the index of the maximum score in a list of strategy scores, with error handling for invalid input.

### Parameters

- **scores** (List[float]): A non-empty list of numerical scores for each strategy.

### Returns

int: The zero-based index of the strategy with the highest score.

### Raises

- ValueError: If the scores list is empty.
- TypeError: If the scores parameter is not a list or contains non-numeric elements.

### Examples

```python
>>> find_optimal_strategy_index([0.5, 1.2, 0.9])
1
```

```python
>>> find_optimal_strategy_index([10, 20, 30])
2
```
