import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.step1_testprompt import step1_testprompt
from code.step2_calculatesum import step2_calculatesum
from code.step3_checkcondition import step3_checkcondition
from code.step4_printresult import step4_printresult

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

step1_testprompt_async = make_async(step1_testprompt)
step2_calculatesum_async = make_async(step2_calculatesum)
step3_checkcondition_async = make_async(step3_checkcondition)
step4_printresult_async = make_async(step4_printresult)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: step1_testprompt
    async def run_step1_testprompt():
        # Call the async version of step1_testprompt with results from dependencies
        return await step1_testprompt_async(user_input)

    # Run level 0 nodes in parallel
    results['step1_testprompt'] = await run_step1_testprompt()

    # Level 1: step2_calculatesum
    async def run_step2_calculatesum():
        # Call the async version of step2_calculatesum with results from dependencies
        return await step2_calculatesum_async(results['step1_testprompt'])

    # Run level 1 nodes in parallel
    results['step2_calculatesum'] = await run_step2_calculatesum()

    # Level 2: step3_checkcondition
    async def run_step3_checkcondition():
        # Call the async version of step3_checkcondition with results from dependencies
        return await step3_checkcondition_async(results['step2_calculatesum'])

    # Run level 2 nodes in parallel
    results['step3_checkcondition'] = await run_step3_checkcondition()

    # Level 3: step4_printresult
    async def run_step4_printresult():
        # Call the async version of step4_printresult with results from dependencies
        return await step4_printresult_async(results['step3_checkcondition'])

    # Run level 3 nodes in parallel
    results['step4_printresult'] = await run_step4_printresult()

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
