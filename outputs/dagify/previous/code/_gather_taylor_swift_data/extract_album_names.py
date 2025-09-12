from typing import List


def extract_album_names(discography_data: str) -> List[str]:
    """
    Extract album names from a discography JSON string.

    Parameters
    ----------
    discography_data : str
        JSON-formatted string containing the discography data.

    Returns
    -------
    List[str]
        A list of album names in the order they appear in the input.

    Raises
    ------
    ValueError
        Raised when the input is not valid JSON or the expected 'albums' key
        is missing.

    Examples
    --------
    >>> discography_data_json = '{"albums": ["Fearless", "1989", "Red"]}'
    >>> album_names = extract_album_names(discography_data_json)
    >>> print(album_names)
    ['Fearless', '1989', 'Red']

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")