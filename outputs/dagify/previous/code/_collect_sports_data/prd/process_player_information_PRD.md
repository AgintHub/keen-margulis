# process_player_information PRD

## Description
Processes raw player data into a structured list of player information.


## Conceptual Info

This shim node is responsible for taking raw player data, processing it, and returning a structured list of player information.

## Docstring

### Summary
Processes raw player data into a list of structured player information.

### Parameters

- **raw_data** (str): Raw player data in string format that needs to be processed.

### Returns

List[str]: A list of strings containing structured player information.

### Raises

- ValueError: If the raw data is not in the expected format or is empty.
- TypeError: If the input raw_data is not of type str.

### Examples

```python
>>> raw_player_data = '[{"name": "John Doe", "position": "Forward"}, {"name": "Jane Doe", "position": "Midfield"}]'
>>> processed_data = process_player_information(raw_data=raw_player_data)
['John Doe - Forward', 'Jane Doe - Midfield']
```

```python
>>> raw_player_data = '[{"name": "Bob Smith", "position": "Defender"}]'
>>> processed_data = process_player_information(raw_data=raw_player_data)
['Bob Smith - Defender']
```
