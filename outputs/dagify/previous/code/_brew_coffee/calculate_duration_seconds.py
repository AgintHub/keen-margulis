def calculate_duration_seconds(start_time: str, end_time: str) -> float:
    """
    Computes the elapsed time in seconds between two ISO 8601 timestamps.

    Parameters
    ----------
    start_time : str
        The start timestamp in ISO 8601 format.
    end_time : str
        The end timestamp in ISO 8601 format.

    Returns
    -------
    float
        The duration in seconds between start_time and end_time.

    Raises
    ------
    ValueError
        If end_time is earlier than start_time or if timestamps cannot be
        parsed.
    TypeError
        If either start_time or end_time is not a string.

    Examples
    --------
    >>> duration = calculate_duration_seconds('2023-01-01T12:00:00Z',
    '2023-01-01T12:05:00Z')
    >>> duration
    300.0

    >>> calculate_duration_seconds('2023-01-01T12:05:00Z',
    '2023-01-01T12:00:00Z')
    ValueError: End time must be after start time.

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")