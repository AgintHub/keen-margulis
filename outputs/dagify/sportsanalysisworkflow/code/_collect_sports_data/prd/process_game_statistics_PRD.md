# process_game_statistics PRD

## Description
A shim function that processes raw game statistics data into a list of formatted game statistics strings.


## Conceptual Info

This shim processes raw game statistics data fetched from the database into a structured list of game statistics strings, playing a crucial role in preparing the data for further analysis or output.

## Docstring

### Summary
Processes raw game statistics data into a list of formatted game statistics strings.

### Parameters

- **raw_data** (str): A string representation of the raw game statistics data fetched from the database.

### Returns

List[str]: A list of strings where each string represents a processed game statistic.

### Raises

- ValueError: If the raw_data is not in the expected format or is missing required information.
- TypeError: If the input raw_data is not of type string.

### Examples

```python
>>> raw_game_data = '[{"score": 10, "team": "A"}, {"score": 5, "team": "B"}]'
>>> processed_game_stats = process_game_statistics(raw_data=raw_game_data)
["Team A scored 10", "Team B scored 5"]
```

```python
>>> raw_game_data = '[{"score": 7, "team": "C"}]'
>>> processed_game_stats = process_game_statistics(raw_data=raw_game_data)
["Team C scored 7"]
```
