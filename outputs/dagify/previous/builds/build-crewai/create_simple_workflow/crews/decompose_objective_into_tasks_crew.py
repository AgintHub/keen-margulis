from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task
from .models import decompose_objective_into_tasks_output

@CrewBase
class decompose_objective_into_tasks_crew:
    """Crew for decompose_objective_into_tasks operations."""

    @agent
    def decompose_objective_into_tasks_agent(self):
        return Agent(
            role="Decompose Objective Into Tasks Specialist",
            goal="""Break down the workflow objective into individual tasks""",
            backstory="""Transforms a high‑level workflow goal into a concrete
                         sequence of actionable tasks, enabling downstream
                         dependency analysis and DAG construction.""",
            verbose=True
        )


    @task
    def decompose_objective_into_tasks_task(self):
        """Task for decompose_objective_into_tasks."""
        agent = self.decompose_objective_into_tasks_agent()
        return Task(
            description="""Simulate the Python function
                           `decompose_objective_into_tasks`.
                       
                       Function specification:
                       Breaks down a workflow objective into discrete tasks.
                       
                       Parameters
                       ----------
                       workflow_objective : str
                           A concise statement describing the primary goal of
                           the workflow.
                       
                       Returns
                       -------
                       Tuple[List[str], int]
                           A tuple containing (1) a list of task descriptions
                           and (2) the count
                           of tasks.
                       
                       Raises
                       ------
                       ValueError
                           Raised when `workflow_objective` is empty or consists
                           only of
                           whitespace.
                       
                       Examples
                       --------
                       >>> tasks, count = decompose_objective_into_tasks('Build
                           a machine learning pipeline for predicting house
                           prices')
                       (['Collect and clean data', 'Split dataset', 'Select
                           model', 'Train model', 'Evaluate model', 'Deploy
                           model'], 6)
                       
                       >>> tasks, count = decompose_objective_into_tasks('Write
                           a report')
                       (['Plan report structure', 'Collect data', 'Write draft',
                           'Revise', 'Finalize'], 5)
                       
                       Using the provided inputs: Using
                           {define_workflow_objective_output}, Break down the
                           workflow objective into individual tasks""",
            agent=agent,
            expected_output="""{
                               tasks: list of strs  # List of task descriptions
                               that represent the decomposed workflow objective
                               task_count: int  # Number of tasks identified in
                               the decomposition
                           }""",
            output_pydantic=decompose_objective_into_tasks_output
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.decompose_objective_into_tasks_agent()],
            tasks=[self.decompose_objective_into_tasks_task()],
            verbose=True
        )
