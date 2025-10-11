# /// script
# dependencies = ["crewai==0.105.0"]
# ///
import sys
import logging
from crewai import Crew
from crews import *

class FilteredStream:
    # @traceable
    def __init__(self, original_stream):
        self.original_stream = original_stream
        self.filtered_messages = [
            "File not found:",
            "agents.yaml",
            "tasks.yaml"
        ]
        self.buffer = ""

    # @traceable
    def write(self, text):
        # Add to buffer
        self.buffer += text

        # If we have a complete line (ends with newline)
        if '\n' in self.buffer:
            lines = self.buffer.split('\n')
            # Process all complete lines
            for line in lines[:-1]:
                if not any(msg in line for msg in self.filtered_messages):
                    self.original_stream.write(line + '\n')
            # Keep the last incomplete line in buffer
            self.buffer = lines[-1]

    # @traceable
    def flush(self):
        # Process any remaining buffer content
        if self.buffer and not any(msg in self.buffer for msg in self.filtered_messages):
            self.original_stream.write(self.buffer)
        self.buffer = ""
        self.original_stream.flush()

# Redirect stdout to our filtered stream
sys.stdout = FilteredStream(sys.stdout)

# Suppress CrewAI configuration warnings
logging.basicConfig(level=logging.ERROR)
logging.getLogger().setLevel(logging.ERROR)
import os
import asyncio
from typing import Dict
from crewai import Crew

from crews.create_task_dag_crew import create_task_dag_crew
from crews.decompose_objective_into_tasks_crew import decompose_objective_into_tasks_crew
from crews.define_workflow_objective_crew import define_workflow_objective_crew
from crews.finalize_workflow_crew import finalize_workflow_crew
from crews.identify_task_dependencies_crew import identify_task_dependencies_crew
from crews.validate_dag_crew import validate_dag_crew


# @traceable
async def run_workflow(inputs: Dict = None, openai_api_key: str = None):
    """Execute the full workflow."""
    if openai_api_key:
        os.environ["OPENAI_API_KEY"] = openai_api_key
    elif not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OpenAI API key must be provided")

    if inputs is None:
        inputs = {}

    results = {}
    crews = {}
    crews["create_task_dag"] = create_task_dag_crew().crew()
    crews["decompose_objective_into_tasks"] = decompose_objective_into_tasks_crew().crew()
    crews["define_workflow_objective"] = define_workflow_objective_crew().crew()
    crews["finalize_workflow"] = finalize_workflow_crew().crew()
    crews["identify_task_dependencies"] = identify_task_dependencies_crew().crew()
    crews["validate_dag"] = validate_dag_crew().crew()

    # Level 0 execution
    results["define_workflow_objective"] = await crews["define_workflow_objective"].kickoff_async(inputs=inputs)

    # Level 1 execution
    level_results = await asyncio.gather(crews["decompose_objective_into_tasks"].kickoff_async(inputs={"define_workflow_objective_output": results["define_workflow_objective"].raw}))
    for node_name, result in zip(['decompose_objective_into_tasks'], level_results):
        results[node_name] = result

    # Level 2 execution
    level_results = await asyncio.gather(crews["identify_task_dependencies"].kickoff_async(inputs={"decompose_objective_into_tasks_output": results["decompose_objective_into_tasks"].raw}))
    for node_name, result in zip(['identify_task_dependencies'], level_results):
        results[node_name] = result

    # Level 3 execution
    level_results = await asyncio.gather(crews["create_task_dag"].kickoff_async(inputs={"identify_task_dependencies_output": results["identify_task_dependencies"].raw}))
    for node_name, result in zip(['create_task_dag'], level_results):
        results[node_name] = result

    # Level 4 execution
    level_results = await asyncio.gather(crews["validate_dag"].kickoff_async(inputs={"create_task_dag_output": results["create_task_dag"].raw}))
    for node_name, result in zip(['validate_dag'], level_results):
        results[node_name] = result

    # Level 5 execution
    level_results = await asyncio.gather(crews["finalize_workflow"].kickoff_async(inputs={"validate_dag_output": results["validate_dag"].raw}))
    for node_name, result in zip(['finalize_workflow'], level_results):
        results[node_name] = result

    return results

# @traceable
def run_workflow_sync(inputs: Dict = None, openai_api_key: str = None):
    """Synchronous version of run_workflow."""
    return asyncio.run(run_workflow(inputs, openai_api_key))

if __name__ == "__main__":
    import sys
    import json

    api_key = os.getenv("OPENAI_API_KEY") or (sys.argv[1] if len(sys.argv) > 1 else None)
    if not api_key:
        print("Please provide OpenAI API key")
        sys.exit(1)

    print("Provide any runtime inputs/params/args/context in raw text or JSON format (press Enter for empty input):")
    user_input = input().strip()

    inputs = {"input": user_input} if user_input else {}

    try:
        if user_input:
            # Try to parse as JSON if provided
            json_input = json.loads(user_input)
            inputs = {"input": json_input}
    except json.JSONDecodeError:
        # If not valid JSON, use the raw string
        pass

    results = run_workflow_sync(inputs, openai_api_key=api_key)
