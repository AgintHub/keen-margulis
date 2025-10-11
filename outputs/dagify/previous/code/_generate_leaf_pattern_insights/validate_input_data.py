import json


def validate_input_data(vein_patterns: str, colors: str) -> str:
    """
    Validates input lists of vein patterns and colors to ensure they are not
    empty and contain valid string entries.

    Parameters
    ----------
    vein_patterns : str
        A list of vein patterns as strings that need to be validated.
    colors : str
        A list of colors as strings that need to be validated.

    Returns
    -------
    str
        A message indicating whether the input data is valid or not.

    Raises
    ------
    ValueError
        If either vein_patterns or colors is empty or contains invalid
        entries.
    TypeError
        If the input types for vein_patterns or colors are not as expected.

    Examples
    --------
    >>> validate_input_data(vein_patterns='["pattern1", "pattern2"]',
    colors='["red", "green"]')
    'Input data is valid'

    >>> validate_input_data(vein_patterns='[]', colors='["red", "green"]')
    ValueError: Input lists cannot be empty

    """
    if not isinstance(vein_patterns, str) or not isinstance(colors, str):
        raise TypeError("Input types for vein_patterns or colors are not as expected.")
    
    try:
        vein_patterns_list = json.loads(vein_patterns)
        colors_list = json.loads(colors)
    except json.JSONDecodeError:
        raise TypeError("Input types for vein_patterns or colors are not as expected.")
    
    if not isinstance(vein_patterns_list, list) or not isinstance(colors_list, list):
        raise TypeError("Input types for vein_patterns or colors are not as expected.")
    
    if len(vein_patterns_list) == 0 or len(colors_list) == 0:
        raise ValueError("Input lists cannot be empty")
    
    for pattern in vein_patterns_list:
        if not isinstance(pattern, str):
            raise ValueError("If either vein_patterns or colors is empty or contains invalid entries.")
    
    for color in colors_list:
        if not isinstance(color, str):
            raise ValueError("If either vein_patterns or colors is empty or contains invalid entries.")
    
    return "Input data is valid"