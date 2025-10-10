from typing import List


def identify_irrelevant_articles(titles: str, texts: str) -> List[int]:
    """
    Returns the zero-based indices of news articles deemed irrelevant.

    Parameters
    ----------
    titles : List[str]
        List of article titles.
    texts : List[str]
        List of full article texts.

    Returns
    -------
    List[int]
        Zero-based indices of articles identified as irrelevant.

    Raises
    ------
    ValueError
        If the number of titles and texts differ or if any list is empty.
    TypeError
        If titles or texts are not lists of strings.

    Examples
    --------
    >>> titles = ['Short News', 'Detailed Report']
    >>> texts = ['Hi', 'This is a comprehensive analysis of the recent event.']
    >>> indices = identify_irrelevant_articles(titles, texts)
    >>> print(indices)
    [0]

    >>> titles = ['Empty', 'Irrelevant']
    >>> texts = ['', '!!!']
    >>> indices = identify_irrelevant_articles(titles, texts)
    >>> print(indices)
    [0, 1]

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")