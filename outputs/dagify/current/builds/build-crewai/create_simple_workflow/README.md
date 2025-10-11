# AI Workflow

This is an AI-powered workflow using CrewAI agents to accomplish complex tasks through collaboration.

## Workflow Steps

1. **define_workflow_objective**: Define the objective of the workflow
2. **decompose_objective_into_tasks**: Break down the workflow objective into individual tasks (using output from define_workflow_objective)
3. **identify_task_dependencies**: Identify dependencies between tasks (using output from decompose_objective_into_tasks)
4. **create_task_dag**: Create a DAG representing the tasks and their dependencies (using output from identify_task_dependencies)
5. **validate_dag**: Validate the created DAG for correctness and acyclicity (using output from create_task_dag)
6. **finalize_workflow**: Finalize the workflow DAG (using output from validate_dag)

## Running the Workflow

This workflow is self-contained and requires minimal setup:

1. Install uv if you haven't already:
```bash
pip install uv
```

2. Set your OpenAI API key:
```bash
export OPENAI_API_KEY='your-api-key'
```

3. Run the workflow:
```bash
./run.sh
```

That's it! The workflow will automatically handle all dependencies and execution.

## Input/Output

- The workflow accepts input as either plain text or JSON
- Each agent processes its input and produces structured output
- Final results are displayed for each step of the workflow
