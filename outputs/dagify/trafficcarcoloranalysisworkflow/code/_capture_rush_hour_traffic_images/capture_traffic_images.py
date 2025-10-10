from typing import List


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
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")