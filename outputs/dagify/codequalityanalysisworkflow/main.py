import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.collect_source_code import collect_source_code
from code.perform_static_code_analysis import perform_static_code_analysis
from code.measure_code_complexity import measure_code_complexity
from code.check_code_style import check_code_style
from code.compile_analysis_report import compile_analysis_report

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

collect_source_code_async = make_async(collect_source_code)
perform_static_code_analysis_async = make_async(perform_static_code_analysis)
measure_code_complexity_async = make_async(measure_code_complexity)
check_code_style_async = make_async(check_code_style)
compile_analysis_report_async = make_async(compile_analysis_report)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: collect_source_code
    async def run_collect_source_code():
        # Call the async version of collect_source_code with results from dependencies
        return await collect_source_code_async(user_input)

    # Run level 0 nodes in parallel
    results['collect_source_code'] = await run_collect_source_code()

    # Level 1: check_code_style, measure_code_complexity, perform_static_code_analysis
    async def run_check_code_style():
        # Call the async version of check_code_style with results from dependencies
        return await check_code_style_async(results['collect_source_code'])

    async def run_measure_code_complexity():
        # Call the async version of measure_code_complexity with results from dependencies
        return await measure_code_complexity_async(results['collect_source_code'])

    async def run_perform_static_code_analysis():
        # Call the async version of perform_static_code_analysis with results from dependencies
        return await perform_static_code_analysis_async(results['collect_source_code'])

    # Run level 1 nodes in parallel
    level_1_results = await asyncio.gather(run_check_code_style(), run_measure_code_complexity(), run_perform_static_code_analysis())
    results['check_code_style'] = level_1_results[0]
    results['measure_code_complexity'] = level_1_results[1]
    results['perform_static_code_analysis'] = level_1_results[2]

    # Level 2: compile_analysis_report
    async def run_compile_analysis_report():
        # Call the async version of compile_analysis_report with results from dependencies
        return await compile_analysis_report_async(results['perform_static_code_analysis'], results['measure_code_complexity'], results['check_code_style'])

    # Run level 2 nodes in parallel
    results['compile_analysis_report'] = await run_compile_analysis_report()

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
