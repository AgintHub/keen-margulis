import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.plan_meal import plan_meal
from code.create_shopping_list import create_shopping_list
from code.purchase_ingredients import purchase_ingredients
from code.prepare_ingredients import prepare_ingredients
from code.cook_meal import cook_meal
from code.serve_meal import serve_meal

# Get async mode from environment variable or default to False
ASYNC_MODE = os.environ.get('ASYNC_MODE', '').lower() in ('true', '1', 'yes', 'y')

def make_async(func):
    """Convert a synchronous function to an asynchronous function.

    If the function is already asynchronous, return it unchanged.
    If the function is synchronous, wrap it in an async function.
    """
    # If it's already a coroutine function, return it as is
    if inspect.iscoroutinefunction(func):
        return func

    # Otherwise, wrap it as an async function
    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return async_wrapper

plan_meal_async = make_async(plan_meal)
create_shopping_list_async = make_async(create_shopping_list)
purchase_ingredients_async = make_async(purchase_ingredients)
prepare_ingredients_async = make_async(prepare_ingredients)
cook_meal_async = make_async(cook_meal)
serve_meal_async = make_async(serve_meal)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: plan_meal
    async def run_plan_meal():
        # Call the async version of plan_meal with results from dependencies
        return await plan_meal_async(user_input)

    # Run level 0 nodes in parallel
    results['plan_meal'] = await run_plan_meal()

    # Level 1: create_shopping_list
    async def run_create_shopping_list():
        # Call the async version of create_shopping_list with results from dependencies
        return await create_shopping_list_async(results['plan_meal'])

    # Run level 1 nodes in parallel
    results['create_shopping_list'] = await run_create_shopping_list()

    # Level 2: purchase_ingredients
    async def run_purchase_ingredients():
        # Call the async version of purchase_ingredients with results from dependencies
        return await purchase_ingredients_async(results['create_shopping_list'])

    # Run level 2 nodes in parallel
    results['purchase_ingredients'] = await run_purchase_ingredients()

    # Level 3: prepare_ingredients
    async def run_prepare_ingredients():
        # Call the async version of prepare_ingredients with results from dependencies
        return await prepare_ingredients_async(results['plan_meal'], results['purchase_ingredients'])

    # Run level 3 nodes in parallel
    results['prepare_ingredients'] = await run_prepare_ingredients()

    # Level 4: cook_meal
    async def run_cook_meal():
        # Call the async version of cook_meal with results from dependencies
        return await cook_meal_async(results['prepare_ingredients'])

    # Run level 4 nodes in parallel
    results['cook_meal'] = await run_cook_meal()

    # Level 5: serve_meal
    async def run_serve_meal():
        # Call the async version of serve_meal with results from dependencies
        return await serve_meal_async(results['cook_meal'])

    # Run level 5 nodes in parallel
    results['serve_meal'] = await run_serve_meal()

    # Return all results
    return results

def run_workflow_sync(user_input: str) -> Dict[str, Any]:
    """Synchronous wrapper around the async workflow execution."""
    return asyncio.run(run_workflow(user_input))

def main():
    """Main entry point.

    Handles arguments in the following priority:
    1. Command-line argument (sys.argv[1])
    2. If no argument, uses empty string as input but displays a warning.
    """
    # Get user input from command line or use empty string
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        # No input provided - display help message but continue with empty string
        print('Warning: No input provided. Using empty string as input.')
        print('For better results, provide an input argument:')
        print(f'  python {os.path.basename(__file__)} "your input text here"')
        print('Or use a file as input:')
        print(f'  python {os.path.basename(__file__)} "$(cat input.txt)"')
        user_input = ""

    print(f'Running workflow with input: {user_input}')

    # Run the workflow
    results = run_workflow_sync(user_input)

    # Print results
    try:
        # Convert results to JSON
        json_results = json.dumps(results, indent=2, default=str)
        print(json_results)
    except (TypeError, ValueError) as e:
        print(f'Results could not be converted to JSON: {e}')
        print(f'Raw results: {results}')

    return results

if __name__ == '__main__':
    main()
