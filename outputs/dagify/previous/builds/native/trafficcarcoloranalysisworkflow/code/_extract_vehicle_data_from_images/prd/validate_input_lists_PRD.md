# validate_input_lists PRD

## Description
Validates that the input lists for image paths and timestamps are correctly formatted and consistent.


## Conceptual Info

This shim node validates the input lists for image paths and timestamps to ensure they are correctly formatted and consistent, which is crucial for downstream processing.

## Docstring

### Summary
Validates input lists for image paths and timestamps, checking for consistency and correct formatting.

### Parameters

- **image_paths** (str): A list of file paths to captured traffic images, expected to be in a string format that can be parsed into a list.
- **image_timestamps** (str): A list of timestamps for when each image was captured, expected to be in a string format that can be parsed into a list and in the same order as image_paths.

### Returns

str: A message indicating whether the input lists are valid. Returns 'valid' if both lists are of the same length and correctly formatted, otherwise returns an error message.

### Raises

- ValueError: When the input lists are not of the same length or are not correctly formatted.
- TypeError: When the input types are not as expected (e.g., not strings that can be parsed into lists).

### Examples

```python
>>> validate_input_lists(image_paths='["path1", "path2"]', image_timestamps='["timestamp1", "timestamp2"]')
'valid'
```

```python
>>> validate_input_lists(image_paths='["path1", "path2"]', image_timestamps='["timestamp1"]')
'Error: Input lists are not of the same length.'
```
