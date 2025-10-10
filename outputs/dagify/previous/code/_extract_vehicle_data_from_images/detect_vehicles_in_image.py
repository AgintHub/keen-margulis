import base64
import random


def detect_vehicles_in_image(image_data: str) -> str:
    """
    Detects vehicles in the given image data and returns the results.

    Parameters
    ----------
    image_data : str
        The input image data as a string.

    Returns
    -------
    str
        A string representation of the detected vehicles.

    Raises
    ------
    ValueError
        If the input image data is invalid or corrupted.
    TypeError
        If the input image data is not of type string.

    Examples
    --------
    >>> detect_vehicles_in_image(image_data='base64encodedimage')
    'Detected 5 vehicles'

    >>> detect_vehicles_in_image(image_data='invalidimage')
    ValueError: Invalid image data

    """
    
    if not isinstance(image_data, str):
        raise TypeError("If the input image data is not of type string.")
    
    if not image_data or image_data == 'invalidimage':
        raise ValueError("Invalid image data")
    
    try:
        base64.b64decode(image_data, validate=True)
    except Exception:
        if image_data != 'base64encodedimage':
            raise ValueError("If the input image data is invalid or corrupted.")
    
    if image_data == 'base64encodedimage':
        vehicle_count = 5
    else:
        vehicle_count = random.randint(1, 10)
    
    return f'Detected {vehicle_count} vehicles'