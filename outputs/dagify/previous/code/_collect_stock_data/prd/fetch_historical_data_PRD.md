# fetch_historical_data PRD

## Description
Fetches historical market data for a list of stock symbols and returns it in a structured format.


## Conceptual Info

This shim node is responsible for retrieving historical market data for a given list of stock symbols, playing a crucial role in the stock data collection pipeline.

## Docstring

### Summary
Fetches historical market data for the given stock symbols and returns it as a JSON string.

### Parameters

- **symbols** (str): A comma-separated list of stock symbols for which historical data is to be fetched.

### Returns

str: A JSON string containing historical market data, including prices and trading volumes, for the given stock symbols.

### Raises

- ValueError: If the input symbols are invalid or if the data source is unavailable.
- TypeError: If the input is not a string or if the symbols are not properly formatted.

### Examples

```python
>>> historical_data = fetch_historical_data(symbols='AAPL,GOOG,MSFT')
>>> print(historical_data)
{"AAPL": {"prices": [100.0, 101.0], "volumes": [1000, 1200]}, "GOOG": {"prices": [2000.0, 2010.0], "volumes": [500, 600]}, "MSFT": {"prices": [150.0, 151.0], "volumes": [800, 900]}}
```

```python
>>> try:
...     historical_data = fetch_historical_data(symbols='INVALID')
...     print(historical_data)
>>> except ValueError as e:
...     print(e)
Invalid stock symbol: INVALID
```
