# fetch_stock_prices PRD

## Description
Fetches stock prices from specified data sources and returns them as a list of floats.


## Conceptual Info

This shim function is designed to retrieve stock prices from various data sources. It plays a crucial role in the market data collection process by providing the necessary stock price data.

## Docstring

### Summary
Fetches stock prices from the specified data sources and returns them as a list of floats.

### Parameters

- **sources** (str): A string representing the data sources to fetch stock prices from.

### Returns

List[float]: A list of floating-point numbers representing the stock prices fetched from the specified data sources.

### Raises

- ValueError: If the input 'sources' is not a valid string or is empty.
- TypeError: If the input 'sources' is not of type string.

### Examples

```python
>>> fetch_stock_prices('yahoo_finance')
[100.5, 101.2, 102.1]
```

```python
>>> fetch_stock_prices('nasdaq')
[200.1, 201.5, 202.3]
```
