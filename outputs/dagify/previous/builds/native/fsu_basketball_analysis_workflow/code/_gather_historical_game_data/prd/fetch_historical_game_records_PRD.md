# fetch_historical_game_records PRD

## Description
Fetches historical game records for a specified team from given data sources.


## Conceptual Info

This shim node is responsible for retrieving historical game data for a specified team from various data sources. It plays a crucial role in the data gathering pipeline for sports analytics.

## Docstring

### Summary
Fetches historical game records for a given team from specified data sources.

### Parameters

- **sources** (str): Comma-separated list of data sources to fetch historical game records from.
- **team** (str): Name of the team for which to fetch historical game records.

### Returns

List[dict]: List of dictionaries where each dictionary represents a historical game record.

### Raises

- ValueError: If the input sources or team name is invalid or empty.
- TypeError: If the input types for sources or team are not strings.

### Examples

```python
>>> fetch_historical_game_records(sources='source1,source2', team='FSU')
[{'date': '2022-01-01', 'opponent': 'TeamA', 'score': '80-70'}, {'date': '2022-01-03', 'opponent': 'TeamB', 'score': '90-85'}]
```

```python
>>> fetch_historical_game_records(sources='sports_db', team='UF')
[{'date': '2022-02-01', 'opponent': 'TeamC', 'score': '70-60'}]
```
