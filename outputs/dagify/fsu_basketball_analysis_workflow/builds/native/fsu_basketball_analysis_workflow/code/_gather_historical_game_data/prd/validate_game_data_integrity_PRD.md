# validate_game_data_integrity PRD

## Description
Validates the integrity of raw game data to ensure it is accurate and consistent.


## Conceptual Info

This shim validates raw game data to ensure its integrity and accuracy before it is used for further processing.

## Docstring

### Summary
Validates the integrity of raw game data to ensure it is accurate and consistent.

### Parameters

- **raw_data** (str): Raw game data in string format that needs to be validated.

### Returns

List[dict]: List of dictionaries containing the validated game data, where each dictionary represents a game with relevant statistics and information.

### Raises

- ValueError: If the input raw data is malformed or cannot be parsed into a list of dictionaries.
- TypeError: If the input raw data is not of type string.

### Examples

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
