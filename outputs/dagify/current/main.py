import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.analyze_pawn_structure import analyze_pawn_structure
from code.assess_king_safety import assess_king_safety
from code.evaluate_material_balance import evaluate_material_balance
from code.parse_chess_position import parse_chess_position
from code.synthesize_analysis import synthesize_analysis

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

analyze_pawn_structure_async = make_async(analyze_pawn_structure)
assess_king_safety_async = make_async(assess_king_safety)
evaluate_material_balance_async = make_async(evaluate_material_balance)
parse_chess_position_async = make_async(parse_chess_position)
synthesize_analysis_async = make_async(synthesize_analysis)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: parse_chess_position
    async def run_parse_chess_position():
        # Call the async version of parse_chess_position with results from dependencies
        return await parse_chess_position_async(user_input)

    # Run level 0 nodes in parallel
    results['parse_chess_position'] = await run_parse_chess_position()

    # Level 1: evaluate_material_balance, assess_king_safety, analyze_pawn_structure
    async def run_evaluate_material_balance():
        # Call the async version of evaluate_material_balance with results from dependencies
        return await evaluate_material_balance_async(results['parse_chess_position'])

    async def run_assess_king_safety():
        # Call the async version of assess_king_safety with results from dependencies
        return await assess_king_safety_async(results['parse_chess_position'])

    async def run_analyze_pawn_structure():
        # Call the async version of analyze_pawn_structure with results from dependencies
        return await analyze_pawn_structure_async(results['parse_chess_position'])

    # Run level 1 nodes in parallel
    level_1_results = await asyncio.gather(run_evaluate_material_balance(), run_assess_king_safety(), run_analyze_pawn_structure())
    results['evaluate_material_balance'] = level_1_results[0]
    results['assess_king_safety'] = level_1_results[1]
    results['analyze_pawn_structure'] = level_1_results[2]

    # Level 2: synthesize_analysis
    async def run_synthesize_analysis():
        # Call the async version of synthesize_analysis with results from dependencies
        return await synthesize_analysis_async(results['evaluate_material_balance'], results['analyze_pawn_structure'], results['assess_king_safety'])

    # Run level 2 nodes in parallel
    results['synthesize_analysis'] = await run_synthesize_analysis()

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
