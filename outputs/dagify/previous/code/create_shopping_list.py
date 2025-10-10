from ._create_shopping_list.validate_meal_plan_input import validate_meal_plan_input
from ._create_shopping_list.extract_ingredients_from_plan import extract_ingredients_from_plan
from ._create_shopping_list.process_shopping_ingredients import process_shopping_ingredients

from pydantic import BaseModel, Field
from typing import List


class PlanMealOutput(BaseModel):
    """Pydantic model for plan_meal node outputs."""
    meal_name: str = Field(..., description="Name of the meal to be cooked")
    ingredients: str = (
        Field(..., description="List of ingredients required for the meal")
    )
    cooking_techniques: str = (
        Field(..., description="List of cooking techniques required for the meal")
    )


class CreateShoppingListOutput(BaseModel):
    """Pydantic model for create_shopping_list node outputs."""
    shopping_list: List[str] = (
        Field(..., description="List of ingredients to purchase")
    )


def create_shopping_list(plan_meal_input: PlanMealOutput, **kwargs) -> CreateShoppingListOutput:
    """
    Create a shopping list from the meal plan ingredients.

    Parameters
    ----------
    meal_plan : dict
        Meal plan details containing ingredients, meal name, and cooking
        techniques.

    Returns
    -------
    List[str]
        A list of ingredients to purchase for the meal.

    Raises
    ------
    KeyError
        If 'ingredients' key is missing from the meal plan.
    TypeError
        If the meal plan is not a dictionary or if ingredients is not a
        list.

    Examples
    --------
    >>> meal_plan = {'meal_name': 'Pasta', 'ingredients': ['pasta', 'sauce',
    'cheese'], 'cooking_techniques': ['boiling', 'heating']}
    >>> shopping_list = create_shopping_list(meal_plan)
    >>> print(shopping_list)
    ['pasta', 'sauce', 'cheese']

    >>> meal_plan = {'meal_name': 'Salad', 'ingredients': ['lettuce',
    'tomatoes', 'cucumber'], 'cooking_techniques': []}
    >>> shopping_list = create_shopping_list(meal_plan)
    >>> print(shopping_list)
    ['lettuce', 'tomatoes', 'cucumber']

    """
    validated_input: dict = validate_meal_plan_input(meal_plan=plan_meal_input)
    ingredients_list: List[str] = extract_ingredients_from_plan(meal_plan=validated_input)
    processed_ingredients: List[str] = process_shopping_ingredients(ingredients=ingredients_list)
    return CreateShoppingListOutput(shopping_list=processed_ingredients)