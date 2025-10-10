# get_major_tournaments PRD

## Description
Retrieves a list of major international tournaments for a specified sport.


## Conceptual Info

This shim provides a bridge to the external data source that contains information about prominent international competitions for a sport, enabling the rest of the system to consume this data in a consistent format.

## Docstring

### Summary
Return a list of major international tournaments for the specified sport.

### Parameters

- **sport** (str): Name of the sport for which to retrieve major tournaments.

### Returns

list: A list of strings, each string being the name of a major tournament associated with the sport.

### Raises

- ValueError: Raised when the sport name is not recognized or supported.
- TypeError: Raised when the `sport` argument is not of type `str`.

### Examples

```python
>>> tournaments = get_major_tournaments('soccer')
['FIFA World Cup', 'UEFA Champions League', 'Copa América']
```

```python
>>> tournaments = get_major_tournaments('tennis')
['Wimbledon', 'French Open', 'US Open', 'Australian Open']
```
