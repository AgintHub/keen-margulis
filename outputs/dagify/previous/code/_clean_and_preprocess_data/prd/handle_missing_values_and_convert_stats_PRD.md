# handle_missing_values_and_convert_stats PRD

## Description
Handles missing values in game statistics and converts them into a numerical format.


## Conceptual Info

This shim node is responsible for handling missing values in the input game statistics and converting them into a numerical format that can be used for further analysis.

## Docstring

### Summary
Handles missing values in game statistics and converts them to a list of floats.

### Parameters

- **game_statistics** (str): Input game statistics as a string, potentially containing missing values.

### Returns

List[float]: List of cleaned and converted game statistics in numerical format.

### Raises

- ValueError: If the input string is malformed or cannot be converted to numerical format.
- TypeError: If the input is not a string.

### Examples

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
