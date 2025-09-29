# extract_market_prices PRD

## Description
Extracts a list of market prices from the provided validated market data.


## Conceptual Info

This shim extracts market prices from validated market data, playing a crucial role in the market data processing pipeline.

## Docstring

### Summary
Extracts market prices from the provided validated market data string.

### Parameters

- **data** (str): Validated market data containing prices to be extracted.

### Returns

List[float]: List of extracted market prices.

### Raises

- ValueError: If the input data is malformed or does not contain valid market prices.
- TypeError: If the input data is not of type string.

### Examples

```python
>>> extract_market_prices(data='{"prices": [10.5, 20.3, 30.7]}')
[10.5, 20.3, 30.7]
```

```python
>>> extract_market_prices(data='{}')
[]
```
