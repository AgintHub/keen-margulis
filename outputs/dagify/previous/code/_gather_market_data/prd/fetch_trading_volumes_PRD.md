# fetch_trading_volumes PRD

## Description
Fetches trading volumes for specified assets over a given date range.


## Conceptual Info

This shim node is designed to retrieve trading volume data for a list of assets over a specified date range, playing a crucial role in market data gathering and analysis.

## Docstring

### Summary
Fetches trading volumes for specified assets between given start and end dates.

### Parameters

- **assets** (str): Comma-separated string of asset identifiers to fetch trading volumes for.
- **start_date** (str): Start date of the period in 'YYYY-MM-DD' format.
- **end_date** (str): End date of the period in 'YYYY-MM-DD' format.

### Returns

List[float]: List of trading volumes corresponding to the specified assets over the given date range.

### Raises

- ValueError: If the date range is invalid or assets string is malformed.
- TypeError: If input types are not as expected.

### Examples

```python
>>> fetch_trading_volumes(assets='AAPL,GOOG', start_date='2023-01-01', end_date='2023-01-31')
[1000.0, 500.0]
```

```python
>>> fetch_trading_volumes(assets='MSFT,AMZN', start_date='2023-02-01', end_date='2023-02-28')
[2000.0, 1500.0]
```
