# calculate_average_profit PRD

## Description
Calculates the average profit from a list of trade profits.


## Conceptual Info

This shim node is responsible for calculating the average profit from a list of trade profits, serving as a crucial component in monitoring trade performance.

## Docstring

### Summary
Calculates the average profit from a list of trade profits.

### Parameters

- **profits** (List[float]): A list of trade profits.

### Returns

float: The average profit calculated from the input profits. Returns 0 if the input list is empty.

### Raises

- TypeError: If the input is not a list or if the list contains non-numeric values.
- ValueError: If the input list contains NaN or infinity values.

### Examples

```python
>>> profits = [100.0, 200.0, 300.0]
>>> average_profit = calculate_average_profit(profits)
>>> print(average_profit)
200.0
```

```python
>>> profits = []
>>> average_profit = calculate_average_profit(profits)
>>> print(average_profit)
0
```
