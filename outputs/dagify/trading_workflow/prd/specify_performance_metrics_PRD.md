# specify_performance_metrics PRD

## Description
Define metrics to evaluate the performance of the trading system.


## Conceptual Info

The `specify_performance_metrics` node takes the high‑level objectives defined for the trading system and produces a set of quantitative performance indicators that can be used by downstream monitoring and control systems. These metrics provide a standardized way to benchmark the strategy against its risk tolerance and return targets.

## Docstring

### Summary
Generate a dictionary of performance metrics based on defined trading objectives.

### Parameters

- **return_target_percent** (float): Target annualized return expressed as a percentage (e.g., 12.0 for 12%).
- **max_drawdown_percent** (float): Maximum acceptable drawdown expressed as a percentage of equity (e.g., 10.0 for 10%).
- **risk_tolerance_category** (str): Risk tolerance level, one of 'conservative', 'moderate', or 'aggressive'.
- **constraints** (List[str]): Additional textual constraints or special requirements for the strategy.

### Returns

dict[str, float]: A mapping from metric names to their computed float values. The dictionary contains the keys: roi, sharpe_ratio, max_drawdown, annualized_volatility, win_rate, and annualized_return.

### Raises

- ValueError: If any of the required input parameters are missing or of an incorrect type.

### Examples

```python
>>> metrics = specify_performance_metrics(
...     return_target_percent=12.0,
...     max_drawdown_percent=10.0,
...     risk_tolerance_category='moderate',
...     constraints=['No leverage']
>>> )
{'roi': 0.12, 'sharpe_ratio': 1.4, 'max_drawdown': 0.10, 'annualized_volatility': 0.25, 'win_rate': 0.55, 'annualized_return': 0.12}
```

```python
>>> metrics = specify_performance_metrics(
...     return_target_percent=8.0,
...     max_drawdown_percent=5.0,
...     risk_tolerance_category='conservative',
...     constraints=[]
>>> )
{'roi': 0.08, 'sharpe_ratio': 1.1, 'max_drawdown': 0.05, 'annualized_volatility': 0.18, 'win_rate': 0.60, 'annualized_return': 0.08}
```
