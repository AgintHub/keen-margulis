from typing import List


import re


def get_unique_colors(colors: str) -> List[str]:
    """
    Extracts and returns a list of unique colors from the input string of
    colors.

    Parameters
    ----------
    colors : str
        Input string containing a list of colors separated by commas or
        other delimiters.

    Returns
    -------
    List[str]
        A list of unique colors extracted from the input string.

    Raises
    ------
    ValueError
        If the input string is empty or contains invalid color formats.
    TypeError
        If the input is not a string.

    Examples
    --------
    >>> get_unique_colors(colors='red,blue,red,green')
    ['red', 'blue', 'green']

    >>> get_unique_colors(colors='yellow,blue,yellow,blue')
    ['yellow', 'blue']

    """
    
    if not isinstance(colors, str):
        raise TypeError("If the input is not a string.")
    
    if not colors.strip():
        raise ValueError("If the input string is empty or contains invalid color formats.")
    
    color_list = re.split(r'[,;\s]+', colors.strip())
    
    valid_colors = []
    for color in color_list:
        color = color.strip()
        if color:
            if re.match(r'^[a-zA-Z]+$', color):
                valid_colors.append(color.lower())
            else:
                raise ValueError("If the input string is empty or contains invalid color formats.")
    
    if not valid_colors:
        raise ValueError("If the input string is empty or contains invalid color formats.")
    
    unique_colors = []
    seen = set()
    for color in valid_colors:
        if color not in seen:
            unique_colors.append(color)
            seen.add(color)
    
    return unique_colors