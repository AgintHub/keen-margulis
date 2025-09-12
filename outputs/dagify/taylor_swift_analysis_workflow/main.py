import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.fetch_song_data import fetch_song_data
from code.analyze_lyrics import analyze_lyrics
from code.extract_themes import extract_themes
from code.sentiment_analysis import sentiment_analysis
from code.trend_over_time import trend_over_time
from code.generate_summary import generate_summary

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

fetch_song_data_async = make_async(fetch_song_data)
analyze_lyrics_async = make_async(analyze_lyrics)
extract_themes_async = make_async(extract_themes)
sentiment_analysis_async = make_async(sentiment_analysis)
trend_over_time_async = make_async(trend_over_time)
generate_summary_async = make_async(generate_summary)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: fetch_song_data
    async def run_fetch_song_data():
        # Call the async version of fetch_song_data with results from dependencies
        return await fetch_song_data_async(user_input)

    # Run level 0 nodes in parallel
    results['fetch_song_data'] = await run_fetch_song_data()

    # Level 1: sentiment_analysis, analyze_lyrics
    async def run_sentiment_analysis():
        # Call the async version of sentiment_analysis with results from dependencies
        return await sentiment_analysis_async(results['fetch_song_data'])

    async def run_analyze_lyrics():
        # Call the async version of analyze_lyrics with results from dependencies
        return await analyze_lyrics_async(results['fetch_song_data'])

    # Run level 1 nodes in parallel
    level_1_results = await asyncio.gather(run_sentiment_analysis(), run_analyze_lyrics())
    results['sentiment_analysis'] = level_1_results[0]
    results['analyze_lyrics'] = level_1_results[1]

    # Level 2: extract_themes, trend_over_time
    async def run_extract_themes():
        # Call the async version of extract_themes with results from dependencies
        return await extract_themes_async(results['analyze_lyrics'])

    async def run_trend_over_time():
        # Call the async version of trend_over_time with results from dependencies
        return await trend_over_time_async(results['fetch_song_data'], results['sentiment_analysis'])

    # Run level 2 nodes in parallel
    level_2_results = await asyncio.gather(run_extract_themes(), run_trend_over_time())
    results['extract_themes'] = level_2_results[0]
    results['trend_over_time'] = level_2_results[1]

    # Level 3: generate_summary
    async def run_generate_summary():
        # Call the async version of generate_summary with results from dependencies
        return await generate_summary_async(results['extract_themes'], results['trend_over_time'])

    # Run level 3 nodes in parallel
    results['generate_summary'] = await run_generate_summary()

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
