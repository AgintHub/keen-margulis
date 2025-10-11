# _extract_player_statistics - Complete PRD Documentation

## Overview
PRDs for nodes in the '_extract_player_statistics' module.

## Table of Contents

- [validate_input_lists_length](#validate_input_lists_length)

- [validate_input_data_types](#validate_input_data_types)

- [parse_game_statistics](#parse_game_statistics)

- [aggregate_player_statistics](#aggregate_player_statistics)

- [extract_player_names](#extract_player_names)

- [extract_points_scored](#extract_points_scored)

- [extract_rebounds](#extract_rebounds)

- [extract_assists](#extract_assists)



---

## validate_input_lists_length

### Description
Validates that input lists have the same length.

### Conceptual Info

This shim function validates that the input lists (game_dates, opponents, scores, game_statistics) have the same length, ensuring data consistency before further processing.

### Docstring

**Summary:** Validates the lengths of input lists to ensure they are consistent.

**Parameters:**

- game_dates (str): A list of game dates in string format, expected to be comma-separated or another consistent delimiter.
- opponents (str): A list of opponents in string format, expected to be comma-separated or another consistent delimiter.
- scores (str): A list of game scores in string format, expected to be comma-separated or another consistent delimiter.
- game_statistics (str): A list of game statistics in string format, expected to be comma-separated or another consistent delimiter.
**Returns:** str - A success message if all input lists have the same length, otherwise an error message.

**Raises:**

- ValueError: When the input lists do not have the same length.
- TypeError: When the input types are not as expected (e.g., not strings or not properly formatted lists).
**Examples:**

```python
>>> validate_input_lists_length(game_dates='2022-01-01,2022-01-02', opponents='TeamA,TeamB', scores='10-5,8-7', game_statistics='stats1,stats2')
'Success: All input lists have the same length.'
```

```python
>>> validate_input_lists_length(game_dates='2022-01-01,2022-01-02', opponents='TeamA', scores='10-5,8-7', game_statistics='stats1,stats2')
'Error: Input lists do not have the same length.'
```



---

## validate_input_data_types

### Description
Validates the data types of input parameters game_dates, opponents, scores, and game_statistics.

### Conceptual Info

This shim node is responsible for validating the data types of the input parameters game_dates, opponents, scores, and game_statistics to ensure they are of the expected type.

### Docstring

**Summary:** Validates the input data types for game_dates, opponents, scores, and game_statistics.

**Parameters:**

- game_dates (str): A string representing the list of game dates.
- opponents (str): A string representing the list of opponents.
- scores (str): A string representing the list of game scores.
- game_statistics (str): A string representing the list of game statistics.
**Returns:** str - A string indicating the result of the validation.

**Raises:**

- TypeError: If any of the input parameters are not of the expected type.
- ValueError: If the input parameters contain invalid data.
**Examples:**

```python
>>> validate_input_data_types(game_dates='2022-01-01', opponents='Team A', scores='10-5', game_statistics='stats')
>>> print(output)
'Validation successful'
```

```python
>>> validate_input_data_types(game_dates=123, opponents='Team A', scores='10-5', game_statistics='stats')
>>> print(output)
'TypeError: game_dates must be a string'
```



---

## parse_game_statistics

### Description
Parses game statistics from a list of strings into a list of dictionaries.

### Conceptual Info

This shim node is responsible for parsing game statistics from a list of strings into a structured format (list of dictionaries) that can be further processed by downstream nodes.

### Docstring

**Summary:** Parses game statistics from a list of strings into a list of dictionaries.

**Parameters:**

- game_statistics (str): A list of game statistics in string format that need to be parsed.
**Returns:** List[dict] - A list of dictionaries where each dictionary contains the parsed game statistics.

**Raises:**

- ValueError: If the input game statistics are not in the expected format.
- TypeError: If the input is not a list of strings.
**Examples:**

```python
>>> game_statistics = ['team:A,points:100,rebounds:50', 'team:B,points:90,rebounds:40']
>>> parse_game_statistics(game_statistics=game_statistics)
[{'team': 'A', 'points': '100', 'rebounds': '50'}, {'team': 'B', 'points': '90', 'rebounds': '40'}]
```

```python
>>> game_statistics = ['player:X,score:85,assists:7', 'player:Y,score:75,assists:5']
>>> parse_game_statistics(game_statistics=game_statistics)
[{'player': 'X', 'score': '85', 'assists': '7'}, {'player': 'Y', 'score': '75', 'assists': '5'}]
```



---

## aggregate_player_statistics

### Description
Aggregates player statistics from a list of parsed game statistics into a comprehensive dictionary.

### Conceptual Info

This shim aggregates individual game statistics into a comprehensive summary for each player, facilitating further analysis.

### Docstring

**Summary:** Aggregates player statistics from a list of game statistics.

**Parameters:**

- parsed_stats (str): A list of dictionaries where each dictionary contains game statistics for a player.
**Returns:** str - A dictionary where keys are player names and values are dictionaries of aggregated statistics.

**Raises:**

- ValueError: If the input list is empty or if the dictionaries do not contain valid statistic data.
- TypeError: If the input is not a list or if the elements are not dictionaries.
**Examples:**

```python
>>> parsed_stats = [{'player': 'John', 'points': 10, 'rebounds': 5},
...              {'player': 'Jane', 'points': 15, 'rebounds': 3},
...              {'player': 'John', 'points': 12, 'rebounds': 4}]
>>> aggregate_player_statistics(parsed_stats=parsed_stats)
{'John': {'points': 22, 'rebounds': 9}, 'Jane': {'points': 15, 'rebounds': 3}}
```

```python
>>> parsed_stats = [{'player': 'Alice', 'assists': 7}, {'player': 'Bob', 'assists': 5}]
>>> aggregate_player_statistics(parsed_stats=parsed_stats)
{'Alice': {'assists': 7}, 'Bob': {'assists': 5}}
```



---

## extract_player_names

### Description
Extracts player names from aggregated statistics.

### Conceptual Info

This shim function is designed to extract a list of player names from a given aggregated statistics object, playing a crucial role in the data processing pipeline of sports statistics analysis.

### Docstring

**Summary:** Extracts player names from aggregated statistics.

**Parameters:**

- aggregated_stats (str): Aggregated player statistics as a string, expected to contain player names.
**Returns:** List[str] - A list of player names extracted from the aggregated statistics.

**Raises:**

- ValueError: If the input aggregated_stats is not a valid string or does not contain player names.
- TypeError: If the input aggregated_stats is not of type str.
**Examples:**

```python
>>> aggregated_stats = '{ "Player1": { "score": 10 }, "Player2": { "score": 20 } }'
>>> extract_player_names(aggregated_stats=aggregated_stats)
['Player1', 'Player2']
```

```python
>>> aggregated_stats = '{ "John": { "score": 5 }, "Doe": { "score": 15 } }'
>>> extract_player_names(aggregated_stats=aggregated_stats)
['John', 'Doe']
```



---

## extract_points_scored

### Description
Extracts the total points scored by each player from aggregated game statistics.

### Conceptual Info

This shim extracts points scored by players from aggregated statistics, playing a crucial role in generating player performance summaries.

### Docstring

**Summary:** Extracts the total points scored by each player from the provided aggregated statistics.

**Parameters:**

- aggregated_stats (str): A string representation of aggregated game statistics, containing player performance data.
- player_names (str): A string representation of the list of player names corresponding to the statistics in aggregated_stats.
**Returns:** List[int] - A list of integers representing the total points scored by each player in the order corresponding to player_names.

**Raises:**

- ValueError: If the aggregated_stats string is not properly formatted or if it doesn't contain valid player statistics.
- TypeError: If aggregated_stats or player_names are not strings, or if the parsed statistics do not contain expected data types.
**Examples:**

```python
>>> aggregated_stats = '{\"Player1\": {\"points\": 10}, \"Player2\": {\"points\": 20}}'
>>> player_names = '[\"Player1\", \"Player2\"]'
>>> extract_points_scored(aggregated_stats=aggregated_stats, player_names=player_names)
[10, 20]
```

```python
>>> aggregated_stats = '{\"John\": {\"points\": 15}, \"Doe\": {\"points\": 25}}'
>>> player_names = '[\"John\", \"Doe\"]'
>>> extract_points_scored(aggregated_stats=aggregated_stats, player_names=player_names)
[15, 25]
```



---

## extract_rebounds

### Description
Extracts rebounds for each player from aggregated statistics.

### Conceptual Info

This shim extracts rebounds for each player from the aggregated game statistics.

### Docstring

**Summary:** Extract rebounds for each player from aggregated statistics.

**Parameters:**

- aggregated_stats (str): Aggregated player statistics containing rebounds information.
- player_names (str): List of player names corresponding to the statistics in aggregated_stats.
**Returns:** List[int] - List of total rebounds for each player in the order of player_names.

**Raises:**

- ValueError: If the aggregated_stats string is malformed or missing required data.
- TypeError: If the input types are not as expected.
**Examples:**

```python
>>> aggregated_stats = '{\"Player1\": {\"rebounds\": 10}, \"Player2\": {\"rebounds\": 5}}'
>>> player_names = '[\"Player1\", \"Player2\"]'
>>> extract_rebounds(aggregated_stats=aggregated_stats, player_names=player_names)
[10, 5]
```

```python
>>> aggregated_stats = '{\"PlayerA\": {\"rebounds\": 7}, \"PlayerB\": {\"rebounds\": 3}}'
>>> player_names = '[\"PlayerA\", \"PlayerB\"]'
>>> extract_rebounds(aggregated_stats=aggregated_stats, player_names=player_names)
[7, 3]
```



---

## extract_assists

### Description
Extracts the total assists for each player from the aggregated game statistics.

### Conceptual Info

This shim function is designed to extract the total assists for each player from the aggregated game statistics. It plays a crucial role in the larger system by providing a specific statistical output required for further analysis or processing.

### Docstring

**Summary:** Extracts total assists for each player from aggregated game statistics.

**Parameters:**

- aggregated_stats (str): Aggregated game statistics containing player performance data.
- player_names (str): List of player names corresponding to the statistics.
**Returns:** List[int] - A list of integers representing the total assists for each player in the order of player_names.

**Raises:**

- ValueError: If the aggregated_stats string is malformed or cannot be parsed.
- TypeError: If the input types are incorrect, such as aggregated_stats or player_names not being strings.
**Examples:**

```python
>>> aggregated_stats = "{'Player1': {'assists': 10}, 'Player2': {'assists': 5}}"
>>> player_names = "['Player1', 'Player2']"
>>> extract_assists(aggregated_stats, player_names)
[10, 5]
```

```python
>>> aggregated_stats = "{'PlayerA': {'assists': 8}, 'PlayerB': {'assists': 12}}"
>>> player_names = "['PlayerA', 'PlayerB']"
>>> extract_assists(aggregated_stats, player_names)
[8, 12]
```

