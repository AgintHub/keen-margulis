# _identify_key_players - Complete PRD Documentation

## Overview
PRDs for nodes in the '_identify_key_players' module.

## Table of Contents

- [validate_inputs](#validate_inputs)

- [fetch_top_players_for_sport](#fetch_top_players_for_sport)

- [filter_active_players](#filter_active_players)

- [map_players_to_leagues](#map_players_to_leagues)

- [select_best_players](#select_best_players)

- [extract_player_names](#extract_player_names)

- [extract_player_leagues](#extract_player_leagues)



---

## validate_inputs

### Description
Validates that the sport is a non‑empty string and leagues is a non‑empty list of strings, returning a boolean result

### Conceptual Info

The validate_inputs shim is a guard that ensures downstream processing only occurs when the sport name and list of leagues are properly specified, preventing errors in later data‑fetching stages.

### Docstring

**Summary:** Return a boolean indicating whether the provided sport and leagues are valid.

**Parameters:**

- sport (str): The name of the sport; must be a non‑empty string.
- leagues (LIST_STR): A list of league names; must contain at least one non‑empty string.
**Returns:** bool - True if both `sport` and `leagues` are valid, otherwise False.

**Raises:**

- ValueError: Raised when `sport` is an empty string or `leagues` is empty or contains non‑string elements.
- TypeError: Raised when `sport` is not a string or `leagues` is not a list.
**Examples:**

```python
>>> validate_inputs('soccer', ['Premier League', 'La Liga'])
True
```

```python
>>> validate_inputs('', ['Premier League'])
False
```



---

## fetch_top_players_for_sport

### Description
Retrieves the top N players for a specified sport from an external source and returns a list of player profile dictionaries represented as JSON strings.

### Conceptual Info

The shim encapsulates the logic required to obtain the top-ranked players for a given sport, abstracting the external API calls and data formatting so downstream components can work with a clean, consistent data structure.

### Docstring

**Summary:** Fetch the top `target_count` players for the specified sport, returning a list of player profile dictionaries encoded as JSON strings.

**Parameters:**

- sport (str): The name of the sport for which to retrieve top players.
- target_count (int or str): The number of top players to fetch.
**Returns:** LIST_STR - A list of JSON strings, each representing a player profile dictionary with keys such as 'name', 'position', 'team', 'league', and 'stats'.

**Raises:**

- ValueError: Raised when `sport` is empty or `target_count` is not a positive integer.
- TypeError: Raised when input types do not match the expected `str` and `int`/`str` signatures.
**Examples:**

```python
>>> fetch_top_players_for_sport('soccer', 5)
["{\\\"name\\\": \\\"Lionel Messi\\\", \\\"position\\\": \\\"Forward\\\", \\\"team\\\": \\\"Paris Saint-Germain\\\", \\\"league\\\": \\\"Ligue 1\\\", \\\"stats\\\": {}}", "{\\\"name\\\": \\\"Cristiano Ronaldo\\\", \\\"position\\\": \\\"Forward\\\", \\\"team\\\": \\\"Manchester United\\\", \\\"league\\\": \\\"Premier League\\\", \\\"stats\\\": {}}"]
```

```python
>>> fetch_top_players_for_sport('basketball', 3)
["{\\\"name\\\": \\\"LeBron James\\\", \\\"position\\\": \\\"SF\\\", \\\"team\\\": \\\"Los Angeles Lakers\\\", \\\"league\\\": \\\"NBA\\\", \\\"stats\\\": {}}", "{\\\"name\\\": \\\"Kevin Durant\\\", \\\"position\\\": \\\"PF\\\", \\\"team\\\": \\\"Brooklyn Nets\\\", \\\"league\\\": \\\"NBA\\\", \\\"stats\\\": {}}", "{\\\"name\\\": \\\"Stephen Curry\\\", \\\"position\\\": \\\"PG\\\", \\\"team\\\": \\\"Golden State Warriors\\\", \\\"league\\\": \\\"NBA\\\", \\\"stats\\\": {}}"]
```



---

## filter_active_players

### Description
Filters a list of player dictionaries to include only currently active players.

### Conceptual Info

The `filter_active_players` shim isolates players who are currently active from a raw list of player data, enabling downstream logic to focus on relevant candidates.

### Docstring

**Summary:** Return a filtered list of active players from given player data.

**Parameters:**

- players_data (str): A JSON-formatted string representing a list of player dictionaries. Each dictionary must contain at least a 'status' key with values such as 'active', 'retired', 'injured', etc.
**Returns:** str - A JSON string representing a list of dictionaries, each describing an active player. The returned value is compatible with JSON parsing into a Python list of dicts.

**Raises:**

- ValueError: Raised if the input string cannot be parsed as JSON or if the parsed object is not a list.
- TypeError: Raised if `players_data` is not of type `str`.
**Examples:**

```python
>>> sample_input = '[{"name": "Alice", "status": "active"}, {"name": "Bob", "status": "retired"}]'
>>> result = filter_active_players(sample_input)
>>> print(result)
"[{'name': 'Alice', 'status': 'active'}]"
```

```python
>>> invalid_input = '{"name": "Charlie", "status": "active"}'
>>> try:
...     filter_active_players(invalid_input)
>>> except ValueError as e:
...     print(e)
"Input must be a JSON list of player dictionaries."
```



---

## map_players_to_leagues

### Description
Map each player in a list to one of the available leagues, returning a list of dictionaries with player names and their corresponding league or None if not found.

### Conceptual Info

This shim transforms raw player data by aligning each player with one of the provided major leagues, ensuring downstream processes receive consistent league information.

### Docstring

**Summary:** Return a list of player dictionaries with an added league field matched against available leagues.

**Parameters:**

- players (List[dict]): A list of dictionaries where each dictionary contains at least a 'name' key and a 'league' key indicating the player's league.
- available_leagues (List[str]): A list of valid league names that players may be matched to.
**Returns:** List[dict] - A list where each element is a dictionary with keys `name` and `league`. The `league` value is the matched league name or `None` if the player's league is not in `available_leagues`.

**Raises:**

- ValueError: Raised when `players` or `available_leagues` are empty.
- TypeError: Raised when the input types are not `List[dict]` and `List[str]` respectively.
**Examples:**

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



---

## select_best_players

### Description
Selects the best players from a list of players with league information, constrained by minimum and maximum count.

### Conceptual Info

This shim encapsulates the core logic for filtering and selecting players based on quantity constraints. It is used after players have been mapped to leagues and serves as the final decision point before returning the key player list to higher-level modules.

### Docstring

**Summary:** Selects the best players from a list of player dictionaries, constrained by specified minimum and maximum counts.

**Parameters:**

- players_with_leagues (List[dict]): A list of dictionaries, each containing at least a 'player_name' and 'league' key, representing all candidate players.
- min_count (int): The minimum number of players that must be returned.
- max_count (int): The maximum number of players that may be returned.
**Returns:** List[dict] - A list of dictionaries representing the selected players. Each dictionary includes at least the keys 'player_name' and 'league'.

**Raises:**

- ValueError: Raised if `min_count` is greater than `max_count`, if no players are available, or if the selection constraints cannot be satisfied.
- TypeError: Raised if input arguments are not of the expected types.
**Examples:**

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



---

## extract_player_names

### Description
Extracts player names from a list of player dictionaries for downstream use.

### Conceptual Info

This shim isolates the extraction of player names from complex player data, enabling downstream nodes to work with clean, unambiguous name lists.

### Docstring

**Summary:** Extracts the 'name' field from each dictionary in a list of player data and returns a list of names.

**Parameters:**

- player_data (List[dict]): A list where each element is a dictionary representing a player, containing at least a 'name' key.
**Returns:** List[str] - A list of player names extracted from the input data.

**Raises:**

- ValueError: Raised if any dictionary in `player_data` lacks a 'name' key.
- TypeError: Raised if `player_data` is not a list.
**Examples:**

```python
>>> players = [{'name': 'LeBron James', 'team': 'Lakers'}, {'name': 'Kevin Durant', 'team': 'Nets'}]
>>> extract_player_names(players)
['LeBron James', 'Kevin Durant']
```

```python
>>> players = [{'name': 'Stephen Curry'}, {'name': 'James Harden', 'team': 'Nets'}]
>>> extract_player_names(players)
['Stephen Curry', 'James Harden']
```



---

## extract_player_leagues

### Description
Extracts the league names from a list of player dictionaries.

### Conceptual Info

This shim isolates the logic that pulls league information from player records, enabling downstream nodes to operate on a clean list of leagues without caring about the underlying player data structure.

### Docstring

**Summary:** Return a list of league names extracted from each player dictionary in the provided list.

**Parameters:**

- player_data (List[dict]): A list of dictionaries where each dictionary represents a player and must contain a key named 'league' with a string value.
**Returns:** List[str] - A list of strings, each representing the league name associated with a player.

**Raises:**

- ValueError: Raised if `player_data` is not a list, is empty, or any dictionary lacks a 'league' key.
- TypeError: Raised if `player_data` is not of type list or if any element is not a dictionary.
**Examples:**

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

