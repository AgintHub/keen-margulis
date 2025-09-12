# extract_peak_positions PRD

## Description
Extracts the highest chart positions from a list of chart performance metrics.


## Conceptual Info

This shim identifies the best chart performance for each song by scanning the performance history.

## Docstring

### Summary
Extracts peak chart positions from a list of chart performance metrics.

### Parameters

- **chart_positions** (List[int]): A list of integer chart positions recorded over time.

### Returns

List[int]: A list containing the maximum (best) chart position for each song.

### Raises

- ValueError: Raised when the input list is empty or contains non-integer values.

### Examples

```python
>>> extract_peak_positions([10, 5, 2, 3, 4])
>>> # returns [10, 5, 4, 4, 4]
[10, 5, 4, 4, 4]
```
