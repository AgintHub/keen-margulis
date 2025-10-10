# detect_vehicles_in_image PRD

## Description
Detects vehicles within a given image and returns the detection results.


## Conceptual Info

This shim function is designed to detect vehicles within an image. It takes image data as input and returns the detection results as a string.

## Docstring

### Summary
Detects vehicles in the given image data and returns the results.

### Parameters

- **image_data** (str): The input image data as a string.

### Returns

str: A string representation of the detected vehicles.

### Raises

- ValueError: If the input image data is invalid or corrupted.
- TypeError: If the input image data is not of type string.

### Examples

```python
>>> detect_vehicles_in_image(image_data='base64encodedimage')
'Detected 5 vehicles'
```

```python
>>> detect_vehicles_in_image(image_data='invalidimage')
ValueError: Invalid image data
```
