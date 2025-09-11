# calculate_position_sizing PRD

## Description
Calculate the position sizing for each trading instrument based on the trading rules and strategy.


## Conceptual Info

This node calculates the position sizing for each trading instrument based on the trading rules and strategy.

## Docstring

### Summary
Calculates the position sizing for each trading instrument based on the trading rules and strategy.

### Parameters

- **trading_rules** (dict): Trading rules determined by the determine_trading_rules node, including entry_points, exit_points, stop_loss_levels, position_sizing_strategy, and trading_rules_summary.
- **trading_instruments** (List[str]): List of trading instruments identified for inclusion in the workflow.

### Returns

dict: A dictionary containing instrument_position_sizes, position_size_explanations, total_portfolio_value, and is_position_sizing_valid.

### Raises

- ValueError: If the trading rules or instruments are invalid.

### Examples

```python
>>> trading_rules = {
...     'entry_points': [10.0, 20.0],
...     'exit_points': [15.0, 25.0],
...     'stop_loss_levels': [9.0, 19.0],
...     'position_sizing_strategy': 'fixed',
...     'trading_rules_summary': 'Example trading rules'
>>> }
>>> trading_instruments = ['Instrument1', 'Instrument2']
>>> calculate_position_sizing(trading_rules, trading_instruments)
{'instrument_position_sizes': [100.0, 200.0], 'position_size_explanations': ['Fixed position size of 100.0', 'Fixed position size of 200.0'], 'total_portfolio_value': 300.0, 'is_position_sizing_valid': True}
```
