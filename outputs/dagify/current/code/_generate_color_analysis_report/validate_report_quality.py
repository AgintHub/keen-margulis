import json
import os


def validate_report_quality(summary: str, visualization_path: str, input_data: str) -> bool:
    """
    Validates the quality of a generated color analysis report.

    Parameters
    ----------
    summary : str
        Summary text of the color analysis report
    visualization_path : str
        File path to the color distribution visualization
    input_data : str
        Original input data used for generating the report, expected to be a
        string representation of AnalyzeColorDistributionOutput

    Returns
    -------
    bool
        True if the report is valid and of good quality, False otherwise

    Raises
    ------
    ValueError
        If the input data is inconsistent or missing required fields
    TypeError
        If the input types are incorrect or if the input_data cannot be
        parsed into AnalyzeColorDistributionOutput

    Examples
    --------
    >>> summary_text = 'The most common colors are red, blue, and green.'
    >>> visualization_path = '/path/to/visualization.png'
    >>> input_data = AnalyzeColorDistributionOutput(color_frequencies=[0.3, 0.2,
    0.1], most_common_colors=['red', 'blue', 'green'],
    color_distribution_stats=[0.5, 0.2, 0.1])
    >>> validate_report_quality(summary=summary_text,
    visualization_path=visualization_path, input_data=input_data)
    True

    >>> summary_text = ''
    >>> visualization_path = '/path/to/visualization.png'
    >>> input_data = AnalyzeColorDistributionOutput(color_frequencies=[0.3, 0.2,
    0.1], most_common_colors=['red', 'blue', 'green'],
    color_distribution_stats=[0.5, 0.2, 0.1])
    >>> validate_report_quality(summary=summary_text,
    visualization_path=visualization_path, input_data=input_data)
    False

    """
    
    if not isinstance(summary, str):
        raise TypeError("summary must be a string")
    if not isinstance(visualization_path, str):
        raise TypeError("visualization_path must be a string")
    if not isinstance(input_data, str):
        raise TypeError("input_data must be a string")
    
    try:
        parsed_data = json.loads(input_data)
    except json.JSONDecodeError:
        raise TypeError("input_data cannot be parsed into AnalyzeColorDistributionOutput")
    
    required_fields = ['color_frequencies', 'most_common_colors', 'color_distribution_stats']
    for field in required_fields:
        if field not in parsed_data:
            raise ValueError(f"input data is missing required field: {field}")
    
    color_frequencies = parsed_data['color_frequencies']
    most_common_colors = parsed_data['most_common_colors']
    color_distribution_stats = parsed_data['color_distribution_stats']
    
    if not isinstance(color_frequencies, list) or not color_frequencies:
        raise ValueError("color_frequencies must be a non-empty list")
    if not isinstance(most_common_colors, list) or not most_common_colors:
        raise ValueError("most_common_colors must be a non-empty list")
    if not isinstance(color_distribution_stats, list) or not color_distribution_stats:
        raise ValueError("color_distribution_stats must be a non-empty list")
    
    for freq in color_frequencies:
        if not isinstance(freq, (int, float)) or freq < 0:
            raise ValueError("color_frequencies must contain non-negative numbers")
    
    for stat in color_distribution_stats:
        if not isinstance(stat, (int, float)) or stat < 0:
            raise ValueError("color_distribution_stats must contain non-negative numbers")
    
    for color in most_common_colors:
        if not isinstance(color, str) or not color.strip():
            raise ValueError("most_common_colors must contain non-empty strings")
    
    if len(color_frequencies) != len(most_common_colors):
        raise ValueError("color_frequencies and most_common_colors must have the same length")
    
    if not summary.strip():
        return False
    
    if not visualization_path.strip():
        return False
    
    if not os.path.exists(visualization_path):
        return False
    
    summary_lower = summary.lower()
    colors_mentioned = 0
    for color in most_common_colors:
        if color.lower() in summary_lower:
            colors_mentioned += 1
    
    if colors_mentioned < len(most_common_colors) * 0.5:
        return False
    
    return True