import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.analyze_cultural_influences import analyze_cultural_influences
from code.analyze_economic_influences import analyze_economic_influences
from code.analyze_political_influences import analyze_political_influences
from code.analyze_social_influences import analyze_social_influences
from code.compile_historical_narrative import compile_historical_narrative
from code.define_historical_context import define_historical_context
from code.draw_conclusions import draw_conclusions
from code.identify_key_factors import identify_key_factors
from code.synthesize_influences import synthesize_influences

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

analyze_cultural_influences_async = make_async(analyze_cultural_influences)
analyze_economic_influences_async = make_async(analyze_economic_influences)
analyze_political_influences_async = make_async(analyze_political_influences)
analyze_social_influences_async = make_async(analyze_social_influences)
compile_historical_narrative_async = make_async(compile_historical_narrative)
define_historical_context_async = make_async(define_historical_context)
draw_conclusions_async = make_async(draw_conclusions)
identify_key_factors_async = make_async(identify_key_factors)
synthesize_influences_async = make_async(synthesize_influences)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: define_historical_context
    async def run_define_historical_context():
        # Call the async version of define_historical_context with results from dependencies
        return await define_historical_context_async(user_input)

    # Run level 0 nodes in parallel
    results['define_historical_context'] = await run_define_historical_context()

    # Level 1: identify_key_factors
    async def run_identify_key_factors():
        # Call the async version of identify_key_factors with results from dependencies
        return await identify_key_factors_async(results['define_historical_context'])

    # Run level 1 nodes in parallel
    results['identify_key_factors'] = await run_identify_key_factors()

    # Level 2: analyze_cultural_influences, analyze_social_influences, analyze_economic_influences, analyze_political_influences
    async def run_analyze_cultural_influences():
        # Call the async version of analyze_cultural_influences with results from dependencies
        return await analyze_cultural_influences_async(results['identify_key_factors'])

    async def run_analyze_social_influences():
        # Call the async version of analyze_social_influences with results from dependencies
        return await analyze_social_influences_async(results['identify_key_factors'])

    async def run_analyze_economic_influences():
        # Call the async version of analyze_economic_influences with results from dependencies
        return await analyze_economic_influences_async(results['identify_key_factors'])

    async def run_analyze_political_influences():
        # Call the async version of analyze_political_influences with results from dependencies
        return await analyze_political_influences_async(results['identify_key_factors'])

    # Run level 2 nodes in parallel
    level_2_results = await asyncio.gather(run_analyze_cultural_influences(), run_analyze_social_influences(), run_analyze_economic_influences(), run_analyze_political_influences())
    results['analyze_cultural_influences'] = level_2_results[0]
    results['analyze_social_influences'] = level_2_results[1]
    results['analyze_economic_influences'] = level_2_results[2]
    results['analyze_political_influences'] = level_2_results[3]

    # Level 3: synthesize_influences
    async def run_synthesize_influences():
        # Call the async version of synthesize_influences with results from dependencies
        return await synthesize_influences_async(results['analyze_social_influences'], results['analyze_political_influences'], results['analyze_economic_influences'], results['analyze_cultural_influences'])

    # Run level 3 nodes in parallel
    results['synthesize_influences'] = await run_synthesize_influences()

    # Level 4: draw_conclusions
    async def run_draw_conclusions():
        # Call the async version of draw_conclusions with results from dependencies
        return await draw_conclusions_async(results['synthesize_influences'])

    # Run level 4 nodes in parallel
    results['draw_conclusions'] = await run_draw_conclusions()

    # Level 5: compile_historical_narrative
    async def run_compile_historical_narrative():
        # Call the async version of compile_historical_narrative with results from dependencies
        return await compile_historical_narrative_async(results['draw_conclusions'])

    # Run level 5 nodes in parallel
    results['compile_historical_narrative'] = await run_compile_historical_narrative()

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
