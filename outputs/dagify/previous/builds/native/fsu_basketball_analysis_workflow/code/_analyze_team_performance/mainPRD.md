# _analyze_team_performance - Complete PRD Documentation

## Overview
PRDs for nodes in the '_analyze_team_performance' module.

## Table of Contents

- [validate_input_data](#validate_input_data)

- [parse_score_strings](#parse_score_strings)

- [count_wins](#count_wins)

- [count_losses](#count_losses)

- [format_win_loss_record](#format_win_loss_record)

- [extract_team_scores](#extract_team_scores)

- [extract_opponent_scores](#extract_opponent_scores)

- [calculate_average_score](#calculate_average_score)



---

## validate_input_data

### Description
Validates the input data for team performance analysis by checking the consistency and format of game dates, opponents, scores, and game statistics.

### Conceptual Info

This shim node is responsible for validating the input data required for team performance analysis, ensuring that the data is consistent and properly formatted.

### Docstring

**Summary:** Validates input data for team performance analysis by checking the consistency and format of game dates, opponents, scores, and game statistics.

**Parameters:**

- game_dates (str): List of game dates in string format
- opponents (str): List of opponents in string format
- scores (str): List of game scores in string format (e.g., '74-68')
- game_statistics (str): List of game statistics in string format
**Returns:** str - Output indicating whether the input data is valid or not

**Raises:**

- ValueError: When the input lists are of different lengths or when the score format is invalid
- TypeError: When the input types are not strings or when the input lists contain non-string elements
**Examples:**

```python
>>> validate_input_data(game_dates='2022-01-01,2022-01-02', opponents='Team A,Team B', scores='74-68,70-75', game_statistics='rebounds,turnovers')
>>> validate_input_data(game_dates='2022-01-01,2022-01-02', opponents='Team A,Team B', scores='74-68,invalid_score', game_statistics='rebounds,turnovers')
Valid input data
```

```python
>>> validate_input_data(game_dates='2022-01-01', opponents='Team A,Team B', scores='74-68,70-75', game_statistics='rebounds,turnovers')
ValueError: Input lists must be of the same length
```



---

## parse_score_strings

### Description
Parses a list of score strings into a list of tuples containing the team and opponent scores.

### Conceptual Info

This shim function is responsible for parsing a list of score strings into a structured format that can be used for further analysis, such as calculating win/loss records and average scores.

### Docstring

**Summary:** Parses a list of score strings into a list of tuples containing team and opponent scores.

**Parameters:**

- scores (str): A list of score strings, where each score string is in the format 'team_score-opponent_score' (e.g., '74-68').
**Returns:** List[tuple] - A list of tuples, where each tuple contains the team score and opponent score as integers.

**Raises:**

- ValueError: If a score string is not in the expected format.
**Examples:**

```python
>>> scores = ['74-68', '80-75', '60-90']
>>> parsed_scores = parse_score_strings(scores=scores)
[(74, 68), (80, 75), (60, 90)]
```

```python
>>> scores = ['100-50', '25-30']
>>> parsed_scores = parse_score_strings(scores=scores)
[(100, 50), (25, 30)]
```



---

## count_wins

### Description
Counts the number of wins from a list of parsed game scores.

### Conceptual Info

This shim node is designed to count the number of wins from a given list of parsed game scores, playing a crucial role in analyzing team performance.

### Docstring

**Summary:** Counts the number of wins from a list of parsed game scores.

**Parameters:**

- parsed_scores (List[str]): A list of strings representing parsed game scores (e.g., '74-68').
**Returns:** int - The total count of wins based on the provided game scores.

**Raises:**

- ValueError: If the input scores are not in the expected format.
- TypeError: If the input is not a list of strings.
**Examples:**

```python
>>> count_wins(parsed_scores=['74-68', '60-70', '80-75'])
2
```

```python
>>> count_wins(parsed_scores=['50-60', '70-65', '60-70'])
1
```



---

## count_losses

### Description
Counts the number of losses from a list of parsed game scores.

### Conceptual Info

This shim node is designed to count the number of losses from a given list of parsed game scores, playing a crucial role in analyzing team performance.

### Docstring

**Summary:** Counts the number of losses from a list of parsed game scores represented as a string.

**Parameters:**

- parsed_scores (str): A string representation of parsed game scores, expected to be in a format that can be interpreted to determine wins or losses.
**Returns:** int - The total count of losses derived from the input parsed scores.

**Raises:**

- ValueError: If the input string cannot be parsed into a recognizable score format.
- TypeError: If the input is not a string.
**Examples:**

```python
>>> count_losses(parsed_scores='10-5,8-7,3-10')
1
```

```python
>>> count_losses(parsed_scores='15-20,25-30,10-15')
3
```



---

## format_win_loss_record

### Description
Formats the win/loss record into a string representation.

### Conceptual Info

This shim node is responsible for formatting the win/loss record of a team into a string representation, typically used in sports analytics.

### Docstring

**Summary:** Formats the win and loss counts into a string representation.

**Parameters:**

- wins (str): The number of wins as a string.
- losses (str): The number of losses as a string.
**Returns:** str - The formatted win/loss record (e.g., '20-10').

**Raises:**

- ValueError: If either wins or losses cannot be converted to a non-negative integer.
- TypeError: If wins or losses are not strings.
**Examples:**

```python
>>> format_win_loss_record(wins='20', losses='10')
'20-10'
```

```python
>>> format_win_loss_record(wins='0', losses='5')
'0-5'
```



---

## extract_team_scores

### Description
Extracts team scores from a list of parsed score tuples.

### Conceptual Info

This shim function is designed to take a list of parsed score tuples and extract the team scores, returning them as a list of integers. It plays a crucial role in analyzing team performance by isolating the scores achieved by the team in question.

### Docstring

**Summary:** Extract team scores from a list of parsed score tuples.

**Parameters:**

- parsed_scores (List[tuple]): A list of tuples where each tuple contains two integers representing the team score and the opponent score, respectively.
**Returns:** List[int] - A list of integers representing the team scores extracted from the input parsed scores.

**Raises:**

- ValueError: If the input list is empty or if any tuple in the list does not contain exactly two integers.
- TypeError: If the input is not a list of tuples or if the elements of the tuples are not integers.
**Examples:**

```python
>>> parsed_scores = [(74, 68), (80, 75), (90, 85)]
>>> team_scores = extract_team_scores(parsed_scores)
[74, 80, 90]
```

```python
>>> parsed_scores = [(60, 70), (65, 75), (70, 80)]
>>> team_scores = extract_team_scores(parsed_scores)
[60, 65, 70]
```



---

## extract_opponent_scores

### Description
Extracts opponent scores from a list of parsed score tuples into a list of integers.

### Conceptual Info

This shim function is designed to extract opponent scores from a list of parsed score tuples, which are derived from game score strings.

### Docstring

**Summary:** Extract opponent scores from a list of parsed score tuples.

**Parameters:**

- parsed_scores (List[tuple[int, int]]): List of tuples containing team and opponent scores
**Returns:** List[int] - List of opponent scores as integers

**Raises:**

- TypeError: If parsed_scores is not a list of tuples or if tuple elements are not integers
- ValueError: If parsed_scores list is empty or contains tuples without exactly two elements
**Examples:**

```python
>>> parsed_scores = [(100, 90), (80, 95), (70, 85)]
>>> opponent_scores = extract_opponent_scores(parsed_scores=parsed_scores)
[90, 95, 85]
```

```python
>>> parsed_scores = [(75, 80), (90, 85)]
>>> opponent_scores = extract_opponent_scores(parsed_scores=parsed_scores)
[80, 85]
```



---

## calculate_average_score

### Description
Calculates the average score from a list of scores.

### Conceptual Info

This shim calculates the average score from a given list of scores, playing a crucial role in analyzing team performance by providing a key metric.

### Docstring

**Summary:** Calculates the average score from a list of scores provided as input.

**Parameters:**

- scores (List[int]): A list of integer scores for which the average needs to be calculated.
**Returns:** float - The average score calculated from the input list of scores.

**Raises:**

- ValueError: If the input list is empty or contains non-numeric values.
- TypeError: If the input is not a list or if the list contains non-integer values.
**Examples:**

```python
>>> calculate_average_score(scores=[10, 20, 30])
20.0
```

```python
>>> calculate_average_score(scores=[15, 25, 35, 45])
30.0
```

