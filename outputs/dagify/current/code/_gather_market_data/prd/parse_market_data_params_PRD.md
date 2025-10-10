# parse_market_data_params PRD

## Description
Parses input parameters for market data gathering into a structured dictionary.


## Conceptual Info

This shim function is responsible for parsing input parameters for market data gathering into a structured dictionary that can be used by subsequent functions.

## Docstring

### Summary
Parses input string and keyword arguments into a dictionary of market data parameters.

### Parameters

- **input_string** (str): The input string containing market data parameters in a specific format.
- **kwargs** (str): Additional keyword arguments containing market data parameters.

### Returns

str: A JSON string representing a dictionary with keys 'assets', 'start_date', and 'end_date'.

### Raises

- ValueError: If the input string or keyword arguments are invalid or missing required parameters.
- TypeError: If the input types are incorrect or cannot be parsed.

### Examples

```python
>>> parse_market_data_params(input_string='assets:AAPL,GOOG;start_date:2022-01-01;end_date:2022-12-31', kwargs='{}')
>>> parse_market_data_params(input_string='assets:MSFT;start_date:2023-01-01;end_date:2023-06-30', kwargs='{"assets": ["MSFT"]}')
>>> parse_market_data_params(input_string='', kwargs='{"assets": ["AAPL", "GOOG"], "start_date": "2022-01-01", "end_date": "2022-12-31"}')
{"assets": ["AAPL", "GOOG"], "start_date": "2022-01-01", "end_date": "2022-12-31"}
```
