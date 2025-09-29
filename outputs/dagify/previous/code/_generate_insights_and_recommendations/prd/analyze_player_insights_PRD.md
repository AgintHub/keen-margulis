# analyze_player_insights PRD

## Description
Analyzes player performance metrics, strengths, and weaknesses to generate insights.


## Conceptual Info

This shim analyzes player performance data to generate insights that can be used for improvement recommendations.

## Docstring

### Summary
Analyzes player performance metrics, strengths, and weaknesses to generate a list of insights.

### Parameters

- **metrics** (str): String representation of player performance metrics
- **strengths** (str): String representation of player strengths
- **weaknesses** (str): String representation of player weaknesses

### Returns

List[str]: List of insights derived from the analysis of player performance metrics, strengths, and weaknesses

### Raises

- ValueError: When input validation fails due to missing or malformed data
- TypeError: When input types are incorrect, such as non-string inputs

### Examples

```python
>>> analyze_player_insights(metrics='[0.8, 0.7, 0.9]', strengths='["shooting", "passing"]', weaknesses='["dribbling"]')
['Improve dribbling skills', 'Maintain high shooting and passing accuracy']
```

```python
>>> analyze_player_insights(metrics='[0.5, 0.6, 0.4]', strengths='["defense"]', weaknesses='["speed", "agility"]')
['Focus on improving speed and agility', 'Continue to develop defensive skills']
```
