# find_most_common_colors PRD

## Description
Identifies the most common colors from a list of unique colors and their corresponding counts.


## Conceptual Info

This shim function is designed to process input data about unique colors and their counts to determine the most common colors. It plays a crucial role in analyzing color distributions within the larger system.

## Docstring

### Summary
Finds the most common colors from the given unique colors and their counts.

### Parameters

- **unique_colors** (str): A string representation of a list of unique colors (e.g., "['red', 'blue', 'green']").
- **counts** (str): A string representation of a list of counts corresponding to the unique colors (e.g., "[3, 2, 1]").

### Returns

List[str]: A list of the most common colors observed.

### Raises

- ValueError: If the input strings cannot be parsed into lists or if the lengths of the parsed lists do not match.
- TypeError: If the input types are not strings or if the parsed lists contain non-numeric counts.

### Examples

```python
>>> unique_colors = "['red', 'blue', 'green']"
>>> counts = "[3, 2, 1]"
>>> find_most_common_colors(unique_colors, counts)
['red']
```

```python
>>> unique_colors = "['yellow', 'blue', 'red']"
>>> counts = "[2, 2, 2]"
>>> find_most_common_colors(unique_colors, counts)
['yellow', 'blue', 'red']
```
