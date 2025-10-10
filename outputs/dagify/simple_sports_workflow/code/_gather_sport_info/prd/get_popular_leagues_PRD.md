# get_popular_leagues PRD

## Description
Returns a list of major professional leagues for a specified sport.


## Conceptual Info

The get_popular_leagues shim provides a standardized list of major professional leagues for a given sport, enabling higher‑level components to retrieve consistent league information without embedding domain knowledge directly.

## Docstring

### Summary
Retrieve a list of prominent professional leagues for the specified sport.

### Parameters

- **sport** (str): The name of the sport for which to fetch popular leagues.

### Returns

LIST_STR: A list of league names (strings) that are considered the most popular or influential within the specified sport.

### Raises

- ValueError: Raised when the provided sport name is not supported or cannot be matched to known sports.
- TypeError: Raised when the sport argument is not of type str.

### Examples

```python
>>> leagues = get_popular_leagues('soccer')
>>> print(leagues)
['Premier League', 'La Liga', 'Bundesliga']
```

```python
>>> leagues = get_popular_leagues('basketball')
>>> print(leagues)
['NBA', 'EuroLeague', 'NBL']
```
