# identify_player_strengths PRD

## Description
Identifies player strengths based on performance metrics and player information.


## Conceptual Info

This shim node is responsible for analyzing player performance metrics and information to identify the player's strengths, playing a crucial role in the player performance analysis pipeline.

## Docstring

### Summary
Analyzes performance metrics and player information to identify player strengths.

### Parameters

- **performance_metrics** (str): String representation of performance metrics used to identify strengths.
- **player_info** (str): String containing relevant information about the player.

### Returns

List[str]: A list of strings representing the identified strengths of the player.

### Raises

- ValueError: If the input performance metrics or player information are invalid or cannot be processed.
- TypeError: If the input types are not as expected (e.g., not strings).

### Examples

```python
>>> identify_player_strengths(performance_metrics='[0.8, 0.7, 0.9]', player_info='Experienced player with strong shooting skills')
>>> print(output)
['Shooting', 'Teamwork']
```

```python
>>> identify_player_strengths(performance_metrics='[0.4, 0.6, 0.5]', player_info='New player with potential')
>>> print(output)
['Speed', 'Agility']
```
