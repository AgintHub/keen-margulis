from typing import List


import ast


def combine_pattern_lists(vein_patterns: str, color_patterns: str) -> List[str]:
    """
    Combines two lists of patterns into a single list, removing duplicates and
    maintaining order.

    Parameters
    ----------
    vein_patterns : str
        A string representation of a list of vein patterns, e.g.,
        '[pattern1, pattern2]'.
    color_patterns : str
        A string representation of a list of color patterns, e.g., '[color1,
        color2]'.

    Returns
    -------
    List[str]
        A combined list of unique patterns from both input lists,
        maintaining the original order.

    Raises
    ------
    ValueError
        If either input string is not a valid list representation.
    TypeError
        If the input strings cannot be parsed into lists.

    Examples
    --------
    >>> vein_patterns = '[vein_pattern1, vein_pattern2]'
    >>> color_patterns = '[color_pattern1, color_pattern2]'
    >>> combined = combine_pattern_lists(vein_patterns=vein_patterns,
    color_patterns=color_patterns)
    ['vein_pattern1', 'vein_pattern2', 'color_pattern1', 'color_pattern2']

    >>> vein_patterns = '[pattern1, pattern2]'
    >>> color_patterns = '[pattern2, pattern3]'
    >>> combined = combine_pattern_lists(vein_patterns=vein_patterns,
    color_patterns=color_patterns)
    ['pattern1', 'pattern2', 'pattern3']

    """
    try:
        vein_list = ast.literal_eval(vein_patterns)
        if not isinstance(vein_list, list):
            raise ValueError("vein_patterns is not a valid list representation")
    except (ValueError, SyntaxError) as e:
        raise ValueError("vein_patterns is not a valid list representation") from e
    except Exception as e:
        raise TypeError("vein_patterns cannot be parsed into a list") from e
    
    try:
        color_list = ast.literal_eval(color_patterns)
        if not isinstance(color_list, list):
            raise ValueError("color_patterns is not a valid list representation")
    except (ValueError, SyntaxError) as e:
        raise ValueError("color_patterns is not a valid list representation") from e
    except Exception as e:
        raise TypeError("color_patterns cannot be parsed into a list") from e
    
    combined_list = []
    seen = set()
    
    for pattern in vein_list:
        if pattern not in seen:
            combined_list.append(pattern)
            seen.add(pattern)
    
    for pattern in color_list:
        if pattern not in seen:
            combined_list.append(pattern)
            seen.add(pattern)
    
    return combined_list