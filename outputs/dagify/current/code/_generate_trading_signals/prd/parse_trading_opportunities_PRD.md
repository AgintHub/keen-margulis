# parse_trading_opportunities PRD

## Description
Parses a list of trading opportunities from string format to a structured dictionary representation.


## Conceptual Info

This shim function is crucial for transforming raw trading opportunity data into a format that can be further analyzed and processed by downstream components in the trading pipeline.

## Docstring

### Summary
Converts a list of trading opportunities in string format into a list of dictionaries, each representing a structured trading opportunity.

### Parameters

- **opportunities** (List[str]): A list of trading opportunities as strings that need to be parsed into a structured format.

### Returns

List[dict]: A list of dictionaries where each dictionary represents a parsed trading opportunity with relevant details.

### Raises

- ValueError: If the input list contains strings that cannot be parsed into valid trading opportunities.
- TypeError: If the input is not a list or if the elements of the list are not strings.

### Examples

```python
>>> parse_trading_opportunities(opportunities=['opportunity1', 'opportunity2'])
[{'details': 'parsed_opportunity1'}, {'details': 'parsed_opportunity2'}]
```

```python
>>> parse_trading_opportunities(opportunities=['invalid_opportunity'])
ValueError: Invalid opportunity format
```
