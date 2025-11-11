import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.define_objective import define_objective
from code.decompose_objective import decompose_objective
from code.identify_dependencies import identify_dependencies
from code.define_node_outputs import define_node_outputs
from code.construct_dag import construct_dag
from code.validate_dag import validate_dag
from code.finalize_workflow import finalize_workflow

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

define_objective_async = make_async(define_objective)
decompose_objective_async = make_async(decompose_objective)
identify_dependencies_async = make_async(identify_dependencies)
define_node_outputs_async = make_async(define_node_outputs)
construct_dag_async = make_async(construct_dag)
validate_dag_async = make_async(validate_dag)
finalize_workflow_async = make_async(finalize_workflow)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: define_objective
    async def run_define_objective():
        # Call the async version of define_objective with results from dependencies
        return await define_objective_async(user_input)

    # Run level 0 nodes in parallel
    results['define_objective'] = await run_define_objective()

    # Level 1: decompose_objective
    async def run_decompose_objective():
        # Call the async version of decompose_objective with results from dependencies
        return await decompose_objective_async(results['define_objective'])

    # Run level 1 nodes in parallel
    results['decompose_objective'] = await run_decompose_objective()

    # Level 2: identify_dependencies, define_node_outputs
    async def run_identify_dependencies():
        # Call the async version of identify_dependencies with results from dependencies
        return await identify_dependencies_async(results['decompose_objective'])

    async def run_define_node_outputs():
        # Call the async version of define_node_outputs with results from dependencies
        return await define_node_outputs_async(results['decompose_objective'])

    # Run level 2 nodes in parallel
    level_2_results = await asyncio.gather(run_identify_dependencies(), run_define_node_outputs())
    results['identify_dependencies'] = level_2_results[0]
    results['define_node_outputs'] = level_2_results[1]

    # Level 3: construct_dag
    async def run_construct_dag():
        # Call the async version of construct_dag with results from dependencies
        return await construct_dag_async(results['identify_dependencies'], results['define_node_outputs'])

    # Run level 3 nodes in parallel
    results['construct_dag'] = await run_construct_dag()

    # Level 4: validate_dag
    async def run_validate_dag():
        # Call the async version of validate_dag with results from dependencies
        return await validate_dag_async(results['construct_dag'])

    # Run level 4 nodes in parallel
    results['validate_dag'] = await run_validate_dag()

    # Level 5: finalize_workflow
    async def run_finalize_workflow():
        # Call the async version of finalize_workflow with results from dependencies
        return await finalize_workflow_async(results['validate_dag'])

    # Run level 5 nodes in parallel
    results['finalize_workflow'] = await run_finalize_workflow()

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
