# extract_player_statistics PRD

## Description
Extract player statistics from game data


## Conceptual Info

This node processes historical game data to extract individual player statistics, including points scored, rebounds, and assists.

## Docstring

### Summary
Extracts player statistics from historical game data, returning lists of player names and their respective statistics.

### Parameters

- **game_dates** (List[str]): List of game dates from the historical game data.
- **opponents** (List[str]): List of opponents from the historical game data.
- **scores** (List[str]): List of game scores from the historical game data.
- **game_statistics** (List[str]): List of game statistics from the historical game data.

### Returns

Tuple[List[str], List[int], List[int], List[int]]: A tuple containing lists of player names, points scored, rebounds, and assists.

### Raises

- ValueError: If the input lists are not of the same length.
- TypeError: If the input data types are not as expected.

### Examples

```python
>>> game_dates = ['2022-01-01', '2022-01-03']
>>> opponents = ['Team A', 'Team B']
>>> scores = ['80-70', '90-85']
>>> game_statistics = ['Player1:20,5,3;Player2:15,7,2', 'Player1:22,6,4;Player2:18,8,3']
>>> extract_player_statistics(game_dates, opponents, scores, game_statistics)
(['Player1', 'Player2'], [42, 33], [11, 15], [7, 5])
```

```python
>>> game_dates = ['2022-02-01']
>>> opponents = ['Team C']
>>> scores = ['100-90']
>>> game_statistics = ['Player1:25,4,5;Player2:20,6,4']
>>> extract_player_statistics(game_dates, opponents, scores, game_statistics)
(['Player1', 'Player2'], [25, 20], [4, 6], [5, 4])
```
