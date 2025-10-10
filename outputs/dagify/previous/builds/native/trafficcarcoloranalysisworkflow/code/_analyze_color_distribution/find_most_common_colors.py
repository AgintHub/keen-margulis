from typing import List


import ast


def find_most_common_colors(unique_colors: str, counts: str) -> List[str]:
    """
    Finds the most common colors from the given unique colors and their counts.

    Parameters
    ----------
    unique_colors : str
        A string representation of a list of unique colors (e.g., "['red',
        'blue', 'green']").
    counts : str
        A string representation of a list of counts corresponding to the
        unique colors (e.g., "[3, 2, 1]").

    Returns
    -------
    List[str]
        A list of the most common colors observed.

    Raises
    ------
    ValueError
        If the input strings cannot be parsed into lists or if the lengths
        of the parsed lists do not match.
    TypeError
        If the input types are not strings or if the parsed lists contain
        non-numeric counts.

    Examples
    --------
    >>> unique_colors = "['red', 'blue', 'green']"
    >>> counts = "[3, 2, 1]"
    >>> find_most_common_colors(unique_colors, counts)
    ['red']

    >>> unique_colors = "['yellow', 'blue', 'red']"
    >>> counts = "[2, 2, 2]"
    >>> find_most_common_colors(unique_colors, counts)
    ['yellow', 'blue', 'red']

    """
    if not isinstance(unique_colors, str) or not isinstance(counts, str):
        raise TypeError("Input types must be strings")
    
    try:
        colors_list = ast.literal_eval(unique_colors)
        counts_list = ast.literal_eval(counts)
    except (ValueError, SyntaxError) as e:
        raise ValueError("Input strings cannot be parsed into lists") from e
    
    if not isinstance(colors_list, list) or not isinstance(counts_list, list):
        raise ValueError("Input strings must represent lists")
    
    if len(colors_list) != len(counts_list):
        raise ValueError("The lengths of the parsed lists do not match")
    
    for count in counts_list:
        if not isinstance(count, (int, float)):
            raise TypeError("The parsed lists contain non-numeric counts")
    
    if not counts_list:
        return []
    
    max_count = max(counts_list)
    most_common_colors = [colors_list[i] for i, count in enumerate(counts_list) if count == max_count]
    
    return most_common_colors