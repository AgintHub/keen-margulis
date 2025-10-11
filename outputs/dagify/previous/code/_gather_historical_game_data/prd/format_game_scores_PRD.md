# format_game_scores PRD

## Description
Formats game scores from a list of game records into a list of score strings.


## Conceptual Info

This shim node is responsible for taking game records, extracting the scores, and formatting them into a standardized list of strings.

## Docstring

### Summary
Formats game scores from a list of game records into a list of score strings.

### Parameters

- **games** (str): A string representation of game records, expected to be a JSON-like structure containing game information including scores.

### Returns

List[str]: A list of strings where each string represents a formatted game score (e.g., '74-68').

### Raises

- ValueError: If the input string cannot be parsed into a valid game record structure.
- TypeError: If the input is not a string.

### Examples

```python
>>> games = '[{"score": "74-68"}, {"score": "80-75"}]'
>>> format_game_scores(games=games)
['74-68', '80-75']
```

```python
>>> games = '[{"score": "60-70"}]'
>>> format_game_scores(games=games)
['60-70']
```
