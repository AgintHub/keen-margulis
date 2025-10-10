# normalize_market_data PRD

## Description
Normalizes market data by processing current prices, historical prices, and trading volumes into a standardized format.


## Conceptual Info

This shim node is responsible for normalizing market data, which includes current prices, historical prices, and trading volumes, into a standardized format that can be used for further analysis.

## Docstring

### Summary
Normalizes market data inputs into a standardized dictionary format.

### Parameters

- **current_prices** (str): A string representation of a list of current prices of assets.
- **historical_prices** (str): A string representation of a list of historical prices of assets.
- **trading_volumes** (str): A string representation of a list of trading volumes of assets.

### Returns

str: A string representation of a dictionary containing the normalized market data.

### Raises

- ValueError: If the input strings cannot be parsed into lists of floats.
- TypeError: If the input parameters are not strings.

### Examples

```python
>>> normalize_market_data('[100.0, 200.0]', '[50.0, 150.0, 250.0]', '[1000.0, 2000.0]')
'{"current_prices": [100.0, 200.0], "historical_prices": [50.0, 150.0, 250.0], "trading_volumes": [1000.0, 2000.0]}'
```

```python
>>> normalize_market_data('[150.0, 250.0]', '[75.0, 175.0, 275.0]', '[1500.0, 2500.0]')
'{"current_prices": [150.0, 250.0], "historical_prices": [75.0, 175.0, 275.0], "trading_volumes": [1500.0, 2500.0]}'
```
