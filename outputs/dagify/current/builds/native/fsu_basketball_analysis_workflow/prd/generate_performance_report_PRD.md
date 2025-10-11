# generate_performance_report PRD

## Description
Generate a comprehensive performance report for FSU basketball team


## Conceptual Info

This node generates a comprehensive performance report for the FSU basketball team by synthesizing team performance analysis and top performer identification.

## Docstring

### Summary
Generate a comprehensive performance report for the FSU basketball team.

### Parameters

- **team_performance_analysis** (dict): Analysis of team performance including win/loss record, average score, and average opponent score.
- **top_performers** (dict): Identification of top performers including top scorers, rebounders, and assisters.

### Returns

dict: A dictionary containing the report summary, team statistics, and top performers summary.

### Raises

- ValueError: If team performance analysis or top performers data is missing or invalid.

### Examples

```python
>>> team_performance_analysis = {'win_loss_record': '20-10', 'average_score': 74.5, 'average_opponent_score': 68.2}
>>> top_performers = {'top_scorers': ['Player1', 'Player2'], 'top_rebounders': ['Player3'], 'top_assisters': ['Player4']}
>>> generate_performance_report(team_performance_analysis, top_performers)
{'report_summary': 'The team had a 20-10 record with an average score of 74.5 and average opponent score of 68.2. Top scorers were Player1 and Player2.', 'team_statistics': ['Win/Loss Record: 20-10', 'Average Score: 74.5', 'Average Opponent Score: 68.2'], 'top_performers_summary': 'Top scorers: Player1, Player2. Top rebounders: Player3. Top assisters: Player4.'}
```
