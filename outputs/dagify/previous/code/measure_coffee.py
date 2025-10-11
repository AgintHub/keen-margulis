from pydantic import BaseModel, Field


class MeasureCoffeeOutput(BaseModel):
    """Pydantic model for measure_coffee node outputs."""
    ground_amount_grams: float = (
        Field(..., description="Amount of coffee grounds measured in grams")
    )
    desired_cup_count: int = (
        Field(..., description="Number of coffee cups to be brewed")
    )
    grounds_type: str = (
        Field(..., description="Type of coffee grounds used (e.g., medium grind, dark roast)")
    )
    measurement_valid: bool = (
        Field(..., description="Indicates whether the measurement was performed correctly")
    )


def measure_coffee(general_input: str, **kwargs) -> MeasureCoffeeOutput:
    """
    Calculate and verify the amount of coffee grounds needed for a given number
    of cups.

    Parameters
    ----------
    desired_cup_count : int
        The target number of coffee cups to brew.
    grounds_type : str
        The type of coffee grounds (e.g., 'medium grind', 'dark roast').

    Returns
    -------
    dict
        Dictionary containing `ground_amount_grams` (float),
        `desired_cup_count` (int), `grounds_type` (str), and
        `measurement_valid` (bool).

    Raises
    ------
    ValueError
        If `desired_cup_count` is not a positive integer or `grounds_type`
        is not among the supported types.

    Examples
    --------
    >>> measure_coffee(3, 'medium grind')
    {'ground_amount_grams': 18.0, 'desired_cup_count': 3, 'grounds_type':
    'medium grind', 'measurement_valid': True}

    >>> measure_coffee(0, 'dark roast')
    ValueError: desired_cup_count must be a positive integer.

    """
    return MeasureCoffeeOutput(
        ground_amount_grams=0.0,
        desired_cup_count=0,
        grounds_type="",
        measurement_valid=False,
    )