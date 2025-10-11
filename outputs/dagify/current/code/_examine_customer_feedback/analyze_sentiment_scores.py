from typing import List


def analyze_sentiment_scores(feedback_list: str) -> List[float]:
    """
    Analyzes the sentiment of customer feedback comments and returns a list of
    sentiment scores.

    Parameters
    ----------
    feedback_list : List[str]
        A list of customer feedback comments to be analyzed.

    Returns
    -------
    List[float]
        A list of sentiment scores between 0 and 1, where 0 represents very
        negative sentiment and 1 represents very positive sentiment.

    Raises
    ------
    ValueError
        If the input feedback_list is empty or contains non-string values.
    TypeError
        If the input feedback_list is not a list.

    Examples
    --------
    >>> feedback_list = ['I loved the service!', 'The product was okay.',
    'Terrible experience.']
    >>> sentiment_scores = analyze_sentiment_scores(feedback_list=feedback_list)
    [0.9, 0.5, 0.1]

    >>> feedback_list = ['Great product!', 'Average service.', 'Poor quality.']
    >>> sentiment_scores = analyze_sentiment_scores(feedback_list=feedback_list)
    [0.8, 0.4, 0.2]

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")