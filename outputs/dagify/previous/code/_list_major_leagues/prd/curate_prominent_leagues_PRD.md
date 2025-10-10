# curate_prominent_leagues PRD

## Description
Curates a list of prominent leagues for a given sport from an input list of leagues.


## Conceptual Info

The shim function `curate_prominent_leagues` refines a raw list of sports leagues by applying prominence rules specific to the sport, producing a concise list of leagues that are considered major or flagship for that sport.

## Docstring

### Summary
Curates a list of prominent leagues for the specified sport from a given list of league names.

### Parameters

- **leagues** (List[str]): A list of league names (strings) to be curated.
- **sport** (str): The name of the sport for which prominence rules should be applied.

### Returns

List[str]: A list of league names that are considered prominent for the given sport.

### Raises

- ValueError: Raised if `sport` is not recognized or if no prominent leagues can be identified.
- TypeError: Raised if `leagues` is not a list of strings or if `sport` is not a string.

### Examples

```python
>>> leagues = ['NBA', 'NCAA', 'WNBA', 'EuroLeague']
>>> sport = 'Basketball'
>>> curated = curate_prominent_leagues(leagues=leagues, sport=sport)
>>> print(curated)
['NBA', 'EuroLeague']
```

```python
>>> leagues = ['Premier League', 'Champions League', 'FA Cup']
>>> sport = 'Football'
>>> curated = curate_prominent_leagues(leagues=leagues, sport=sport)
>>> print(curated)
['Premier League', 'Champions League']
```
