import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.analyze_chart_performance import analyze_chart_performance
from code.analyze_lyrics_sentiment import analyze_lyrics_sentiment
from code.gather_taylor_swift_data import gather_taylor_swift_data
from code.identify_common_themes import identify_common_themes
from code.synthesize_analysis_results import synthesize_analysis_results

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

analyze_chart_performance_async = make_async(analyze_chart_performance)
analyze_lyrics_sentiment_async = make_async(analyze_lyrics_sentiment)
gather_taylor_swift_data_async = make_async(gather_taylor_swift_data)
identify_common_themes_async = make_async(identify_common_themes)
synthesize_analysis_results_async = make_async(synthesize_analysis_results)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: gather_taylor_swift_data
    async def run_gather_taylor_swift_data():
        # Call the async version of gather_taylor_swift_data with results from dependencies
        return await gather_taylor_swift_data_async(user_input)

    # Run level 0 nodes in parallel
    results['gather_taylor_swift_data'] = await run_gather_taylor_swift_data()

    # Level 1: analyze_lyrics_sentiment, analyze_chart_performance, identify_common_themes
    async def run_analyze_lyrics_sentiment():
        # Call the async version of analyze_lyrics_sentiment with results from dependencies
        return await analyze_lyrics_sentiment_async(results['gather_taylor_swift_data'])

    async def run_analyze_chart_performance():
        # Call the async version of analyze_chart_performance with results from dependencies
        return await analyze_chart_performance_async(results['gather_taylor_swift_data'])

    async def run_identify_common_themes():
        # Call the async version of identify_common_themes with results from dependencies
        return await identify_common_themes_async(results['gather_taylor_swift_data'])

    # Run level 1 nodes in parallel
    level_1_results = await asyncio.gather(run_analyze_lyrics_sentiment(), run_analyze_chart_performance(), run_identify_common_themes())
    results['analyze_lyrics_sentiment'] = level_1_results[0]
    results['analyze_chart_performance'] = level_1_results[1]
    results['identify_common_themes'] = level_1_results[2]

    # Level 2: synthesize_analysis_results
    async def run_synthesize_analysis_results():
        # Call the async version of synthesize_analysis_results with results from dependencies
        return await synthesize_analysis_results_async(results['analyze_lyrics_sentiment'], results['identify_common_themes'], results['analyze_chart_performance'])

    # Run level 2 nodes in parallel
    results['synthesize_analysis_results'] = await run_synthesize_analysis_results()

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
