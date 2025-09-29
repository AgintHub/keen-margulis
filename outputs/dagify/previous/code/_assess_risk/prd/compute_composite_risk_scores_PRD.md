# compute_composite_risk_scores PRD

## Description
This shim node computes composite risk scores from various risk components.


## Conceptual Info

This shim node plays a crucial role in risk assessment by aggregating multiple risk metrics into a single composite score, facilitating a more comprehensive risk evaluation.

## Docstring

### Summary
Computes composite risk scores from various risk components.

### Parameters

- **components** (List[List[float]]): A list of lists containing different risk metrics, such as volatility, liquidity, trend analysis, and economic indicators.

### Returns

List[float]: A list of composite risk scores, where each score represents an aggregated risk level derived from the input components.

### Raises

- ValueError: If the input components are empty or not in the expected format.
- TypeError: If the input components are not a list of lists of floats.

### Examples

```python
>>> risk_components = [[0.5, 0.6, 0.7], [0.2, 0.3, 0.4], [0.1, 0.2, 0.3], [0.8, 0.7, 0.6]]
>>> composite_risk_scores = compute_composite_risk_scores(components=risk_components)
[0.45, 0.55, 0.65]
```

```python
>>> risk_components = [[0.9, 0.8], [0.7, 0.6], [0.5, 0.4]]
>>> composite_risk_scores = compute_composite_risk_scores(components=risk_components)
[0.7, 0.6]
```
