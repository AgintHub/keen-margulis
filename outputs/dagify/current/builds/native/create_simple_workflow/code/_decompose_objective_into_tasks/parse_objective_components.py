from typing import List


def parse_objective_components(objective: str) -> List[str]:
    """
    Parses the provided objective string into a list of its constituent
    components.

    Parameters
    ----------
    objective : str
        A validated workflow objective string to be parsed.

    Returns
    -------
    List[str]
        A list of strings, each representing an actionable component of the
        objective.

    Raises
    ------
    ValueError
        Raised when the objective string cannot be parsed into any
        component.
    TypeError
        Raised when the provided objective is not of type str.

    Examples
    --------
    >>> parsed = parse_objective_components('Build a web app that allows users
    to upload photos and share them with friends')
    >>> print(parsed)
    ['Build a web app', 'allow users to upload photos', 'share them with
    friends']

    >>> parsed = parse_objective_components('Create a financial model to
    forecast quarterly earnings')
    >>> print(parsed)
    ['Create a financial model', 'forecast quarterly earnings']

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")