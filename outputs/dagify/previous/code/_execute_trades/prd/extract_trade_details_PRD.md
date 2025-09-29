# extract_trade_details PRD

## Description
Extracts detailed information about a trade execution based on the trade execution result and the trading signal.


## Conceptual Info

This shim function plays a crucial role in extracting detailed information about trade executions based on the result of the trade execution and the trading signal received.

## Docstring

### Summary
Extracts trade details from a trade execution result based on the provided trading signal.

### Parameters

- **result** (str): The trade execution result containing information about the trade outcome.
- **signal** (str): The trading signal (buy/sell/hold) that was executed.

### Returns

str: A string containing the extracted trade details, formatted appropriately based on the signal and result.

### Raises

- ValueError: If the input signal is not one of 'buy', 'sell', or 'hold'.
- TypeError: If the input result is not a string or is not properly formatted.

### Examples

```python
>>> extract_trade_details(result='{"trade_id": 123, "status": "success"}', signal='buy')
"Trade ID: 123, Status: success, Signal: buy"
```

```python
>>> extract_trade_details(result='{"trade_id": 456, "status": "failed"}', signal='sell')
"Trade ID: 456, Status: failed, Signal: sell"
```
