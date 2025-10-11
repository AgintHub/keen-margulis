# analyze_business_operations PRD

## Description
Analyze business operations data


## Conceptual Info

This node analyzes business operations data gathered from various sources to identify strengths, weaknesses, and efficiency metrics.

## Docstring

### Summary
Analyzes business operations data to identify areas of strength and weakness.

### Parameters

- **business_operations_data** (str): Data related to business operations gathered from the 'gather_wcfb_data' node.

### Returns

Tuple[List[str], List[str], List[float]]: A tuple containing a list of business operation strengths, a list of business operation weaknesses, and a list of efficiency metrics for business operations.

### Raises

- ValueError: If the input 'business_operations_data' is empty or not in the expected format.

### Examples

```python
>>> business_operations_data = '{"sales": 1000, "expenses": 500, "productivity": 0.8}'
>>> strengths, weaknesses, efficiency_metrics = analyze_business_operations(business_operations_data)
>>> print(strengths, weaknesses, efficiency_metrics)
['High sales'] ['High expenses'] [0.8]
```

```python
>>> business_operations_data = '{"sales": 800, "expenses": 600, "productivity": 0.7}'
>>> strengths, weaknesses, efficiency_metrics = analyze_business_operations(business_operations_data)
>>> print(strengths, weaknesses, efficiency_metrics)
['Moderate sales'] ['High expenses'] [0.7]
```
