# simple_sports_workflow - Complete PRD Documentation

## Overview
PRDs for nodes in the 'simple_sports_workflow' module.

## Table of Contents

- [determine_sport_type](#determine_sport_type)

- [gather_sport_info](#gather_sport_info)

- [identify_key_players](#identify_key_players)

- [identify_sport](#identify_sport)

- [list_major_leagues](#list_major_leagues)

- [summarize_sport_info](#summarize_sport_info)



---

## determine_sport_type

### Description
Determine if the sport is team-based or individual

### Conceptual Info

Classifies a sport as team-based or individual using a concise rationale.

### Docstring

**Summary:** Determines whether a sport is team-based or individual.

**Parameters:**

- selected_sport (str): The name of the sport identified by the parent node.
**Returns:** Dict[str, str] - A dictionary containing `sport_type` and `rationale` keys.

**Raises:**

- ValueError: If `selected_sport` is empty or not recognized.
**Examples:**

```python
>>> result = determine_sport_type('soccer')
>>> print(result['sport_type'])
>>> print(result['rationale'])
'team-based'
'Soccer is a team sport because each side fields 11 players who must coordinate to score goals.'
```

```python
>>> result = determine_sport_type('tennis')
>>> print(result['sport_type'])
>>> print(result['rationale'])
'individual'
'Tennis is played by one or two players competing against each other, making it an individual sport.'
```



---

## gather_sport_info

### Description
Gather general information about the identified sport

### Conceptual Info

This node compiles core facts about a sport once its name is known, providing a structured set of rules, leagues, and tournaments.

### Docstring

**Summary:** Gather general information about the identified sport.

**Parameters:**

- selected_sport (str): The name of the sport identified by the user, e.g., 'soccer', 'basketball', 'tennis'.
**Returns:** dict - A dictionary with three keys:
  * rules (List[str]) – key rules governing the sport.
  * popular_leagues (List[str]) – major professional leagues.
  * major_tournaments (List[str]) – major international tournaments.

**Raises:**

- ValueError: If `selected_sport` is empty or not recognized in the knowledge base.
**Examples:**

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



---

## identify_key_players

### Description
Identify key players in the sport

### Conceptual Info

This node selects a short list of currently active, top‑tier players for a given sport and maps each player to one of the sport's major professional leagues.

### Docstring

**Summary:** Retrieve 3–5 prominent active players for a specified sport along with the league each player belongs to.

**Parameters:**

- selected_sport (str): The sport for which key players should be identified (e.g., 'soccer', 'basketball').
- league_names (List[str]): A list of major professional leagues associated with the sport, obtained from the `list_major_leagues` node.
**Returns:** Tuple[List[str], List[str]] - A tuple containing two lists: the first list holds the names of 3‑5 key players, and the second list holds the corresponding league names for each player.

**Raises:**

- ValueError: Raised if the function cannot find at least three suitable players or if the input lists are empty.
**Examples:**

```python
>>> player_names, player_leagues = identify_key_players(
...     'soccer',
...     ['Premier League', 'La Liga', 'Serie A']
>>> )
(['Lionel Messi', 'Cristiano Ronaldo', 'Neymar Jr.'], ['Premier League', 'La Liga', 'Serie A'])
```

```python
>>> names, leagues = identify_key_players(
...     'basketball',
...     ['NBA', 'EuroLeague']
>>> )
(['LeBron James', 'Kevin Durant', 'Stephen Curry'], ['NBA', 'NBA', 'NBA'])
```



---

## identify_sport

### Description
Identify the sport of interest

### Conceptual Info

Collects user input to determine which sport to analyze, serving as the foundational data for all subsequent nodes in the sports workflow.

### Docstring

**Summary:** Prompts the user to specify a sport of interest and returns the selected sport name as a string.

**Returns:** str - The selected sport name.

**Raises:**

- ValueError: Raised if the user provides an empty or whitespace-only input.
**Examples:**

```python
>>> sport = identify_sport()
'soccer'
```

```python
>>> sport = identify_sport()
'basketball'
```



---

## list_major_leagues

### Description
List major professional leagues for the sport

### Conceptual Info

Retrieves a curated list of the most prominent professional leagues for a given sport, facilitating downstream tasks such as player identification and summary generation.

### Docstring

**Summary:** Enumerates the major professional leagues for a specified sport.

**Parameters:**

- selected_sport (str): The name of the sport for which to retrieve major professional leagues. Must be a non-empty string and match one of the supported sports.
**Returns:** List[str] - A list of league names (strings) representing the top professional leagues associated with the input sport.

**Raises:**

- ValueError: Raised if `selected_sport` is an empty string or if the sport is not recognized in the internal league mapping.
**Examples:**

```python
>>> league_names = list_major_leagues(selected_sport="basketball")
["NBA", "EuroLeague", "NBL", "CBA", "Liga ACB"]
```

```python
>>> league_names = list_major_leagues(selected_sport="soccer")
["Premier League", "La Liga", "Bundesliga", "Serie A", "Ligue 1"]
```



---

## summarize_sport_info

### Description
Summarize the gathered information about the sport

### Conceptual Info

Creates a succinct, 200‑word or fewer summary of a sport, integrating its classification (team or individual), major professional leagues, and key active players.

### Docstring

**Summary:** Generate a concise summary of a sport and return a structured dictionary with metadata.

**Parameters:**

- sport_type (str): Classification of the sport, e.g., "team-based" or "individual".
- major_leagues (List[str]): Names of the major professional leagues for the sport.
- key_players (List[str]): A list of 3–5 active players and their leagues (formatted as "Player – League").
**Returns:** Dict[str, Any] - Dictionary containing sport_type (str), major_leagues (List[str]), key_players (List[str]), summary (str), and word_count (int).

**Raises:**

- ValueError: If the constructed summary exceeds 200 words.
- TypeError: If any input parameter is of an unexpected type.
**Examples:**

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

