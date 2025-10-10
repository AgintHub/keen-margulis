# extract_leaf_images PRD

## Description
Extracts image file names or URLs from raw leaf data.


## Conceptual Info

This shim function is responsible for extracting image file names or URLs from the raw leaf data provided as input.

## Docstring

### Summary
Extracts image file names or URLs from raw leaf data.

### Parameters

- **raw_data** (str): Raw data containing leaf information in a string format, potentially JSON encoded.

### Returns

List[str]: List of image file names or URLs extracted from the raw data.

### Raises

- ValueError: If the raw_data is not a valid string or if it's not properly formatted.
- TypeError: If the input raw_data is not of type str.

### Examples

```python
>>> raw_data = '[{"image": "leaf1.jpg"}, {"image": "leaf2.jpg"}]'
>>> extract_leaf_images(raw_data=raw_data)
['leaf1.jpg', 'leaf2.jpg']
```

```python
>>> raw_data = '[{"other": "data"}, {"image": "leaf3.jpg"}]'
>>> extract_leaf_images(raw_data=raw_data)
['leaf3.jpg']
```
