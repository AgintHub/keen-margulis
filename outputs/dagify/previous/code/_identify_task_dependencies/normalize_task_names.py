from typing import List


def normalize_task_names(task_names: str) -> List[str]:
    """
    Normalize task names to a consistent format.

    Parameters
    ----------
    task_names : List[str]
        A list of raw task names to be normalised.

    Returns
    -------
    List[str]
        The input names transformed to lowercase, stripped of
        leading/trailing whitespace, and with all non‑alphanumeric
        characters removed.

    Raises
    ------
    ValueError
        Raised if `task_names` is an empty list.
    TypeError
        Raised if any element of `task_names` is not a string.

    Examples
    --------
    >>> normalized = normalize_task_names(["  Deploy   App  ", "Test-API!",
    "Review/Docs"])
    >>> print(normalized)
    ['deploy app', 'testapi', 'reviewdocs']

    >>> try:
    ...     normalize_task_names([])
    >>> except ValueError as e:
    ...     print(str(e))
    "task_names list cannot be empty"

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")