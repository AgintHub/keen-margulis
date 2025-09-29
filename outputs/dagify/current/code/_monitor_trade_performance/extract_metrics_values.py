from typing import List


def extract_metrics_values(performance_data: str) -> List[float]:
    """
    Extracts numerical performance metrics from the input performance data
    string.

    Parameters
    ----------
    performance_data : str
        A string representation of performance metrics calculated by the
        calculate_performance_metrics function.

    Returns
    -------
    List[float]
        A list of numerical performance metrics extracted from the input
        string.

    Raises
    ------
    ValueError
        If the input string is malformed or cannot be parsed into numerical
        metrics.
    TypeError
        If the input is not a string.

    Examples
    --------
    >>> performance_data = 'returns:0.05,Sharpe_ratio:1.2,max_drawdown:0.15'
    >>> extracted_metrics = extract_metrics_values(performance_data)
    [0.05, 1.2, 0.15]

    >>> performance_data = 'metric1:10,metric2:20.5,metric3:30.2'
    >>> extracted_metrics = extract_metrics_values(performance_data)
    [10.0, 20.5, 30.2]

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")