def validate_word_count_limit(word_count: str, max_words: str) -> str:
    """
    Validates that the provided word count does not exceed the maximum limit,
    raising a ValueError if the limit is exceeded.

    Parameters
    ----------
    word_count : int
        Current number of words in the generated summary.
    max_words : int
        Maximum number of words allowed for the summary.

    Returns
    -------
    str
        A message confirming successful validation, e.g. "Word count within
        limit (150/200)."

    Raises
    ------
    ValueError
        Raised when word_count exceeds max_words.
    TypeError
        Raised when word_count or max_words is not an integer.

    Examples
    --------
    >>> validate_word_count_limit(word_count=150, max_words=200)
    'Word count within limit (150/200).'

    >>> validate_word_count_limit(word_count=250, max_words=200)
    ValueError: 'Word count 250 exceeds maximum allowed 200.'

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")