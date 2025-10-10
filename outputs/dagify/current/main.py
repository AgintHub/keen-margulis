import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.determine_sport_type import determine_sport_type
from code.gather_sport_info import gather_sport_info
from code.identify_key_players import identify_key_players
from code.identify_sport import identify_sport
from code.list_major_leagues import list_major_leagues
from code.summarize_sport_info import summarize_sport_info

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

determine_sport_type_async = make_async(determine_sport_type)
gather_sport_info_async = make_async(gather_sport_info)
identify_key_players_async = make_async(identify_key_players)
identify_sport_async = make_async(identify_sport)
list_major_leagues_async = make_async(list_major_leagues)
summarize_sport_info_async = make_async(summarize_sport_info)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: identify_sport
    async def run_identify_sport():
        # Call the async version of identify_sport with results from dependencies
        return await identify_sport_async(user_input)

    # Run level 0 nodes in parallel
    results['identify_sport'] = await run_identify_sport()

    # Level 1: list_major_leagues, determine_sport_type, gather_sport_info
    async def run_list_major_leagues():
        # Call the async version of list_major_leagues with results from dependencies
        return await list_major_leagues_async(results['identify_sport'])

    async def run_determine_sport_type():
        # Call the async version of determine_sport_type with results from dependencies
        return await determine_sport_type_async(results['identify_sport'])

    async def run_gather_sport_info():
        # Call the async version of gather_sport_info with results from dependencies
        return await gather_sport_info_async(results['identify_sport'])

    # Run level 1 nodes in parallel
    level_1_results = await asyncio.gather(run_list_major_leagues(), run_determine_sport_type(), run_gather_sport_info())
    results['list_major_leagues'] = level_1_results[0]
    results['determine_sport_type'] = level_1_results[1]
    results['gather_sport_info'] = level_1_results[2]

    # Level 2: identify_key_players
    async def run_identify_key_players():
        # Call the async version of identify_key_players with results from dependencies
        return await identify_key_players_async(results['identify_sport'], results['list_major_leagues'])

    # Run level 2 nodes in parallel
    results['identify_key_players'] = await run_identify_key_players()

    # Level 3: summarize_sport_info
    async def run_summarize_sport_info():
        # Call the async version of summarize_sport_info with results from dependencies
        return await summarize_sport_info_async(results['gather_sport_info'], results['determine_sport_type'], results['list_major_leagues'], results['identify_key_players'])

    # Run level 3 nodes in parallel
    results['summarize_sport_info'] = await run_summarize_sport_info()

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
