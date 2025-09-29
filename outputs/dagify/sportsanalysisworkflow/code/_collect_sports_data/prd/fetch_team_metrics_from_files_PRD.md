# fetch_team_metrics_from_files PRD

## Description
Fetches team performance metrics from specified file sources and returns them as a list of dictionaries.


## Conceptual Info

This shim function is responsible for extracting team performance metrics from various file sources. It plays a crucial role in the data collection pipeline by providing the necessary team metrics data.

## Docstring

### Summary
Fetches team performance metrics from the specified file sources and returns the data as a list of dictionaries.

### Parameters

- **file_sources** (str): A string indicating the file sources from which to fetch team metrics.

### Returns

List[dict]: A list of dictionaries where each dictionary contains team performance metrics.

### Raises

- FileNotFoundError: Raised when the specified file sources do not exist.
- ValueError: Raised when the data fetched from the file sources is not in the expected format.

### Examples

```python
>>> fetch_team_metrics_from_files(file_sources='team_metrics.csv')
>>> # Assuming 'team_metrics.csv' contains: team_name,win_rate,score_average
>>> # teamA,0.7,20.5
>>> # teamB,0.4,15.2
[{'team_name': 'teamA', 'win_rate': 0.7, 'score_average': 20.5}, {'team_name': 'teamB', 'win_rate': 0.4, 'score_average': 15.2}]
```

```python
>>> fetch_team_metrics_from_files(file_sources='invalid_file.txt')
FileNotFoundError: The file 'invalid_file.txt' was not found.
```
