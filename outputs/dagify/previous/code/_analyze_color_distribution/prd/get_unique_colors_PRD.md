# get_unique_colors PRD

## Description
Extracts unique colors from a given list of vehicle colors.


## Conceptual Info

This shim function is designed to extract and return a list of unique colors from a given input list of vehicle colors, playing a crucial role in color distribution analysis.

## Docstring

### Summary
Extracts and returns a list of unique colors from the input string of colors.

### Parameters

- **colors** (str): Input string containing a list of colors separated by commas or other delimiters.

### Returns

List[str]: A list of unique colors extracted from the input string.

### Raises

- ValueError: If the input string is empty or contains invalid color formats.
- TypeError: If the input is not a string.

### Examples

```python
>>> get_unique_colors(colors='red,blue,red,green')
['red', 'blue', 'green']
```

```python
>>> get_unique_colors(colors='yellow,blue,yellow,blue')
['yellow', 'blue']
```
