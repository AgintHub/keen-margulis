# determine_trading_rules PRD

## Description
Determine the trading rules that will be used in the trading workflow, including entry and exit points, stop-loss levels, and position sizing.


## Conceptual Info

This node determines the trading rules for a trading workflow based on a selected trading strategy.

## Docstring

### Summary
Determine trading rules including entry and exit points, stop-loss levels, and position sizing based on a selected trading strategy.

### Parameters

- **selected_strategy** (dict): A dictionary containing the selected trading strategy details, including 'selected_strategy_name', 'strategy_principles', and 'strategy_metrics'.

### Returns

dict: A dictionary containing the determined trading rules, including 'entry_points', 'exit_points', 'stop_loss_levels', 'position_sizing_strategy', and 'trading_rules_summary'.

### Raises

- ValueError: If the selected trading strategy is invalid or does not contain required details.

### Examples

```python
>>> determine_trading_rules({'selected_strategy_name': 'Moving Average Crossover', 'strategy_principles': ['MA_50', 'MA_200'], 'strategy_metrics': [' Sharpe Ratio']})
{'entry_points': [1.0, 2.0], 'exit_points': [3.0, 4.0], 'stop_loss_levels': [0.9, 1.9], 'position_sizing_strategy': 'Fixed Fractional', 'trading_rules_summary': 'Based on Moving Average Crossover strategy'}
```
