# compile_game_statistics PRD

## Description
Compiles game statistics from a list of validated game data into a list of strings.


## Conceptual Info

This shim node is responsible for compiling game statistics from a list of validated game data. It takes in a string representation of the game data and outputs a list of strings representing the compiled game statistics.

## Docstring

### Summary
Compiles game statistics from input game data.

### Parameters

- **games** (str): A string representation of validated game data.

### Returns

List[str]: A list of strings where each string represents compiled game statistics.

### Raises

- ValueError: If the input game data is not in the expected format.
- TypeError: If the input is not a string.

### Examples

```python
>>> compile_game_statistics(games='[{\"score\": \"74-68\", \"stats\": {\"rebounds\": 40, \"turnovers\": 15}}]')
['Rebounds: 40', 'Turnovers: 15']
```

```python
>>> compile_game_statistics(games='[{\"score\": \"90-85\", \"stats\": {\"rebounds\": 45, \"turnovers\": 12}}]')
['Rebounds: 45', 'Turnovers: 12']
```
