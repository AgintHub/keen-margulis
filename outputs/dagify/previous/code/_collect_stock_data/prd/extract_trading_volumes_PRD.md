# extract_trading_volumes PRD

## Description
Extracts trading volumes from raw market data for stock symbols.


## Conceptual Info

This shim function is designed to process raw market data and extract trading volumes for a list of stock symbols, playing a crucial role in stock data analysis.

## Docstring

### Summary
Extracts and returns trading volumes from raw market data.

### Parameters

- **data** (str): Raw market data containing trading information for stock symbols, expected to be in a format that can be processed to extract trading volumes.

### Returns

List[int]: A list of integers representing the trading volumes for each stock symbol analyzed.

### Raises

- ValueError: If the input data is not in the expected format or if trading volumes cannot be extracted.
- TypeError: If the input data type is not a string.

### Examples

```python
>>> raw_data = '{"stock1": {"volume": 1000}, "stock2": {"volume": 2000}}'
>>> trading_volumes = extract_trading_volumes(data=raw_data)
[1000, 2000]
```

```python
>>> raw_data = '{"AAPL": {"trading_volume": 5000}, "GOOG": {"trading_volume": 3000}}'
>>> trading_volumes = extract_trading_volumes(data=raw_data)
[5000, 3000]
```
