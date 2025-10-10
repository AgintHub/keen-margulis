# _list_major_leagues - Complete PRD Documentation

## Overview
PRDs for nodes in the '_list_major_leagues' module.

## Table of Contents

- [validate_sport_input](#validate_sport_input)

- [get_sport_league_mapping](#get_sport_league_mapping)

- [retrieve_leagues_for_sport](#retrieve_leagues_for_sport)

- [curate_prominent_leagues](#curate_prominent_leagues)



---

## validate_sport_input

### Description
Validates and normalizes the sport name input, ensuring it matches supported sports before further processing.

### Conceptual Info

This shim ensures that any sport name passed into the system is valid and in a consistent format, acting as a gatekeeper before downstream operations.

### Docstring

**Summary:** Validate and normalize a sport name.

**Parameters:**

- sport_name (str): The sport name provided by the user, to be validated.
**Returns:** str - The validated and canonical sport name.

**Raises:**

- ValueError: Raised when sport_name is empty or does not match any supported sport.
- TypeError: Raised when sport_name is not a string.
**Examples:**

```python
>>> validate_sport_input('soccer')
'soccer'
```

```python
>>> validate_sport_input('')
ValueError: Sport name must not be empty.
```



---

## get_sport_league_mapping

### Description
Retrieves a JSON string that maps sports names to lists of their major professional league identifiers.

### Conceptual Info

This shim provides a central, hard‑coded mapping of sports to their major professional leagues, enabling downstream nodes to retrieve league information without external API calls.

### Docstring

**Summary:** Return a JSON string mapping each sport to its list of major league names.

**Returns:** str - A JSON string representing a dictionary where keys are sport names (e.g., "soccer", "basketball") and values are lists of league names (e.g., ["Premier League", "La Liga"]).

**Raises:**

- ValueError: If the mapping cannot be constructed or is empty.
- RuntimeError: If an internal error occurs while generating the mapping.
**Examples:**

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



---

## retrieve_leagues_for_sport

### Description
Returns the list of major league names for a given sport using a provided mapping dictionary.

### Conceptual Info

This shim provides the core lookup logic for mapping a sport name to its major professional leagues. It decouples the lookup from higher‑level orchestration and allows the mapping dictionary to be supplied by configuration or a separate node.

### Docstring

**Summary:** Retrieves a list of league names for the given sport based on a mapping dictionary.

**Parameters:**

- sport (str): The name of the sport to look up, e.g., "soccer".
- mapping (dict): A dictionary where keys are sport names and values are lists of league names.
**Returns:** List[str] - A list of league names corresponding to the requested sport.

**Raises:**

- ValueError: Raised if the sport is not present in the mapping dictionary.
- TypeError: Raised if sport is not a string or mapping is not a dict.
**Examples:**

```python
>>> mapping = {
...     "soccer": ["Premier League", "La Liga"],
...     "basketball": ["NBA", "EuroLeague"],
>>> }
>>> print(retrieve_leagues_for_sport("soccer", mapping))
["Premier League", "La Liga"]
```

```python
>>> try:
...     retrieve_leagues_for_sport("cricket", mapping)
>>> except ValueError as e:
...     print(str(e))
"Sport 'cricket' not found in mapping dictionary."
```



---

## curate_prominent_leagues

### Description
Curates a list of prominent leagues for a given sport from an input list of leagues.

### Conceptual Info

The shim function `curate_prominent_leagues` refines a raw list of sports leagues by applying prominence rules specific to the sport, producing a concise list of leagues that are considered major or flagship for that sport.

### Docstring

**Summary:** Curates a list of prominent leagues for the specified sport from a given list of league names.

**Parameters:**

- leagues (List[str]): A list of league names (strings) to be curated.
- sport (str): The name of the sport for which prominence rules should be applied.
**Returns:** List[str] - A list of league names that are considered prominent for the given sport.

**Raises:**

- ValueError: Raised if `sport` is not recognized or if no prominent leagues can be identified.
- TypeError: Raised if `leagues` is not a list of strings or if `sport` is not a string.
**Examples:**

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

