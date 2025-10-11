from pydantic import BaseModel, Field


class BoilWaterOutput(BaseModel):
    """Pydantic model for boil_water node outputs."""
    boiled: bool = (
        Field(..., description="Whether the water has reached the boiling point and is ready for brewing.")
    )
    temperature_celsius: float = (
        Field(..., description="Current temperature of the water in degrees Celsius after boiling.")
    )
    boil_time_seconds: int = (
        Field(..., description="Duration taken to bring the water to boiling temperature, measured in seconds.")
    )


def boil_water(general_input: str, **kwargs) -> BoilWaterOutput:
    """
    Heats a liquid to its boiling point and returns the readiness status, final
    temperature, and heating duration.

    Parameters
    ----------
    liquid_type : str
        Name of the liquid to be boiled (e.g., "water", "milk", "tea").
    volume : float
        Volume of the liquid in liters.

    Returns
    -------
    dict
        Dictionary containing `boiled` (bool), `temperature_celsius`
        (float), and `boil_time_seconds` (int).

    Raises
    ------
    ValueError
        Raised if an unsupported liquid type is provided.
    RuntimeError
        Raised if the heating simulation fails to converge within realistic
        limits.

    Examples
    --------
    >>> result = boil_liquid(liquid_type='water', volume=0.5)
    >>> print(result)
    {'boiled': True, 'temperature_celsius': 100.0, 'boil_time_seconds': 90}

    """
    return BoilWaterOutput(
        boiled=False,
        temperature_celsius=0.0,
        boil_time_seconds=0,
    )