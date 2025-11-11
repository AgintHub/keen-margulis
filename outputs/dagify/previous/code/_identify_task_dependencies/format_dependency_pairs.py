from typing import List


def format_dependency_pairs(dependencies: str) -> List[str]:
    """
    Converts a list of dependency tuples into formatted strings.

    Parameters
    ----------
    dependencies : List[tuple]
        A list of tuples where each tuple contains two task names (parent,
        child).

    Returns
    -------
    List[str]
        A list of strings, each representing a dependency pair in the form
        'parent -> child'.

    Raises
    ------
    ValueError
        Raised when the input list is empty or contains non‑tuple elements.
    TypeError
        Raised when the input is not a list.

    Examples
    --------
    >>> format_dependency_pairs([('Task1', 'Task2'), ('Task3', 'Task4')])
    ["Task1 -> Task2", "Task3 -> Task4"]

    >>> format_dependency_pairs([('A', 'B')])
    ["A -> B"]

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")