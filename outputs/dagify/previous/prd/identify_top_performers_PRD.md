# identify_top_performers PRD

## Description
Identify top performing players based on statistics


## Conceptual Info

This node identifies top performing players based on their statistics such as points scored, rebounds, and assists. It takes the output from the 'extract_player_statistics' node and processes it to determine the top performers in each category.

## Docstring

### Summary
Identify top performing players based on points scored, rebounds, assists, and other relevant metrics.

### Parameters

- **player_names** (List[str]): List of player names extracted from game data.
- **points_scored** (List[int]): List of total points scored by each player.
- **rebounds** (List[int]): List of total rebounds by each player.
- **assists** (List[int]): List of total assists by each player.

### Returns

Tuple[List[str], List[str], List[str]]: A tuple containing lists of top scorers, top rebounders, and top assisters.

### Raises

- ValueError: If the input lists are of different lengths.
- TypeError: If the input types are not as expected.

### Examples

```python
>>> player_names = ['Player1', 'Player2', 'Player3']
>>> points_scored = [20, 15, 25]
>>> rebounds = [5, 10, 7]
>>> assists = [8, 6, 9]
>>> top_scorers, top_rebounders, top_assisters = identify_top_performers(player_names, points_scored, rebounds, assists)
(['Player3', 'Player1', 'Player2'], ['Player2', 'Player3', 'Player1'], ['Player3', 'Player1', 'Player2'])
```

```python
>>> player_names = ['PlayerA', 'PlayerB']
>>> points_scored = [30, 20]
>>> rebounds = [8, 12]
>>> assists = [7, 5]
>>> top_scorers, top_rebounders, top_assisters = identify_top_performers(player_names, points_scored, rebounds, assists)
(['PlayerA', 'PlayerB'], ['PlayerB', 'PlayerA'], ['PlayerA', 'PlayerB'])
```
