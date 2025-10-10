# count_shape_categories PRD

## Description
Counts the occurrences of each shape category in the given list of categories.


## Conceptual Info

This shim node is responsible for counting the occurrences of each shape category in a given list, playing a crucial role in analyzing leaf shapes.

## Docstring

### Summary
Counts the occurrences of each shape category in the given list of categories.

### Parameters

- **categories** (str): A string representing the shape categories, expected to be a list or a string that can be parsed into a list of categories.

### Returns

List[int]: A list of integers where each integer represents the count of a unique shape category in the input.

### Raises

- ValueError: If the input categories are not in an expected format or if there's an issue parsing the categories.
- TypeError: If the input categories are not of type str or if the parsed categories are not as expected.

### Examples

```python
>>> count_shape_categories(categories='category1,category2,category1')
[2, 1]
```

```python
>>> count_shape_categories(categories='oval, lance, oval, round')
[2, 1, 1]
```
