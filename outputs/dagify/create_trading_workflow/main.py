import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.calculate_position_sizing import calculate_position_sizing
from code.configure_trading_system import configure_trading_system
from code.determine_trading_rules import determine_trading_rules
from code.develop_trading_dashboard import develop_trading_dashboard
from code.evaluate_trading_performance import evaluate_trading_performance
from code.identify_trading_instruments import identify_trading_instruments
from code.implement_order_execution import implement_order_execution
from code.implement_trading_risk_management import implement_trading_risk_management
from code.select_trading_strategy import select_trading_strategy
from code.set_market_environment import set_market_environment

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

calculate_position_sizing_async = make_async(calculate_position_sizing)
configure_trading_system_async = make_async(configure_trading_system)
determine_trading_rules_async = make_async(determine_trading_rules)
develop_trading_dashboard_async = make_async(develop_trading_dashboard)
evaluate_trading_performance_async = make_async(evaluate_trading_performance)
identify_trading_instruments_async = make_async(identify_trading_instruments)
implement_order_execution_async = make_async(implement_order_execution)
implement_trading_risk_management_async = make_async(implement_trading_risk_management)
select_trading_strategy_async = make_async(select_trading_strategy)
set_market_environment_async = make_async(set_market_environment)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: identify_trading_instruments, set_market_environment
    async def run_identify_trading_instruments():
        # Call the async version of identify_trading_instruments with results from dependencies
        return await identify_trading_instruments_async(user_input)

    async def run_set_market_environment():
        # Call the async version of set_market_environment with results from dependencies
        return await set_market_environment_async(user_input)

    # Run level 0 nodes in parallel
    level_0_results = await asyncio.gather(run_identify_trading_instruments(), run_set_market_environment())
    results['identify_trading_instruments'] = level_0_results[0]
    results['set_market_environment'] = level_0_results[1]

    # Level 1: configure_trading_system, select_trading_strategy
    async def run_configure_trading_system():
        # Call the async version of configure_trading_system with results from dependencies
        return await configure_trading_system_async(results['set_market_environment'])

    async def run_select_trading_strategy():
        # Call the async version of select_trading_strategy with results from dependencies
        return await select_trading_strategy_async(results['identify_trading_instruments'])

    # Run level 1 nodes in parallel
    level_1_results = await asyncio.gather(run_configure_trading_system(), run_select_trading_strategy())
    results['configure_trading_system'] = level_1_results[0]
    results['select_trading_strategy'] = level_1_results[1]

    # Level 2: develop_trading_dashboard, determine_trading_rules
    async def run_develop_trading_dashboard():
        # Call the async version of develop_trading_dashboard with results from dependencies
        return await develop_trading_dashboard_async(results['configure_trading_system'])

    async def run_determine_trading_rules():
        # Call the async version of determine_trading_rules with results from dependencies
        return await determine_trading_rules_async(results['select_trading_strategy'])

    # Run level 2 nodes in parallel
    level_2_results = await asyncio.gather(run_develop_trading_dashboard(), run_determine_trading_rules())
    results['develop_trading_dashboard'] = level_2_results[0]
    results['determine_trading_rules'] = level_2_results[1]

    # Level 3: implement_trading_risk_management, calculate_position_sizing
    async def run_implement_trading_risk_management():
        # Call the async version of implement_trading_risk_management with results from dependencies
        return await implement_trading_risk_management_async(results['develop_trading_dashboard'])

    async def run_calculate_position_sizing():
        # Call the async version of calculate_position_sizing with results from dependencies
        return await calculate_position_sizing_async(results['determine_trading_rules'])

    # Run level 3 nodes in parallel
    level_3_results = await asyncio.gather(run_implement_trading_risk_management(), run_calculate_position_sizing())
    results['implement_trading_risk_management'] = level_3_results[0]
    results['calculate_position_sizing'] = level_3_results[1]

    # Level 4: implement_order_execution, evaluate_trading_performance
    async def run_implement_order_execution():
        # Call the async version of implement_order_execution with results from dependencies
        return await implement_order_execution_async(results['calculate_position_sizing'])

    async def run_evaluate_trading_performance():
        # Call the async version of evaluate_trading_performance with results from dependencies
        return await evaluate_trading_performance_async(results['implement_trading_risk_management'])

    # Run level 4 nodes in parallel
    level_4_results = await asyncio.gather(run_implement_order_execution(), run_evaluate_trading_performance())
    results['implement_order_execution'] = level_4_results[0]
    results['evaluate_trading_performance'] = level_4_results[1]

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
