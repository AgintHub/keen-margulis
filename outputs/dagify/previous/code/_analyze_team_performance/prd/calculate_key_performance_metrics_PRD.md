# calculate_key_performance_metrics PRD

## Description
Calculates key performance metrics based on game statistics and performance metrics.


## Conceptual Info

This shim node is crucial for analyzing team performance by calculating key metrics that are derived from game statistics and performance metrics.

## Docstring

### Summary
Calculates key performance metrics based on the provided game statistics and performance metrics.

### Parameters

- **game_stats** (str): A string representation of game statistics.
- **performance_metrics** (str): A string representation of performance metrics.

### Returns

List[float]: A list of calculated key performance metrics as floating-point numbers.

### Raises

- ValueError: If the input game statistics or performance metrics are invalid or cannot be parsed.
- TypeError: If the input types are not strings as expected.

### Examples

```python
>>> game_stats = '1,2,3,4,5'
>>> performance_metrics = '0.1,0.2,0.3,0.4,0.5'
>>> calculate_key_performance_metrics(game_stats, performance_metrics)
[0.2, 0.4, 0.6, 0.8, 1.0]
```

```python
>>> game_stats = '10,20,30'
>>> performance_metrics = '0.5,0.6,0.7'
>>> calculate_key_performance_metrics(game_stats, performance_metrics)
[5.0, 12.0, 21.0]
```
