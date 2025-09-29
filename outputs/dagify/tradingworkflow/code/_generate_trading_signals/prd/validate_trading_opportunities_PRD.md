# validate_trading_opportunities PRD

## Description
Validates a list of trading opportunities to ensure they are properly formatted and meet required criteria.


## Conceptual Info

This shim node is responsible for validating a list of trading opportunities. It ensures that the opportunities are properly formatted and meet specific criteria before they are used in further processing.

## Docstring

### Summary
Validates a list of trading opportunities to ensure they are properly formatted and meet required criteria.

### Parameters

- **opportunities** (str): A string representing a list of trading opportunities, likely in a serialized format such as JSON.

### Returns

List[str]: A list of validated trading opportunities. Each opportunity is represented as a string.

### Raises

- ValueError: When the input string is not a valid representation of a list of trading opportunities.
- TypeError: When the input is not a string.

### Examples

```python
>>> import json
>>> opportunities = json.dumps(['opportunity1', 'opportunity2'])
>>> result = validate_trading_opportunities(opportunities=opportunities)
['opportunity1', 'opportunity2']
```

```python
>>> try:
...     validate_trading_opportunities(opportunities=123)
>>> except TypeError as e:
...     print(e)
Input opportunities must be a string.
```
