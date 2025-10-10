# fetch_current_prices PRD

## Description
Fetches current prices for the given assets.


## Conceptual Info

This shim node is responsible for retrieving the current market prices of specified financial assets.

## Docstring

### Summary
Fetches current prices for a given list of assets represented as a comma-separated string.

### Parameters

- **assets** (str): Comma-separated string of asset identifiers (e.g., stock symbols, currency pairs).

### Returns

List[float]: A list of current prices corresponding to the assets provided, in the same order.

### Raises

- ValueError: If the input string is empty or contains invalid asset identifiers.
- TypeError: If the input is not a string.

### Examples

```python
>>> fetch_current_prices('AAPL,GOOG,MSFT')
[150.5, 2800.2, 230.1]
```

```python
>>> fetch_current_prices('EURUSD,GBPUSD')
[1.1001, 1.3002]
```
