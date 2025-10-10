# _gather_sport_info - Complete PRD Documentation

## Overview
PRDs for nodes in the '_gather_sport_info' module.

## Table of Contents

- [validate_sport_name](#validate_sport_name)

- [fetch_sport_rules](#fetch_sport_rules)

- [get_popular_leagues](#get_popular_leagues)

- [get_major_tournaments](#get_major_tournaments)



---

## validate_sport_name

### Description
Validates a given sport name against a predefined list and returns the canonical form.

### Conceptual Info

The shim is responsible for ensuring that the sport name provided by the user or upstream nodes is recognized and mapped to a standard, canonical form before further processing. It acts as a gatekeeper, preventing invalid or misspelled sport names from propagating through the system.

### Docstring

**Summary:** Validate a sport name against a known list and return its canonical form.

**Parameters:**

- sport_name (str): The sport name to be validated. Can be a full name or abbreviation.
**Returns:** str - The canonical sport name that matches an entry in the supported sports list.

**Raises:**

- TypeError: Raised if sport_name is not a string.
- ValueError: Raised if sport_name does not match any known sport.
**Examples:**

```python
>>> validate_sport_name('soccer')
'Football'
```

```python
>>> validate_sport_name('basketball')
'Basketball'
```



---

## fetch_sport_rules

### Description
Fetches a list of key rules for a specified sport.

### Conceptual Info

The fetch_sport_rules shim obtains the primary rules for a given sport, enabling downstream components to provide accurate and comprehensive sport information.

### Docstring

**Summary:** Retrieve a list of key rules for the specified sport.

**Parameters:**

- sport (str): Name of the sport for which rules are requested (e.g., 'soccer', 'basketball').
**Returns:** list[str] - A list of strings, each describing a key rule that governs the specified sport.

**Raises:**

- ValueError: If the sport name is not recognized or not supported.
- TypeError: If the `sport` argument is not of type `str`.
**Examples:**

```python
>>> rules = fetch_sport_rules('basketball')
['3‑point line distance: 23.75 ft', 'Maximum team size: 5 players', 'Shot clock: 24 seconds']
```

```python
>>> fetch_sport_rules('unknown_sport')
ValueError: Unsupported sport name: unknown_sport
```



---

## get_popular_leagues

### Description
Returns a list of major professional leagues for a specified sport.

### Conceptual Info

The get_popular_leagues shim provides a standardized list of major professional leagues for a given sport, enabling higher‑level components to retrieve consistent league information without embedding domain knowledge directly.

### Docstring

**Summary:** Retrieve a list of prominent professional leagues for the specified sport.

**Parameters:**

- sport (str): The name of the sport for which to fetch popular leagues.
**Returns:** LIST_STR - A list of league names (strings) that are considered the most popular or influential within the specified sport.

**Raises:**

- ValueError: Raised when the provided sport name is not supported or cannot be matched to known sports.
- TypeError: Raised when the sport argument is not of type str.
**Examples:**

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



---

## get_major_tournaments

### Description
Retrieves a list of major international tournaments for a specified sport.

### Conceptual Info

This shim provides a bridge to the external data source that contains information about prominent international competitions for a sport, enabling the rest of the system to consume this data in a consistent format.

### Docstring

**Summary:** Return a list of major international tournaments for the specified sport.

**Parameters:**

- sport (str): Name of the sport for which to retrieve major tournaments.
**Returns:** list - A list of strings, each string being the name of a major tournament associated with the sport.

**Raises:**

- ValueError: Raised when the sport name is not recognized or supported.
- TypeError: Raised when the `sport` argument is not of type `str`.
**Examples:**

```python
>>> tournaments = get_major_tournaments('soccer')
['FIFA World Cup', 'UEFA Champions League', 'Copa América']
```

```python
>>> tournaments = get_major_tournaments('tennis')
['Wimbledon', 'French Open', 'US Open', 'Australian Open']
```

