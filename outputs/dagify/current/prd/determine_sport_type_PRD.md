# determine_sport_type PRD

## Description
Determine if the sport is team-based or individual


## Conceptual Info

Classifies a sport as team-based or individual using a concise rationale.

## Docstring

### Summary
Determines whether a sport is team-based or individual.

### Parameters

- **selected_sport** (str): The name of the sport identified by the parent node.

### Returns

Dict[str, str]: A dictionary containing `sport_type` and `rationale` keys.

### Raises

- ValueError: If `selected_sport` is empty or not recognized.

### Examples

```python
>>> result = determine_sport_type('soccer')
>>> print(result['sport_type'])
>>> print(result['rationale'])
'team-based'
'Soccer is a team sport because each side fields 11 players who must coordinate to score goals.'
```

```python
>>> result = determine_sport_type('tennis')
>>> print(result['sport_type'])
>>> print(result['rationale'])
'individual'
'Tennis is played by one or two players competing against each other, making it an individual sport.'
```
