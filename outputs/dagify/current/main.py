import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.create_dag_structure import create_dag_structure
from code.decompose_task_into_subtasks import decompose_task_into_subtasks
from code.define_node_prompts_and_descriptions import define_node_prompts_and_descriptions
from code.define_task_objective import define_task_objective
from code.finalize_dag_workflow import finalize_dag_workflow
from code.identify_dependencies_between_subtasks import identify_dependencies_between_subtasks

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

create_dag_structure_async = make_async(create_dag_structure)
decompose_task_into_subtasks_async = make_async(decompose_task_into_subtasks)
define_node_prompts_and_descriptions_async = make_async(define_node_prompts_and_descriptions)
define_task_objective_async = make_async(define_task_objective)
finalize_dag_workflow_async = make_async(finalize_dag_workflow)
identify_dependencies_between_subtasks_async = make_async(identify_dependencies_between_subtasks)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: define_task_objective
    async def run_define_task_objective():
        # Call the async version of define_task_objective with results from dependencies
        return await define_task_objective_async(user_input)

    # Run level 0 nodes in parallel
    results['define_task_objective'] = await run_define_task_objective()

    # Level 1: decompose_task_into_subtasks
    async def run_decompose_task_into_subtasks():
        # Call the async version of decompose_task_into_subtasks with results from dependencies
        return await decompose_task_into_subtasks_async(results['define_task_objective'])

    # Run level 1 nodes in parallel
    results['decompose_task_into_subtasks'] = await run_decompose_task_into_subtasks()

    # Level 2: identify_dependencies_between_subtasks
    async def run_identify_dependencies_between_subtasks():
        # Call the async version of identify_dependencies_between_subtasks with results from dependencies
        return await identify_dependencies_between_subtasks_async(results['decompose_task_into_subtasks'])

    # Run level 2 nodes in parallel
    results['identify_dependencies_between_subtasks'] = await run_identify_dependencies_between_subtasks()

    # Level 3: create_dag_structure
    async def run_create_dag_structure():
        # Call the async version of create_dag_structure with results from dependencies
        return await create_dag_structure_async(results['identify_dependencies_between_subtasks'])

    # Run level 3 nodes in parallel
    results['create_dag_structure'] = await run_create_dag_structure()

    # Level 4: define_node_prompts_and_descriptions
    async def run_define_node_prompts_and_descriptions():
        # Call the async version of define_node_prompts_and_descriptions with results from dependencies
        return await define_node_prompts_and_descriptions_async(results['create_dag_structure'])

    # Run level 4 nodes in parallel
    results['define_node_prompts_and_descriptions'] = await run_define_node_prompts_and_descriptions()

    # Level 5: finalize_dag_workflow
    async def run_finalize_dag_workflow():
        # Call the async version of finalize_dag_workflow with results from dependencies
        return await finalize_dag_workflow_async(results['define_node_prompts_and_descriptions'])

    # Run level 5 nodes in parallel
    results['finalize_dag_workflow'] = await run_finalize_dag_workflow()

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
