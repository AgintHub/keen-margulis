from typing import List


def extract_release_dates(discography_data: str) -> List[str]:
    """
    Extracts release dates for each album from the provided discography metadata
    JSON.

    Parameters
    ----------
    discography_data : str
        JSON string representing the discography metadata containing album
        names and release dates.

    Returns
    -------
    List[str]
        A list of album release dates extracted from the input data.

    Raises
    ------
    ValueError
        Raised when the input JSON is invalid or missing required fields.

    Examples
    --------
    >>> import json
    >>> # Sample discography data
    >>> sample_json = json.dumps({
    ...     "albums": [
    ...         {"name": "Album1", "release_date": "2020-01-01"},
    ...         {"name": "Album2", "release_date": "2021-01-01"}
    ...     ]
    >>> })
    >>> release_dates = extract_release_dates(sample_json)
    >>> print(release_dates)
    ["2020-01-01", "2021-01-01"]

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")