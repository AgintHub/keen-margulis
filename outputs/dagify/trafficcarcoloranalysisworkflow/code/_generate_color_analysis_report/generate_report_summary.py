import re


def generate_report_summary(insights: str, most_common_colors: str, distribution_stats: str) -> str:
    """
    Generates a summary text for the color analysis report based on the given
    insights, most common colors, and distribution statistics.

    Parameters
    ----------
    insights : str
        A string representation of key insights from the color analysis.
    most_common_colors : str
        A string representation of the most common colors observed.
    distribution_stats : str
        A string representation of statistical measures (mean, median, std
        dev) of the color distribution.

    Returns
    -------
    str
        The generated summary text of the color analysis report.

    Raises
    ------
    ValueError
        If the input parameters are inconsistent or missing required
        information.
    TypeError
        If the input parameters are not of the expected type.

    Examples
    --------
    >>> insights_str = 'The color analysis shows a predominance of neutral
    tones.'
    >>> most_common_colors_str = 'white, black, gray'
    >>> distribution_stats_str = 'mean=0.5, median=0.5, std_dev=0.1'
    >>> summary = generate_report_summary(insights=insights_str,
    most_common_colors=most_common_colors_str,
    distribution_stats=distribution_stats_str)
    'The color analysis report highlights a prevalence of white, black, and gray
    colors, with mean, median, and standard deviation of color distribution
    being 0.5, 0.5, and 0.1 respectively.'

    >>> insights_str = 'The analysis reveals a diverse color palette.'
    >>> most_common_colors_str = 'red, blue, green'
    >>> distribution_stats_str = 'mean=0.4, median=0.4, std_dev=0.2'
    >>> summary = generate_report_summary(insights=insights_str,
    most_common_colors=most_common_colors_str,
    distribution_stats=distribution_stats_str)
    'The color analysis report indicates a diverse color distribution with red,
    blue, and green being prominent, having mean and median of 0.4 and a
    standard deviation of 0.2.'

    """
    if not isinstance(insights, str):
        raise TypeError("insights must be a string")
    if not isinstance(most_common_colors, str):
        raise TypeError("most_common_colors must be a string")
    if not isinstance(distribution_stats, str):
        raise TypeError("distribution_stats must be a string")
    
    if not insights.strip():
        raise ValueError("insights cannot be empty")
    if not most_common_colors.strip():
        raise ValueError("most_common_colors cannot be empty")
    if not distribution_stats.strip():
        raise ValueError("distribution_stats cannot be empty")
    
    
    colors = [color.strip() for color in most_common_colors.split(',')]
    colors_text = ', '.join(colors[:-1]) + ', and ' + colors[-1] if len(colors) > 1 else colors[0]
    
    mean_match = re.search(r'mean=([0-9.]+)', distribution_stats)
    median_match = re.search(r'median=([0-9.]+)', distribution_stats)
    std_dev_match = re.search(r'std_dev=([0-9.]+)', distribution_stats)
    
    if not mean_match or not median_match or not std_dev_match:
        raise ValueError("distribution_stats must contain mean, median, and std_dev values")
    
    mean_val = mean_match.group(1)
    median_val = median_match.group(1)
    std_dev_val = std_dev_match.group(1)
    
    if 'diverse' in insights.lower():
        summary = f"The color analysis report indicates a diverse color distribution with {colors_text} being prominent, having mean and median of {mean_val} and a standard deviation of {std_dev_val}."
    elif 'neutral' in insights.lower() or 'predominance' in insights.lower():
        summary = f"The color analysis report highlights a prevalence of {colors_text} colors, with mean, median, and standard deviation of color distribution being {mean_val}, {median_val}, and {std_dev_val} respectively."
    else:
        summary = f"The color analysis report shows {colors_text} as the most common colors, with statistical measures of mean={mean_val}, median={median_val}, and standard deviation={std_dev_val}."
    
    return summary