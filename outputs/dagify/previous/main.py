import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.capture_rush_hour_traffic_images import capture_rush_hour_traffic_images
from code.extract_vehicle_data_from_images import extract_vehicle_data_from_images
from code.analyze_color_distribution import analyze_color_distribution
from code.generate_color_analysis_report import generate_color_analysis_report

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

capture_rush_hour_traffic_images_async = make_async(capture_rush_hour_traffic_images)
extract_vehicle_data_from_images_async = make_async(extract_vehicle_data_from_images)
analyze_color_distribution_async = make_async(analyze_color_distribution)
generate_color_analysis_report_async = make_async(generate_color_analysis_report)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: capture_rush_hour_traffic_images
    async def run_capture_rush_hour_traffic_images():
        # Call the async version of capture_rush_hour_traffic_images with results from dependencies
        return await capture_rush_hour_traffic_images_async(user_input)

    # Run level 0 nodes in parallel
    results['capture_rush_hour_traffic_images'] = await run_capture_rush_hour_traffic_images()

    # Level 1: extract_vehicle_data_from_images
    async def run_extract_vehicle_data_from_images():
        # Call the async version of extract_vehicle_data_from_images with results from dependencies
        return await extract_vehicle_data_from_images_async(results['capture_rush_hour_traffic_images'])

    # Run level 1 nodes in parallel
    results['extract_vehicle_data_from_images'] = await run_extract_vehicle_data_from_images()

    # Level 2: analyze_color_distribution
    async def run_analyze_color_distribution():
        # Call the async version of analyze_color_distribution with results from dependencies
        return await analyze_color_distribution_async(results['extract_vehicle_data_from_images'])

    # Run level 2 nodes in parallel
    results['analyze_color_distribution'] = await run_analyze_color_distribution()

    # Level 3: generate_color_analysis_report
    async def run_generate_color_analysis_report():
        # Call the async version of generate_color_analysis_report with results from dependencies
        return await generate_color_analysis_report_async(results['analyze_color_distribution'])

    # Run level 3 nodes in parallel
    results['generate_color_analysis_report'] = await run_generate_color_analysis_report()

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
