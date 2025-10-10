# capture_traffic_images PRD

## Description
Captures traffic images based on camera settings, schedule, focus settings, and lighting optimization.


## Conceptual Info

This shim node is responsible for capturing traffic images based on the provided inputs such as camera devices, capture schedule, focus settings, and lighting optimization parameters. It serves as a placeholder for the complex functionality of image capture that will be implemented later.

## Docstring

### Summary
Captures traffic images using the specified camera devices, schedule, focus settings, and lighting optimization.

### Parameters

- **cameras** (str): A string representing the camera devices to be used for capturing images.
- **schedule** (str): A string representing the schedule or timing for capturing traffic images.
- **focus_settings** (str): A string specifying the focus settings for the camera devices.
- **lighting_optimization** (str): A string indicating whether lighting optimization should be enabled or not.

### Returns

List[bytes]: A list of captured traffic images in bytes format.

### Raises

- ValueError: If the input parameters are invalid or cannot be parsed correctly.
- TypeError: If the input types do not match the expected types.

### Examples

```python
>>> capture_traffic_images(cameras='camera1,camera2', schedule='{"start_time": "08:00", "end_time": "09:00"}', focus_settings='vehicle_features', lighting_optimization='True')
>>> → [b'image1_data', b'image2_data']
[b'image1_data', b'image2_data']
```

```python
>>> capture_traffic_images(cameras='camera3', schedule='{"start_time": "17:00", "end_time": "18:00"}', focus_settings='traffic_signs', lighting_optimization='False')
>>> → [b'image3_data']
[b'image3_data']
```
