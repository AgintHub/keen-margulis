# parse_trade_details PRD

## Description
Parses trade details from a list of strings into a structured list of dictionaries.


## Conceptual Info

This shim node is responsible for transforming raw trade details provided as a list of strings into a structured format (list of dictionaries) that can be used for further analysis, such as analyzing trade performance and generating strategy adjustments.

## Docstring

### Summary
Parses trade details from a list of strings into a structured list of dictionaries, where each dictionary represents a trade with relevant details.

### Parameters

- **trade_details** (List[str]): A list of strings containing trade details in a raw format.

### Returns

List[dict]: A list of dictionaries, where each dictionary contains structured information about a trade, including trade type, quantity, and price.

### Raises

- ValueError: If the input list contains strings that cannot be parsed into valid trade details.
- TypeError: If the input is not a list of strings.

### Examples

```python
>>> trade_details = ['Trade type: Buy, Quantity: 100, Price: 50.0', 'Trade type: Sell, Quantity: 50, Price: 55.0']
>>> parsed_trade_details = parse_trade_details(trade_details=trade_details)
>>> print(parsed_trade_details)
[{'trade_type': 'Buy', 'quantity': 100, 'price': 50.0}, {'trade_type': 'Sell', 'quantity': 50, 'price': 55.0}]
```

```python
>>> trade_details = ['Invalid trade detail']
>>> try:
...     parse_trade_details(trade_details=trade_details)
>>> except ValueError as e:
...     print(e)
"Failed to parse trade details: Invalid trade detail"
```
