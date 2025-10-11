# extract_rebounds PRD

## Description
Extracts rebounds for each player from aggregated statistics.


## Conceptual Info

This shim extracts rebounds for each player from the aggregated game statistics.

## Docstring

### Summary
Extract rebounds for each player from aggregated statistics.

### Parameters

- **aggregated_stats** (str): Aggregated player statistics containing rebounds information.
- **player_names** (str): List of player names corresponding to the statistics in aggregated_stats.

### Returns

List[int]: List of total rebounds for each player in the order of player_names.

### Raises

- ValueError: If the aggregated_stats string is malformed or missing required data.
- TypeError: If the input types are not as expected.

### Examples

```python
>>> aggregated_stats = '{\"Player1\": {\"rebounds\": 10}, \"Player2\": {\"rebounds\": 5}}'
>>> player_names = '[\"Player1\", \"Player2\"]'
>>> extract_rebounds(aggregated_stats=aggregated_stats, player_names=player_names)
[10, 5]
```

```python
>>> aggregated_stats = '{\"PlayerA\": {\"rebounds\": 7}, \"PlayerB\": {\"rebounds\": 3}}'
>>> player_names = '[\"PlayerA\", \"PlayerB\"]'
>>> extract_rebounds(aggregated_stats=aggregated_stats, player_names=player_names)
[7, 3]
```
