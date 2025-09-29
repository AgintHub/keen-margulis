# _clean_and_preprocess_data - Complete PRD Documentation

## Overview
PRDs for nodes in the '_clean_and_preprocess_data' module.

## Table of Contents

- [validate_input_data](#validate_input_data)

- [handle_missing_values_and_convert_stats](#handle_missing_values_and_convert_stats)

- [clean_and_normalize_player_information](#clean_and_normalize_player_information)

- [normalize_and_transform_team_metrics](#normalize_and_transform_team_metrics)

- [calculate_data_quality_score](#calculate_data_quality_score)



---

## validate_input_data

### Description
Validates the input data for the clean_and_preprocess_data function to ensure it conforms to expected formats and structures.

### Conceptual Info

This shim node is responsible for validating the input data passed to the clean_and_preprocess_data function, ensuring it meets the required structure and format expectations.

### Docstring

**Summary:** Validates the input data for the clean_and_preprocess_data function.

**Parameters:**

- collect_sports_data_input (CollectSportsDataOutput): The input data containing game statistics, player information, team performance metrics, and a flag indicating whether data collection was successful.
**Returns:** str - A string indicating whether the input data is valid.

**Raises:**

- TypeError: If the input is not of type CollectSportsDataOutput.
- ValueError: If any of the input fields are missing or malformed.
**Examples:**

```python
>>> from pydantic import BaseModel, Field
>>> from typing import List
>>> class CollectSportsDataOutput(BaseModel):
...     game_statistics: List[str] = Field(..., description='List of game statistics')
...     player_information: List[str] = Field(..., description='List of player information')
...     team_performance_metrics: List[float] = Field(..., description='List of team performance metrics')
...     is_data_collection_successful: bool = Field(..., description='Boolean indicating data collection success')
>>> input_data = CollectSportsDataOutput(game_statistics=['stat1', 'stat2'], player_information=['player1', 'player2'], team_performance_metrics=[0.5, 0.6], is_data_collection_successful=True)
>>> validate_input_data(input_data)
'Input data is valid'
```

```python
>>> input_data = CollectSportsDataOutput(game_statistics=[], player_information=['player1', 'player2'], team_performance_metrics=[0.5, 0.6], is_data_collection_successful=True)
>>> validate_input_data(input_data)
'Input data is invalid: game_statistics is empty'
```



---

## handle_missing_values_and_convert_stats

### Description
Handles missing values in game statistics and converts them into a numerical format.

### Conceptual Info

This shim node is responsible for handling missing values in the input game statistics and converting them into a numerical format that can be used for further analysis.

### Docstring

**Summary:** Handles missing values in game statistics and converts them to a list of floats.

**Parameters:**

- game_statistics (str): Input game statistics as a string, potentially containing missing values.
**Returns:** List[float] - List of cleaned and converted game statistics in numerical format.

**Raises:**

- ValueError: If the input string is malformed or cannot be converted to numerical format.
- TypeError: If the input is not a string.
**Examples:**

```python
>>> handle_missing_values_and_convert_stats(game_statistics='1.2,3.4,,5.6')
>>> print(output)
[1.2, 3.4, 0.0, 5.6]
```

```python
>>> handle_missing_values_and_convert_stats(game_statistics='1,2,3,,4')
>>> print(output)
[1.0, 2.0, 3.0, 0.0, 4.0]
```



---

## clean_and_normalize_player_information

### Description
Cleans and normalizes player information by processing a list of strings containing player data.

### Conceptual Info

This shim function is designed to process and normalize player information, likely removing unwanted characters, handling case sensitivity, and ensuring data consistency.

### Docstring

**Summary:** Cleans and normalizes player information from input strings.

**Parameters:**

- player_information (str): Input string containing player information that needs to be cleaned and normalized.
**Returns:** List[str] - A list of strings representing the cleaned and normalized player information.

**Raises:**

- ValueError: If the input string is malformed or contains invalid data.
- TypeError: If the input is not a string.
**Examples:**

```python
>>> clean_and_normalize_player_information(player_information='John Doe,25,Forward')
>>> clean_and_normalize_player_information(player_information=' Jane Smith ,30, Guard ')
['John Doe,25,Forward', 'Jane Smith,30,Guard']
```

```python
>>> clean_and_normalize_player_information(player_information='Invalid Data')
['Invalid Data']
```



---

## normalize_and_transform_team_metrics

### Description
Normalizes and transforms team performance metrics into a standardized format for further analysis.

### Conceptual Info

This shim function is designed to normalize and transform team performance metrics into a standardized numerical format, making them suitable for analysis and further processing within the data pipeline.

### Docstring

**Summary:** Normalizes and transforms team performance metrics from a string representation into a list of floats.

**Parameters:**

- team_metrics (str): String representation of team performance metrics to be normalized and transformed.
**Returns:** List[float] - List of normalized and transformed team performance metrics as floats.

**Raises:**

- ValueError: If the input string cannot be parsed into numerical metrics.
- TypeError: If the input is not a string or if the metrics cannot be converted to float.
**Examples:**

```python
>>> normalize_and_transform_team_metrics(team_metrics='[1.2, 3.4, 5.6]')
[0.1, 0.3, 0.5]
```

```python
>>> normalize_and_transform_team_metrics(team_metrics='10, 20, 30')
[0.1, 0.2, 0.3]
```



---

## calculate_data_quality_score

### Description
This shim node calculates a data quality score based on the original statistics, cleaned statistics, player information, and team metrics.

### Conceptual Info

This shim function is designed to evaluate the quality of sports data by comparing original and cleaned statistics, player information, and team metrics, producing a score that reflects data quality.

### Docstring

**Summary:** Calculate a data quality score based on original statistics, cleaned statistics, player information, and team metrics.

**Parameters:**

- original_stats (str): Original game statistics serialized as a string.
- cleaned_stats (str): Cleaned game statistics serialized as a string.
- player_info (str): Preprocessed player information serialized as a string.
- team_metrics (str): Transformed team performance metrics serialized as a string.
**Returns:** float - A float value representing the data quality score.

**Raises:**

- ValueError: If any input parameter is empty or malformed.
- TypeError: If input parameters are not of the expected type.
**Examples:**

```python
>>> original_stats = '[1, 2, 3]'
>>> cleaned_stats = '[1.0, 2.0, 3.0]'
>>> player_info = '["John", "Doe"]'
>>> team_metrics = '[0.8, 0.9]'
>>> score = calculate_data_quality_score(original_stats, cleaned_stats, player_info, team_metrics)
0.85
```

```python
>>> original_stats = '[]'
>>> cleaned_stats = '[1.0, 2.0, 3.0]'
>>> player_info = '["John", "Doe"]'
>>> team_metrics = '[0.8, 0.9]'
ValueError: Input parameters cannot be empty.
```

