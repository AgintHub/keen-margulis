# determine_improvement_areas PRD

## Description
Determines areas for player improvement based on their strengths, weaknesses, and performance metrics.


## Conceptual Info

This shim function plays a crucial role in analyzing player performance by identifying areas that require improvement based on their strengths, weaknesses, and performance metrics.

## Docstring

### Summary
Determines areas for player improvement based on strengths, weaknesses, and performance metrics.

### Parameters

- **strengths** (str): The player's strengths as identified by the system.
- **weaknesses** (str): The player's weaknesses as identified by the system.
- **performance_metrics** (str): The player's performance metrics used to assess their overall performance.

### Returns

List[str]: A list of areas where the player needs improvement.

### Raises

- ValueError: If the input parameters are not valid or are missing required information.
- TypeError: If the input parameters are not of the expected type.

### Examples

```python
>>> strengths = 'good shooting, fast runner'
>>> weaknesses = 'poor defense, slow passer'
>>> performance_metrics = '70% shooting accuracy, 4.5 speed rating'
>>> improvement_areas = determine_improvement_areas(strengths, weaknesses, performance_metrics)
['defensive techniques', 'passing accuracy']
```

```python
>>> strengths = 'excellent dribbling, high stamina'
>>> weaknesses = 'inaccurate shooting, weak tackling'
>>> performance_metrics = '90% dribbling success, 8.5 stamina rating'
>>> improvement_areas = determine_improvement_areas(strengths, weaknesses, performance_metrics)
['shooting practice', 'tackling drills']
```
