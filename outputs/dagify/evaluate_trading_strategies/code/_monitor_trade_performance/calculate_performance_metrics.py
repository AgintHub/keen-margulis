from typing import List


def calculate_performance_metrics(outcomes: str, volumes: str) -> List[float]:
    """
    Calculate performance metrics for a series of trades.

    Parameters
    ----------
    outcomes : List[str]
        A list of trade outcomes, e.g., ['profit', 'loss', 'neutral'].
    volumes : List[int]
        A list of integers representing trade volumes corresponding to each
        outcome.

    Returns
    -------
    List[float]
        A list of floats representing computed performance metrics for each
        trade.

    Raises
    ------
    ValueError
        Raised when the lengths of outcomes and volumes do not match or when
        invalid outcome strings are provided.
    TypeError
        Raised when the input arguments are not of type list or contain
        elements of incorrect type.

    Examples
    --------
    >>> outcomes = ['profit', 'loss', 'neutral', 'profit']
    >>> volumes = [100, 200, 150, 120]
    >>> metrics = calculate_performance_metrics(outcomes, volumes)
    >>> print(metrics)
    [0.6, -0.5, 0.0, 0.4]

    >>> outcomes = ['loss', 'loss']
    >>> volumes = [300, 300]
    >>> metrics = calculate_performance_metrics(outcomes, volumes)
    >>> print(metrics)
    [-1.0, -1.0]

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")