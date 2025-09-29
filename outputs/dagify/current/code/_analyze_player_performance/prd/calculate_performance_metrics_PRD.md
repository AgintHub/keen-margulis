# calculate_performance_metrics PRD

## Description
Calculates player performance metrics based on game statistics and player information.


## Conceptual Info

This shim node is responsible for computing player performance metrics by processing game statistics and player information.

## Docstring

### Summary
Calculates player performance metrics based on the provided game statistics and player information.

### Parameters

- **game_statistics** (str): String representation of game statistics that will be used to calculate performance metrics.
- **player_info** (str): String representation of player information that will be used to calculate performance metrics.

### Returns

List[float]: A list of floating-point numbers representing the calculated player performance metrics.

### Raises

- ValueError: If the input game statistics or player information is invalid or cannot be processed.
- TypeError: If the input types are not as expected (e.g., not strings).

### Examples

```python
>>> game_stats = 'points:10,rebounds:5,assists:7'
>>> player_info = 'name:John,position:Forward,minutes_played:30'
>>> performance_metrics = calculate_performance_metrics(game_statistics=game_stats, player_info=player_info)
[0.8, 0.7, 0.9]
```

```python
>>> game_stats = 'points:15,rebounds:3,assists:5'
>>> player_info = 'name:Jane,position:Guard,minutes_played:25'
>>> performance_metrics = calculate_performance_metrics(game_statistics=game_stats, player_info=player_info)
[0.9, 0.6, 0.8]
```
