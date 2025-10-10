from typing import List


def extract_confidence_scores(results: str) -> List[float]:
    """
    Extracts sentiment confidence scores from a list of sentiment analysis
    result dictionaries.

    Parameters
    ----------
    results : List[dict]
        A list of dictionaries returned by the sentiment analysis batch
        function; each dictionary should contain a key
        'sentiment_confidence' mapping to a float between 0.0 and 1.0.

    Returns
    -------
    List[float]
        A list of confidence scores, preserving the order of the input
        results.

    Raises
    ------
    ValueError
        Raised if any result dictionary lacks the 'sentiment_confidence' key
        or if the value is not a float between 0.0 and 1.0.
    TypeError
        Raised if the input is not a list or if any element in the list is
        not a dictionary.

    Examples
    --------
    >>> sample_results = [
    ...     {'sentiment_confidence': 0.85},
    ...     {'sentiment_confidence': 0.42},
    >>> ]
    >>> extract_confidence_scores(sample_results)
    [0.85, 0.42]

    >>> invalid_results = [
    ...     {'confidence': 0.9},
    ...     {'sentiment_confidence': 0.75}
    >>> ]
    >>> extract_confidence_scores(invalid_results)
    ValueError: Missing or invalid 'sentiment_confidence' key in result
    dictionary.

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")