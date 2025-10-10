# get_confidence_values PRD

## Description
Extracts confidence scores from a string containing color information and confidence scores.


## Conceptual Info

This shim function is designed to extract confidence scores from a given string that contains color information along with their corresponding confidence scores. It plays a crucial role in the vehicle data extraction pipeline by processing the output of the color extraction step.

## Docstring

### Summary
Extracts confidence scores from a string containing color and confidence information.

### Parameters

- **colors_and_scores** (str): Input string containing color information along with their confidence scores, formatted in a way that can be parsed to extract confidence scores.

### Returns

List[float]: A list of floating-point numbers representing the confidence scores for the detected colors.

### Raises

- ValueError: If the input string is not in the expected format or if confidence scores cannot be extracted.
- TypeError: If the input is not a string.

### Examples

```python
>>> colors_and_scores = 'red:0.8,blue:0.9,green:0.7'
>>> confidence_scores = get_confidence_values(colors_and_scores)
[0.8, 0.9, 0.7]
```

```python
>>> colors_and_scores = 'yellow:0.95,black:0.85'
>>> confidence_scores = get_confidence_values(colors_and_scores)
[0.95, 0.85]
```
