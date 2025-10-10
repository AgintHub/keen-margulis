import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.initializeworkflow import initializeworkflow
from code.definenode1 import definenode1
from code.definenode2 import definenode2
from code.connectnodes import connectnodes
from code.validateworkflow import validateworkflow
from code.finalizeworkflow import finalizeworkflow

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

initializeworkflow_async = make_async(initializeworkflow)
definenode1_async = make_async(definenode1)
definenode2_async = make_async(definenode2)
connectnodes_async = make_async(connectnodes)
validateworkflow_async = make_async(validateworkflow)
finalizeworkflow_async = make_async(finalizeworkflow)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: initializeworkflow
    async def run_initializeworkflow():
        # Call the async version of initializeworkflow with results from dependencies
        return await initializeworkflow_async(user_input)

    # Run level 0 nodes in parallel
    results['initializeworkflow'] = await run_initializeworkflow()

    # Level 1: definenode2, definenode1
    async def run_definenode2():
        # Call the async version of definenode2 with results from dependencies
        return await definenode2_async(results['initializeworkflow'])

    async def run_definenode1():
        # Call the async version of definenode1 with results from dependencies
        return await definenode1_async(results['initializeworkflow'])

    # Run level 1 nodes in parallel
    level_1_results = await asyncio.gather(run_definenode2(), run_definenode1())
    results['definenode2'] = level_1_results[0]
    results['definenode1'] = level_1_results[1]

    # Level 2: connectnodes
    async def run_connectnodes():
        # Call the async version of connectnodes with results from dependencies
        return await connectnodes_async(results['definenode1'], results['definenode2'])

    # Run level 2 nodes in parallel
    results['connectnodes'] = await run_connectnodes()

    # Level 3: validateworkflow
    async def run_validateworkflow():
        # Call the async version of validateworkflow with results from dependencies
        return await validateworkflow_async(results['connectnodes'])

    # Run level 3 nodes in parallel
    results['validateworkflow'] = await run_validateworkflow()

    # Level 4: finalizeworkflow
    async def run_finalizeworkflow():
        # Call the async version of finalizeworkflow with results from dependencies
        return await finalizeworkflow_async(results['validateworkflow'])

    # Run level 4 nodes in parallel
    results['finalizeworkflow'] = await run_finalizeworkflow()

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
