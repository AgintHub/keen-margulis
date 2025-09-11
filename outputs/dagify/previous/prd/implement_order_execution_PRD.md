# implement_order_execution PRD

## Description
This node implements the order execution logic for each trading instrument, including entry orders, stop-loss orders, and profit targets.


## Conceptual Info

This node is responsible for executing orders for each trading instrument, taking into account entry orders, stop-loss orders, and profit targets.

## Docstring

### Summary
Implement the order execution logic for each trading instrument.

### Parameters

- **instrument_position_sizes** (List[float]): List of position sizes for each trading instrument
- **entry_points** (List[float]): List of entry points for each trading instrument
- **stop_loss_levels** (List[float]): List of stop-loss levels for each trading instrument
- **profit_targets** (List[float]): List of profit targets for each trading instrument

### Returns

dict: A dictionary containing the order execution status, executed orders, entry order prices, stop-loss order prices, and profit target prices.

### Raises

- ValueError: If the input lists are not of the same length.
- RuntimeError: If an error occurs during order execution.

### Examples

```python
>>> instrument_position_sizes = [100.0, 200.0, 300.0]
>>> entry_points = [10.0, 20.0, 30.0]
>>> stop_loss_levels = [9.0, 19.0, 29.0]
>>> profit_targets = [11.0, 21.0, 31.0]
>>> implement_order_execution(instrument_position_sizes, entry_points, stop_loss_levels, profit_targets)
{'order_execution_status': True, 'executed_orders': ['order1', 'order2', 'order3'], 'entry_order_prices': [10.0, 20.0, 30.0], 'stop_loss_order_prices': [9.0, 19.0, 29.0], 'profit_target_prices': [11.0, 21.0, 31.0]}
```
