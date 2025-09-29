# collect_stock_data PRD

## Description
Collect raw stock market data from reliable sources.


## Conceptual Info

This node collects raw stock market data, including historical prices and trading volumes, for specified stock symbols from reliable sources.

## Docstring

### Summary
Collects historical stock prices and trading volumes for given stock symbols.

### Parameters

- **stock_symbols** (List[str]): List of stock symbols to gather data for.

### Returns

Tuple[List[str], List[float], List[int]]: A tuple containing the list of stock symbols, their historical prices, and trading volumes.

### Raises

- ValueError: If the input stock symbols list is empty or contains invalid symbols.
- ConnectionError: If there's a failure connecting to the data source.

### Examples

```python
>>> stock_data = collect_stock_data(['AAPL', 'GOOG'])
>>> print(stock_data)
(['AAPL', 'GOOG'], [150.5, 2800.2], [100000, 50000])
```

```python
>>> stock_symbols = ['MSFT', 'AMZN']
>>> data = collect_stock_data(stock_symbols)
>>> print(data)
(['MSFT', 'AMZN'], [220.1, 3200.5], [80000, 70000])
```
