# make_trading_decisions PRD

## Description
Make trading decisions


## Conceptual Info

This node generates trading decisions based on the trading signals and their confidence levels produced by the 'generate_trading_signals' node.

## Docstring

### Summary
Makes trading decisions based on generated trading signals and their confidence levels.

### Parameters

- **trading_signals** (List[str]): Generated trading signals from the 'generate_trading_signals' node.
- **signal_confidence** (List[float]): Confidence levels of the generated trading signals from the 'generate_trading_signals' node.

### Returns

{'trading_decisions': List[str], 'decision_rationale': List[str]}: A dictionary containing the made trading decisions and the rationale behind them.

### Raises

- ValueError: If the lengths of 'trading_signals' and 'signal_confidence' do not match.

### Examples

```python
>>> trading_signals = ['Buy', 'Sell', 'Hold']
>>> signal_confidence = [0.8, 0.7, 0.9]
>>> result = make_trading_decisions(trading_signals, signal_confidence)
{'trading_decisions': ['Buy', 'Hold', 'Hold'], 'decision_rationale': ['High confidence buy signal', 'Low confidence sell signal', 'High confidence hold signal']}
```

```python
>>> trading_signals = ['Buy', 'Sell']
>>> signal_confidence = [0.6, 0.4]
>>> result = make_trading_decisions(trading_signals, signal_confidence)
{'trading_decisions': ['Buy', 'Sell'], 'decision_rationale': ['Moderate confidence buy signal', 'Low confidence sell signal']}
```
