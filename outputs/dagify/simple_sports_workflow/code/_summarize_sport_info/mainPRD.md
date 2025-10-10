# _summarize_sport_info - Complete PRD Documentation

## Overview
PRDs for nodes in the '_summarize_sport_info' module.

## Table of Contents

- [validate_input_types](#validate_input_types)

- [format_players_with_leagues](#format_players_with_leagues)

- [generate_sport_summary](#generate_sport_summary)

- [count_words](#count_words)

- [validate_word_count_limit](#validate_word_count_limit)



---

## validate_input_types

### Description
Validate that the provided Pydantic model instances match their expected types before processing.

### Conceptual Info

This shim ensures that all inputs to downstream processing functions are correctly typed Pydantic models, preventing runtime type errors and maintaining data integrity.

### Docstring

**Summary:** Validate that the provided inputs are instances of their expected Pydantic models and raise appropriate errors if not.

**Parameters:**

- gather_sport_info_input (GatherSportInfoOutput): Instance of GatherSportInfoOutput containing sport rules, popular leagues, and major tournaments.
- determine_sport_type_input (DetermineSportTypeOutput): Instance of DetermineSportTypeOutput containing the sport type and rationale.
- list_major_leagues_input (ListMajorLeaguesOutput): Instance of ListMajorLeaguesOutput containing a list of major league names.
- identify_key_players_input (IdentifyKeyPlayersOutput): Instance of IdentifyKeyPlayersOutput containing key player names and their leagues.
**Returns:** str - Returns an empty string on successful validation.

**Raises:**

- TypeError: Raised if any input argument is not an instance of its expected Pydantic model class.
- ValueError: Raised if any required attribute is missing or has an incorrect type within a provided model.
**Examples:**

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



---

## format_players_with_leagues

### Description
Formats player names with their respective leagues into a list of strings.

### Conceptual Info

This shim takes two comma‑separated strings—player names and corresponding leagues—and produces a list of strings pairing each player with their league. It is used to transform raw API output into a user‑friendly format for summaries.

### Docstring

**Summary:** Return a list of strings pairing each player name with its league.

**Parameters:**

- player_names (str): Comma‑separated list of player names. Leading/trailing whitespace around each name is ignored.
- player_leagues (str): Comma‑separated list of leagues corresponding to each player. Leading/trailing whitespace around each league is ignored.
**Returns:** List[str] - A list where each element is formatted as ``"<Player> (<League>)"``. The order matches the input order.

**Raises:**

- ValueError: Raised if the number of player names does not equal the number of leagues.
- TypeError: Raised if either argument is not a string.
**Examples:**

```python
>>> format_players_with_leagues('LeBron James,Stephen Curry', 'NBA,NBA')
["LeBron James (NBA)", "Stephen Curry (NBA)"]
```

```python
>>> format_players_with_leagues('Lionel Messi', 'La Liga')
["Lionel Messi (La Liga)"]
```



---

## generate_sport_summary

### Description
Generates a concise summary of a sport based on its type, major leagues, key players, rules, and tournaments.

### Conceptual Info

This shim encapsulates the logic for synthesizing structured sport data into a readable, concise paragraph suitable for display or further processing.

### Docstring

**Summary:** Generate a concise, up‑to‑200‑word summary of a sport based on its type, major leagues, key players, rules, and tournaments.

**Parameters:**

- sport_type (str): Indicates whether the sport is team‑based or individual.
- major_leagues (List[str]): List of major professional leagues associated with the sport.
- key_players (List[str]): List of 3‑5 key players, each formatted with their league (e.g., "LeBron James (NBA)").
- sport_rules (List[str]): Key rules governing the sport.
- tournaments (List[str]): Major international tournaments or competitions for the sport.
**Returns:** str - A single paragraph summary not exceeding 200 words.

**Raises:**

- ValueError: If any input list is empty or if `sport_type` is not "Team" or "Individual".
- TypeError: If any input is of an incorrect type.
**Examples:**

```python
>>> summary = generate_sport_summary(
...     sport_type='Team',
...     major_leagues=['NBA', 'EuroLeague'],
...     key_players=['LeBron James (NBA)', 'Luka Dončić (EuroLeague)'],
...     sport_rules=['Each team has 5 players', 'Shot clock 24 seconds'],
...     tournaments=['NBA Finals', 'EuroLeague Final Four']
>>> )
>>> print(summary)
"The sport is team-based, featuring major leagues such as the NBA and EuroLeague. Key players include LeBron James (NBA) and Luka Dončić (EuroLeague). Rules emphasize a 5‑player lineup and a 24‑second shot clock. Major tournaments are the NBA Finals and EuroLeague Final Four."
```

```python
>>> summary = generate_sport_summary(
...     sport_type='Individual',
...     major_leagues=['ATP', 'Grand Slam'],
...     key_players=['Novak Djokovic (ATP)', 'Rafael Nadal (ATP)'],
...     sport_rules=['Matches are best of 3 sets', 'Tie‑break at 6‑6'],
...     tournaments=['Wimbledon', 'US Open']
>>> )
>>> print(summary)
"The sport is individual, featuring major leagues like the ATP and Grand Slam tournaments. Key players include Novak Djokovic (ATP) and Rafael Nadal (ATP). Rules include best‑of‑3 sets and tie‑breaks at 6‑6. Major tournaments are Wimbledon and the US Open."
```



---

## count_words

### Description
Counts the number of words in a given text string.

### Conceptual Info

The count_words shim encapsulates a simple word counting operation that can be reused by other nodes in the data pipeline, ensuring consistent and testable behavior for text metrics.

### Docstring

**Summary:** Return the total number of words contained in the input string.

**Parameters:**

- text (str): The text to be analyzed. Must be a non-empty string.
**Returns:** int - An integer representing the number of words in `text`. Words are sequences of characters separated by whitespace.

**Raises:**

- TypeError: Raised if `text` is not of type `str`.
- ValueError: Raised if `text` is an empty string or contains only whitespace.
**Examples:**

```python
>>> count_words('Hello world')
2
```

```python
>>> count_words('This is a test.')
4
```



---

## validate_word_count_limit

### Description
Checks that a summary word count does not exceed a specified maximum and raises an error if it does.

### Conceptual Info

This shim ensures that generated summaries stay within a predefined word count, helping to maintain consistency and compliance with downstream constraints.

### Docstring

**Summary:** Validates that the provided word count does not exceed the maximum limit, raising a ValueError if the limit is exceeded.

**Parameters:**

- word_count (int): Current number of words in the generated summary.
- max_words (int): Maximum number of words allowed for the summary.
**Returns:** str - A message confirming successful validation, e.g. "Word count within limit (150/200)."

**Raises:**

- ValueError: Raised when word_count exceeds max_words.
- TypeError: Raised when word_count or max_words is not an integer.
**Examples:**

```python
>>> validate_word_count_limit(word_count=150, max_words=200)
'Word count within limit (150/200).'
```

```python
>>> validate_word_count_limit(word_count=250, max_words=200)
ValueError: 'Word count 250 exceeds maximum allowed 200.'
```

