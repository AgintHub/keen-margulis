# process_team_performance_metrics PRD

## Description
Processes raw team performance data into a list of float metrics.


## Conceptual Info

This shim node processes raw team performance data into a list of float metrics, serving as an intermediary step in the data processing pipeline.

## Docstring

### Summary
Processes raw team performance data into a list of float metrics.

### Parameters

- **raw_data** (str): Raw team performance data in a string format that needs to be processed into float metrics.

### Returns

List[float]: A list of float values representing the processed team performance metrics.

### Raises

- ValueError: If the raw data cannot be parsed or processed correctly.
- TypeError: If the input raw data is not of type string.

### Examples

```python
>>> raw_team_data = '[{"metric1": 10.5}, {"metric2": 20.8}]'
>>> processed_metrics = process_team_performance_metrics(raw_data=raw_team_data)
>>> print(processed_metrics)
[10.5, 20.8]
```

```python
>>> raw_team_data = '[{"wins": 5}, {"losses": 3}]'
>>> processed_metrics = process_team_performance_metrics(raw_data=raw_team_data)
>>> print(processed_metrics)
[5.0, 3.0]
```
