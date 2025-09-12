# extract_chart_positions PRD

## Description
Extracts an ordered list of integer chart positions from the provided chart_data string, preserving the original data order.


## Conceptual Info

Shim to convert raw chart metadata into a concrete sequence of numeric chart positions for downstream validation and analytics.

## Docstring

### Summary
Parse a chart_data string to produce an ordered List[int] of chart positions.

### Parameters

- **chart_data** (STR): Raw chart data string containing numeric tokens separated by delimiters

### Returns

LIST_INT: List of parsed integer chart positions in the same order as tokens found in chart_data

### Raises

- ValueError: Raised when a token cannot be parsed as an integer, or when input is not a string

### Examples

```python
>>> chart_data = '1, 4, 7, 9'
>>> positions = extract_chart_positions(chart_data=chart_data)
[1, 4, 7, 9]
```

```python
>>> chart_data = '2 5; 8'
>>> positions = extract_chart_positions(chart_data=chart_data)
[2, 5, 8]
```
