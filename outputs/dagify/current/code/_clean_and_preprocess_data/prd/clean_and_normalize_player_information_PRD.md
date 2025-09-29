# clean_and_normalize_player_information PRD

## Description
Cleans and normalizes player information by processing a list of strings containing player data.


## Conceptual Info

This shim function is designed to process and normalize player information, likely removing unwanted characters, handling case sensitivity, and ensuring data consistency.

## Docstring

### Summary
Cleans and normalizes player information from input strings.

### Parameters

- **player_information** (str): Input string containing player information that needs to be cleaned and normalized.

### Returns

List[str]: A list of strings representing the cleaned and normalized player information.

### Raises

- ValueError: If the input string is malformed or contains invalid data.
- TypeError: If the input is not a string.

### Examples

```python
>>> clean_and_normalize_player_information(player_information='John Doe,25,Forward')
>>> clean_and_normalize_player_information(player_information=' Jane Smith ,30, Guard ')
['John Doe,25,Forward', 'Jane Smith,30,Guard']
```

```python
>>> clean_and_normalize_player_information(player_information='Invalid Data')
['Invalid Data']
```
