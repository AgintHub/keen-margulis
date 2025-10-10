# generate_strategy_adjustments PRD

## Description
Generates a list of strategy adjustments based on trade performance and execution status.


## Conceptual Info

This shim node is responsible for generating adjustments to a trading strategy based on the performance of previous trades and their execution status.

## Docstring

### Summary
Generates a list of strategy adjustments based on the provided performance metrics and execution status.

### Parameters

- **performance** (str): A string representation of performance metrics, potentially in JSON or another structured format.
- **execution_status** (str): A string indicating the status of trade execution, potentially containing success/failure information.

### Returns

List[str]: A list of strings representing the adjustments to be made to the trading strategy.

### Raises

- ValueError: If the input performance metrics or execution status are not in the expected format.
- TypeError: If the input types are not as expected (e.g., not strings).

### Examples

```python
>>> generate_strategy_adjustments(performance='{"win_rate": 0.8, "profit": 1000}', execution_status='success')
['Increase investment by 10%', 'Adjust stop-loss to 5%']
```

```python
>>> generate_strategy_adjustments(performance='{"win_rate": 0.4, "loss": 500}', execution_status='failure')
['Reduce investment by 20%', 'Review trading parameters']
```
