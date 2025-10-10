from typing import List


import json


def extract_leaf_characteristics(raw_data: str) -> List[str]:
    """
    Extracts characteristic descriptions from raw leaf data.

    Parameters
    ----------
    raw_data : str
        Raw data containing leaf information in a string format.

    Returns
    -------
    List[str]
        List of characteristic descriptions for each leaf.

    Raises
    ------
    ValueError
        When the input raw data is not in the expected format.
    TypeError
        When the input type is not a string.

    Examples
    --------
    >>> extract_leaf_characteristics(raw_data='{"leaf1": "green", "leaf2":
    "yellow"}')
    ['green', 'yellow']

    >>> extract_leaf_characteristics(raw_data='{"leaf1": "oval", "leaf2":
    "heart-shaped"}')
    ['oval', 'heart-shaped']

    """
    
    if not isinstance(raw_data, str):
        raise TypeError("When the input type is not a string.")
    
    try:
        data = json.loads(raw_data)
    except json.JSONDecodeError:
        raise ValueError("When the input raw data is not in the expected format.")
    
    if not isinstance(data, dict):
        raise ValueError("When the input raw data is not in the expected format.")
    
    characteristics = []
    for leaf_key, characteristic in data.items():
        if isinstance(characteristic, str):
            characteristics.append(characteristic)
        else:
            raise ValueError("When the input raw data is not in the expected format.")
    
    return characteristics