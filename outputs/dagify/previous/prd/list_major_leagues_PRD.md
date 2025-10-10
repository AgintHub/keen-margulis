# list_major_leagues PRD

## Description
List major professional leagues for the sport


## Conceptual Info

Retrieves a curated list of the most prominent professional leagues for a given sport, facilitating downstream tasks such as player identification and summary generation.

## Docstring

### Summary
Enumerates the major professional leagues for a specified sport.

### Parameters

- **selected_sport** (str): The name of the sport for which to retrieve major professional leagues. Must be a non-empty string and match one of the supported sports.

### Returns

List[str]: A list of league names (strings) representing the top professional leagues associated with the input sport.

### Raises

- ValueError: Raised if `selected_sport` is an empty string or if the sport is not recognized in the internal league mapping.

### Examples

```python
>>> league_names = list_major_leagues(selected_sport="basketball")
["NBA", "EuroLeague", "NBL", "CBA", "Liga ACB"]
```

```python
>>> league_names = list_major_leagues(selected_sport="soccer")
["Premier League", "La Liga", "Bundesliga", "Serie A", "Ligue 1"]
```
