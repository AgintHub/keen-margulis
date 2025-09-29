# validate_data_format PRD

## Description
Validates the format of input data against an expected data type.


## Conceptual Info

This shim validates the format of input data against a specified expected type, ensuring data consistency and correctness in the larger system.

## Docstring

### Summary
Validates the format of input data against an expected data type.

### Parameters

- **data** (str): The input data to be validated, expected to be a string representation of a list of dictionaries.
- **expected_type** (str): The expected type of the input data, which can be 'game_stats', 'player_info', or 'team_metrics'.

### Returns

bool: A boolean indicating whether the input data matches the expected type.

### Raises

- ValueError: If the input data is not a valid JSON or does not match the expected structure.
- TypeError: If the input data or expected type is not of the correct type.

### Examples

```python
>>> validate_data_format(data='[{"score": 10, "team": "A"}]', expected_type='game_stats')
>>> validate_data_format(data='[{"name": "John", "age": 30}]', expected_type='player_info')
>>> validate_data_format(data='[{"metric": "possession", "value": 0.5}]', expected_type='team_metrics')
True
```

```python
>>> validate_data_format(data='invalid_json', expected_type='game_stats')
False
```
