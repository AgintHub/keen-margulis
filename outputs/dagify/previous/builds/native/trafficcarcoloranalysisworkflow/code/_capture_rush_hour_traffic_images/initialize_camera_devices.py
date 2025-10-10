from typing import List


import json
import os


def initialize_camera_devices(input_config: str) -> List[str]:
    """
    Initializes camera devices based on the input configuration and returns a
    list of device identifiers.

    Parameters
    ----------
    input_config : str
        Input configuration for initializing camera devices, expected to be
        a string that can be parsed or used directly to configure the
        devices.

    Returns
    -------
    List[str]
        A list of strings representing the identifiers of the initialized
        camera devices.

    Raises
    ------
    ValueError
        If the input configuration is invalid or cannot be parsed.
    RuntimeError
        If there is a failure in initializing the camera devices.

    Examples
    --------
    >>> initialize_camera_devices(input_config='camera_config.json')
    ['camera1', 'camera2', 'camera3']

    >>> initialize_camera_devices(input_config='invalid_config')
    ValueError: Invalid input configuration

    """
    if not input_config or not isinstance(input_config, str):
        raise ValueError("Invalid input configuration")
    
    try:
        if input_config.endswith('.json'):
            if not os.path.exists(input_config):
                raise ValueError("Configuration file not found")
            
            with open(input_config, 'r') as f:
                config_data = json.load(f)
        else:
            try:
                config_data = json.loads(input_config)
            except json.JSONDecodeError:
                config_data = {'cameras': [input_config]}
    except (json.JSONDecodeError, FileNotFoundError, PermissionError):
        raise ValueError("Invalid input configuration")
    
    device_identifiers = []
    
    try:
        if isinstance(config_data, dict):
            if 'cameras' in config_data:
                cameras = config_data['cameras']
                if isinstance(cameras, list):
                    for i, camera in enumerate(cameras):
                        if isinstance(camera, dict) and 'id' in camera:
                            device_identifiers.append(camera['id'])
                        elif isinstance(camera, str):
                            device_identifiers.append(camera)
                        else:
                            device_identifiers.append(f'camera{i+1}')
                else:
                    device_identifiers.append('camera1')
            else:
                device_identifiers.append('camera1')
        elif isinstance(config_data, list):
            for i, item in enumerate(config_data):
                if isinstance(item, dict) and 'id' in item:
                    device_identifiers.append(item['id'])
                elif isinstance(item, str):
                    device_identifiers.append(item)
                else:
                    device_identifiers.append(f'camera{i+1}')
        else:
            device_identifiers.append('camera1')
        
        if not device_identifiers:
            device_identifiers = ['camera1']
            
    except Exception as e:
        raise RuntimeError("Failed to initialize camera devices") from e
    
    return device_identifiers