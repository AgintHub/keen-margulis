# analyze_sport_characteristics PRD

## Description
Analyzes a validated sport name and returns a JSON string describing key characteristics used for classification.


## Conceptual Info

Provides structured sport data required for determining whether a sport is team-based or individual and for generating a rationale.

## Docstring

### Summary
Analyzes a validated sport name and returns a JSON string of its key characteristics.

### Parameters

- **sport** (str): A non-empty, validated string containing the name of the sport to analyze.

### Returns

str: A JSON-formatted string representing a dictionary with keys such as sport_name, team_based, players_per_side, field_type, equipment, and governing_body.

### Raises

- ValueError: Raised if the provided sport name is empty or unrecognized.
- TypeError: Raised if the input is not a string.

### Examples

```python
>>> analyze_sport_characteristics('soccer')
"{\"sport_name\": \"soccer\", \"team_based\": true, \"players_per_side\": 11, \"field_type\": \"field\", \"equipment\": [\"ball\", \"goal\"], \"governing_body\": \"FIFA\"}"
```

```python
>>> analyze_sport_characteristics('archery')
"{\"sport_name\": \"archery\", \"team_based\": false, \"players_per_side\": 1, \"field_type\": \"outdoor\", \"equipment\": [\"bow\", \"arrow\"], \"governing_body\": \"World Archery Federation\"}"
```
