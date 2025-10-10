from typing import List


def get_color_names(colors_and_scores: str) -> List[str]:
    """
    Extracts color names from the provided color information and confidence
    scores.

    Parameters
    ----------
    colors_and_scores : str
        A string containing color information and confidence scores,
        formatted appropriately for processing.

    Returns
    -------
    List[str]
        A list of color names extracted from the input color information.

    Raises
    ------
    ValueError
        If the input string is not properly formatted or contains invalid
        color information.
    TypeError
        If the input is not a string.

    Examples
    --------
    >>> get_color_names(colors_and_scores='red:0.8,blue:0.2')
    ['red', 'blue']

    >>> get_color_names(colors_and_scores='green:0.9,yellow:0.1')
    ['green', 'yellow']

    """
    if not isinstance(colors_and_scores, str):
        raise TypeError("Input must be a string")
    
    if not colors_and_scores.strip():
        raise ValueError("Input string cannot be empty")
    
    color_names = []
    
    pairs = colors_and_scores.split(',')
    
    for pair in pairs:
        pair = pair.strip()
        if not pair:
            continue
            
        if ':' not in pair:
            raise ValueError(f"Invalid format: '{pair}' - expected 'color:score' format")
            
        parts = pair.split(':', 1)
        if len(parts) != 2:
            raise ValueError(f"Invalid format: '{pair}' - expected 'color:score' format")
            
        color_name = parts[0].strip()
        score_str = parts[1].strip()
        
        if not color_name:
            raise ValueError(f"Empty color name in pair: '{pair}'")
            
        try:
            float(score_str)
        except ValueError:
            raise ValueError(f"Invalid score '{score_str}' in pair: '{pair}' - score must be a number")
            
        color_names.append(color_name)
    
    return color_names