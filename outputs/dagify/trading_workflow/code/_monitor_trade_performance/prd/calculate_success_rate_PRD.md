# calculate_success_rate PRD

## Description
Calculates the success rate of trades based on their status.


## Conceptual Info

This node calculates the success rate of trades by analyzing their status, playing a crucial role in monitoring trade performance.

## Docstring

### Summary
Calculates the success rate of trades based on their status.

### Parameters

- **trade_status** (List[str]): A list of strings representing the status of each trade (e.g., 'success', 'failure').

### Returns

float: The success rate of the trades as a float value between 0 and 1.

### Raises

- ValueError: If the input list is empty or contains invalid status values.
- TypeError: If the input is not a list or if the list contains non-string values.

### Examples

```python
>>> trade_status = ['success', 'failure', 'success']
>>> success_rate = calculate_success_rate(trade_status=trade_status)
0.6666666666666666
```

```python
>>> trade_status = ['success', 'success', 'success']
>>> success_rate = calculate_success_rate(trade_status=trade_status)
1.0
```
