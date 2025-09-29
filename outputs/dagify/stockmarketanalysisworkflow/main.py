import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.collect_stock_data import collect_stock_data
from code.process_stock_data import process_stock_data
from code.analyze_stock_trends import analyze_stock_trends
from code.calculate_stock_metrics import calculate_stock_metrics
from code.generate_stock_insights import generate_stock_insights

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

collect_stock_data_async = make_async(collect_stock_data)
process_stock_data_async = make_async(process_stock_data)
analyze_stock_trends_async = make_async(analyze_stock_trends)
calculate_stock_metrics_async = make_async(calculate_stock_metrics)
generate_stock_insights_async = make_async(generate_stock_insights)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: collect_stock_data
    async def run_collect_stock_data():
        # Call the async version of collect_stock_data with results from dependencies
        return await collect_stock_data_async(user_input)

    # Run level 0 nodes in parallel
    results['collect_stock_data'] = await run_collect_stock_data()

    # Level 1: process_stock_data
    async def run_process_stock_data():
        # Call the async version of process_stock_data with results from dependencies
        return await process_stock_data_async(results['collect_stock_data'])

    # Run level 1 nodes in parallel
    results['process_stock_data'] = await run_process_stock_data()

    # Level 2: analyze_stock_trends, calculate_stock_metrics
    async def run_analyze_stock_trends():
        # Call the async version of analyze_stock_trends with results from dependencies
        return await analyze_stock_trends_async(results['collect_stock_data'], results['process_stock_data'])

    async def run_calculate_stock_metrics():
        # Call the async version of calculate_stock_metrics with results from dependencies
        return await calculate_stock_metrics_async(results['process_stock_data'])

    # Run level 2 nodes in parallel
    level_2_results = await asyncio.gather(run_analyze_stock_trends(), run_calculate_stock_metrics())
    results['analyze_stock_trends'] = level_2_results[0]
    results['calculate_stock_metrics'] = level_2_results[1]

    # Level 3: generate_stock_insights
    async def run_generate_stock_insights():
        # Call the async version of generate_stock_insights with results from dependencies
        return await generate_stock_insights_async(results['analyze_stock_trends'], results['calculate_stock_metrics'])

    # Run level 3 nodes in parallel
    results['generate_stock_insights'] = await run_generate_stock_insights()

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
