from typing import List


def extract_opponent_scores(parsed_scores: str) -> List[int]:
    """
    Extract opponent scores from a list of parsed score tuples.

    Parameters
    ----------
    parsed_scores : List[tuple[int, int]]
        List of tuples containing team and opponent scores

    Returns
    -------
    List[int]
        List of opponent scores as integers

    Raises
    ------
    TypeError
        If parsed_scores is not a list of tuples or if tuple elements are
        not integers
    ValueError
        If parsed_scores list is empty or contains tuples without exactly
        two elements

    Examples
    --------
    >>> parsed_scores = [(100, 90), (80, 95), (70, 85)]
    >>> opponent_scores = extract_opponent_scores(parsed_scores=parsed_scores)
    [90, 95, 85]

    >>> parsed_scores = [(75, 80), (90, 85)]
    >>> opponent_scores = extract_opponent_scores(parsed_scores=parsed_scores)
    [80, 85]

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")