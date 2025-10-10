# validate_input_types PRD

## Description
Validate that the provided Pydantic model instances match their expected types before processing.


## Conceptual Info

This shim ensures that all inputs to downstream processing functions are correctly typed Pydantic models, preventing runtime type errors and maintaining data integrity.

## Docstring

### Summary
Validate that the provided inputs are instances of their expected Pydantic models and raise appropriate errors if not.

### Parameters

- **gather_sport_info_input** (GatherSportInfoOutput): Instance of GatherSportInfoOutput containing sport rules, popular leagues, and major tournaments.
- **determine_sport_type_input** (DetermineSportTypeOutput): Instance of DetermineSportTypeOutput containing the sport type and rationale.
- **list_major_leagues_input** (ListMajorLeaguesOutput): Instance of ListMajorLeaguesOutput containing a list of major league names.
- **identify_key_players_input** (IdentifyKeyPlayersOutput): Instance of IdentifyKeyPlayersOutput containing key player names and their leagues.

### Returns

str: Returns an empty string on successful validation.

### Raises

- TypeError: Raised if any input argument is not an instance of its expected Pydantic model class.
- ValueError: Raised if any required attribute is missing or has an incorrect type within a provided model.

### Examples

```python
>>> from pydantic import BaseModel, Field
>>> from typing import List
>>> class GatherSportInfoOutput(BaseModel):
...     rules: List[str] = Field(...)
...     popular_leagues: List[str] = Field(...)
...     major_tournaments: List[str] = Field(...)
>>> class DetermineSportTypeOutput(BaseModel):
...     sport_type: str = Field(...)
...     rationale: str = Field(...)
>>> class ListMajorLeaguesOutput(BaseModel):
...     league_names: List[str] = Field(...)
>>> class IdentifyKeyPlayersOutput(BaseModel):
...     player_names: List[str] = Field(...)
...     player_leagues: List[str] = Field(...)
>>> validate_input_types(
...     gather_sport_info_input=GatherSportInfoOutput(rules=['rule1'], popular_leagues=['league1'], major_tournaments=['tourn1']),
...     determine_sport_type_input=DetermineSportTypeOutput(sport_type='team', rationale='teams play together'),
...     list_major_leagues_input=ListMajorLeaguesOutput(league_names=['league1']),
...     identify_key_players_input=IdentifyKeyPlayersOutput(player_names=['player1'], player_leagues=['league1'])
>>> )
""
```

```python
>>> validate_input_types(
...     gather_sport_info_input={'rules': ['rule1']},  # Wrong type
...     determine_sport_type_input=DetermineSportTypeOutput(sport_type='team', rationale='teams play together'),
...     list_major_leagues_input=ListMajorLeaguesOutput(league_names=['league1']),
...     identify_key_players_input=IdentifyKeyPlayersOutput(player_names=['player1'], player_leagues=['league1'])
>>> )
"TypeError: gather_sport_info_input must be an instance of GatherSportInfoOutput"
```
