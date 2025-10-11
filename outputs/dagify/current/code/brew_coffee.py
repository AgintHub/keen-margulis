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


class PrepareCoffeeMakerOutput(BaseModel):
    """Pydantic model for prepare_coffee_maker node outputs."""
    coffee_grounds_amount_g: float = (
        Field(..., description="The amount of coffee grounds added to the coffee maker's filter in grams")
    )
    filter_prepared: bool = (
        Field(..., description="Whether the filter is properly prepared and ready")
    )
    coffee_maker_status: str = (
        Field(..., description="Current status of the coffee maker (e.g., 'ready', 'error')")
    )


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


def brew_coffee(boil_water_input: BoilWaterOutput, prepare_coffee_maker_input: PrepareCoffeeMakerOutput, **kwargs) -> BrewCoffeeOutput:
    """
    Boil the specified liquid to its target boiling temperature and report
    readiness metrics.

    Parameters
    ----------
    target_temperature_celsius : float
        Desired boiling temperature for the liquid in degrees Celsius.

    Returns
    -------
    dict
        Dictionary containing boiled status, temperature, and boil time.

    Raises
    ------
    ValueError
        Raised if the liquid fails to reach the target temperature within
        the allowed timeframe.

    Examples
    --------
    >>> result = boil_any_liquid(target_temperature_celsius=100.0)
    >>> print(result['boiled'], result['temperature_celsius'],
    result['boil_time_seconds'])
    True 100.0 45

    """
    return BrewCoffeeOutput(
        brew_start_timestamp="",
        brew_end_timestamp="",
        brew_duration_seconds=0.0,
        brewed_volume_cups=0,
        brewed_success=False,
        final_temperature_c=0.0,
    )