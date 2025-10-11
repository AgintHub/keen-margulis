from typing import List


def extract_team_scores(parsed_scores: str) -> List[int]:
    """
    Extract team scores from a list of parsed score tuples.

    Parameters
    ----------
    parsed_scores : List[tuple]
        A list of tuples where each tuple contains two integers representing
        the team score and the opponent score, respectively.

    Returns
    -------
    List[int]
        A list of integers representing the team scores extracted from the
        input parsed scores.

    Raises
    ------
    ValueError
        If the input list is empty or if any tuple in the list does not
        contain exactly two integers.
    TypeError
        If the input is not a list of tuples or if the elements of the
        tuples are not integers.

    Examples
    --------
    >>> parsed_scores = [(74, 68), (80, 75), (90, 85)]
    >>> team_scores = extract_team_scores(parsed_scores)
    [74, 80, 90]

    >>> parsed_scores = [(60, 70), (65, 75), (70, 80)]
    >>> team_scores = extract_team_scores(parsed_scores)
    [60, 65, 70]

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")