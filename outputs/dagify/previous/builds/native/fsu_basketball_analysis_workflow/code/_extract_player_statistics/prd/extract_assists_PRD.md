# extract_assists PRD

## Description
Extracts the total assists for each player from the aggregated game statistics.


## Conceptual Info

This shim function is designed to extract the total assists for each player from the aggregated game statistics. It plays a crucial role in the larger system by providing a specific statistical output required for further analysis or processing.

## Docstring

### Summary
Extracts total assists for each player from aggregated game statistics.

### Parameters

- **aggregated_stats** (str): Aggregated game statistics containing player performance data.
- **player_names** (str): List of player names corresponding to the statistics.

### Returns

List[int]: A list of integers representing the total assists for each player in the order of player_names.

### Raises

- ValueError: If the aggregated_stats string is malformed or cannot be parsed.
- TypeError: If the input types are incorrect, such as aggregated_stats or player_names not being strings.

### Examples

```python
>>> aggregated_stats = "{'Player1': {'assists': 10}, 'Player2': {'assists': 5}}"
>>> player_names = "['Player1', 'Player2']"
>>> extract_assists(aggregated_stats, player_names)
[10, 5]
```

```python
>>> aggregated_stats = "{'PlayerA': {'assists': 8}, 'PlayerB': {'assists': 12}}"
>>> player_names = "['PlayerA', 'PlayerB']"
>>> extract_assists(aggregated_stats, player_names)
[8, 12]
```
