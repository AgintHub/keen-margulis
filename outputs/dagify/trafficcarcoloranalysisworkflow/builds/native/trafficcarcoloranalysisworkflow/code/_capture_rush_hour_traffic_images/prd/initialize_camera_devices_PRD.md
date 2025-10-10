# initialize_camera_devices PRD

## Description
Initializes camera devices and returns a list of device identifiers based on the input configuration.


## Conceptual Info

This shim node is responsible for initializing camera devices based on the provided input configuration and returning a list of device identifiers that can be used for further operations.

## Docstring

### Summary
Initializes camera devices based on the input configuration and returns a list of device identifiers.

### Parameters

- **input_config** (str): Input configuration for initializing camera devices, expected to be a string that can be parsed or used directly to configure the devices.

### Returns

List[str]: A list of strings representing the identifiers of the initialized camera devices.

### Raises

- ValueError: If the input configuration is invalid or cannot be parsed.
- RuntimeError: If there is a failure in initializing the camera devices.

### Examples

```python
>>> initialize_camera_devices(input_config='camera_config.json')
['camera1', 'camera2', 'camera3']
```

```python
>>> initialize_camera_devices(input_config='invalid_config')
ValueError: Invalid input configuration
```
