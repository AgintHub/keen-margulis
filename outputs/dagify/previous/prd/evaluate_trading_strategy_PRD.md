# evaluate_trading_strategy PRD

## Description
Evaluate the trading strategy based on the simulation results.


## Conceptual Info

The node evaluates the trading strategy's effectiveness based on simulated trade outcomes and performance metrics.

## Docstring

### Summary
Evaluates the trading strategy based on simulated trades and performance metrics.

### Parameters

- **simulated_trades** (List[float]): 2D list of simulated trade outcomes from the 'simulate_trades' node.
- **performance_metrics** (List[float]): List of performance metrics for the simulated trades from the 'simulate_trades' node.

### Returns

Tuple[float, List[str]]: A tuple containing the overall effectiveness of the trading strategy as a float and a list of areas for improvement as strings.

### Raises

- ValueError: If the simulated trades or performance metrics are empty or invalid.

### Examples

```python
>>> simulated_trades = [[100.0, 105.0, 110.0], [120.0, 115.0, 110.0]]
>>> performance_metrics = [0.05, 0.02, -0.03]
>>> evaluate_trading_strategy(simulated_trades, performance_metrics)
(0.75, ['Risk Management', 'Trading Rules'])
```

```python
>>> simulated_trades = [[100.0, 95.0, 90.0], [85.0, 80.0, 75.0]]
>>> performance_metrics = [-0.05, -0.02, -0.03]
>>> evaluate_trading_strategy(simulated_trades, performance_metrics)
(0.25, ['Market Analysis', 'Position Sizing'])
```
