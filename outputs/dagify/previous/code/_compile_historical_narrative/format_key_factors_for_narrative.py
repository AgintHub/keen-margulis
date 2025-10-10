from typing import List


def format_key_factors_for_narrative(factors: str, assessments: str) -> List[str]:
    """
    Formats key factors and impact assessments into narrative-friendly strings
    for use in a historical narrative.

    Parameters
    ----------
    factors : List[str]
        List of key factor names extracted from the analysis.
    assessments : List[str]
        List of impact assessments (e.g., 'high', 'medium', 'low')
        corresponding to each factor.

    Returns
    -------
    List[str]
        A list where each element is a string in the form '<factor>:
        <assessment> impact', ready for narrative inclusion.

    Raises
    ------
    ValueError
        Raised when the lengths of `factors` and `assessments` differ or
        when either list is empty.
    TypeError
        Raised when `factors` or `assessments` are not lists of strings.

    Examples
    --------
    >>> format_key_factors_for_narrative(factors=['Economy', 'Culture'],
    assessments=['high', 'medium'])
    ['Economy: high impact', 'Culture: medium impact']

    >>> format_key_factors_for_narrative(factors=['Infrastructure'],
    assessments=['low'])
    ['Infrastructure: low impact']

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")