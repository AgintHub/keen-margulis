import json
import matplotlib.pyplot as plt
import os
import tempfile
import uuid


def create_color_distribution_chart(color_frequencies: str, color_names: str) -> str:
    """
    Creates a color distribution chart based on the provided color frequencies
    and names.

    Parameters
    ----------
    color_frequencies : str
        A string representation of color frequencies, expected to be a list
        or array that can be parsed.
    color_names : str
        A string representation of color names corresponding to the
        frequencies provided.

    Returns
    -------
    str
        The file path to the generated color distribution chart
        visualization.

    Raises
    ------
    ValueError
        If the input color frequencies or names are not in the expected
        format or are inconsistent.
    RuntimeError
        If the visualization generation fails for any reason.

    Examples
    --------
    >>> color_frequencies = '[0.2, 0.3, 0.5]'
    >>> color_names = '["red", "green", "blue"]'
    >>> output = create_color_distribution_chart(color_frequencies, color_names)
    '/path/to/visualization/file.png'

    >>> color_frequencies = '[0.1, 0.4, 0.5]'
    >>> color_names = '["yellow", "green", "blue"]'
    >>> output = create_color_distribution_chart(color_frequencies, color_names)
    '/path/to/another/visualization/file.png'

    """
    try:
        frequencies = json.loads(color_frequencies)
        names = json.loads(color_names)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format in input strings: {e}")
    
    if not isinstance(frequencies, list) or not isinstance(names, list):
        raise ValueError("Color frequencies and names must be lists")
    
    if len(frequencies) != len(names):
        raise ValueError("Color frequencies and names must have the same length")
    
    if not all(isinstance(f, (int, float)) for f in frequencies):
        raise ValueError("All color frequencies must be numeric")
    
    if not all(isinstance(n, str) for n in names):
        raise ValueError("All color names must be strings")
    
    try:
        plt.figure(figsize=(10, 6))
        plt.pie(frequencies, labels=names, autopct='%1.1f%%', startangle=90)
        plt.title('Color Distribution Chart')
        plt.axis('equal')
        
        temp_dir = tempfile.gettempdir()
        filename = f"color_distribution_{uuid.uuid4().hex}.png"
        filepath = os.path.join(temp_dir, filename)
        
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    except Exception as e:
        raise RuntimeError(f"Failed to generate visualization: {e}")