from typing import List


import json


def extract_leaf_images(raw_data: str) -> List[str]:
    """
    Extracts image file names or URLs from raw leaf data.

    Parameters
    ----------
    raw_data : str
        Raw data containing leaf information in a string format, potentially
        JSON encoded.

    Returns
    -------
    List[str]
        List of image file names or URLs extracted from the raw data.

    Raises
    ------
    ValueError
        If the raw_data is not a valid string or if it's not properly
        formatted.
    TypeError
        If the input raw_data is not of type str.

    Examples
    --------
    >>> raw_data = '[{"image": "leaf1.jpg"}, {"image": "leaf2.jpg"}]'
    >>> extract_leaf_images(raw_data=raw_data)
    ['leaf1.jpg', 'leaf2.jpg']

    >>> raw_data = '[{"other": "data"}, {"image": "leaf3.jpg"}]'
    >>> extract_leaf_images(raw_data=raw_data)
    ['leaf3.jpg']

    """
    if not isinstance(raw_data, str):
        raise TypeError("If the input raw_data is not of type str.")
    
    try:
        data = json.loads(raw_data)
    except json.JSONDecodeError:
        raise ValueError("If the raw_data is not a valid string or if it's not properly formatted.")
    
    if not isinstance(data, list):
        raise ValueError("If the raw_data is not a valid string or if it's not properly formatted.")
    
    images = []
    for item in data:
        if isinstance(item, dict) and 'image' in item:
            images.append(item['image'])
    
    return images