# analyze_team_performance PRD

## Description
Examine team statistics to determine strengths, weaknesses, and areas for improvement.


## Conceptual Info

Analyze team performance by examining preprocessed data to identify key metrics, trends, strengths, weaknesses, and areas for improvement.

## Docstring

### Summary
Analyze team performance using preprocessed data to determine key metrics and trends.

### Parameters

- **cleaned_game_statistics** (List[float]): Cleaned game statistics from the clean_and_preprocess_data node.
- **transformed_team_performance_metrics** (List[float]): Transformed team performance metrics from the clean_and_preprocess_data node.

### Returns

Tuple[List[float], List[str], List[str], List[str]]: A tuple containing team performance metrics, team strengths, team weaknesses, and areas for team improvement.

### Raises

- ValueError: If input data is empty or malformed.

### Examples

```python
>>> cleaned_game_statistics = [0.8, 0.7, 0.9]
>>> transformed_team_performance_metrics = [0.85, 0.75, 0.95]
>>> team_performance = analyze_team_performance(cleaned_game_statistics, transformed_team_performance_metrics)
([0.85, 0.75, 0.95], ['Strong offense'], ['Weak defense'], ['Improve teamwork'])
```
