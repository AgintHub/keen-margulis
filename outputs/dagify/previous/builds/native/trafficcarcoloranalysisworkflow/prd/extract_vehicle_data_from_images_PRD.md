# extract_vehicle_data_from_images PRD

## Description
Use computer vision to extract vehicle data including colors from captured images


## Conceptual Info

This node utilizes computer vision techniques to analyze images captured during rush hour traffic and extract vehicle color information.

## Docstring

### Summary
Extracts vehicle color data from a list of image paths using computer vision.

### Parameters

- **image_paths** (List[str]): List of file paths to the images captured during rush hour traffic.
- **image_timestamps** (List[str]): Timestamps for when each image was captured (same order as image_paths).

### Returns

Tuple[List[str], List[float]]: A tuple containing a list of detected vehicle colors and their corresponding confidence scores.

### Raises

- ValueError: If the input lists (image_paths and image_timestamps) are of different lengths.
- FileNotFoundError: If any of the image paths in image_paths do not exist.
- Exception: If there's an issue processing an image (e.g., due to corruption or unsupported format).

### Examples

```python
>>> image_paths = ['/path/to/image1.jpg', '/path/to/image2.jpg']
>>> image_timestamps = ['2023-04-01 08:00:00', '2023-04-01 08:01:00']
>>> vehicle_colors, vehicle_confidence_scores = extract_vehicle_data_from_images(image_paths, image_timestamps)
(['red', 'blue'], [0.9, 0.85])
```

```python
>>> image_paths = ['/path/to/image3.jpg']
>>> image_timestamps = ['2023-04-01 08:02:00']
>>> vehicle_colors, vehicle_confidence_scores = extract_vehicle_data_from_images(image_paths, image_timestamps)
(['black'], [0.95])
```
