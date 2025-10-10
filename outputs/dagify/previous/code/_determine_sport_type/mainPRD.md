# _determine_sport_type - Complete PRD Documentation

## Overview
PRDs for nodes in the '_determine_sport_type' module.

## Table of Contents

- [validate_sport_input](#validate_sport_input)

- [analyze_sport_characteristics](#analyze_sport_characteristics)

- [classify_sport_type](#classify_sport_type)

- [generate_classification_rationale](#generate_classification_rationale)



---

## validate_sport_input

### Description
Validates a sport name against a predefined list of supported sports and returns the standardized sport name.

### Conceptual Info

This shim ensures that only known sports are propagated through the system, preventing downstream errors and normalizing input for consistent processing.

### Docstring

**Summary:** Validates the input sport name against a list of supported sports and returns the canonical name.

**Parameters:**

- sport_name (str): The sport name to validate. Must be a non-empty string.
**Returns:** str - The validated sport name in lowercase, matching one of the supported sports.

**Raises:**

- TypeError: If sport_name is not of type str.
- ValueError: If sport_name is not found in the list of supported sports.
**Examples:**

```python
>>> result = validate_sport_input("soccer")
>>> print(result)
'soccer'
```

```python
>>> validate_sport_input("unknown_sport")
ValueError: "'unknown_sport' is not a supported sport name."
```



---

## analyze_sport_characteristics

### Description
Analyzes a validated sport name and returns a JSON string describing key characteristics used for classification.

### Conceptual Info

Provides structured sport data required for determining whether a sport is team-based or individual and for generating a rationale.

### Docstring

**Summary:** Analyzes a validated sport name and returns a JSON string of its key characteristics.

**Parameters:**

- sport (str): A non-empty, validated string containing the name of the sport to analyze.
**Returns:** str - A JSON-formatted string representing a dictionary with keys such as sport_name, team_based, players_per_side, field_type, equipment, and governing_body.

**Raises:**

- ValueError: Raised if the provided sport name is empty or unrecognized.
- TypeError: Raised if the input is not a string.
**Examples:**

```python
>>> analyze_sport_characteristics('soccer')
"{\"sport_name\": \"soccer\", \"team_based\": true, \"players_per_side\": 11, \"field_type\": \"field\", \"equipment\": [\"ball\", \"goal\"], \"governing_body\": \"FIFA\"}"
```

```python
>>> analyze_sport_characteristics('archery')
"{\"sport_name\": \"archery\", \"team_based\": false, \"players_per_side\": 1, \"field_type\": \"outdoor\", \"equipment\": [\"bow\", \"arrow\"], \"governing_body\": \"World Archery Federation\"}"
```



---

## classify_sport_type

### Description
Classifies a sport as team-based or individual based on its characteristics.

### Conceptual Info

Shim to determine sport type classification based on extracted characteristics.

### Docstring

**Summary:** Classifies a sport as either team-based or individual based on provided characteristics.

**Parameters:**

- characteristics (dict): Dictionary containing sport characteristics such as team_size, individual_ranking, or other relevant attributes.
**Returns:** str - Either 'team' or 'individual' indicating the sport type.

**Raises:**

- ValueError: Raised when required characteristics are missing or contain invalid values.
- TypeError: Raised when the input is not a dictionary.
**Examples:**

```python
>>> classify_sport_type({'team_size': 'large', 'individual_ranking': False})
'team'
```

```python
>>> classify_sport_type({'team_size': 'none', 'individual_ranking': True})
'individual'
```



---

## generate_classification_rationale

### Description
Generates a concise one‑sentence rationale explaining why a given sport is classified as team‑based or individual.

### Conceptual Info

In the larger system, this shim is responsible for converting structured sport data into an explanatory sentence that can be displayed to users or used for auditing the classification logic.

### Docstring

**Summary:** Generate a concise justification for classifying a sport as team-based or individual.

**Parameters:**

- sport (str): The name of the sport (e.g., 'Soccer').
- sport_type (str): The classification of the sport, expected values are 'team-based' or 'individual'.
- characteristics (dict): A dictionary of sport characteristics such as 'team', 'players_per_side', etc.
**Returns:** str - A single‑sentence rationale explaining the classification.

**Raises:**

- ValueError: If `sport_type` is not 'team-based' or 'individual', or if required keys are missing from `characteristics`.
- TypeError: If any argument is not of the expected type.
**Examples:**

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

