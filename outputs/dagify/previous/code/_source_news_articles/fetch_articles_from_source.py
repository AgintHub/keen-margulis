def fetch_articles_from_source(source: str) -> str:
    """
    Fetches news articles from a specified source and returns article metadata
    as a JSON string.

    Parameters
    ----------
    source : str
        Identifier of the news source to query (e.g., 'NYTimes', 'BBC').
        Must be a non-empty string.

    Returns
    -------
    str
        JSON-formatted string containing a dictionary with keys: 'urls',
        'titles', 'texts', and 'sources', each mapping to a list of strings.

    Raises
    ------
    ValueError
        Raised when the `source` argument is an empty string or represents
        an unsupported news source.
    TypeError
        Raised when the `source` argument is not of type `str`.

    Examples
    --------
    >>> result = fetch_articles_from_source('NYTimes')
    "{\"urls\": [\"https://nytimes.com/article1\"], \"titles\": [\"Breaking
    News\"], \"texts\": [\"Full article text...\"], \"sources\": [\"NYTimes\"]}"

    >>> try:
    ...     fetch_articles_from_source('')
    >>> except ValueError as e:
    ...     print(e)
    "Source identifier must be a non-empty string."

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")