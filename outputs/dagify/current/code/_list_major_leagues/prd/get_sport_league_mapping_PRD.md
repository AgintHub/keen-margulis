# get_sport_league_mapping PRD

## Description
Retrieves a JSON string that maps sports names to lists of their major professional league identifiers.


## Conceptual Info

This shim provides a central, hard‑coded mapping of sports to their major professional leagues, enabling downstream nodes to retrieve league information without external API calls.

## Docstring

### Summary
Return a JSON string mapping each sport to its list of major league names.

### Returns

str: A JSON string representing a dictionary where keys are sport names (e.g., "soccer", "basketball") and values are lists of league names (e.g., ["Premier League", "La Liga"]).

### Raises

- ValueError: If the mapping cannot be constructed or is empty.
- RuntimeError: If an internal error occurs while generating the mapping.

### Examples

```python
>>> mapping_str = get_sport_league_mapping()
>>> print(mapping_str)
"{'soccer': ['Premier League', 'La Liga'], 'basketball': ['NBA'], 'baseball': ['MLB']}"
```

```python
>>> import json
>>> mapping = json.loads(get_sport_league_mapping())
>>> print(mapping['soccer'])
["Premier League", "La Liga"]
```
