# execute_trades PRD

## Description
Execute trades based on the selected optimal strategy.


## Conceptual Info

This node executes trades based on the optimal strategy selected by its parent node, 'select_optimal_strategy'. It takes the optimal strategy and its confidence level as inputs and produces the outcomes and volumes of the executed trades.

## Docstring

### Summary
Execute trades based on the selected optimal strategy, producing trade outcomes and volumes.

### Parameters

- **optimal_strategy** (str): The selected optimal trading strategy from the 'select_optimal_strategy' node.
- **strategy_confidence** (float): The confidence level in the selected optimal strategy from the 'select_optimal_strategy' node.

### Returns

Tuple[List[str], List[int]]: A tuple containing two lists: the first list contains the outcomes of the executed trades as strings, and the second list contains the volumes of the executed trades as integers.

### Raises

- ValueError: If the optimal strategy is not recognized or if the strategy confidence is outside the valid range (0 to 1).
- RuntimeError: If there's an issue executing the trades based on the provided strategy.

### Examples

```python
>>> optimal_strategy = 'buy'
>>> strategy_confidence = 0.8
>>> trade_outcomes, trade_volumes = execute_trades(optimal_strategy, strategy_confidence)
(['success', 'success'], [100, 200])
```

```python
>>> optimal_strategy = 'sell'
>>> strategy_confidence = 0.7
>>> trade_outcomes, trade_volumes = execute_trades(optimal_strategy, strategy_confidence)
(['success', 'failed'], [50, 0])
```
