# analyze_trade_performance PRD

## Description
Analyzes trade performance based on provided trade data and returns performance metrics.


## Conceptual Info

This shim node analyzes trade performance by processing trade data and returning key performance metrics.

## Docstring

### Summary
Analyzes trade performance based on the provided trade data and returns a dictionary of performance metrics as a JSON string.

### Parameters

- **trade_data** (str): A JSON string representing a list of dictionaries containing trade details

### Returns

str: A JSON string representing a dictionary of performance metrics

### Raises

- ValueError: When the input trade data is not a valid JSON string or does not represent a list of dictionaries
- TypeError: When the input trade data is not a string

### Examples

```python
>>> import json
>>> trade_data = json.dumps([{'trade_type': 'buy', 'quantity': 100, 'price': 50.0}, {'trade_type': 'sell', 'quantity': 50, 'price': 55.0}])
>>> analyze_trade_performance(trade_data=trade_data)
{"total_profit": 250.0, "return_on_investment": 0.05}
```

```python
>>> import json
>>> trade_data = json.dumps([{'trade_type': 'buy', 'quantity': 200, 'price': 40.0}])
>>> analyze_trade_performance(trade_data=trade_data)
{"total_profit": 0.0, "return_on_investment": 0.0}
```
