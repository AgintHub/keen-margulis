# extract_colors_from_vehicles PRD

## Description
Extracts colors from detected vehicles in an image.


## Conceptual Info

This shim node is responsible for extracting color information from detected vehicles in images, playing a crucial role in the vehicle's data extraction pipeline.

## Docstring

### Summary
Extracts colors and their confidence scores from detected vehicles.

### Parameters

- **detected_vehicles** (str): A string representation of detected vehicles, potentially containing their image data or detection results.

### Returns

str: A string containing the extracted colors and their confidence scores, formatted as a list or dictionary.

### Raises

- ValueError: If the input string is not properly formatted or if vehicle detection data is invalid.
- TypeError: If the input is not a string.

### Examples

```python
>>> extract_colors_from_vehicles(detected_vehicles='vehicle_data')
'colors_and_scores'
```

```python
>>> extract_colors_from_vehicles(detected_vehicles='invalid_data')
ValueError: Invalid vehicle detection data format.
```
