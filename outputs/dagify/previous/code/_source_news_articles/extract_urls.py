from typing import List


def extract_urls(data: str) -> List[str]:
    """
    Parses the input article data string to extract all URLs and returns them as
    a list of strings.

    Parameters
    ----------
    data : str
        A JSON-formatted string representation of article data containing
        URLs.

    Returns
    -------
    List[str]
        A list of URL strings extracted from the input data.

    Raises
    ------
    ValueError
        Raised when the input data does not contain any URLs.
    TypeError
        Raised when the input data is not a string.

    Examples
    --------
    >>> urls = extract_urls(data='{"content": "Check https://example.com and
    http://test.com"}')
    ['https://example.com', 'http://test.com']

    >>> urls = extract_urls(data='{}')
    []

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")