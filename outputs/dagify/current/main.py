import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.analyze_leaf_shapes import analyze_leaf_shapes
from code.collect_leaf_data import collect_leaf_data
from code.extract_leaf_features import extract_leaf_features
from code.generate_leaf_pattern_insights import generate_leaf_pattern_insights

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

analyze_leaf_shapes_async = make_async(analyze_leaf_shapes)
collect_leaf_data_async = make_async(collect_leaf_data)
extract_leaf_features_async = make_async(extract_leaf_features)
generate_leaf_pattern_insights_async = make_async(generate_leaf_pattern_insights)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: collect_leaf_data
    async def run_collect_leaf_data():
        # Call the async version of collect_leaf_data with results from dependencies
        return await collect_leaf_data_async(user_input)

    # Run level 0 nodes in parallel
    results['collect_leaf_data'] = await run_collect_leaf_data()

    # Level 1: analyze_leaf_shapes
    async def run_analyze_leaf_shapes():
        # Call the async version of analyze_leaf_shapes with results from dependencies
        return await analyze_leaf_shapes_async(results['collect_leaf_data'])

    # Run level 1 nodes in parallel
    results['analyze_leaf_shapes'] = await run_analyze_leaf_shapes()

    # Level 2: extract_leaf_features
    async def run_extract_leaf_features():
        # Call the async version of extract_leaf_features with results from dependencies
        return await extract_leaf_features_async(results['collect_leaf_data'], results['analyze_leaf_shapes'])

    # Run level 2 nodes in parallel
    results['extract_leaf_features'] = await run_extract_leaf_features()

    # Level 3: generate_leaf_pattern_insights
    async def run_generate_leaf_pattern_insights():
        # Call the async version of generate_leaf_pattern_insights with results from dependencies
        return await generate_leaf_pattern_insights_async(results['extract_leaf_features'])

    # Run level 3 nodes in parallel
    results['generate_leaf_pattern_insights'] = await run_generate_leaf_pattern_insights()

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
