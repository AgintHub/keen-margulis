from typing import List


def count_color_occurrences(colors: str, unique_colors: str) -> List[int]:
    """
    Counts occurrences of each unique color in a list of colors.

    Parameters
    ----------
    colors : str
        A string representing a list of colors.
    unique_colors : str
        A string representing a list of unique colors.

    Returns
    -------
    List[int]
        A list of integers representing the count of occurrences for each
        unique color in the order they appear in unique_colors.

    Raises
    ------
    ValueError
        If the input strings cannot be properly parsed into lists of colors.
    TypeError
        If the input is not of type string or if the parsing results in
        incorrect types.

    Examples
    --------
    >>> colors = 'red,blue,red,green,blue,blue'
    >>> unique_colors = 'red,blue,green'
    >>> count_color_occurrences(colors=colors, unique_colors=unique_colors)
    [2, 3, 1]

    >>> colors = 'yellow,yellow,red,red,red'
    >>> unique_colors = 'yellow,red'
    >>> count_color_occurrences(colors=colors, unique_colors=unique_colors)
    [2, 3]

    """
    if not isinstance(colors, str) or not isinstance(unique_colors, str):
        raise TypeError("Input is not of type string")
    
    try:
        colors_list = [color.strip() for color in colors.split(',') if color.strip()]
        unique_colors_list = [color.strip() for color in unique_colors.split(',') if color.strip()]
    except Exception as e:
        raise ValueError("Input strings cannot be properly parsed into lists of colors") from e
    
    if not all(isinstance(color, str) for color in colors_list + unique_colors_list):
        raise TypeError("Parsing results in incorrect types")
    
    counts = []
    for unique_color in unique_colors_list:
        count = colors_list.count(unique_color)
        counts.append(count)
    
    return counts