# format_trading_signal PRD

## Description
Formats trading signal details into a standardized string representation for further processing or output.


## Conceptual Info

This shim node is responsible for taking trading signal details and formatting them into a standardized string representation. It plays a crucial role in the generate_trading_signals function by ensuring that the output is consistent and can be easily processed or displayed.

## Docstring

### Summary
Formats the given trading signal details into a standardized string representation.

### Parameters

- **signal_details** (str): A string containing the trading signal details to be formatted.

### Returns

str: The formatted trading signal as a string, following a standardized format.

### Raises

- ValueError: If the input signal_details are not in the expected format or are missing required information.
- TypeError: If the input signal_details is not of type str.

### Examples

```python
>>> signal_details = '{"signal_type": "buy", "symbol": "AAPL", "confidence": 0.8}'
>>> formatted_signal = format_trading_signal(signal_details=signal_details)
'BUY:AAPL:0.8'
```

```python
>>> signal_details = '{"signal_type": "sell", "symbol": "GOOG", "confidence": 0.4}'
>>> formatted_signal = format_trading_signal(signal_details=signal_details)
'SELL:GOOG:0.4'
```
