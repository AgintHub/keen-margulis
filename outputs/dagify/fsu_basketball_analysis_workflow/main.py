import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.gather_historical_game_data import gather_historical_game_data
from code.extract_player_statistics import extract_player_statistics
from code.analyze_team_performance import analyze_team_performance
from code.identify_top_performers import identify_top_performers
from code.generate_performance_report import generate_performance_report

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

gather_historical_game_data_async = make_async(gather_historical_game_data)
extract_player_statistics_async = make_async(extract_player_statistics)
analyze_team_performance_async = make_async(analyze_team_performance)
identify_top_performers_async = make_async(identify_top_performers)
generate_performance_report_async = make_async(generate_performance_report)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: gather_historical_game_data
    async def run_gather_historical_game_data():
        # Call the async version of gather_historical_game_data with results from dependencies
        return await gather_historical_game_data_async(user_input)

    # Run level 0 nodes in parallel
    results['gather_historical_game_data'] = await run_gather_historical_game_data()

    # Level 1: analyze_team_performance, extract_player_statistics
    async def run_analyze_team_performance():
        # Call the async version of analyze_team_performance with results from dependencies
        return await analyze_team_performance_async(results['gather_historical_game_data'])

    async def run_extract_player_statistics():
        # Call the async version of extract_player_statistics with results from dependencies
        return await extract_player_statistics_async(results['gather_historical_game_data'])

    # Run level 1 nodes in parallel
    level_1_results = await asyncio.gather(run_analyze_team_performance(), run_extract_player_statistics())
    results['analyze_team_performance'] = level_1_results[0]
    results['extract_player_statistics'] = level_1_results[1]

    # Level 2: identify_top_performers
    async def run_identify_top_performers():
        # Call the async version of identify_top_performers with results from dependencies
        return await identify_top_performers_async(results['extract_player_statistics'])

    # Run level 2 nodes in parallel
    results['identify_top_performers'] = await run_identify_top_performers()

    # Level 3: generate_performance_report
    async def run_generate_performance_report():
        # Call the async version of generate_performance_report with results from dependencies
        return await generate_performance_report_async(results['analyze_team_performance'], results['identify_top_performers'])

    # Run level 3 nodes in parallel
    results['generate_performance_report'] = await run_generate_performance_report()

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
