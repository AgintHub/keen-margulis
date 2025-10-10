# extract_player_names PRD

## Description
Extracts player names from a list of player dictionaries for downstream use.


## Conceptual Info

This shim isolates the extraction of player names from complex player data, enabling downstream nodes to work with clean, unambiguous name lists.

## Docstring

### Summary
Extracts the 'name' field from each dictionary in a list of player data and returns a list of names.

### Parameters

- **player_data** (List[dict]): A list where each element is a dictionary representing a player, containing at least a 'name' key.

### Returns

List[str]: A list of player names extracted from the input data.

### Raises

- ValueError: Raised if any dictionary in `player_data` lacks a 'name' key.
- TypeError: Raised if `player_data` is not a list.

### Examples

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
