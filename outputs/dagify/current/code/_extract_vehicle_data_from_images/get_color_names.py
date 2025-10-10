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
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")