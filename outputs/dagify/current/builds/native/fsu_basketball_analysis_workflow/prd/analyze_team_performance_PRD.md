# analyze_team_performance PRD

## Description
Analyze overall team performance based on game data


## Conceptual Info

This node analyzes the overall team performance based on historical game data, calculating key metrics such as win/loss record, average score, and average opponent score.

## Docstring

### Summary
Analyzes team performance based on historical game data, computing win/loss record and average scores.

### Parameters

- **game_dates** (List[str]): List of game dates from historical game data.
- **opponents** (List[str]): List of opponents from historical game data.
- **scores** (List[str]): List of game scores from historical game data, formatted as 'team_score-opponent_score'.
- **game_statistics** (List[str]): List of game statistics from historical game data.

### Returns

Tuple[str, float, float]: A tuple containing the team's win/loss record, average score, and average opponent score.

### Raises

- ValueError: If the input lists are of different lengths or if scores are not properly formatted.

### Examples

```python
>>> game_dates = ['2023-01-01', '2023-01-03']
>>> opponents = ['Team A', 'Team B']
>>> scores = ['80-70', '75-85']
>>> game_statistics = ['stats1', 'stats2']
>>> analyze_team_performance(game_dates, opponents, scores, game_statistics)
('1-1', 77.5, 77.5)
```

```python
>>> game_dates = ['2023-02-01', '2023-02-03', '2023-02-05']
>>> opponents = ['Team C', 'Team D', 'Team E']
>>> scores = ['90-80', '85-95', '100-90']
>>> game_statistics = ['stats3', 'stats4', 'stats5']
>>> analyze_team_performance(game_dates, opponents, scores, game_statistics)
('2-1', 91.66666666666667, 88.33333333333333)
```
