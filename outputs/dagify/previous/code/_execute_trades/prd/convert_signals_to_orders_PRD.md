# convert_signals_to_orders PRD

## Description
Converts trading signals and their confidence levels into a list of trade orders represented as dictionaries.


## Conceptual Info

This shim function is responsible for transforming trading signals and their associated confidence levels into a structured format representing trade orders, which can be used for execution.

## Docstring

### Summary
Converts trading signals and confidence levels into trade orders.

### Parameters

- **signals** (str): A JSON encoded string representing a list of trading signals.
- **confidence_levels** (str): A JSON encoded string representing a list of confidence levels corresponding to the trading signals.

### Returns

List[dict]: A list of dictionaries where each dictionary contains details of a trade order, including trade type, quantity, and price, derived from the input signals and confidence levels.

### Raises

- ValueError: Raised when the input signals or confidence levels are not valid JSON encoded lists, or when their lengths do not match.
- TypeError: Raised when the decoded JSON does not result in a list for signals or a list of floats for confidence levels.

### Examples

```python
>>> import json
>>> signals = json.dumps(['buy', 'sell'])
>>> confidence_levels = json.dumps([0.8, 0.7])
>>> convert_signals_to_orders(signals, confidence_levels)
[{'trade_type': 'buy', 'confidence': 0.8, 'quantity': 100, 'price': 50.0}, {'trade_type': 'sell', 'confidence': 0.7, 'quantity': 50, 'price': 51.0}]
```

```python
>>> import json
>>> signals = json.dumps(['buy'])
>>> confidence_levels = json.dumps([0.9])
>>> convert_signals_to_orders(signals, confidence_levels)
[{'trade_type': 'buy', 'confidence': 0.9, 'quantity': 200, 'price': 49.0}]
```
