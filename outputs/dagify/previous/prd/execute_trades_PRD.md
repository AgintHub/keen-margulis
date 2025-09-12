# execute_trades PRD

## Description
Execute trades


## Conceptual Info

This node executes trades based on the trading decisions made by its parent node, 'make_trading_decisions'.

## Docstring

### Summary
Executes trades based on the provided trading decisions and returns the status and outcomes of these trades.

### Parameters

- **trading_decisions** (List[str]): Made trading decisions, output from 'make_trading_decisions' node.
- **decision_rationale** (List[str]): Rationale behind the trading decisions, output from 'make_trading_decisions' node.

### Returns

{'trade_execution_status': List[str], 'trade_outcomes': List[str]}: A dictionary containing two lists: 'trade_execution_status' for the status of trade executions and 'trade_outcomes' for the outcomes of the executed trades.

### Raises

- ValueError: If the input lists ('trading_decisions' and 'decision_rationale') are not of the same length.
- RuntimeError: If there is an issue during the execution of trades.

### Examples

```python
>>> trading_decisions = ['buy', 'sell', 'hold']
>>> decision_rationale = ['good opportunity', 'bad market', 'wait for more info']
>>> result = execute_trades(trading_decisions, decision_rationale)
{'trade_execution_status': ['success', 'success', 'pending'], 'trade_outcomes': ['profit', 'loss', 'awaiting']}
```

```python
>>> trading_decisions = ['buy']
>>> decision_rationale = ['confident in market']
>>> result = execute_trades(trading_decisions, decision_rationale)
{'trade_execution_status': ['success'], 'trade_outcomes': ['profit']}
```
