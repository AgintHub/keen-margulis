# count_color_occurrences PRD

## Description
Counts occurrences of each unique color in a given list of colors.


## Conceptual Info

This shim function is designed to count the occurrences of each unique color in a given list of colors. It plays a crucial role in analyzing color distributions within the larger system.

## Docstring

### Summary
Counts occurrences of each unique color in a list of colors.

### Parameters

- **colors** (str): A string representing a list of colors.
- **unique_colors** (str): A string representing a list of unique colors.

### Returns

List[int]: A list of integers representing the count of occurrences for each unique color in the order they appear in unique_colors.

### Raises

- ValueError: If the input strings cannot be properly parsed into lists of colors.
- TypeError: If the input is not of type string or if the parsing results in incorrect types.

### Examples

```python
>>> colors = 'red,blue,red,green,blue,blue'
>>> unique_colors = 'red,blue,green'
>>> count_color_occurrences(colors=colors, unique_colors=unique_colors)
[2, 3, 1]
```

```python
>>> colors = 'yellow,yellow,red,red,red'
>>> unique_colors = 'yellow,red'
>>> count_color_occurrences(colors=colors, unique_colors=unique_colors)
[2, 3]
```
