from typing import List


def combine_variation_lists(vein_variations: str, color_variations: str) -> List[str]:
    """
    Combines two input strings representing vein and color variations into a
    unified list of variations.

    Parameters
    ----------
    vein_variations : str
        A string representing the variations in vein patterns.
    color_variations : str
        A string representing the variations in color patterns.

    Returns
    -------
    List[str]
        A list containing the combined variations of vein and color
        patterns.

    Raises
    ------
    ValueError
        If either of the input strings is not properly formatted or empty.
    TypeError
        If the input parameters are not of type string.

    Examples
    --------
    >>> vein_variations = 'looped,netted,parallel'
    >>> color_variations = 'green,blue,yellow'
    >>> result = combine_variation_lists(vein_variations=vein_variations,
    color_variations=color_variations)
    ['looped', 'netted', 'parallel', 'green', 'blue', 'yellow']

    >>> vein_variations = 'simple,complex'
    >>> color_variations = 'red,green'
    >>> result = combine_variation_lists(vein_variations=vein_variations,
    color_variations=color_variations)
    ['simple', 'complex', 'red', 'green']

    """
    if not isinstance(vein_variations, str):
        raise TypeError("vein_variations must be of type string")
    if not isinstance(color_variations, str):
        raise TypeError("color_variations must be of type string")
    
    if not vein_variations.strip() or not color_variations.strip():
        raise ValueError("Input strings cannot be empty or contain only whitespace")
    
    vein_list = [item.strip() for item in vein_variations.split(',') if item.strip()]
    color_list = [item.strip() for item in color_variations.split(',') if item.strip()]
    
    if not vein_list or not color_list:
        raise ValueError("Input strings are not properly formatted")
    
    return vein_list + color_list