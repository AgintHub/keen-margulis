from ._prepare_ingredients.validate_meal_plan import validate_meal_plan
from ._prepare_ingredients.validate_ingredient_compatibility import validate_ingredient_compatibility
from ._prepare_ingredients.parse_ingredients_from_plan import parse_ingredients_from_plan
from ._prepare_ingredients.parse_cooking_techniques import parse_cooking_techniques
from ._prepare_ingredients.determine_prep_methods import determine_prep_methods
from ._prepare_ingredients.apply_preparation_methods import apply_preparation_methods

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


class PurchaseIngredientsOutput(BaseModel):
    """Pydantic model for purchase_ingredients node outputs."""
    purchased_ingredients: List[str] = (
        Field(..., description="List of ingredients purchased")
    )


class PrepareIngredientsOutput(BaseModel):
    """Pydantic model for prepare_ingredients node outputs."""
    prepared_ingredients: List[str] = (
        Field(..., description="List of prepared ingredients")
    )


def prepare_ingredients(plan_meal_input: PlanMealOutput, purchase_ingredients_input: PurchaseIngredientsOutput, **kwargs) -> PrepareIngredientsOutput:
    """
    Prepare ingredients by washing, chopping, and measuring them according to
    the meal plan.

    Parameters
    ----------
    meal_plan : dict
        Meal plan containing the meal name, ingredients, and cooking
        techniques. Expected to be the output of the 'plan_meal' node.
    purchased_ingredients : List[str]
        List of ingredients that have been purchased. Expected to be the
        output of the 'purchase_ingredients' node.

    Returns
    -------
    List[str]
        List of prepared ingredients.

    Raises
    ------
    ValueError
        If the meal plan is invalid or if purchased ingredients do not match
        the meal plan.

    Examples
    --------
    >>> meal_plan = {'meal_name': 'Salad', 'ingredients': ['Lettuce',
    'Tomatoes'], 'cooking_techniques': []}
    >>> purchased_ingredients = ['Lettuce', 'Tomatoes']
    >>> prepared_ingredients = prepare_ingredients(meal_plan,
    purchased_ingredients)
    ['Washed Lettuce', 'Chopped Tomatoes']

    >>> meal_plan = {'meal_name': 'Soup', 'ingredients': ['Carrots',
    'Potatoes'], 'cooking_techniques': ['Boiling']}
    >>> purchased_ingredients = ['Carrots', 'Potatoes']
    >>> prepared_ingredients = prepare_ingredients(meal_plan,
    purchased_ingredients)
    ['Chopped Carrots', 'Peeled and Chopped Potatoes']

    """
    validate_meal_plan(meal_plan=plan_meal_input)
    validate_ingredient_compatibility(meal_plan=plan_meal_input, purchased_ingredients=purchase_ingredients_input.purchased_ingredients)
    
    required_ingredients: List[str] = parse_ingredients_from_plan(ingredients_str=plan_meal_input.ingredients)
    cooking_techniques: List[str] = parse_cooking_techniques(techniques_str=plan_meal_input.cooking_techniques)
    
    prepared_ingredients_list: List[str] = []
    for ingredient in required_ingredients:
        if ingredient in purchase_ingredients_input.purchased_ingredients:
            prep_methods: List[str] = determine_prep_methods(ingredient=ingredient, cooking_techniques=cooking_techniques)
            prepared_ingredient: str = apply_preparation_methods(ingredient=ingredient, methods=prep_methods)
            prepared_ingredients_list.append(prepared_ingredient)
    
    return PrepareIngredientsOutput(prepared_ingredients=prepared_ingredients_list)