# parse_trade_profits PRD

## Description
Parses trade results to extract profit values as a list of floats.


## Conceptual Info

This shim function is designed to parse trade results and extract profit values, playing a crucial role in analyzing trade performance.

## Docstring

### Summary
Parses a string of trade results and returns a list of profit values as floats.

### Parameters

- **trade_results** (str): A string containing the results of executed trades, potentially including profit information.

### Returns

List[float]: A list of floating-point numbers representing the profit values extracted from the trade results.

### Raises

- ValueError: If the input string is malformed or does not contain valid profit information.
- TypeError: If the input is not a string.

### Examples

```python
>>> parse_trade_profits(trade_results='Trade1:Profit=100.5,Trade2:Profit=200.8')
[100.5, 200.8]
```

```python
>>> parse_trade_profits(trade_results='Profit:150.2;Loss:50.1')
[150.2]
```
