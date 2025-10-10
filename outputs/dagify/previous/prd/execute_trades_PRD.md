# execute_trades PRD

## Description
Execute trades based on the generated signals


## Conceptual Info

This node executes trades based on the generated trading signals, providing results and status of the trades.

## Docstring

### Summary
Execute trades according to the generated trading signals and return the results and status of the trades.

### Parameters

- **trading_signals** (List[str]): Generated trading signals (buy/sell/hold) from the parent node 'generate_trading_signals'.
- **signal_confidence** (List[float]): Confidence levels for the generated trading signals from the parent node 'generate_trading_signals'.

### Returns

Tuple[List[str], List[str]]: A tuple containing two lists: the first list contains the results of the executed trades, and the second list contains the status of the executed trades.

### Raises

- ValueError: If the lengths of 'trading_signals' and 'signal_confidence' do not match.
- RuntimeError: If there is an issue executing the trades.

### Examples

```python
>>> trading_signals = ['buy', 'sell', 'hold']
>>> signal_confidence = [0.8, 0.7, 0.9]
>>> trade_results, trade_status = execute_trades(trading_signals, signal_confidence)
(['trade executed', 'trade executed', 'no action'], ['success', 'success', 'held'])
```

```python
>>> trading_signals = ['buy', 'sell']
>>> signal_confidence = [0.85, 0.65]
>>> trade_results, trade_status = execute_trades(trading_signals, signal_confidence)
(['trade executed', 'trade executed'], ['success', 'success'])
```
