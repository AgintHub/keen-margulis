# monitor_trade_performance PRD

## Description
Monitor the performance of executed trades and adjust strategies as needed.


## Conceptual Info

This node monitors the performance of trades executed by the 'execute_trades' node and provides recommendations for adjusting trading strategies based on the performance metrics.

## Docstring

### Summary
Monitor trade performance and provide strategy adjustment recommendations.

### Parameters

- **trade_outcomes** (List[str]): Outcomes of executed trades from the 'execute_trades' node.
- **trade_volumes** (List[int]): Volumes of executed trades from the 'execute_trades' node.

### Returns

Tuple[List[float], List[str]]: A tuple containing performance metrics of executed trades and recommendations for strategy adjustments.

### Raises

- ValueError: If trade outcomes or volumes are empty or mismatched.

### Examples

```python
>>> trade_outcomes = ['success', 'failure', 'success']
>>> trade_volumes = [100, 200, 300]
>>> monitor_trade_performance(trade_outcomes, trade_volumes)
([0.8, 0.2], ['Increase risk for successful trades', 'Review strategy for failed trades'])
```

```python
>>> trade_outcomes = ['success', 'success', 'success']
>>> trade_volumes = [500, 600, 700]
>>> monitor_trade_performance(trade_outcomes, trade_volumes)
([1.0], ['Continue current successful strategy'])
```
