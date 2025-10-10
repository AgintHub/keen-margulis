# generate_sport_summary PRD

## Description
Generates a concise summary of a sport based on its type, major leagues, key players, rules, and tournaments.


## Conceptual Info

This shim encapsulates the logic for synthesizing structured sport data into a readable, concise paragraph suitable for display or further processing.

## Docstring

### Summary
Generate a concise, up‑to‑200‑word summary of a sport based on its type, major leagues, key players, rules, and tournaments.

### Parameters

- **sport_type** (str): Indicates whether the sport is team‑based or individual.
- **major_leagues** (List[str]): List of major professional leagues associated with the sport.
- **key_players** (List[str]): List of 3‑5 key players, each formatted with their league (e.g., "LeBron James (NBA)").
- **sport_rules** (List[str]): Key rules governing the sport.
- **tournaments** (List[str]): Major international tournaments or competitions for the sport.

### Returns

str: A single paragraph summary not exceeding 200 words.

### Raises

- ValueError: If any input list is empty or if `sport_type` is not "Team" or "Individual".
- TypeError: If any input is of an incorrect type.

### Examples

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
