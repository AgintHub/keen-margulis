import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.create_task_dag import create_task_dag
from code.decompose_objective_into_tasks import decompose_objective_into_tasks
from code.define_workflow_objective import define_workflow_objective
from code.finalize_workflow import finalize_workflow
from code.identify_task_dependencies import identify_task_dependencies
from code.validate_dag import validate_dag

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

create_task_dag_async = make_async(create_task_dag)
decompose_objective_into_tasks_async = make_async(decompose_objective_into_tasks)
define_workflow_objective_async = make_async(define_workflow_objective)
finalize_workflow_async = make_async(finalize_workflow)
identify_task_dependencies_async = make_async(identify_task_dependencies)
validate_dag_async = make_async(validate_dag)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: define_workflow_objective
    async def run_define_workflow_objective():
        # Call the async version of define_workflow_objective with results from dependencies
        return await define_workflow_objective_async(user_input)

    # Run level 0 nodes in parallel
    results['define_workflow_objective'] = await run_define_workflow_objective()

    # Level 1: decompose_objective_into_tasks
    async def run_decompose_objective_into_tasks():
        # Call the async version of decompose_objective_into_tasks with results from dependencies
        return await decompose_objective_into_tasks_async(results['define_workflow_objective'])

    # Run level 1 nodes in parallel
    results['decompose_objective_into_tasks'] = await run_decompose_objective_into_tasks()

    # Level 2: identify_task_dependencies
    async def run_identify_task_dependencies():
        # Call the async version of identify_task_dependencies with results from dependencies
        return await identify_task_dependencies_async(results['decompose_objective_into_tasks'])

    # Run level 2 nodes in parallel
    results['identify_task_dependencies'] = await run_identify_task_dependencies()

    # Level 3: create_task_dag
    async def run_create_task_dag():
        # Call the async version of create_task_dag with results from dependencies
        return await create_task_dag_async(results['identify_task_dependencies'])

    # Run level 3 nodes in parallel
    results['create_task_dag'] = await run_create_task_dag()

    # Level 4: validate_dag
    async def run_validate_dag():
        # Call the async version of validate_dag with results from dependencies
        return await validate_dag_async(results['create_task_dag'])

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
