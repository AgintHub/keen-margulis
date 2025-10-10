from typing import List


def extract_titles(data: str) -> List[str]:
    """
    Extracts headline titles from a raw string of article data.

    Parameters
    ----------
    data : str
        A string representation of one or more articles. Each article should
        contain a line starting with 'Title: ' followed by the headline
        text.

    Returns
    -------
    list[str]
        A list of the extracted titles in the same order they appear in the
        input.

    Raises
    ------
    ValueError
        If the input string is empty or contains no titles.
    TypeError
        If the input parameter is not of type `str`.

    Examples
    --------
    >>> titles = extract_titles("Title: First News\nBody: ...\nTitle: Second
    News\nBody: ...")
    >>> print(titles)
    ['First News', 'Second News']

    >>> extract_titles(123)
    >>> extract_titles('')
    TypeError: data must be a string
    ValueError: input string contains no titles

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")