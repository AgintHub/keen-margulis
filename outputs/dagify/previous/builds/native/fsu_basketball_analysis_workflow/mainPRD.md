# fsu_basketball_analysis_workflow - Complete PRD Documentation

## Overview
PRDs for nodes in the 'fsu_basketball_analysis_workflow' module.

## Table of Contents

- [analyze_team_performance](#analyze_team_performance)

- [extract_player_statistics](#extract_player_statistics)

- [gather_historical_game_data](#gather_historical_game_data)

- [generate_performance_report](#generate_performance_report)

- [identify_top_performers](#identify_top_performers)



---

## analyze_team_performance

### Description
Analyze overall team performance based on game data

### Conceptual Info

This node analyzes the overall team performance based on historical game data, calculating key metrics such as win/loss record, average score, and average opponent score.

### Docstring

**Summary:** Analyzes team performance based on historical game data, computing win/loss record and average scores.

**Parameters:**

- game_dates (List[str]): List of game dates from historical game data.
- opponents (List[str]): List of opponents from historical game data.
- scores (List[str]): List of game scores from historical game data, formatted as 'team_score-opponent_score'.
- game_statistics (List[str]): List of game statistics from historical game data.
**Returns:** Tuple[str, float, float] - A tuple containing the team's win/loss record, average score, and average opponent score.

**Raises:**

- ValueError: If the input lists are of different lengths or if scores are not properly formatted.
**Examples:**

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



---

## extract_player_statistics

### Description
Extract player statistics from game data

### Conceptual Info

This node processes historical game data to extract individual player statistics, including points scored, rebounds, and assists.

### Docstring

**Summary:** Extracts player statistics from historical game data, returning lists of player names and their respective statistics.

**Parameters:**

- game_dates (List[str]): List of game dates from the historical game data.
- opponents (List[str]): List of opponents from the historical game data.
- scores (List[str]): List of game scores from the historical game data.
- game_statistics (List[str]): List of game statistics from the historical game data.
**Returns:** Tuple[List[str], List[int], List[int], List[int]] - A tuple containing lists of player names, points scored, rebounds, and assists.

**Raises:**

- ValueError: If the input lists are not of the same length.
- TypeError: If the input data types are not as expected.
**Examples:**

```python
>>> game_dates = ['2022-01-01', '2022-01-03']
>>> opponents = ['Team A', 'Team B']
>>> scores = ['80-70', '90-85']
>>> game_statistics = ['Player1:20,5,3;Player2:15,7,2', 'Player1:22,6,4;Player2:18,8,3']
>>> extract_player_statistics(game_dates, opponents, scores, game_statistics)
(['Player1', 'Player2'], [42, 33], [11, 15], [7, 5])
```

```python
>>> game_dates = ['2022-02-01']
>>> opponents = ['Team C']
>>> scores = ['100-90']
>>> game_statistics = ['Player1:25,4,5;Player2:20,6,4']
>>> extract_player_statistics(game_dates, opponents, scores, game_statistics)
(['Player1', 'Player2'], [25, 20], [4, 6], [5, 4])
```



---

## gather_historical_game_data

### Description
Collect historical game data for FSU basketball team

### Conceptual Info

This node is responsible for collecting historical game data for the FSU basketball team, including game dates, opponents, scores, and game statistics.

### Docstring

**Summary:** Gathers historical game data for the FSU basketball team.

**Returns:** Tuple[List[str], List[str], List[str], List[str]] - A tuple containing lists of game dates, opponents, scores, and game statistics.

**Raises:**

- DataCollectionError: If there's an issue collecting the historical game data.
**Examples:**

```python
>>> game_data = gather_historical_game_data()
>>> print(game_data)
(['2023-01-01', '2023-01-03'], ['Team A', 'Team B'], ['74-68', '80-75'], ['Rebounds: 40, Turnovers: 15', 'Rebounds: 35, Turnovers: 10'])
```



---

## generate_performance_report

### Description
Generate a comprehensive performance report for FSU basketball team

### Conceptual Info

This node generates a comprehensive performance report for the FSU basketball team by synthesizing team performance analysis and top performer identification.

### Docstring

**Summary:** Generate a comprehensive performance report for the FSU basketball team.

**Parameters:**

- team_performance_analysis (dict): Analysis of team performance including win/loss record, average score, and average opponent score.
- top_performers (dict): Identification of top performers including top scorers, rebounders, and assisters.
**Returns:** dict - A dictionary containing the report summary, team statistics, and top performers summary.

**Raises:**

- ValueError: If team performance analysis or top performers data is missing or invalid.
**Examples:**

```python
>>> team_performance_analysis = {'win_loss_record': '20-10', 'average_score': 74.5, 'average_opponent_score': 68.2}
>>> top_performers = {'top_scorers': ['Player1', 'Player2'], 'top_rebounders': ['Player3'], 'top_assisters': ['Player4']}
>>> generate_performance_report(team_performance_analysis, top_performers)
{'report_summary': 'The team had a 20-10 record with an average score of 74.5 and average opponent score of 68.2. Top scorers were Player1 and Player2.', 'team_statistics': ['Win/Loss Record: 20-10', 'Average Score: 74.5', 'Average Opponent Score: 68.2'], 'top_performers_summary': 'Top scorers: Player1, Player2. Top rebounders: Player3. Top assisters: Player4.'}
```



---

## identify_top_performers

### Description
Identify top performing players based on statistics

### Conceptual Info

This node identifies top performing players based on their statistics such as points scored, rebounds, and assists. It takes the output from the 'extract_player_statistics' node and processes it to determine the top performers in each category.

### Docstring

**Summary:** Identify top performing players based on points scored, rebounds, assists, and other relevant metrics.

**Parameters:**

- player_names (List[str]): List of player names extracted from game data.
- points_scored (List[int]): List of total points scored by each player.
- rebounds (List[int]): List of total rebounds by each player.
- assists (List[int]): List of total assists by each player.
**Returns:** Tuple[List[str], List[str], List[str]] - A tuple containing lists of top scorers, top rebounders, and top assisters.

**Raises:**

- ValueError: If the input lists are of different lengths.
- TypeError: If the input types are not as expected.
**Examples:**

```python
>>> player_names = ['Player1', 'Player2', 'Player3']
>>> points_scored = [20, 15, 25]
>>> rebounds = [5, 10, 7]
>>> assists = [8, 6, 9]
>>> top_scorers, top_rebounders, top_assisters = identify_top_performers(player_names, points_scored, rebounds, assists)
(['Player3', 'Player1', 'Player2'], ['Player2', 'Player3', 'Player1'], ['Player3', 'Player1', 'Player2'])
```

```python
>>> player_names = ['PlayerA', 'PlayerB']
>>> points_scored = [30, 20]
>>> rebounds = [8, 12]
>>> assists = [7, 5]
>>> top_scorers, top_rebounders, top_assisters = identify_top_performers(player_names, points_scored, rebounds, assists)
(['PlayerA', 'PlayerB'], ['PlayerB', 'PlayerA'], ['PlayerA', 'PlayerB'])
```

