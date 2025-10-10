# generate_performance_summary PRD

## Description
Generates a performance summary string based on the provided success rate and average profit.


## Conceptual Info

This shim generates a human-readable summary of trade performance based on the success rate and average profit of trades.

## Docstring

### Summary
Generates a performance summary string based on the provided success rate and average profit.

### Parameters

- **success_rate** (str): The rate of successful trades as a string representation of a float.
- **average_profit** (str): The average profit of trades as a string representation of a float.

### Returns

str: A summary of the trade performance including the success rate and average profit.

### Raises

- ValueError: If the input success rate or average profit cannot be converted to a float.
- TypeError: If the input types are not strings.

### Examples

```python
>>> generate_performance_summary(success_rate='0.8', average_profit='100.5')
'Trade performance summary: 80.0% success rate, average profit: $100.50'
```

```python
>>> generate_performance_summary(success_rate='0.9', average_profit='200.75')
'Trade performance summary: 90.0% success rate, average profit: $200.75'
```
