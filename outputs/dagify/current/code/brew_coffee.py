from ._brew_coffee.validate_brewing_readiness import validate_brewing_readiness
from ._brew_coffee.get_current_timestamp import get_current_timestamp
from ._brew_coffee.calculate_brewing_parameters import calculate_brewing_parameters
from ._brew_coffee.execute_brewing_process import execute_brewing_process
from ._brew_coffee.calculate_duration_seconds import calculate_duration_seconds
from ._brew_coffee.measure_final_temperature import measure_final_temperature
from ._brew_coffee.calculate_brewed_volume import calculate_brewed_volume

from pydantic import BaseModel, Field


class BoilWaterOutput(BaseModel):
    """Pydantic model for boil_water node outputs."""
    boiled: bool = (
        Field(..., description = (
            "Whether the water has reached the boiling point and is ready for brewing.")
        )
    )
    temperature_celsius: float = (
        Field(..., description = (
            "Current temperature of the water in degrees Celsius after boiling.")
        )
    )
    boil_time_seconds: int = (
        Field(..., description = (
            "Duration taken to bring the water to boiling temperature, measured in seconds.")
        )
    )


class PrepareCoffeeMakerOutput(BaseModel):
    """Pydantic model for prepare_coffee_maker node outputs."""
    coffee_grounds_amount_g: float = (
        Field(..., description = (
            "The amount of coffee grounds added to the coffee maker's filter in grams")
        )
    )
    filter_prepared: bool = (
        Field(..., description = (
            "Whether the filter is properly prepared and ready")
        )
    )
    coffee_maker_status: str = (
        Field(..., description = (
            "Current status of the coffee maker (e.g., 'ready', 'error')")
        )
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
        Field(..., description = (
            "Total duration of the brewing process in seconds")
        )
    )
    brewed_volume_cups: int = (
        Field(..., description="Number of cups of coffee brewed")
    )
    brewed_success: bool = (
        Field(..., description = (
            "Whether the brewing process completed successfully")
        )
    )
    final_temperature_c: float = (
        Field(..., description = (
            "Final temperature of the brewed coffee in degrees Celsius")
        )
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
    validate_brewing_readiness(water_status=boil_water_input, coffee_maker_status=prepare_coffee_maker_input)
    
    start_time: str = get_current_timestamp()
    
    brewing_parameters: dict = calculate_brewing_parameters(
        water_temp=boil_water_input.temperature_celsius,
        coffee_amount=prepare_coffee_maker_input.coffee_grounds_amount_g
    )
    
    brew_success: bool = execute_brewing_process(
        water_input=boil_water_input,
        coffee_maker_input=prepare_coffee_maker_input,
        parameters=brewing_parameters
    )
    
    end_time: str = get_current_timestamp()
    duration: float = calculate_duration_seconds(start_time=start_time, end_time=end_time)
    
    final_temp: float = measure_final_temperature(success=brew_success, initial_temp=boil_water_input.temperature_celsius)
    volume_cups: int = calculate_brewed_volume(coffee_amount=prepare_coffee_maker_input.coffee_grounds_amount_g)
    
    return BrewCoffeeOutput(
        brew_start_timestamp=start_time,
        brew_end_timestamp=end_time,
        brew_duration_seconds=duration,
        brewed_volume_cups=volume_cups,
        brewed_success=brew_success,
        final_temperature_c=final_temp
    )