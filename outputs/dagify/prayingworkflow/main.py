import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.prepareforprayer import prepareforprayer
from code.invokeprayer import invokeprayer
from code.reflectonprayer import reflectonprayer
from code.concludeprayer import concludeprayer

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

prepareforprayer_async = make_async(prepareforprayer)
invokeprayer_async = make_async(invokeprayer)
reflectonprayer_async = make_async(reflectonprayer)
concludeprayer_async = make_async(concludeprayer)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: prepareforprayer
    async def run_prepareforprayer():
        # Call the async version of prepareforprayer with results from dependencies
        return await prepareforprayer_async(user_input)

    # Run level 0 nodes in parallel
    results['prepareforprayer'] = await run_prepareforprayer()

    # Level 1: invokeprayer
    async def run_invokeprayer():
        # Call the async version of invokeprayer with results from dependencies
        return await invokeprayer_async(results['prepareforprayer'])

    # Run level 1 nodes in parallel
    results['invokeprayer'] = await run_invokeprayer()

    # Level 2: reflectonprayer
    async def run_reflectonprayer():
        # Call the async version of reflectonprayer with results from dependencies
        return await reflectonprayer_async(results['invokeprayer'])

    # Run level 2 nodes in parallel
    results['reflectonprayer'] = await run_reflectonprayer()

    # Level 3: concludeprayer
    async def run_concludeprayer():
        # Call the async version of concludeprayer with results from dependencies
        return await concludeprayer_async(results['reflectonprayer'])

    # Run level 3 nodes in parallel
    results['concludeprayer'] = await run_concludeprayer()

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
