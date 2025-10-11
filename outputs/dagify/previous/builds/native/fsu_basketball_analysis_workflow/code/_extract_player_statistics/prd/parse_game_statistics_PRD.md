# parse_game_statistics PRD

## Description
Parses game statistics from a list of strings into a list of dictionaries.


## Conceptual Info

This shim node is responsible for parsing game statistics from a list of strings into a structured format (list of dictionaries) that can be further processed by downstream nodes.

## Docstring

### Summary
Parses game statistics from a list of strings into a list of dictionaries.

### Parameters

- **game_statistics** (str): A list of game statistics in string format that need to be parsed.

### Returns

List[dict]: A list of dictionaries where each dictionary contains the parsed game statistics.

### Raises

- ValueError: If the input game statistics are not in the expected format.
- TypeError: If the input is not a list of strings.

### Examples

```python
>>> game_statistics = ['team:A,points:100,rebounds:50', 'team:B,points:90,rebounds:40']
>>> parse_game_statistics(game_statistics=game_statistics)
[{'team': 'A', 'points': '100', 'rebounds': '50'}, {'team': 'B', 'points': '90', 'rebounds': '40'}]
```

```python
>>> game_statistics = ['player:X,score:85,assists:7', 'player:Y,score:75,assists:5']
>>> parse_game_statistics(game_statistics=game_statistics)
[{'player': 'X', 'score': '85', 'assists': '7'}, {'player': 'Y', 'score': '75', 'assists': '5'}]
```
