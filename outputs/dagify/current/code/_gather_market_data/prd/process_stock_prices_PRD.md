# process_stock_prices PRD

## Description
Parses raw stock price data from a string and returns a list of float prices.


## Conceptual Info

This shim takes raw stock price data in textual form, validates and parses it into a structured list of floats for downstream market‑data processing.

## Docstring

### Summary
Converts raw stock price data into a list of floats.

### Parameters

- **data** (str): Raw stock price data, either as a comma‑separated string or a JSON array string.

### Returns

LIST_FLOAT: A list of float values representing the processed stock prices.

### Raises

- ValueError: Raised when the input string cannot be parsed into valid float values.
- TypeError: Raised when the input is not of type str.

### Examples

```python
>>> prices = process_stock_prices('100.5, 101.2, 102')
[100.5, 101.2, 102.0]
```

```python
>>> try:
...     process_stock_prices('abc, 200')
>>> except ValueError as e:
...     print(e)
"Invalid stock price data: cannot convert to float"
```
