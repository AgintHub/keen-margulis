# generate_timestamps PRD

## Description
Generates timestamps for captured images based on the number of images and capture start time.


## Conceptual Info

This shim generates a list of timestamps for captured images based on the number of images and the start time of the capture.

## Docstring

### Summary
Generates timestamps for captured images.

### Parameters

- **image_count** (str): Number of images captured as a string.
- **capture_start_time** (str): Start time of the image capture in a format that can be used to generate subsequent timestamps.

### Returns

List[str]: List of timestamps for when each image was captured, in a consistent format.

### Raises

- ValueError: If the image_count is not a valid positive integer or if capture_start_time is not in an expected format.
- TypeError: If image_count is not a string or if capture_start_time is not a string.

### Examples

```python
>>> generate_timestamps(image_count='5', capture_start_time='2023-04-01 08:00:00')
['2023-04-01 08:00:00', '2023-04-01 08:00:01', '2023-04-01 08:00:02', '2023-04-01 08:00:03', '2023-04-01 08:00:04']
```

```python
>>> generate_timestamps(image_count='3', capture_start_time='2023-04-01 09:00:00')
['2023-04-01 09:00:00', '2023-04-01 09:00:01', '2023-04-01 09:00:02']
```
