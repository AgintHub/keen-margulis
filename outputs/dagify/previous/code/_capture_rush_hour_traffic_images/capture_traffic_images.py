from typing import List


import json
import random
import string


def capture_traffic_images(cameras: str, schedule: str, focus_settings: str, lighting_optimization: str) -> List[str]:
    """
    Captures traffic images using the specified camera devices, schedule, focus
    settings, and lighting optimization.

    Parameters
    ----------
    cameras : str
        A string representing the camera devices to be used for capturing
        images.
    schedule : str
        A string representing the schedule or timing for capturing traffic
        images.
    focus_settings : str
        A string specifying the focus settings for the camera devices.
    lighting_optimization : str
        A string indicating whether lighting optimization should be enabled
        or not.

    Returns
    -------
    List[bytes]
        A list of captured traffic images in bytes format.

    Raises
    ------
    ValueError
        If the input parameters are invalid or cannot be parsed correctly.
    TypeError
        If the input types do not match the expected types.

    Examples
    --------
    >>> capture_traffic_images(cameras='camera1,camera2',
    schedule='{"start_time": "08:00", "end_time": "09:00"}',
    focus_settings='vehicle_features', lighting_optimization='True')
    >>> → [b'image1_data', b'image2_data']
    [b'image1_data', b'image2_data']

    >>> capture_traffic_images(cameras='camera3', schedule='{"start_time":
    "17:00", "end_time": "18:00"}', focus_settings='traffic_signs',
    lighting_optimization='False')
    >>> → [b'image3_data']
    [b'image3_data']

    """
    
    if not isinstance(cameras, str):
        raise TypeError("cameras must be a string")
    if not isinstance(schedule, str):
        raise TypeError("schedule must be a string")
    if not isinstance(focus_settings, str):
        raise TypeError("focus_settings must be a string")
    if not isinstance(lighting_optimization, str):
        raise TypeError("lighting_optimization must be a string")
    
    if not cameras.strip():
        raise ValueError("cameras parameter cannot be empty")
    
    camera_list = [cam.strip() for cam in cameras.split(',') if cam.strip()]
    if not camera_list:
        raise ValueError("No valid cameras found in cameras parameter")
    
    try:
        schedule_data = json.loads(schedule)
        if not isinstance(schedule_data, dict):
            raise ValueError("Schedule must be a JSON object")
        if 'start_time' not in schedule_data or 'end_time' not in schedule_data:
            raise ValueError("Schedule must contain start_time and end_time")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in schedule parameter")
    
    valid_focus_settings = ['vehicle_features', 'traffic_signs', 'pedestrians', 'general']
    if focus_settings not in valid_focus_settings:
        raise ValueError(f"Invalid focus_settings. Must be one of: {valid_focus_settings}")
    
    if lighting_optimization.lower() not in ['true', 'false']:
        raise ValueError("lighting_optimization must be 'True' or 'False'")
    
    captured_images = []
    for i, camera in enumerate(camera_list):
        image_size = random.randint(1000, 5000)
        image_data = ''.join(random.choices(string.ascii_letters + string.digits, k=image_size))
        captured_images.append(image_data)
    
    return captured_images