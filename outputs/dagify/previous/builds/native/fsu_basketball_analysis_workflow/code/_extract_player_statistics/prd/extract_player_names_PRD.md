# extract_player_names PRD

## Description
Extracts player names from aggregated statistics.


## Conceptual Info

This shim function is designed to extract a list of player names from a given aggregated statistics object, playing a crucial role in the data processing pipeline of sports statistics analysis.

## Docstring

### Summary
Extracts player names from aggregated statistics.

### Parameters

- **aggregated_stats** (str): Aggregated player statistics as a string, expected to contain player names.

### Returns

List[str]: A list of player names extracted from the aggregated statistics.

### Raises

- ValueError: If the input aggregated_stats is not a valid string or does not contain player names.
- TypeError: If the input aggregated_stats is not of type str.

### Examples

```python
>>> aggregated_stats = '{ "Player1": { "score": 10 }, "Player2": { "score": 20 } }'
>>> extract_player_names(aggregated_stats=aggregated_stats)
['Player1', 'Player2']
```

```python
>>> aggregated_stats = '{ "John": { "score": 5 }, "Doe": { "score": 15 } }'
>>> extract_player_names(aggregated_stats=aggregated_stats)
['John', 'Doe']
```
