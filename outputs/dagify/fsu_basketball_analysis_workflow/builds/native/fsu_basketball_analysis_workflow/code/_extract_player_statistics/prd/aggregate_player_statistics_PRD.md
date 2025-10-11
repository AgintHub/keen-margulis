# aggregate_player_statistics PRD

## Description
Aggregates player statistics from a list of parsed game statistics into a comprehensive dictionary.


## Conceptual Info

This shim aggregates individual game statistics into a comprehensive summary for each player, facilitating further analysis.

## Docstring

### Summary
Aggregates player statistics from a list of game statistics.

### Parameters

- **parsed_stats** (str): A list of dictionaries where each dictionary contains game statistics for a player.

### Returns

str: A dictionary where keys are player names and values are dictionaries of aggregated statistics.

### Raises

- ValueError: If the input list is empty or if the dictionaries do not contain valid statistic data.
- TypeError: If the input is not a list or if the elements are not dictionaries.

### Examples

```python
>>> parsed_stats = [{'player': 'John', 'points': 10, 'rebounds': 5},
...              {'player': 'Jane', 'points': 15, 'rebounds': 3},
...              {'player': 'John', 'points': 12, 'rebounds': 4}]
>>> aggregate_player_statistics(parsed_stats=parsed_stats)
{'John': {'points': 22, 'rebounds': 9}, 'Jane': {'points': 15, 'rebounds': 3}}
```

```python
>>> parsed_stats = [{'player': 'Alice', 'assists': 7}, {'player': 'Bob', 'assists': 5}]
>>> aggregate_player_statistics(parsed_stats=parsed_stats)
{'Alice': {'assists': 7}, 'Bob': {'assists': 5}}
```
