from ._prepare_coffee_maker.validate_measurement_inputs import validate_measurement_inputs
from ._prepare_coffee_maker.load_grounds_into_filter import load_grounds_into_filter
from ._prepare_coffee_maker.verify_filter_readiness import verify_filter_readiness
from ._prepare_coffee_maker.check_coffee_maker_status import check_coffee_maker_status

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
        Field(..., description = (
            "Type of coffee grounds used (e.g., medium grind, dark roast)")
        )
    )
    measurement_valid: bool = (
        Field(..., description = (
            "Indicates whether the measurement was performed correctly")
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


def prepare_coffee_maker(measure_coffee_input: MeasureCoffeeOutput, **kwargs) -> PrepareCoffeeMakerOutput:
    """
    Adds the specified amount of coffee grounds into the coffee maker's filter,
    validates the measurement, and reports the amount added, filter status, and
    overall maker status.

    Parameters
    ----------
    ground_amount_grams : float
        Amount of coffee grounds measured in grams (from measure_coffee).
    desired_cup_count : int
        Number of coffee cups to be brewed (from measure_coffee).
    grounds_type : str
        Type of coffee grounds used (e.g., medium grind, dark roast).
    measurement_valid : bool
        Flag indicating whether the measurement was performed correctly.

    Returns
    -------
    dict
        Dictionary with keys `coffee_grounds_amount_g` (float),
        `filter_prepared` (bool), and `coffee_maker_status` (str).

    Raises
    ------
    ValueError
        If `measurement_valid` is False or `ground_amount_grams` is
        non‑positive.

    Examples
    --------
    >>> result = prepare_coffee_maker(
    ...     ground_amount_grams=15.0,
    ...     desired_cup_count=2,
    ...     grounds_type='medium',
    ...     measurement_valid=True)
    >>> print(result)
    {'coffee_grounds_amount_g': 15.0, 'filter_prepared': True,
    'coffee_maker_status': 'ready'}

    >>> try:
    ...     prepare_coffee_maker(
    ...         ground_amount_grams=15.0,
    ...         desired_cup_count=2,
    ...         grounds_type='medium',
    ...         measurement_valid=False)
    >>> except ValueError as e:
    ...     print(e)
    Invalid measurement: measurement_valid is False

    """
    validate_measurement_inputs(
        measurement_valid=measure_coffee_input.measurement_valid,
        ground_amount_grams=measure_coffee_input.ground_amount_grams
    )
    
    load_grounds_into_filter(
        amount_grams=measure_coffee_input.ground_amount_grams,
        grounds_type=measure_coffee_input.grounds_type
    )
    
    filter_status: bool = verify_filter_readiness(
        expected_amount=measure_coffee_input.ground_amount_grams,
        cup_count=measure_coffee_input.desired_cup_count
    )
    
    maker_status: str = check_coffee_maker_status(
        filter_prepared=filter_status,
        grounds_loaded=True
    )
    
    return PrepareCoffeeMakerOutput(
        coffee_grounds_amount_g=measure_coffee_input.ground_amount_grams,
        filter_prepared=filter_status,
        coffee_maker_status=maker_status
    )