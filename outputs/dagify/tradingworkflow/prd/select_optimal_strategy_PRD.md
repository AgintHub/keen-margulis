# select_optimal_strategy PRD

## Description
Select the optimal trading strategy based on evaluations and risk assessments.


## Conceptual Info

This node selects the optimal trading strategy based on the evaluations and risk assessments provided by its parent node, 'evaluate_trading_strategies'.

## Docstring

### Summary
Selects the optimal trading strategy based on evaluations and risk assessments.

### Parameters

- **strategy_evaluations** (List[str]): Evaluations of different trading strategies from the 'evaluate_trading_strategies' node.
- **strategy_risks** (List[float]): Risk assessments for each trading strategy from the 'evaluate_trading_strategies' node.

### Returns

Tuple[str, float]: A tuple containing the optimal trading strategy and its confidence level.

### Raises

- ValueError: If the lengths of 'strategy_evaluations' and 'strategy_risks' do not match.

### Examples

```python
>>> strategy_evaluations = ['Good', 'Average', 'Poor']
>>> strategy_risks = [0.1, 0.5, 0.8]
>>> optimal_strategy, strategy_confidence = select_optimal_strategy(strategy_evaluations, strategy_risks)
('Good', 0.9)
```

```python
>>> strategy_evaluations = ['Average', 'Good', 'Poor']
>>> strategy_risks = [0.5, 0.1, 0.8]
>>> optimal_strategy, strategy_confidence = select_optimal_strategy(strategy_evaluations, strategy_risks)
('Good', 0.9)
```
