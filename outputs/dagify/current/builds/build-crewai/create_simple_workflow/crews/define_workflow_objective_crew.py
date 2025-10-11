from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task
from .models import define_workflow_objective_output

@CrewBase
class define_workflow_objective_crew:
    """Crew for define_workflow_objective operations."""

    @agent
    def define_workflow_objective_agent(self):
        return Agent(
            role="Define Workflow Objective Specialist",
            goal="""Define the objective of the workflow""",
            backstory="""Captures the high‑level purpose of the workflow, providing
                         a clear goal that drives the subsequent task
                         decomposition, dependency analysis, and DAG
                         construction.""",
            verbose=True
        )


    @task
    def define_workflow_objective_task(self):
        """Task for define_workflow_objective."""
        agent = self.define_workflow_objective_agent()
        return Task(
            description="""Simulate the Python function `define_workflow_objective`.
                       
                       Function specification:
                       Generate a concise objective statement for the workflow
                           based on the user’s intent.
                       
                       Returns
                       -------
                       str
                           Concise objective of the workflow.
                       
                       Raises
                       ------
                       ValueError
                           If the generated objective is empty or exceeds an
                           acceptable length.
                       
                       Examples
                       --------
                       >>> objective = define_workflow_objective()
                       'Implement an automated data ingestion pipeline for
                           real‑time analytics'
                       
                       >>> objective = define_workflow_objective()
                       'Develop a user‑friendly mobile application for inventory
                           management'
                       
                       Using the provided inputs: Using {input}, Define the
                           objective of the workflow""",
            agent=agent,
            expected_output="""{
                               workflow_objective: str  # The primary goal of
                               the workflow expressed as a concise statement.
                           }""",
            output_pydantic=define_workflow_objective_output
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.define_workflow_objective_agent()],
            tasks=[self.define_workflow_objective_task()],
            verbose=True
        )
