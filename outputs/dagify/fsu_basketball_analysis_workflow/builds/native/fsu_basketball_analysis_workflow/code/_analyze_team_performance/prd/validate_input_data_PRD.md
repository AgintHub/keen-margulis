# validate_input_data PRD

## Description
Validates the input data for team performance analysis by checking the consistency and format of game dates, opponents, scores, and game statistics.


## Conceptual Info

This shim node is responsible for validating the input data required for team performance analysis, ensuring that the data is consistent and properly formatted.

## Docstring

### Summary
Validates input data for team performance analysis by checking the consistency and format of game dates, opponents, scores, and game statistics.

### Parameters

- **game_dates** (str): List of game dates in string format
- **opponents** (str): List of opponents in string format
- **scores** (str): List of game scores in string format (e.g., '74-68')
- **game_statistics** (str): List of game statistics in string format

### Returns

str: Output indicating whether the input data is valid or not

### Raises

- ValueError: When the input lists are of different lengths or when the score format is invalid
- TypeError: When the input types are not strings or when the input lists contain non-string elements

### Examples

```python
>>> validate_input_data(game_dates='2022-01-01,2022-01-02', opponents='Team A,Team B', scores='74-68,70-75', game_statistics='rebounds,turnovers')
>>> validate_input_data(game_dates='2022-01-01,2022-01-02', opponents='Team A,Team B', scores='74-68,invalid_score', game_statistics='rebounds,turnovers')
Valid input data
```

```python
>>> validate_input_data(game_dates='2022-01-01', opponents='Team A,Team B', scores='74-68,70-75', game_statistics='rebounds,turnovers')
ValueError: Input lists must be of the same length
```
