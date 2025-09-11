# identify_trading_instruments PRD

## Description
Identify the trading instruments to be included in the trading workflow, such as stocks, options, futures, and forex.


## Conceptual Info

This node identifies the trading instruments to be included in the trading workflow.

## Docstring

### Summary
Identify trading instruments for the trading workflow.

### Parameters

- **instruments_info** (dict): Dictionary containing information about trading instruments.

### Returns

dict: Dictionary containing identified trading instruments, exchanges, listings, and market capitalizations.

### Raises

- ValueError: If instruments_info is empty or None.

### Examples

```python
>>> identify_trading_instruments({'instruments': ['AAPL', 'GOOG'], 'exchanges': ['NASDAQ'], 'listings': ['AAPL', 'GOOG'], 'market_capitalizations': [1000.0, 2000.0]})
{'trading_instruments': ['AAPL', 'GOOG'], 'exchanges': ['NASDAQ'], 'listings': ['AAPL', 'GOOG'], 'market_capitalizations': [1000.0, 2000.0]}
```
