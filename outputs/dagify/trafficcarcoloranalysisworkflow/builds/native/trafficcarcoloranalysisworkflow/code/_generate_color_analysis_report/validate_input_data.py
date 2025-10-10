import json


def validate_input_data(color_frequencies: str, most_common_colors: str, color_distribution_stats: str) -> bool:
    """
    Validates input data for color distribution analysis.

    Parameters
    ----------
    color_frequencies : str
        String representation of a list containing frequency of each
        observed vehicle color.
    most_common_colors : str
        String representation of a list containing most common vehicle
        colors observed.
    color_distribution_stats : str
        String representation of a list containing statistical measures
        (mean, median, std dev) of color distribution.

    Returns
    -------
    bool
        True if the input data is valid, False otherwise.

    Raises
    ------
    ValueError
        When input data is inconsistent or missing required fields.
    TypeError
        When input types are incorrect.

    Examples
    --------
    >>> validate_input_data(color_frequencies='[0.2, 0.3, 0.5]',
    most_common_colors='["red", "blue", "green"]',
    color_distribution_stats='[0.1, 0.2, 0.3]')
    True

    >>> validate_input_data(color_frequencies='[]', most_common_colors='["red",
    "blue"]', color_distribution_stats='[0.1, 0.2]')
    False

    """
    try:
        if not isinstance(color_frequencies, str) or not isinstance(most_common_colors, str) or not isinstance(color_distribution_stats, str):
            raise TypeError("All inputs must be strings")
        
        freq_list = json.loads(color_frequencies)
        colors_list = json.loads(most_common_colors)
        stats_list = json.loads(color_distribution_stats)
        
        if not isinstance(freq_list, list) or not isinstance(colors_list, list) or not isinstance(stats_list, list):
            raise ValueError("All inputs must be string representations of lists")
        
        if len(freq_list) == 0 or len(colors_list) == 0 or len(stats_list) == 0:
            return False
        
        if not all(isinstance(f, (int, float)) for f in freq_list):
            raise ValueError("Color frequencies must be numeric values")
        
        if not all(isinstance(c, str) for c in colors_list):
            raise ValueError("Most common colors must be strings")
        
        if not all(isinstance(s, (int, float)) for s in stats_list):
            raise ValueError("Color distribution stats must be numeric values")
        
        if len(freq_list) != len(colors_list):
            raise ValueError("Color frequencies and most common colors must have the same length")
        
        if len(stats_list) != 3:
            raise ValueError("Color distribution stats must contain exactly 3 values (mean, median, std dev)")
        
        if not all(f >= 0 for f in freq_list):
            raise ValueError("Color frequencies must be non-negative")
        
        return True
        
    except (json.JSONDecodeError, TypeError, ValueError):
        return False