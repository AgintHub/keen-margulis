from ._boil_water.extract_liquid_type import extract_liquid_type
from ._boil_water.extract_volume import extract_volume
from ._boil_water.validate_liquid_type import validate_liquid_type
from ._boil_water.get_boiling_point import get_boiling_point
from ._boil_water.get_heat_capacity import get_heat_capacity
from ._boil_water.simulate_heating_process import simulate_heating_process
from ._boil_water.check_boiling_status import check_boiling_status

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
    liquid_type: str = extract_liquid_type(general_input=general_input, kwargs=kwargs)
    volume: float = extract_volume(general_input=general_input, kwargs=kwargs)
    
    is_supported: bool = validate_liquid_type(liquid_type=liquid_type)
    if not is_supported:
        raise ValueError(f"Unsupported liquid type: {liquid_type}")
    
    boiling_point: float = get_boiling_point(liquid_type=liquid_type)
    heat_capacity: float = get_heat_capacity(liquid_type=liquid_type)
    
    heating_simulation: dict = simulate_heating_process(
        volume=volume,
        target_temperature=boiling_point,
        heat_capacity=heat_capacity
    )
    
    if not heating_simulation.get("converged", False):
        raise RuntimeError("Heating simulation failed to converge within realistic limits")
    
    final_temperature: float = heating_simulation["final_temperature"]
    boil_time: int = heating_simulation["time_seconds"]
    is_boiled: bool = check_boiling_status(temperature=final_temperature, boiling_point=boiling_point)
    
    return BoilWaterOutput(
        boiled=is_boiled,
        temperature_celsius=final_temperature,
        boil_time_seconds=boil_time
    )