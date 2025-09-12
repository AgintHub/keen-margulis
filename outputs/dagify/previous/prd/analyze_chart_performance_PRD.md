# analyze_chart_performance PRD

## Description
Analyze the chart performance of Taylor Swift's songs.


## Conceptual Info

This node analyzes the chart performance data of Taylor Swift's songs to identify trends and patterns.

## Docstring

### Summary
Analyze chart performance data to identify trends and peak positions.

### Parameters

- **chart_performance_data** (List[int]): List of chart performance metrics for Taylor Swift's songs, obtained from the 'gather_taylor_swift_data' node.

### Returns

{'chart_trends': List[str], 'peak_positions': List[int]}: A dictionary containing a list of trends observed in chart performance and a list of peak chart positions for each song.

### Raises

- ValueError: If the input chart performance data is empty or malformed.

### Examples

```python
>>> chart_performance_data = [10, 5, 1, 8, 3]
>>> result = analyze_chart_performance(chart_performance_data)
>>> print(result)
{'chart_trends': ['Increasing trend', 'Decreasing trend'], 'peak_positions': [1, 3, 5, 8, 10]}
```

```python
>>> chart_performance_data = [20, 15, 10, 5]
>>> result = analyze_chart_performance(chart_performance_data)
>>> print(result)
{'chart_trends': ['Decreasing trend'], 'peak_positions': [5, 10, 15, 20]}
```
