# identify_team_weaknesses PRD

## Description
Identifies team weaknesses based on performance metrics and trends.


## Conceptual Info

This shim node analyzes team performance metrics and trends to identify weaknesses that need improvement.

## Docstring

### Summary
Identifies team weaknesses based on the provided performance metrics and trends.

### Parameters

- **metrics** (str): String representation of team performance metrics.
- **trends** (str): String representation of team performance trends.

### Returns

List[str]: List of identified team weaknesses.

### Raises

- ValueError: When input metrics or trends are invalid or malformed.
- TypeError: When input types are incorrect, such as non-string inputs.

### Examples

```python
>>> metrics = '0.8,0.7,0.9'
>>> trends = 'up,down,up'
>>> identify_team_weaknesses(metrics=metrics, trends=trends)
['Defensive instability', 'Inconsistent performance']
```

```python
>>> metrics = '0.5,0.6,0.4'
>>> trends = 'down,up,down'
>>> identify_team_weaknesses(metrics=metrics, trends=trends)
['Low scoring rate', 'Declining performance']
```
