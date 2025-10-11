# _gather_historical_game_data - Complete PRD Documentation

## Overview
PRDs for nodes in the '_gather_historical_game_data' module.

## Table of Contents

- [identify_fsu_basketball_data_sources](#identify_fsu_basketball_data_sources)

- [fetch_historical_game_records](#fetch_historical_game_records)

- [validate_game_data_integrity](#validate_game_data_integrity)

- [extract_game_dates](#extract_game_dates)

- [extract_opponent_names](#extract_opponent_names)

- [format_game_scores](#format_game_scores)

- [compile_game_statistics](#compile_game_statistics)



---

## identify_fsu_basketball_data_sources

### Description
Identifies data sources for Florida State University basketball historical game data.

### Conceptual Info

This shim function is responsible for identifying relevant data sources for Florida State University basketball historical game data. It serves as a crucial step in gathering the necessary data for further processing and analysis.

### Docstring

**Summary:** Identifies and returns a list of data sources for FSU basketball historical game data.

**Returns:** List[str] - A list of strings representing the identified data sources for FSU basketball historical game data.

**Raises:**

- RuntimeError: If unable to identify any data sources.
**Examples:**

```python
>>> data_sources = identify_fsu_basketball_data_sources()
['https://example.com/fsu-basketball-data', 'https://another-source.com/fsu-games']
```



---

## fetch_historical_game_records

### Description
Fetches historical game records for a specified team from given data sources.

### Conceptual Info

This shim node is responsible for retrieving historical game data for a specified team from various data sources. It plays a crucial role in the data gathering pipeline for sports analytics.

### Docstring

**Summary:** Fetches historical game records for a given team from specified data sources.

**Parameters:**

- sources (str): Comma-separated list of data sources to fetch historical game records from.
- team (str): Name of the team for which to fetch historical game records.
**Returns:** List[dict] - List of dictionaries where each dictionary represents a historical game record.

**Raises:**

- ValueError: If the input sources or team name is invalid or empty.
- TypeError: If the input types for sources or team are not strings.
**Examples:**

```python
>>> fetch_historical_game_records(sources='source1,source2', team='FSU')
[{'date': '2022-01-01', 'opponent': 'TeamA', 'score': '80-70'}, {'date': '2022-01-03', 'opponent': 'TeamB', 'score': '90-85'}]
```

```python
>>> fetch_historical_game_records(sources='sports_db', team='UF')
[{'date': '2022-02-01', 'opponent': 'TeamC', 'score': '70-60'}]
```



---

## validate_game_data_integrity

### Description
Validates the integrity of raw game data to ensure it is accurate and consistent.

### Conceptual Info

This shim validates raw game data to ensure its integrity and accuracy before it is used for further processing.

### Docstring

**Summary:** Validates the integrity of raw game data to ensure it is accurate and consistent.

**Parameters:**

- raw_data (str): Raw game data in string format that needs to be validated.
**Returns:** List[dict] - List of dictionaries containing the validated game data, where each dictionary represents a game with relevant statistics and information.

**Raises:**

- ValueError: If the input raw data is malformed or cannot be parsed into a list of dictionaries.
- TypeError: If the input raw data is not of type string.
**Examples:**

```python
>>> raw_game_data = '[{"game_id": 1, "score": "74-68"}, {"game_id": 2, "score": "80-75"}]'
>>> validated_data = validate_game_data_integrity(raw_data=raw_game_data)
[{'game_id': 1, 'score': '74-68'}, {'game_id': 2, 'score': '80-75'}]
```

```python
>>> raw_game_data = '[{"game_id": 1}, {"score": "80-75"}]'
>>> validated_data = validate_game_data_integrity(raw_data=raw_game_data)
ValueError: Input raw data is malformed or missing required fields.
```



---

## extract_game_dates

### Description
Extracts a list of game dates from a given list of game records.

### Conceptual Info

This shim function is designed to extract game dates from a list of game records, playing a crucial role in data processing for historical game data analysis.

### Docstring

**Summary:** Extracts game dates from a list of game records represented as a string.

**Parameters:**

- games (str): A string representation of a list of game records.
**Returns:** List[str] - A list of game dates in string format.

**Raises:**

- ValueError: If the input string is not a valid representation of game records.
- TypeError: If the input is not of type string.
**Examples:**

```python
>>> games = '[{"date": "2022-01-01"}, {"date": "2022-01-15"}]'
>>> extract_game_dates(games=games)
['2022-01-01', '2022-01-15']
```

```python
>>> games = '[{"date": "2023-02-01"}, {"date": "2023-03-01"}]'
>>> extract_game_dates(games=games)
['2023-02-01', '2023-03-01']
```



---

## extract_opponent_names

### Description
Extracts a list of opponent names from the provided games data.

### Conceptual Info

This shim function is designed to extract opponent names from a given string of games data, playing a crucial role in data processing for historical game analysis.

### Docstring

**Summary:** Extracts opponent names from the provided games data string.

**Parameters:**

- games (str): A string representing the games data from which opponent names will be extracted.
**Returns:** List[str] - A list of strings representing the names of opponents extracted from the input games data.

**Raises:**

- ValueError: If the input games data is not in the expected format or is empty.
- TypeError: If the input games data is not a string.
**Examples:**

```python
>>> extract_opponent_names(games='[{\"opponent\": \"Team A\"}, {\"opponent\": \"Team B\"}]')
['Team A', 'Team B']
```

```python
>>> extract_opponent_names(games='[{\"opponent\": \"Team C\"}]')
['Team C']
```



---

## format_game_scores

### Description
Formats game scores from a list of game records into a list of score strings.

### Conceptual Info

This shim node is responsible for taking game records, extracting the scores, and formatting them into a standardized list of strings.

### Docstring

**Summary:** Formats game scores from a list of game records into a list of score strings.

**Parameters:**

- games (str): A string representation of game records, expected to be a JSON-like structure containing game information including scores.
**Returns:** List[str] - A list of strings where each string represents a formatted game score (e.g., '74-68').

**Raises:**

- ValueError: If the input string cannot be parsed into a valid game record structure.
- TypeError: If the input is not a string.
**Examples:**

```python
>>> games = '[{"score": "74-68"}, {"score": "80-75"}]'
>>> format_game_scores(games=games)
['74-68', '80-75']
```

```python
>>> games = '[{"score": "60-70"}]'
>>> format_game_scores(games=games)
['60-70']
```



---

## compile_game_statistics

### Description
Compiles game statistics from a list of validated game data into a list of strings.

### Conceptual Info

This shim node is responsible for compiling game statistics from a list of validated game data. It takes in a string representation of the game data and outputs a list of strings representing the compiled game statistics.

### Docstring

**Summary:** Compiles game statistics from input game data.

**Parameters:**

- games (str): A string representation of validated game data.
**Returns:** List[str] - A list of strings where each string represents compiled game statistics.

**Raises:**

- ValueError: If the input game data is not in the expected format.
- TypeError: If the input is not a string.
**Examples:**

```python
>>> compile_game_statistics(games='[{\"score\": \"74-68\", \"stats\": {\"rebounds\": 40, \"turnovers\": 15}}]')
['Rebounds: 40', 'Turnovers: 15']
```

```python
>>> compile_game_statistics(games='[{\"score\": \"90-85\", \"stats\": {\"rebounds\": 45, \"turnovers\": 12}}]')
['Rebounds: 45', 'Turnovers: 12']
```

