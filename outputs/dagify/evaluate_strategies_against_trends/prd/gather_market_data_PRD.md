# gather_market_data PRD

## Description
Collect relevant market data including prices, volumes, and other indicators


## Conceptual Info

The gather_market_data node is responsible for collecting relevant market data, including current and historical prices, as well as trading volumes for specified assets or instruments.

## Docstring

### Summary
Gathers current and historical market data for the specified assets or instruments, returning current prices, historical prices, and trading volumes.

### Parameters

- **assets** (List[str]): List of asset symbols or identifiers to gather data for.
- **start_date** (str): Start date for historical data in 'YYYY-MM-DD' format.
- **end_date** (str): End date for historical data in 'YYYY-MM-DD' format.

### Returns

Tuple[List[float], List[float], List[float]]: A tuple containing three lists: current prices, historical prices, and trading volumes for the specified assets.

### Raises

- ValueError: If the assets list is empty or if the start_date is later than end_date.
- ConnectionError: If there's a failure in connecting to the data source.

### Examples

```python
>>> assets = ['AAPL', 'GOOG']
>>> start_date = '2022-01-01'
>>> end_date = '2022-12-31'
>>> result = gather_market_data(assets, start_date, end_date)
([150.0, 2800.0], [120.0, 130.0, ...], [1000.0, 2000.0])
```

```python
>>> assets = ['MSFT']
>>> start_date = '2023-01-01'
>>> end_date = '2023-01-31'
>>> result = gather_market_data(assets, start_date, end_date)
([250.0], [240.0, 245.0, ...], [500.0])
```
