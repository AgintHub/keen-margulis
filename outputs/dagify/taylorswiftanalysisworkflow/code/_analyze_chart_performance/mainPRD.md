# _analyze_chart_performance - Complete PRD Documentation

## Overview
PRDs for nodes in the '_analyze_chart_performance' module.

## Table of Contents

- [validate_chart_data](#validate_chart_data)

- [analyze_performance_trends](#analyze_performance_trends)

- [extract_peak_positions](#extract_peak_positions)



---

## validate_chart_data

### Description
Validates a string input by parsing it into a clean List[int] of chart positions suitable for downstream chart analysis.

### Conceptual Info

Data validation shim to sanitize and convert string input into numeric chart positions

### Docstring

**Summary:** Validate and coerce a string representation of chart data into a List[int] for downstream chart analysis

**Parameters:**

- data (str): String encoding of chart positions to validate and parse into integers
**Returns:** List[int] - Validated list of chart positions parsed from the input string

**Raises:**

- TypeError: If input data is not a string
- ValueError: If the string cannot be parsed into integers or contains invalid values
**Examples:**

```python
>>> result = validate_chart_data(data='1, 2, 3, 5')
>>> print(result)
[1, 2, 3, 5]
```

```python
>>> result = validate_chart_data(data='[7 4 10]')
>>> print(result)
[7, 4, 10]
```



---

## analyze_performance_trends

### Description
This shim analyzes a list of chart positions and outputs descriptive trend strings.

### Conceptual Info

Provides trend extraction functionality for the AnalyzeChartPerformance node.

### Docstring

**Summary:** Analyzes chart positions to generate descriptive trend insights.

**Parameters:**

- chart_positions (LIST_INT): A list of integer chart positions representing song performance over time.
**Returns:** LIST_STR - A list of strings, each describing an observed trend in the chart data.

**Raises:**

- ValueError: Raised if the input list is empty or contains non-integer values.
**Examples:**

```python
>>> trends = analyze_performance_trends(chart_positions=[5, 3, 7, 2])
>>> print(trends)
['Improving trend', 'Declining trend']
```



---

## extract_peak_positions

### Description
Extracts the highest chart positions from a list of chart performance metrics.

### Conceptual Info

This shim identifies the best chart performance for each song by scanning the performance history.

### Docstring

**Summary:** Extracts peak chart positions from a list of chart performance metrics.

**Parameters:**

- chart_positions (List[int]): A list of integer chart positions recorded over time.
**Returns:** List[int] - A list containing the maximum (best) chart position for each song.

**Raises:**

- ValueError: Raised when the input list is empty or contains non-integer values.
**Examples:**

```python
>>> extract_peak_positions([10, 5, 2, 3, 4])
>>> # returns [10, 5, 4, 4, 4]
[10, 5, 4, 4, 4]
```

