# extract_points_scored PRD

## Description
Extracts the total points scored by each player from aggregated game statistics.


## Conceptual Info

This shim extracts points scored by players from aggregated statistics, playing a crucial role in generating player performance summaries.

## Docstring

### Summary
Extracts the total points scored by each player from the provided aggregated statistics.

### Parameters

- **aggregated_stats** (str): A string representation of aggregated game statistics, containing player performance data.
- **player_names** (str): A string representation of the list of player names corresponding to the statistics in aggregated_stats.

### Returns

List[int]: A list of integers representing the total points scored by each player in the order corresponding to player_names.

### Raises

- ValueError: If the aggregated_stats string is not properly formatted or if it doesn't contain valid player statistics.
- TypeError: If aggregated_stats or player_names are not strings, or if the parsed statistics do not contain expected data types.

### Examples

```python
>>> aggregated_stats = '{\"Player1\": {\"points\": 10}, \"Player2\": {\"points\": 20}}'
>>> player_names = '[\"Player1\", \"Player2\"]'
>>> extract_points_scored(aggregated_stats=aggregated_stats, player_names=player_names)
[10, 20]
```

```python
>>> aggregated_stats = '{\"John\": {\"points\": 15}, \"Doe\": {\"points\": 25}}'
>>> player_names = '[\"John\", \"Doe\"]'
>>> extract_points_scored(aggregated_stats=aggregated_stats, player_names=player_names)
[15, 25]
```
