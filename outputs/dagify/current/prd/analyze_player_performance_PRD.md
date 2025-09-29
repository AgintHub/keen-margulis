# analyze_player_performance PRD

## Description
Examine player statistics to determine strengths, weaknesses, and areas for improvement.


## Conceptual Info

Analyzes preprocessed player data to identify performance metrics, strengths, weaknesses, and areas for improvement.

## Docstring

### Summary
Analyzes player performance using preprocessed data to identify key metrics and trends.

### Parameters

- **preprocessed_player_information** (List[str]): Preprocessed player information from the clean_and_preprocess_data node.
- **cleaned_game_statistics** (List[float]): Cleaned game statistics from the clean_and_preprocess_data node.

### Returns

Tuple[List[float], List[str], List[str], List[str]]: A tuple containing player performance metrics, strengths, weaknesses, and areas for improvement.

### Raises

- ValueError: If preprocessed_player_information or cleaned_game_statistics are empty or malformed.

### Examples

```python
>>> preprocessed_data = ['Player1', 'Player2']
>>> game_stats = [0.8, 0.9]
>>> result = analyze_player_performance(preprocessed_data, game_stats)
([0.85, 0.9], ['Consistency'], ['Scoring'], ['Defense'])
```
