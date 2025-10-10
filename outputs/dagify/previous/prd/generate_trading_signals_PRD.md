# generate_trading_signals PRD

## Description
Generate trading signals based on the recommended strategies


## Conceptual Info

This node generates trading signals (buy/sell/hold) based on the recommended trading strategies evaluated by its parent node.

## Docstring

### Summary
Generate trading signals and their confidence levels based on recommended strategies.

### Parameters

- **strategy_evaluations** (List[str]): Evaluations of different trading strategies from the parent node 'evaluate_trading_strategies'.
- **recommended_strategies** (List[str]): Recommended trading strategies based on the evaluations from the parent node 'evaluate_trading_strategies'.

### Returns

Tuple[List[str], List[float]]: A tuple containing a list of generated trading signals and a list of their corresponding confidence levels.

### Raises

- ValueError: If the input lists 'strategy_evaluations' and 'recommended_strategies' are of different lengths.
- TypeError: If the input lists contain elements of incorrect types.

### Examples

```python
>>> strategy_evaluations = ['good', 'bad', 'neutral']
>>> recommended_strategies = ['buy', 'sell', 'hold']
>>> trading_signals, signal_confidence = generate_trading_signals(strategy_evaluations, recommended_strategies)
(['buy', 'sell', 'hold'], [0.8, 0.7, 0.9])
```

```python
>>> strategy_evaluations = ['excellent', 'poor']
>>> recommended_strategies = ['buy', 'sell']
>>> trading_signals, signal_confidence = generate_trading_signals(strategy_evaluations, recommended_strategies)
(['buy', 'sell'], [0.9, 0.6])
```
