# select_best_players PRD

## Description
Selects the best players from a list of players with league information, constrained by minimum and maximum count.


## Conceptual Info

This shim encapsulates the core logic for filtering and selecting players based on quantity constraints. It is used after players have been mapped to leagues and serves as the final decision point before returning the key player list to higher-level modules.

## Docstring

### Summary
Selects the best players from a list of player dictionaries, constrained by specified minimum and maximum counts.

### Parameters

- **players_with_leagues** (List[dict]): A list of dictionaries, each containing at least a 'player_name' and 'league' key, representing all candidate players.
- **min_count** (int): The minimum number of players that must be returned.
- **max_count** (int): The maximum number of players that may be returned.

### Returns

List[dict]: A list of dictionaries representing the selected players. Each dictionary includes at least the keys 'player_name' and 'league'.

### Raises

- ValueError: Raised if `min_count` is greater than `max_count`, if no players are available, or if the selection constraints cannot be satisfied.
- TypeError: Raised if input arguments are not of the expected types.

### Examples

```python
>>> players = [
...     {'player_name': 'Alice', 'league': 'NBA'},
...     {'player_name': 'Bob', 'league': 'NBA'},
...     {'player_name': 'Charlie', 'league': 'NCAA'}
>>> ]
>>> result = select_best_players(players_with_leagues=players, min_count=1, max_count=3)
>>> print(result)
[{'player_name': 'Alice', 'league': 'NBA'}, {'player_name': 'Bob', 'league': 'NBA'}, {'player_name': 'Charlie', 'league': 'NCAA'}]
```

```python
>>> players = [
...     {'player_name': 'Alice', 'league': 'NBA'},
...     {'player_name': 'Bob', 'league': 'NBA'}
>>> ]
>>> try:
...     select_best_players(players_with_leagues=players, min_count=3, max_count=2)
>>> except ValueError as e:
...     print(e)
ValueError: min_count cannot be greater than max_count
```
