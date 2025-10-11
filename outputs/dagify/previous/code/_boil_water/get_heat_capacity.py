def get_heat_capacity(liquid_type: str) -> float:
    """
    Return the specific heat capacity of a given liquid.

    Parameters
    ----------
    liquid_type : str
        Name of the liquid (e.g., 'water', 'ethanol').

    Returns
    -------
    float
        Heat capacity of the liquid in J/(kg·K).

    Raises
    ------
    ValueError
        Raised when the specified liquid type is not supported.
    TypeError
        Raised when liquid_type is not a string.

    Examples
    --------
    >>> from get_heat_capacity import get_heat_capacity
    >>> print(get_heat_capacity('water'))
    4186.0

    >>> print(get_heat_capacity('ethanol'))
    2420.0

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")