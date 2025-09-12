from typing import List


def extract_chart_positions(chart_data: str) -> List[int]:
    """
    Parse a chart_data string to produce an ordered List[int] of chart
    positions.

    Parameters
    ----------
    chart_data : STR
        Raw chart data string containing numeric tokens separated by
        delimiters

    Returns
    -------
    LIST_INT
        List of parsed integer chart positions in the same order as tokens
        found in chart_data

    Raises
    ------
    ValueError
        Raised when a token cannot be parsed as an integer, or when input is
        not a string

    Examples
    --------
    >>> chart_data = '1, 4, 7, 9'
    >>> positions = extract_chart_positions(chart_data=chart_data)
    [1, 4, 7, 9]

    >>> chart_data = '2 5; 8'
    >>> positions = extract_chart_positions(chart_data=chart_data)
    [2, 5, 8]

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")