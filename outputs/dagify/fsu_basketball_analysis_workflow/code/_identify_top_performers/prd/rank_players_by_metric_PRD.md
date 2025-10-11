# rank_players_by_metric PRD

## Description
Ranks players based on the provided metric values and returns a list of player names sorted in descending order of their metric values.


## Conceptual Info

This shim node is designed to rank players based on their performance metrics, such as points scored, rebounds, or assists, and return a list of player names sorted by their metric values.

## Docstring

### Summary
Ranks players by their metric values and returns a sorted list of player names.

### Parameters

- **player_names** (str): A string representation of a list of player names.
- **metric_values** (str): A string representation of a list of metric values corresponding to the players.

### Returns

List[str]: A list of player names sorted in descending order of their metric values.

### Raises

- ValueError: If the lengths of player_names and metric_values do not match.
- TypeError: If the input strings cannot be converted to lists or if the metric values are not numeric.

### Examples

```python
>>> player_names = "['Player1', 'Player2', 'Player3']"
>>> metric_values = "[10, 20, 15]"
>>> rank_players_by_metric(player_names, metric_values)
['Player2', 'Player3', 'Player1']
```

```python
>>> player_names = "['Alice', 'Bob', 'Charlie']"
>>> metric_values = "[5, 8, 3]"
>>> rank_players_by_metric(player_names, metric_values)
['Bob', 'Alice', 'Charlie']
```
