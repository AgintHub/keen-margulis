# process_trade_outcomes PRD

## Description
Processes raw trade result dictionaries into a list of human‑readable outcome strings.


## Conceptual Info

This shim transforms raw trade result dictionaries, typically returned by the trading engine, into a standardized list of outcome strings suitable for downstream reporting and validation.

## Docstring

### Summary
Convert raw trade result dictionaries into readable outcome messages.

### Parameters

- **trade_results** (List[dict]): A list of dictionaries, each representing a trade with keys such as 'symbol', 'price', 'volume', and 'status'.

### Returns

List[str]: A list of strings, each summarizing the outcome of a corresponding trade, e.g., 'Trade AAPL: 100 units at $150.0 executed'.

### Raises

- TypeError: Raised if `trade_results` is not a list or if any element is not a dictionary.
- ValueError: Raised if a dictionary lacks required keys ('symbol', 'price', 'volume', 'status').

### Examples

```python
>>> results = [
...     {'symbol': 'AAPL', 'price': 150.0, 'volume': 100, 'status': 'filled'},
...     {'symbol': 'TSLA', 'price': 700.0, 'volume': 50, 'status': 'partial'}
>>> ]
>>> print(process_trade_outcomes(results))
['Trade AAPL: 100 units at $150.0 executed', 'Trade TSLA: 50 units at $700.0 partially executed']
```

```python
>>> print(process_trade_outcomes([]))
[]
```
