import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.boil_water import boil_water
from code.brew_coffee import brew_coffee
from code.measure_coffee import measure_coffee
from code.prepare_coffee_maker import prepare_coffee_maker
from code.serve_coffee import serve_coffee

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

boil_water_async = make_async(boil_water)
brew_coffee_async = make_async(brew_coffee)
measure_coffee_async = make_async(measure_coffee)
prepare_coffee_maker_async = make_async(prepare_coffee_maker)
serve_coffee_async = make_async(serve_coffee)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: measure_coffee, boil_water
    async def run_measure_coffee():
        # Call the async version of measure_coffee with results from dependencies
        return await measure_coffee_async(user_input)

    async def run_boil_water():
        # Call the async version of boil_water with results from dependencies
        return await boil_water_async(user_input)

    # Run level 0 nodes in parallel
    level_0_results = await asyncio.gather(run_measure_coffee(), run_boil_water())
    results['measure_coffee'] = level_0_results[0]
    results['boil_water'] = level_0_results[1]

    # Level 1: prepare_coffee_maker
    async def run_prepare_coffee_maker():
        # Call the async version of prepare_coffee_maker with results from dependencies
        return await prepare_coffee_maker_async(results['measure_coffee'])

    # Run level 1 nodes in parallel
    results['prepare_coffee_maker'] = await run_prepare_coffee_maker()

    # Level 2: brew_coffee
    async def run_brew_coffee():
        # Call the async version of brew_coffee with results from dependencies
        return await brew_coffee_async(results['boil_water'], results['prepare_coffee_maker'])

    # Run level 2 nodes in parallel
    results['brew_coffee'] = await run_brew_coffee()

    # Level 3: serve_coffee
    async def run_serve_coffee():
        # Call the async version of serve_coffee with results from dependencies
        return await serve_coffee_async(results['brew_coffee'])

    # Run level 3 nodes in parallel
    results['serve_coffee'] = await run_serve_coffee()

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
