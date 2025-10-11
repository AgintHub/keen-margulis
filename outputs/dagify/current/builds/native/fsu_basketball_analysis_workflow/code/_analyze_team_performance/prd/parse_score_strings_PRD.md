# parse_score_strings PRD

## Description
Parses a list of score strings into a list of tuples containing the team and opponent scores.


## Conceptual Info

This shim function is responsible for parsing a list of score strings into a structured format that can be used for further analysis, such as calculating win/loss records and average scores.

## Docstring

### Summary
Parses a list of score strings into a list of tuples containing team and opponent scores.

### Parameters

- **scores** (str): A list of score strings, where each score string is in the format 'team_score-opponent_score' (e.g., '74-68').

### Returns

List[tuple]: A list of tuples, where each tuple contains the team score and opponent score as integers.

### Raises

- ValueError: If a score string is not in the expected format.

### Examples

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
