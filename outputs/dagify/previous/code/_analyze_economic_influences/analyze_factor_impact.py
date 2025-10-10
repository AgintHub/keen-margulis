def analyze_factor_impact(factor_name: str, historical_context: str) -> str:
    """
    Analyzes the impact of a given factor on a specified historical context and
    returns a concise textual summary.

    Parameters
    ----------
    factor_name : str
        The name of the factor to analyze, e.g., an economic or social
        phenomenon.
    historical_context : str
        A textual description of the time period or events relevant to the
        factor.

    Returns
    -------
    str
        A short paragraph summarizing the factor’s influence on the provided
        historical context.

    Raises
    ------
    ValueError
        Raised if either factor_name or historical_context is an empty
        string.
    TypeError
        Raised if either factor_name or historical_context is not of type
        str.

    Examples
    --------
    >>> analyze_factor_impact('Great Depression', '1930s global economic
    downturn')
    'The Great Depression severely reduced industrial production and led to
    widespread unemployment across the globe, prompting significant policy
    reforms.'

    >>> analyze_factor_impact('Industrial Revolution', '18th–19th century
    Europe')
    'The Industrial Revolution transformed European societies by shifting
    production from manual labor to mechanized factories, which accelerated
    urbanization and altered social structures.'

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")