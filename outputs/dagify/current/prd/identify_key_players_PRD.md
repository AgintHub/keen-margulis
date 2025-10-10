# identify_key_players PRD

## Description
Identify key players in the sport


## Conceptual Info

This node selects a short list of currently active, top‑tier players for a given sport and maps each player to one of the sport's major professional leagues.

## Docstring

### Summary
Retrieve 3–5 prominent active players for a specified sport along with the league each player belongs to.

### Parameters

- **selected_sport** (str): The sport for which key players should be identified (e.g., 'soccer', 'basketball').
- **league_names** (List[str]): A list of major professional leagues associated with the sport, obtained from the `list_major_leagues` node.

### Returns

Tuple[List[str], List[str]]: A tuple containing two lists: the first list holds the names of 3‑5 key players, and the second list holds the corresponding league names for each player.

### Raises

- ValueError: Raised if the function cannot find at least three suitable players or if the input lists are empty.

### Examples

```python
>>> player_names, player_leagues = identify_key_players(
...     'soccer',
...     ['Premier League', 'La Liga', 'Serie A']
>>> )
(['Lionel Messi', 'Cristiano Ronaldo', 'Neymar Jr.'], ['Premier League', 'La Liga', 'Serie A'])
```

```python
>>> names, leagues = identify_key_players(
...     'basketball',
...     ['NBA', 'EuroLeague']
>>> )
(['LeBron James', 'Kevin Durant', 'Stephen Curry'], ['NBA', 'NBA', 'NBA'])
```
