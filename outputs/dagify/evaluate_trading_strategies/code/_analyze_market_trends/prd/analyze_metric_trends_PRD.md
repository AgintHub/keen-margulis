# analyze_metric_trends PRD

## Description
Generates a list of trend descriptors for a given metric data string.


## Conceptual Info

The shim analyzes a series of metric values and translates them into human‑readable trend descriptors, forming a bridge between raw metric data and higher‑level trend analysis.

## Docstring

### Summary
Returns trend descriptors based on processed metric data.

### Parameters

- **metrics_data** (str): A string containing comma‑separated metric values to analyze.

### Returns

list: List of trend strings derived from the metric data.

### Raises

- ValueError: Raised when the metrics_data string is empty or contains non‑numeric entries.
- TypeError: Raised when metrics_data is not a string.

### Examples

```python
>>> trend = analyze_metric_trends('10.5,12.3,11.8,13.2')
['upward', 'stable']
```

```python
>>> analyze_metric_trends('')
ValueError: Metrics data string must not be empty
```
