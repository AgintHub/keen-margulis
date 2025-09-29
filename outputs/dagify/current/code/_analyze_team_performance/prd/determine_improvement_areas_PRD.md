# determine_improvement_areas PRD

## Description
Determines areas for team improvement based on strengths, weaknesses, and performance metrics.


## Conceptual Info

This shim node plays a crucial role in analyzing team performance by identifying areas for improvement based on the team's strengths, weaknesses, and performance metrics. It acts as a bridge between the analysis of team performance and the formulation of strategies for improvement.

## Docstring

### Summary
Determines areas for team improvement based on the provided strengths, weaknesses, and performance metrics.

### Parameters

- **strengths** (str): Comma-separated list of team strengths
- **weaknesses** (str): Comma-separated list of team weaknesses
- **metrics** (str): Comma-separated list of performance metrics

### Returns

List[str]: List of areas where the team can improve, derived from the input strengths, weaknesses, and metrics.

### Raises

- ValueError: If the input strengths, weaknesses, or metrics are not in the expected format.
- TypeError: If the input types are not as expected (e.g., not strings).

### Examples

```python
>>> strengths = 'good defense,strong teamwork'
>>> weaknesses = 'poor offense,weak bench'
>>> metrics = '50,60,70'
>>> result = determine_improvement_areas(strengths, weaknesses, metrics)
['enhance offense', 'strengthen bench']
```

```python
>>> strengths = 'fast break,good shooting'
>>> weaknesses = 'defensive lapses,turnovers'
>>> metrics = '40,50,60'
>>> result = determine_improvement_areas(strengths, weaknesses, metrics)
['reduce turnovers', 'improve defensive strategy']
```
