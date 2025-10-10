# map_players_to_leagues PRD

## Description
Map each player in a list to one of the available leagues, returning a list of dictionaries with player names and their corresponding league or None if not found.


## Conceptual Info

This shim transforms raw player data by aligning each player with one of the provided major leagues, ensuring downstream processes receive consistent league information.

## Docstring

### Summary
Return a list of player dictionaries with an added league field matched against available leagues.

### Parameters

- **players** (List[dict]): A list of dictionaries where each dictionary contains at least a 'name' key and a 'league' key indicating the player's league.
- **available_leagues** (List[str]): A list of valid league names that players may be matched to.

### Returns

List[dict]: A list where each element is a dictionary with keys `name` and `league`. The `league` value is the matched league name or `None` if the player's league is not in `available_leagues`.

### Raises

- ValueError: Raised when `players` or `available_leagues` are empty.
- TypeError: Raised when the input types are not `List[dict]` and `List[str]` respectively.

### Examples

```python
>>> players = [{'name': 'LeBron James', 'league': 'NBA'},
...            {'name': 'Alex Rodriguez', 'league': 'MLB'}]
>>> leagues = ['NBA', 'NHL']
>>> map_players_to_leagues(players, leagues)
[{'name': 'LeBron James', 'league': 'NBA'}, {'name': 'Alex Rodriguez', 'league': None}]
```

```python
>>> players = [{'name': 'Connor McDavid', 'league': 'NHL'},
...            {'name': 'Serena Williams', 'league': 'Tennis'}]
>>> leagues = ['NHL', 'NBA']
>>> map_players_to_leagues(players, leagues)
[{'name': 'Connor McDavid', 'league': 'NHL'}, {'name': 'Serena Williams', 'league': None}]
```
