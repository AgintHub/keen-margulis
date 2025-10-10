# summarize_sport_info PRD

## Description
Summarize the gathered information about the sport


## Conceptual Info

Creates a succinct, 200‑word or fewer summary of a sport, integrating its classification (team or individual), major professional leagues, and key active players.

## Docstring

### Summary
Generate a concise summary of a sport and return a structured dictionary with metadata.

### Parameters

- **sport_type** (str): Classification of the sport, e.g., "team-based" or "individual".
- **major_leagues** (List[str]): Names of the major professional leagues for the sport.
- **key_players** (List[str]): A list of 3–5 active players and their leagues (formatted as "Player – League").

### Returns

Dict[str, Any]: Dictionary containing sport_type (str), major_leagues (List[str]), key_players (List[str]), summary (str), and word_count (int).

### Raises

- ValueError: If the constructed summary exceeds 200 words.
- TypeError: If any input parameter is of an unexpected type.

### Examples

```python
>>> result = summarize_sport_info(
...     sport_type='team-based',
...     major_leagues=['NBA', 'EuroLeague'],
...     key_players=['LeBron James – NBA', 'Giannis Antetokounmpo – NBA']
>>> )
>>> print(result['summary'])
"Basketball is a team-based sport played worldwide, with major leagues such as the NBA and EuroLeague showcasing elite talent. Key players include LeBron James and Giannis Antetokounmpo, both stars of the NBA."
"word_count: 27"
```

```python
>>> summary_data = summarize_sport_info(
...     sport_type='team-based',
...     major_leagues=['Premier League', 'La Liga', 'Serie A'],
...     key_players=['Lionel Messi – La Liga', 'Cristiano Ronaldo – Serie A', 'Kevin De Bruyne – Premier League']
>>> )
>>> print(summary_data['summary'])
"Football (soccer) is a team-based sport with premier competitions including the Premier League, La Liga, and Serie A. Notable players feature Lionel Messi and Cristiano Ronaldo in top European clubs, along with Kevin De Bruyne."
"word_count: 31"
```
