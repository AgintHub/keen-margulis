import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.collect_historical_market_data import collect_historical_market_data
from code.collect_account_data import collect_account_data
from code.analyze_market_trends import analyze_market_trends
from code.determine_trading_parameters import determine_trading_parameters
from code.identify_trading_opportunities import identify_trading_opportunities
from code.generate_trading_signals import generate_trading_signals
from code.execute_trades import execute_trades

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

collect_historical_market_data_async = make_async(collect_historical_market_data)
collect_account_data_async = make_async(collect_account_data)
analyze_market_trends_async = make_async(analyze_market_trends)
determine_trading_parameters_async = make_async(determine_trading_parameters)
identify_trading_opportunities_async = make_async(identify_trading_opportunities)
generate_trading_signals_async = make_async(generate_trading_signals)
execute_trades_async = make_async(execute_trades)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: collect_account_data, collect_historical_market_data
    async def run_collect_account_data():
        # Call the async version of collect_account_data with results from dependencies
        return await collect_account_data_async(user_input)

    async def run_collect_historical_market_data():
        # Call the async version of collect_historical_market_data with results from dependencies
        return await collect_historical_market_data_async(user_input)

    # Run level 0 nodes in parallel
    level_0_results = await asyncio.gather(run_collect_account_data(), run_collect_historical_market_data())
    results['collect_account_data'] = level_0_results[0]
    results['collect_historical_market_data'] = level_0_results[1]

    # Level 1: analyze_market_trends
    async def run_analyze_market_trends():
        # Call the async version of analyze_market_trends with results from dependencies
        return await analyze_market_trends_async(results['collect_historical_market_data'])

    # Run level 1 nodes in parallel
    results['analyze_market_trends'] = await run_analyze_market_trends()

    # Level 2: determine_trading_parameters, identify_trading_opportunities
    async def run_determine_trading_parameters():
        # Call the async version of determine_trading_parameters with results from dependencies
        return await determine_trading_parameters_async(results['collect_account_data'], results['analyze_market_trends'])

    async def run_identify_trading_opportunities():
        # Call the async version of identify_trading_opportunities with results from dependencies
        return await identify_trading_opportunities_async(results['collect_historical_market_data'], results['analyze_market_trends'])

    # Run level 2 nodes in parallel
    level_2_results = await asyncio.gather(run_determine_trading_parameters(), run_identify_trading_opportunities())
    results['determine_trading_parameters'] = level_2_results[0]
    results['identify_trading_opportunities'] = level_2_results[1]

    # Level 3: generate_trading_signals
    async def run_generate_trading_signals():
        # Call the async version of generate_trading_signals with results from dependencies
        return await generate_trading_signals_async(results['determine_trading_parameters'], results['identify_trading_opportunities'])

    # Run level 3 nodes in parallel
    results['generate_trading_signals'] = await run_generate_trading_signals()

    # Level 4: execute_trades
    async def run_execute_trades():
        # Call the async version of execute_trades with results from dependencies
        return await execute_trades_async(results['generate_trading_signals'])

    # Run level 4 nodes in parallel
    results['execute_trades'] = await run_execute_trades()

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
