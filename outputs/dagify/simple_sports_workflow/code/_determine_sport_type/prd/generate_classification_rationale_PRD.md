# generate_classification_rationale PRD

## Description
Generates a concise one‑sentence rationale explaining why a given sport is classified as team‑based or individual.


## Conceptual Info

In the larger system, this shim is responsible for converting structured sport data into an explanatory sentence that can be displayed to users or used for auditing the classification logic.

## Docstring

### Summary
Generate a concise justification for classifying a sport as team-based or individual.

### Parameters

- **sport** (str): The name of the sport (e.g., 'Soccer').
- **sport_type** (str): The classification of the sport, expected values are 'team-based' or 'individual'.
- **characteristics** (dict): A dictionary of sport characteristics such as 'team', 'players_per_side', etc.

### Returns

str: A single‑sentence rationale explaining the classification.

### Raises

- ValueError: If `sport_type` is not 'team-based' or 'individual', or if required keys are missing from `characteristics`.
- TypeError: If any argument is not of the expected type.

### Examples

```python
>>> rationale = generate_classification_rationale('Soccer', 'team-based', {
...     'team': True,
...     'players_per_side': 11
>>> })
>>> print(rationale)
'Soccer is a team-based sport because it involves 11 players per side.'
```

```python
>>> rationale = generate_classification_rationale('Tennis', 'individual', {
...     'team': False,
...     'players_per_side': 1
>>> })
>>> print(rationale)
'Tennis is an individual sport because it is played by a single player.'
```
