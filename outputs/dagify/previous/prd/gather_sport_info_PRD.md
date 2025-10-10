# gather_sport_info PRD

## Description
Gather general information about the identified sport


## Conceptual Info

This node compiles core facts about a sport once its name is known, providing a structured set of rules, leagues, and tournaments.

## Docstring

### Summary
Gather general information about the identified sport.

### Parameters

- **selected_sport** (str): The name of the sport identified by the user, e.g., 'soccer', 'basketball', 'tennis'.

### Returns

dict: A dictionary with three keys:
  * rules (List[str]) – key rules governing the sport.
  * popular_leagues (List[str]) – major professional leagues.
  * major_tournaments (List[str]) – major international tournaments.

### Raises

- ValueError: If `selected_sport` is empty or not recognized in the knowledge base.

### Examples

```python
>>> gather_sport_info('soccer')
{
  'rules': [
    'Players may not use their hands except the goalkeeper.',
    'Each team has 11 players on the field.',
    'A match lasts 90 minutes with two 45‑minute halves.'
  ],
  'popular_leagues': [
    'Premier League',
    'La Liga',
    'Bundesliga',
    'Serie A'
  ],
  'major_tournaments': [
    'FIFA World Cup',
    'UEFA Champions League',
    'Copa América'
  ]
}
```

```python
>>> gather_sport_info('basketball')
{
  'rules': [
    'Each team has five players on the court.',
    'The game is played in four 12‑minute quarters.',
    'Players must advance the ball by dribbling or passing.'
  ],
  'popular_leagues': [
    'NBA',
    'EuroLeague',
    'NBL'
  ],
  'major_tournaments': [
    'NBA Finals',
    'FIBA World Cup',
    'Olympic Games Basketball' 
  ]
}
```
