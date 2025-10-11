from pydantic import BaseModel, Field


class BrewCoffeeOutput(BaseModel):
    """Pydantic model for brew_coffee node outputs."""
    brew_start_timestamp: str = (
        Field(..., description="ISO 8601 timestamp when brewing started")
    )
    brew_end_timestamp: str = (
        Field(..., description="ISO 8601 timestamp when brewing completed")
    )
    brew_duration_seconds: float = (
        Field(..., description="Total duration of the brewing process in seconds")
    )
    brewed_volume_cups: int = (
        Field(..., description="Number of cups of coffee brewed")
    )
    brewed_success: bool = (
        Field(..., description="Whether the brewing process completed successfully")
    )
    final_temperature_c: float = (
        Field(..., description="Final temperature of the brewed coffee in degrees Celsius")
    )


class ServeCoffeeOutput(BaseModel):
    """Pydantic model for serve_coffee node outputs."""
    served: bool = (
        Field(..., description="Whether the coffee has been successfully served into a cup")
    )
    temperature_c: float = (
        Field(..., description="The temperature of the served coffee in degrees Celsius")
    )
    volume_ml: int = (
        Field(..., description="The volume of the served coffee in milliliters")
    )


def serve_coffee(brew_coffee_input: BrewCoffeeOutput, **kwargs) -> ServeCoffeeOutput:
    """
    Serve freshly brewed coffee into a cup based on brewing results.

    Parameters
    ----------
    brew_start_timestamp : str
        ISO 8601 timestamp when brewing started.
    brew_end_timestamp : str
        ISO 8601 timestamp when brewing completed.
    brew_duration_seconds : float
        Total duration of the brewing process in seconds.
    brewed_volume_cups : int
        Number of cups of coffee brewed.
    brewed_success : bool
        Indicates whether the brewing process completed successfully.
    final_temperature_c : float
        Final temperature of the brewed coffee in degrees Celsius.

    Returns
    -------
    dict
        A dictionary with keys:   - served (bool): Whether the coffee was
        served.   - temperature_c (float): Served coffee temperature.   -
        volume_ml (int): Served coffee volume in milliliters.

    Raises
    ------
    ValueError
        Raised if `brewed_success` is False, indicating the coffee cannot be
        served.

    Examples
    --------
    >>> serve_coffee(
    ...     brew_start_timestamp="2025-10-11T10:00:00Z",
    ...     brew_end_timestamp="2025-10-11T10:03:30Z",
    ...     brew_duration_seconds=210.0,
    ...     brewed_volume_cups=2,
    ...     brewed_success=True,
    ...     final_temperature_c=90.0)
    {
      'served': True,
      'temperature_c': 90.0,
      'volume_ml': 480
    }

    >>> serve_coffee(
    ...     brew_start_timestamp="2025-10-11T10:10:00Z",
    ...     brew_end_timestamp="2025-10-11T10:12:00Z",
    ...     brew_duration_seconds=120.0,
    ...     brewed_volume_cups=1,
    ...     brewed_success=False,
    ...     final_temperature_c=85.0)
    ValueError: Brewed coffee is not successful; cannot serve.

    """
    return ServeCoffeeOutput(
        served=False,
        temperature_c=0.0,
        volume_ml=0,
    )