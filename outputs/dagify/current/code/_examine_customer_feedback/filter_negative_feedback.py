from typing import List


def filter_negative_feedback(feedback_list: str, sentiment_scores: str) -> List[str]:
    """
    Filters negative customer feedback based on sentiment scores.

    Parameters
    ----------
    feedback_list : str
        A string representation of a list of customer feedback comments.
    sentiment_scores : str
        A string representation of a list of sentiment scores corresponding
        to the feedback comments.

    Returns
    -------
    List[str]
        A list of negative customer feedback comments.

    Raises
    ------
    ValueError
        When the input lists are not of the same length or when the
        sentiment scores are not valid.
    TypeError
        When the input types are incorrect.

    Examples
    --------
    >>> feedback_list = '["Great product!", "Terrible service.", "Average
    experience."]'
    >>> sentiment_scores = '[0.8, -0.7, 0.1]'
    >>> filter_negative_feedback(feedback_list=feedback_list,
    sentiment_scores=sentiment_scores)
    ["Terrible service."]

    >>> feedback_list = '["Love the product!", "Hate the service.", "Okay
    experience."]'
    >>> sentiment_scores = '[0.9, -0.8, 0.2]'
    >>> filter_negative_feedback(feedback_list=feedback_list,
    sentiment_scores=sentiment_scores)
    ["Hate the service."]

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")