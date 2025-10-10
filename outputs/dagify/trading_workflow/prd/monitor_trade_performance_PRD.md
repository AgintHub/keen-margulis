# monitor_trade_performance PRD

## Description
Monitor the performance of executed trades


## Conceptual Info

The node analyzes the performance of trades executed by the 'execute_trades' node, providing metrics and a summary.

## Docstring

### Summary
Monitors and analyzes the performance of executed trades based on the trade results and status from the 'execute_trades' node.

### Parameters

- **trade_results** (List[str]): Results of the executed trades from the 'execute_trades' node.
- **trade_status** (List[str]): Status of the executed trades (e.g., success, failure) from the 'execute_trades' node.

### Returns

Tuple[List[float], str]: A tuple containing performance metrics as a list of floats and a summary of the trade performance as a string.

### Raises

- ValueError: If trade results or status are not provided or are invalid.

### Examples

```python
>>> trade_results = ['profit:100', 'loss:50']
>>> trade_status = ['success', 'failure']
>>> performance_metrics, performance_summary = monitor_trade_performance(trade_results, trade_status)
[0.5, 100.0], 'Overall performance: 50% success rate, average profit: 100.0'
```

```python
>>> trade_results = ['profit:200', 'profit:150']
>>> trade_status = ['success', 'success']
>>> performance_metrics, performance_summary = monitor_trade_performance(trade_results, trade_status)
[1.0, 175.0], 'Overall performance: 100% success rate, average profit: 175.0'
```
