# gather_raw_leaf_data PRD

## Description
A shim function that collects raw leaf data from specified sources.


## Conceptual Info

This shim function serves as a placeholder for collecting raw leaf data from various sources. It is part of a larger system that processes leaf images and characteristics.

## Docstring

### Summary
Collects raw leaf data from the specified sources and returns it as a list of dictionaries.

### Parameters

- **sources** (str): A string representing the data sources from which to gather raw leaf data.

### Returns

List[dict]: A list of dictionaries where each dictionary contains raw data for a leaf.

### Raises

- ValueError: If the input 'sources' is not a valid string or is empty.
- TypeError: If the input 'sources' is not of type string.

### Examples

```python
>>> raw_leaf_data = gather_raw_leaf_data(sources='leaf_data_sources')
>>> print(raw_leaf_data)
[{'leaf_id': 1, 'image_url': 'url1', 'characteristics': 'desc1'}, {'leaf_id': 2, 'image_url': 'url2', 'characteristics': 'desc2'}]
```

```python
>>> try:
...     gather_raw_leaf_data(sources='')
>>> except ValueError as e:
...     print(e)
Input 'sources' cannot be empty.
```
