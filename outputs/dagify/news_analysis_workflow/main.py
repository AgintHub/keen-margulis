import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.analyze_sentiment import analyze_sentiment
from code.categorize_news_articles import categorize_news_articles
from code.compile_analysis_report import compile_analysis_report
from code.filter_news_articles import filter_news_articles
from code.identify_trends import identify_trends
from code.source_news_articles import source_news_articles
from code.summarize_news_articles import summarize_news_articles

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

analyze_sentiment_async = make_async(analyze_sentiment)
categorize_news_articles_async = make_async(categorize_news_articles)
compile_analysis_report_async = make_async(compile_analysis_report)
filter_news_articles_async = make_async(filter_news_articles)
identify_trends_async = make_async(identify_trends)
source_news_articles_async = make_async(source_news_articles)
summarize_news_articles_async = make_async(summarize_news_articles)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: source_news_articles
    async def run_source_news_articles():
        # Call the async version of source_news_articles with results from dependencies
        return await source_news_articles_async(user_input)

    # Run level 0 nodes in parallel
    results['source_news_articles'] = await run_source_news_articles()

    # Level 1: filter_news_articles
    async def run_filter_news_articles():
        # Call the async version of filter_news_articles with results from dependencies
        return await filter_news_articles_async(results['source_news_articles'])

    # Run level 1 nodes in parallel
    results['filter_news_articles'] = await run_filter_news_articles()

    # Level 2: categorize_news_articles
    async def run_categorize_news_articles():
        # Call the async version of categorize_news_articles with results from dependencies
        return await categorize_news_articles_async(results['filter_news_articles'])

    # Run level 2 nodes in parallel
    results['categorize_news_articles'] = await run_categorize_news_articles()

    # Level 3: summarize_news_articles
    async def run_summarize_news_articles():
        # Call the async version of summarize_news_articles with results from dependencies
        return await summarize_news_articles_async(results['categorize_news_articles'])

    # Run level 3 nodes in parallel
    results['summarize_news_articles'] = await run_summarize_news_articles()

    # Level 4: identify_trends, analyze_sentiment
    async def run_identify_trends():
        # Call the async version of identify_trends with results from dependencies
        return await identify_trends_async(results['summarize_news_articles'])

    async def run_analyze_sentiment():
        # Call the async version of analyze_sentiment with results from dependencies
        return await analyze_sentiment_async(results['summarize_news_articles'])

    # Run level 4 nodes in parallel
    level_4_results = await asyncio.gather(run_identify_trends(), run_analyze_sentiment())
    results['identify_trends'] = level_4_results[0]
    results['analyze_sentiment'] = level_4_results[1]

    # Level 5: compile_analysis_report
    async def run_compile_analysis_report():
        # Call the async version of compile_analysis_report with results from dependencies
        return await compile_analysis_report_async(results['analyze_sentiment'], results['identify_trends'])

    # Run level 5 nodes in parallel
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
