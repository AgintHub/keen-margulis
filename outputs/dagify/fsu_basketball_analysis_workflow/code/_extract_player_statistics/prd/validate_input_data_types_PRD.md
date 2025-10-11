# validate_input_data_types PRD

## Description
Validates the data types of input parameters game_dates, opponents, scores, and game_statistics.


## Conceptual Info

This shim node is responsible for validating the data types of the input parameters game_dates, opponents, scores, and game_statistics to ensure they are of the expected type.

## Docstring

### Summary
Validates the input data types for game_dates, opponents, scores, and game_statistics.

### Parameters

- **game_dates** (str): A string representing the list of game dates.
- **opponents** (str): A string representing the list of opponents.
- **scores** (str): A string representing the list of game scores.
- **game_statistics** (str): A string representing the list of game statistics.

### Returns

str: A string indicating the result of the validation.

### Raises

- TypeError: If any of the input parameters are not of the expected type.
- ValueError: If the input parameters contain invalid data.

### Examples

```python
>>> validate_input_data_types(game_dates='2022-01-01', opponents='Team A', scores='10-5', game_statistics='stats')
>>> print(output)
'Validation successful'
```

```python
>>> validate_input_data_types(game_dates=123, opponents='Team A', scores='10-5', game_statistics='stats')
>>> print(output)
'TypeError: game_dates must be a string'
```
