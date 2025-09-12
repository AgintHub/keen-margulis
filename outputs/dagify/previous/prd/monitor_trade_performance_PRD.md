# monitor_trade_performance PRD

## Description
Monitor the performance of executed trades


## Conceptual Info

This node analyzes the performance of executed trades, assessing their impact on the portfolio's value and risk exposure.

## Docstring

### Summary
Monitor the performance of executed trades, calculating key metrics and assessing portfolio impact.

### Parameters

- **trade_execution_status** (List[str]): Status of each trade execution (e.g., success, failed, pending) from the execute_trades node
- **trade_execution_timestamps** (List[str]): Timestamps for when each trade was executed from the execute_trades node
- **trade_details** (List[str]): Details of the executed trades, including assets, quantities, and prices from the execute_trades node

### Returns

dict: A dictionary containing trade performance metrics, portfolio value, and risk exposure.

### Raises

- ValueError: If trade execution status, timestamps, or details are inconsistent or missing.

### Examples

```python
>>> trade_execution_status = ['success', 'success']
>>> trade_execution_timestamps = ['2023-01-01 12:00:00', '2023-01-02 12:00:00']
>>> trade_details = ['asset1,100,100.0', 'asset2,50,50.0']
>>> monitor_trade_performance(trade_execution_status, trade_execution_timestamps, trade_details)
{'trade_performance_metrics': [0.05, 0.03], 'portfolio_value': 10500.0, 'risk_exposure': 0.02}
```
