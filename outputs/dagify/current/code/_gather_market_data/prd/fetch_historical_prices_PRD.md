# fetch_historical_prices PRD

## Description
Fetches historical price data for specified assets over a given date range.


## Conceptual Info

This shim node is responsible for retrieving historical price data for a list of assets between specified start and end dates. It plays a crucial role in the gather_market_data function by providing the necessary historical price information.

## Docstring

### Summary
Fetches historical prices for given assets between start_date and end_date.

### Parameters

- **assets** (str): Comma-separated string of asset identifiers to fetch historical prices for.
- **start_date** (str): Start date of the historical period in 'YYYY-MM-DD' format.
- **end_date** (str): End date of the historical period in 'YYYY-MM-DD' format.

### Returns

List[float]: A list of historical prices for the specified assets over the given date range.

### Raises

- ValueError: If the date format is invalid or if start_date is later than end_date.
- TypeError: If assets is not a string or if start_date/end_date are not strings.

### Examples

```python
>>> fetch_historical_prices(assets='AAPL,GOOG', start_date='2022-01-01', end_date='2022-01-31')
[100.0, 101.0, 102.0, ...]
```

```python
>>> fetch_historical_prices(assets='MSFT', start_date='2023-01-01', end_date='2023-01-05')
[200.0, 201.0, 202.0, 203.0, 204.0]
```
