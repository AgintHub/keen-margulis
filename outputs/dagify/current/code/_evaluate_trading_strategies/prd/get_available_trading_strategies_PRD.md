# get_available_trading_strategies PRD

## Description
Returns a list of available trading strategies for evaluation.


## Conceptual Info

This shim function provides a list of available trading strategies that can be used for further evaluation in the trading system.

## Docstring

### Summary
Retrieve a list of available trading strategies.

### Returns

List[str]: A list of available trading strategies as strings.

### Raises

- RuntimeError: If the list of available trading strategies cannot be retrieved.

### Examples

```python
>>> available_strategies = get_available_trading_strategies()
['Strategy1', 'Strategy2', 'Strategy3']
```
