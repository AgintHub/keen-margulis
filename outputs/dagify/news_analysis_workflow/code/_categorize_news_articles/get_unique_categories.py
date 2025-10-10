from typing import List


def get_unique_categories(categories: str) -> List[str]:
    """
    Return a list of unique categories from the provided list, preserving the
    original order of first appearance.

    Parameters
    ----------
    categories : List[str]
        A list of category labels, each a string. The function expects a
        non-empty list containing only strings.

    Returns
    -------
    List[str]
        A list containing each distinct category from `categories` exactly
        once, ordered by the first time it appeared in the input list.

    Raises
    ------
    TypeError
        Raised if `categories` is not a list or if any element is not a
        string.
    ValueError
        Raised if `categories` is an empty list.

    Examples
    --------
    >>> unique = get_unique_categories(['sports', 'politics', 'sports', 'tech'])
    ['sports', 'politics', 'tech']

    >>> unique = get_unique_categories([])
    ValueError: Input list cannot be empty.

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")