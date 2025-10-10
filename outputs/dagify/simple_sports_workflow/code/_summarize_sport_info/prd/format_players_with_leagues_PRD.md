# format_players_with_leagues PRD

## Description
Formats player names with their respective leagues into a list of strings.


## Conceptual Info

This shim takes two comma‑separated strings—player names and corresponding leagues—and produces a list of strings pairing each player with their league. It is used to transform raw API output into a user‑friendly format for summaries.

## Docstring

### Summary
Return a list of strings pairing each player name with its league.

### Parameters

- **player_names** (str): Comma‑separated list of player names. Leading/trailing whitespace around each name is ignored.
- **player_leagues** (str): Comma‑separated list of leagues corresponding to each player. Leading/trailing whitespace around each league is ignored.

### Returns

List[str]: A list where each element is formatted as ``"<Player> (<League>)"``. The order matches the input order.

### Raises

- ValueError: Raised if the number of player names does not equal the number of leagues.
- TypeError: Raised if either argument is not a string.

### Examples

```python
>>> format_players_with_leagues('LeBron James,Stephen Curry', 'NBA,NBA')
["LeBron James (NBA)", "Stephen Curry (NBA)"]
```

```python
>>> format_players_with_leagues('Lionel Messi', 'La Liga')
["Lionel Messi (La Liga)"]
```
