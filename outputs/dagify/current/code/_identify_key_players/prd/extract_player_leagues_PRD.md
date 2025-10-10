# extract_player_leagues PRD

## Description
Extracts the league names from a list of player dictionaries.


## Conceptual Info

This shim isolates the logic that pulls league information from player records, enabling downstream nodes to operate on a clean list of leagues without caring about the underlying player data structure.

## Docstring

### Summary
Return a list of league names extracted from each player dictionary in the provided list.

### Parameters

- **player_data** (List[dict]): A list of dictionaries where each dictionary represents a player and must contain a key named 'league' with a string value.

### Returns

List[str]: A list of strings, each representing the league name associated with a player.

### Raises

- ValueError: Raised if `player_data` is not a list, is empty, or any dictionary lacks a 'league' key.
- TypeError: Raised if `player_data` is not of type list or if any element is not a dictionary.

### Examples

```python
>>> players = [
...     {'name': 'LeBron James', 'league': 'NBA'},
...     {'name': 'Lionel Messi', 'league': 'MLS'}
>>> ]
>>> extract_player_leagues(players)
['NBA', 'MLS']
```

```python
>>> invalid_players = [{'name': 'Unknown'}]
>>> extract_player_leagues(invalid_players)
ValueError: Each player dictionary must contain a 'league' key.
```
