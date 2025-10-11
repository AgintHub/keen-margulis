# _identify_top_performers - Complete PRD Documentation

## Overview
PRDs for nodes in the '_identify_top_performers' module.

## Table of Contents

- [validate_input_lists](#validate_input_lists)

- [rank_players_by_metric](#rank_players_by_metric)



---

## validate_input_lists

### Description
Validates the input lists for player statistics to ensure they are of the same length and contain valid data.

### Conceptual Info

This shim function validates the input lists for player statistics, ensuring they are of the same length and contain valid data, playing a crucial role in maintaining data integrity before further processing.

### Docstring

**Summary:** Validates the input lists for player statistics.

**Parameters:**

- player_names (str): List of player names as a string representation of a list.
- points_scored (str): List of total points scored by each player as a string representation of a list.
- rebounds (str): List of total rebounds by each player as a string representation of a list.
- assists (str): List of total assists by each player as a string representation of a list.
**Returns:** str - Output indicating whether the input lists are valid.

**Raises:**

- ValueError: When the input lists are not of the same length or contain invalid data.
- TypeError: When the input types are incorrect.
**Examples:**

```python
>>> validate_input_lists(player_names='["Player1", "Player2"]', points_scored='[10, 20]', rebounds='[5, 6]', assists='[3, 4]')
'Input lists are valid.'
```

```python
>>> validate_input_lists(player_names='["Player1", "Player2"]', points_scored='[10]', rebounds='[5, 6]', assists='[3, 4]')
ValueError: 'Input lists must be of the same length.'
```



---

## rank_players_by_metric

### Description
Ranks players based on the provided metric values and returns a list of player names sorted in descending order of their metric values.

### Conceptual Info

This shim node is designed to rank players based on their performance metrics, such as points scored, rebounds, or assists, and return a list of player names sorted by their metric values.

### Docstring

**Summary:** Ranks players by their metric values and returns a sorted list of player names.

**Parameters:**

- player_names (str): A string representation of a list of player names.
- metric_values (str): A string representation of a list of metric values corresponding to the players.
**Returns:** List[str] - A list of player names sorted in descending order of their metric values.

**Raises:**

- ValueError: If the lengths of player_names and metric_values do not match.
- TypeError: If the input strings cannot be converted to lists or if the metric values are not numeric.
**Examples:**

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

