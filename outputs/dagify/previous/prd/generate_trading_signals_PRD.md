# generate_trading_signals PRD

## Description
Generate trading signals


## Conceptual Info

This node generates trading signals based on the recommended trading strategies evaluated by its parent node.

## Docstring

### Summary
Generates trading signals and their confidence levels based on recommended trading strategies.

### Parameters

- **recommended_strategies** (List[str]): Recommended trading strategies from the parent node 'evaluate_trading_strategies'.
- **strategy_evaluations** (List[str]): Evaluations of different trading strategies from the parent node 'evaluate_trading_strategies'.

### Returns

Tuple[List[str], List[float]]: A tuple containing the generated trading signals and their corresponding confidence levels.

### Raises

- ValueError: If the input recommended strategies or strategy evaluations are empty or malformed.

### Examples

```python
>>> recommended_strategies = ['mean_reversion', 'trend_following']
>>> strategy_evaluations = ['mean_reversion:0.8', 'trend_following:0.7']
>>> trading_signals, signal_confidence = generate_trading_signals(recommended_strategies, strategy_evaluations)
(['buy', 'sell'], [0.85, 0.75])
```

```python
>>> recommended_strategies = ['momentum']
>>> strategy_evaluations = ['momentum:0.9']
>>> trading_signals, signal_confidence = generate_trading_signals(recommended_strategies, strategy_evaluations)
(['buy'], [0.92])
```
