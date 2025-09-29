from ._cook_meal.extract_cooking_techniques import extract_cooking_techniques
from ._cook_meal.validate_cooking_techniques import validate_cooking_techniques
from ._cook_meal.validate_ingredients_sufficiency import validate_ingredients_sufficiency
from ._cook_meal.create_cooking_plan import create_cooking_plan
from ._cook_meal.execute_cooking_process import execute_cooking_process
from ._cook_meal.finalize_meal_name import finalize_meal_name

from pydantic import BaseModel, Field
from typing import List


class PrepareIngredientsOutput(BaseModel):
    """Pydantic model for prepare_ingredients node outputs."""
    prepared_ingredients: List[str] = (
        Field(..., description="List of prepared ingredients")
    )


class CookMealOutput(BaseModel):
    """Pydantic model for cook_meal node outputs."""
    cooked_meal: str = Field(..., description="Name of the cooked meal")


def cook_meal(prepare_ingredients_input: PrepareIngredientsOutput, **kwargs) -> CookMealOutput:
    """
    Cooks a meal using the prepared ingredients and identified cooking
    techniques.

    Parameters
    ----------
    prepared_ingredients : List[str]
        List of ingredients that have been prepared for cooking.
    cooking_techniques : List[str]
        List of cooking techniques required for the meal, derived from the
        meal plan.

    Returns
    -------
    str
        The name of the meal that has been cooked.

    Raises
    ------
    ValueError
        If the prepared ingredients are not sufficient for cooking the meal.
    TypeError
        If the cooking techniques are not provided or are of incorrect type.

    Examples
    --------
    >>> prepared_ingredients = ['chopped onions', 'minced garlic', 'sliced
    chicken']
    >>> cooking_techniques = ['grilling', 'sauteing']
    >>> cooked_meal = cook_meal(prepared_ingredients, cooking_techniques)
    'Grilled Chicken'

    """
    cooking_techniques: List[str] = extract_cooking_techniques(kwargs=kwargs)
    validate_cooking_techniques(cooking_techniques=cooking_techniques)
    validate_ingredients_sufficiency(prepared_ingredients=prepare_ingredients_input.prepared_ingredients, cooking_techniques=cooking_techniques)
    cooking_plan: dict = create_cooking_plan(prepared_ingredients=prepare_ingredients_input.prepared_ingredients, cooking_techniques=cooking_techniques)
    cooked_result: str = execute_cooking_process(cooking_plan=cooking_plan)
    final_meal_name: str = finalize_meal_name(cooked_result=cooked_result)
    return CookMealOutput(cooked_meal=final_meal_name)