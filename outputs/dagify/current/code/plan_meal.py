from ._plan_meal.parse_meal_requirements import parse_meal_requirements
from ._plan_meal.select_recipe import select_recipe
from ._plan_meal.extract_meal_name import extract_meal_name
from ._plan_meal.identify_ingredients import identify_ingredients
from ._plan_meal.determine_cooking_techniques import determine_cooking_techniques
from ._plan_meal.format_ingredients_list import format_ingredients_list
from ._plan_meal.format_cooking_techniques import format_cooking_techniques

from pydantic import BaseModel, Field


class PlanMealOutput(BaseModel):
    """Pydantic model for plan_meal node outputs."""
    meal_name: str = Field(..., description="Name of the meal to be cooked")
    ingredients: str = (
        Field(..., description="List of ingredients required for the meal")
    )
    cooking_techniques: str = (
        Field(..., description="List of cooking techniques required for the meal")
    )


def plan_meal(general_input: str, **kwargs) -> PlanMealOutput:
    """
    Plan a meal based on the given prompt and return the meal details.

    Returns
    -------
    {meal_name: str, ingredients: List[str], cooking_techniques: List[str]}
        A dictionary containing the meal name, required ingredients, and
        cooking techniques.

    Raises
    ------
    ValueError
        If the meal planning fails due to invalid or insufficient data.

    Examples
    --------
    >>> plan_meal()
    {'meal_name': 'Grilled Chicken', 'ingredients': ['Chicken Breast', 'Olive
    Oil', 'Salt'], 'cooking_techniques': ['Grilling', 'Seasoning']}

    """
    parsed_requirements: dict = parse_meal_requirements(input_text=general_input)
    selected_recipe: dict = select_recipe(requirements=parsed_requirements)
    meal_name: str = extract_meal_name(recipe=selected_recipe)
    ingredients_list: list = identify_ingredients(recipe=selected_recipe)
    cooking_methods: list = determine_cooking_techniques(recipe=selected_recipe)
    formatted_ingredients: str = format_ingredients_list(ingredients=ingredients_list)
    formatted_techniques: str = format_cooking_techniques(techniques=cooking_methods)
    return PlanMealOutput(
        meal_name=meal_name,
        ingredients=formatted_ingredients,
        cooking_techniques=formatted_techniques
    )