# _generate_performance_report - Complete PRD Documentation

## Overview
PRDs for nodes in the '_generate_performance_report' module.

## Table of Contents

- [validate_input_data](#validate_input_data)

- [format_team_statistics](#format_team_statistics)

- [create_top_performers_summary](#create_top_performers_summary)

- [generate_comprehensive_summary](#generate_comprehensive_summary)



---

## validate_input_data

### Description
Validates the input data for team performance analysis and top performers identification.

### Conceptual Info

This shim node validates the input data required for generating a performance report, ensuring that both team performance analysis and top performers identification data are correctly formatted and valid.

### Docstring

**Summary:** Validates input data for team performance and top performers analysis.

**Parameters:**

- team_data (str): Team performance data in the expected format (e.g., AnalyzeTeamPerformanceOutput model)
- performers_data (str): Top performers data in the expected format (e.g., IdentifyTopPerformersOutput model)
**Returns:** str - Validation result or success message indicating that inputs are valid

**Raises:**

- ValueError: When the input data fails validation checks
- TypeError: When the input data types are incorrect
**Examples:**

```python
>>> validate_input_data(team_data='{"win_loss_record": "20-10", "average_score": 80.5, "average_opponent_score": 75.2}', performers_data='{"top_scorers": ["Player1", "Player2"], "top_rebounders": ["Player3"], "top_assisters": ["Player4"]}')
"Validation successful"
```

```python
>>> validate_input_data(team_data='invalid_data', performers_data='{"top_scorers": ["Player1", "Player2"], "top_rebounders": ["Player3"], "top_assisters": ["Player4"]}')
"ValueError: Invalid team data format"
```



---

## format_team_statistics

### Description
Formats team statistics into a list of strings based on win/loss record, average score, and average opponent score.

### Conceptual Info

This shim formats team performance statistics into a structured list for reporting purposes.

### Docstring

**Summary:** Formats team statistics into a list of strings based on the provided win/loss record, average score, and average opponent score.

**Parameters:**

- win_loss (str): The team's win/loss record in the format 'wins-losses'.
- avg_score (str): The average score of the team per game.
- avg_opponent_score (str): The average score of the team's opponents per game.
**Returns:** List[str] - A list of strings representing the formatted team statistics.

**Raises:**

- ValueError: If the win/loss record is not in the correct format.
- TypeError: If any of the input parameters are not strings.
**Examples:**

```python
>>> format_team_statistics(win_loss='20-10', avg_score='80.5', avg_opponent_score='75.2')
['Win/Loss Record: 20-10', 'Average Score: 80.5', 'Average Opponent Score: 75.2']
```

```python
>>> format_team_statistics(win_loss='15-15', avg_score='70.0', avg_opponent_score='70.0')
['Win/Loss Record: 15-15', 'Average Score: 70.0', 'Average Opponent Score: 70.0']
```



---

## create_top_performers_summary

### Description
Creates a summary of top performers based on scorers, rebounders, and assisters.

### Conceptual Info

This shim function generates a summary of top performers in a team based on their performance in scoring, rebounding, and assisting.

### Docstring

**Summary:** Creates a formatted summary of top performers from the provided lists of scorers, rebounders, and assisters.

**Parameters:**

- scorers (List[str]): List of top scorers in the team.
- rebounders (List[str]): List of top rebounders in the team.
- assisters (List[str]): List of top assisters in the team.
**Returns:** str - A formatted summary including the names and roles of top performers.

**Raises:**

- TypeError: If any of the input parameters are not lists of strings.
- ValueError: If any of the input lists are empty.
**Examples:**

```python
>>> create_top_performers_summary(scorers=['Player1', 'Player2'], rebounders=['Player3', 'Player4'], assisters=['Player5', 'Player6'])
'Top scorers: Player1, Player2. Top rebounders: Player3, Player4. Top assisters: Player5, Player6.'
```

```python
>>> create_top_performers_summary(scorers=['John', 'Doe'], rebounders=['Jane', 'Doe'], assisters=['Bob', 'Smith'])
'Top scorers: John, Doe. Top rebounders: Jane, Doe. Top assisters: Bob, Smith.'
```



---

## generate_comprehensive_summary

### Description
Generates a comprehensive summary by combining team performance statistics and top performers information.

### Conceptual Info

This shim function is designed to create a comprehensive summary report by integrating team performance data and top performers statistics. It plays a crucial role in the larger system by providing a concise overview of the team's achievements and standout players.

### Docstring

**Summary:** Generates a comprehensive summary based on team performance and top performers data.

**Parameters:**

- team_performance (AnalyzeTeamPerformanceOutput): An object containing team performance statistics, including win/loss record, average score, and average opponent score.
- top_performers (IdentifyTopPerformersOutput): An object listing top performers in categories such as scoring, rebounding, and assisting.
**Returns:** str - A comprehensive summary that encapsulates both team performance and individual top performers' achievements.

**Raises:**

- ValueError: If either team_performance or top_performers contains invalid or missing data.
- TypeError: If the types of team_performance or top_performers do not match the expected AnalyzeTeamPerformanceOutput and IdentifyTopPerformersOutput respectively.
**Examples:**

```python
>>> team_performance = AnalyzeTeamPerformanceOutput(win_loss_record='20-10', average_score=85.5, average_opponent_score=78.2)
>>> top_performers = IdentifyTopPerformersOutput(top_scorers=['Player1', 'Player2'], top_rebounders=['Player3'], top_assisters=['Player4'])
>>> summary = generate_comprehensive_summary(team_performance=team_performance, top_performers=top_performers)
'The team achieved a 20-10 win/loss record with an average score of 85.5 and average opponent score of 78.2. Top scorers were Player1 and Player2, top rebounder was Player3, and top assister was Player4.'
```

```python
>>> team_performance = AnalyzeTeamPerformanceOutput(win_loss_record='15-15', average_score=80.0, average_opponent_score=80.0)
>>> top_performers = IdentifyTopPerformersOutput(top_scorers=['PlayerA'], top_rebounders=['PlayerB', 'PlayerC'], top_assisters=['PlayerD'])
>>> summary = generate_comprehensive_summary(team_performance=team_performance, top_performers=top_performers)
'The team had a 15-15 win/loss record with balanced average scores of 80.0 for both the team and opponents. Top scorer was PlayerA, top rebounders were PlayerB and PlayerC, and top assister was PlayerD.'
```

