# fetch_market_metrics_data PRD

## Description
Fetches and returns market metrics data as a JSON string


## Conceptual Info

Shim to retrieve raw market metrics from an external data source and deliver them as a JSON string for downstream processing.

## Docstring

### Summary
Fetches market metrics data from the market data source and returns it as a JSON string.

### Returns

str: A JSON-formatted string representing a dictionary of market metrics.

### Raises

- ConnectionError: Raised when unable to connect to the market data source.
- ValueError: Raised when the retrieved data is missing required fields or is malformed.

### Examples

```python
>>> result = fetch_market_metrics_data()
>>> print(result)
"{\"market_metrics\": [\"volatility\", \"liquidity\"]}"
```

```python
>>> try:
...     fetch_market_metrics_data()
>>> except ConnectionError as e:
...     print('Connection failed:', e)
"Connection failed: Failed to connect to market data source"
```
