# classify_sport_type PRD

## Description
Classifies a sport as team-based or individual based on its characteristics.


## Conceptual Info

Shim to determine sport type classification based on extracted characteristics.

## Docstring

### Summary
Classifies a sport as either team-based or individual based on provided characteristics.

### Parameters

- **characteristics** (dict): Dictionary containing sport characteristics such as team_size, individual_ranking, or other relevant attributes.

### Returns

str: Either 'team' or 'individual' indicating the sport type.

### Raises

- ValueError: Raised when required characteristics are missing or contain invalid values.
- TypeError: Raised when the input is not a dictionary.

### Examples

```python
>>> classify_sport_type({'team_size': 'large', 'individual_ranking': False})
'team'
```

```python
>>> classify_sport_type({'team_size': 'none', 'individual_ranking': True})
'individual'
```
