# format_trade_details PRD

## Description
Formats trade execution results into a list of human-readable trade details.


## Conceptual Info

This shim node is responsible for taking trade execution results and formatting them into a list of human-readable strings that contain trade details such as trade type, quantity, and price.

## Docstring

### Summary
Formats trade execution results into a list of human-readable trade details.

### Parameters

- **results** (str): Trade execution results in a string format that needs to be parsed and formatted.

### Returns

List[str]: List of formatted trade details, including information such as trade type, quantity, and price.

### Raises

- ValueError: If the input results string is malformed or cannot be parsed.
- TypeError: If the input results is not of type str.

### Examples

```python
>>> execution_results = '{"trade_type": "buy", "quantity": 100, "price": 50.0}'
>>> formatted_details = format_trade_details(results=execution_results)
>>> print(formatted_details)
["Trade Type: buy, Quantity: 100, Price: 50.0"]
```

```python
>>> execution_results = '[{"trade_type": "sell", "quantity": 50, "price": 55.0}, {"trade_type": "buy", "quantity": 200, "price": 52.0}]'
>>> formatted_details = format_trade_details(results=execution_results)
>>> print(formatted_details)
["Trade Type: sell, Quantity: 50, Price: 55.0", "Trade Type: buy, Quantity: 200, Price: 52.0"]
```
