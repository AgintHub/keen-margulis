# extract_leaf_characteristics PRD

## Description
Extracts characteristic descriptions from raw leaf data.


## Conceptual Info

This shim extracts characteristic information from raw leaf data, serving as an intermediary step in leaf data processing.

## Docstring

### Summary
Extracts characteristic descriptions from raw leaf data.

### Parameters

- **raw_data** (str): Raw data containing leaf information in a string format.

### Returns

List[str]: List of characteristic descriptions for each leaf.

### Raises

- ValueError: When the input raw data is not in the expected format.
- TypeError: When the input type is not a string.

### Examples

```python
>>> extract_leaf_characteristics(raw_data='{"leaf1": "green", "leaf2": "yellow"}')
['green', 'yellow']
```

```python
>>> extract_leaf_characteristics(raw_data='{"leaf1": "oval", "leaf2": "heart-shaped"}')
['oval', 'heart-shaped']
```
