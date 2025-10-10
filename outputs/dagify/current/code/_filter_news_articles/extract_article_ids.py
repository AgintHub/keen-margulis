from typing import List


def extract_article_ids(titles: str, indices: str) -> List[str]:
    """
    Return the titles of articles at the supplied indices.

    Parameters
    ----------
    titles : List[str]
        A list of article titles in the original order.
    indices : List[int]
        A list of integer indices specifying which titles to extract.

    Returns
    -------
    List[str]
        A list of titles at the requested indices, preserving the order of
        indices.

    Raises
    ------
    ValueError
        Raised when an index is out of bounds for the titles list.
    TypeError
        Raised when titles is not a list of strings or indices is not a list
        of integers.

    Examples
    --------
    >>> titles = ['Alpha', 'Beta', 'Gamma', 'Delta']
    >>> indices = [0, 2, 3]
    >>> result = extract_article_ids(titles, indices)
    >>> print(result)
    ['Alpha', 'Gamma', 'Delta']

    >>> titles = ['One', 'Two', 'Three']
    >>> indices = []
    >>> result = extract_article_ids(titles, indices)
    >>> print(result)
    []

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")