# gather_historical_game_data PRD

## Description
Collect historical game data for FSU basketball team


## Conceptual Info

This node is responsible for collecting historical game data for the FSU basketball team, including game dates, opponents, scores, and game statistics.

## Docstring

### Summary
Gathers historical game data for the FSU basketball team.

### Returns

Tuple[List[str], List[str], List[str], List[str]]: A tuple containing lists of game dates, opponents, scores, and game statistics.

### Raises

- DataCollectionError: If there's an issue collecting the historical game data.

### Examples

```python
>>> game_data = gather_historical_game_data()
>>> print(game_data)
(['2023-01-01', '2023-01-03'], ['Team A', 'Team B'], ['74-68', '80-75'], ['Rebounds: 40, Turnovers: 15', 'Rebounds: 35, Turnovers: 10'])
```
