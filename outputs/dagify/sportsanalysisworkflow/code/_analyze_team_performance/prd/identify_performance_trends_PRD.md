# identify_performance_trends PRD

## Description
Identifies performance trends based on calculated metrics and game statistics.


## Conceptual Info

This shim node analyzes the given metrics and game statistics to identify performance trends, playing a crucial role in understanding team performance over time.

## Docstring

### Summary
Analyzes metrics and game statistics to identify performance trends.

### Parameters

- **metrics** (str): Serialized list of calculated key performance metrics.
- **game_stats** (str): Serialized list of game statistics.

### Returns

List[float]: List of identified performance trends represented as floating-point numbers.

### Raises

- ValueError: When the input metrics or game statistics are not valid or cannot be deserialized.
- TypeError: When the input types are incorrect or do not match the expected format.

### Examples

```python
>>> import json
>>> metrics = json.dumps([0.8, 0.9, 0.7]).tolist()
>>> game_stats = json.dumps([100, 120, 90]).tolist()
>>> identify_performance_trends(metrics=metrics, game_stats=game_stats)
[0.85, 0.95, 0.75]
```

```python
>>> import json
>>> metrics = json.dumps([0.5, 0.6, 0.4]).tolist()
>>> game_stats = json.dumps([50, 60, 40]).tolist()
>>> identify_performance_trends(metrics=metrics, game_stats=game_stats)
[0.55, 0.65, 0.45]
```
