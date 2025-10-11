# extract_game_dates PRD

## Description
Extracts a list of game dates from a given list of game records.


## Conceptual Info

This shim function is designed to extract game dates from a list of game records, playing a crucial role in data processing for historical game data analysis.

## Docstring

### Summary
Extracts game dates from a list of game records represented as a string.

### Parameters

- **games** (str): A string representation of a list of game records.

### Returns

List[str]: A list of game dates in string format.

### Raises

- ValueError: If the input string is not a valid representation of game records.
- TypeError: If the input is not of type string.

### Examples

```python
>>> games = '[{"date": "2022-01-01"}, {"date": "2022-01-15"}]'
>>> extract_game_dates(games=games)
['2022-01-01', '2022-01-15']
```

```python
>>> games = '[{"date": "2023-02-01"}, {"date": "2023-03-01"}]'
>>> extract_game_dates(games=games)
['2023-02-01', '2023-03-01']
```
