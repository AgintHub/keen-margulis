from ._serve_meal.validate_cooked_meal_input import validate_cooked_meal_input
from ._serve_meal.determine_plating_style import determine_plating_style
from ._serve_meal.prepare_serving_plate import prepare_serving_plate
from ._serve_meal.arrange_meal_on_plate import arrange_meal_on_plate
from ._serve_meal.add_garnish_and_presentation import add_garnish_and_presentation
from ._serve_meal.finalize_served_meal_name import finalize_served_meal_name

from pydantic import BaseModel, Field


class CookMealOutput(BaseModel):
    """Pydantic model for cook_meal node outputs."""
    cooked_meal: str = Field(..., description="Name of the cooked meal")


class ServeMealOutput(BaseModel):
    """Pydantic model for serve_meal node outputs."""
    served_meal: str = Field(..., description="Name of the served meal")


def serve_meal(cook_meal_input: CookMealOutput, **kwargs) -> ServeMealOutput:
    """
    Serves the cooked meal by taking the cooked meal name as input and returning
    the served meal name.

    Parameters
    ----------
    cooked_meal : str
        The name of the cooked meal, received from the cook_meal node.

    Returns
    -------
    str
        The name of the served meal.

    Raises
    ------
    ValueError
        If the cooked meal name is empty or not a string.

    Examples
    --------
    >>> serve_meal('Grilled Chicken')
    'Grilled Chicken'

    >>> serve_meal('Vegetable Soup')
    'Vegetable Soup'

    """
    cooked_meal_name: str = cook_meal_input.cooked_meal
    
    validate_cooked_meal_input(meal_name=cooked_meal_name)
    
    plating_style: str = determine_plating_style(meal_name=cooked_meal_name)
    
    prepare_serving_plate(style=plating_style)
    
    arrange_meal_on_plate(meal_name=cooked_meal_name, style=plating_style)
    
    add_garnish_and_presentation(meal_name=cooked_meal_name)
    
    served_meal_name: str = finalize_served_meal_name(meal_name=cooked_meal_name)
    
    return ServeMealOutput(served_meal=served_meal_name)