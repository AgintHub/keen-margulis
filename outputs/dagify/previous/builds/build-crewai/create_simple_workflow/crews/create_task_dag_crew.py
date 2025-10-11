from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task
from .models import create_task_dag_output

@CrewBase
class create_task_dag_crew:
    """Crew for create_task_dag operations."""

    @agent
    def create_task_dag_agent(self):
        return Agent(
            role="Create Task Dag Specialist",
            goal="""Create a DAG representing the tasks and their dependencies""",
            backstory="""Builds a directed acyclic graph (DAG) from a list of task
                         identifiers and dependency relations, producing node
                         identifiers, edge lists, and a validity flag.""",
            verbose=True
        )


    @task
    def create_task_dag_task(self):
        """Task for create_task_dag."""
        agent = self.create_task_dag_agent()
        return Task(
            description="""Simulate the Python function `create_task_dag`.
                       
                       Function specification:
                       Constructs a DAG from given tasks and dependency
                           relations.
                       
                       Parameters
                       ----------
                       tasks : List[str]
                           A list of task identifiers that will become the DAG
                           nodes.
                       dependencies : List[str]
                           Each string represents a dependency in the format
                           'TaskA depends on
                           TaskB'.
                       
                       Returns
                       -------
                       dict
                           A dictionary with four keys: task_ids (List[str]),
                           edge_sources
                           (List[str]), edge_destinations (List[str]), and
                           is_valid (bool).
                       
                       Raises
                       ------
                       ValueError
                           Raised when a dependency refers to a task not present
                           in the `tasks`
                           list.
                       ValueError
                           Raised when a dependency string does not match the
                           expected 'TaskA
                           depends on TaskB' pattern.
                       
                       Examples
                       --------
                       >>> tasks = ['A', 'B', 'C']
                       >>> dependencies = ['B depends on A', 'C depends on B']
                       >>> result = create_task_dag(tasks, dependencies)
                       >>> print(result)
                       {'task_ids': ['A', 'B', 'C'], 'edge_sources': ['A', 'B'],
                           'edge_destinations': ['B', 'C'], 'is_valid': True}
                       
                       >>> tasks = ['A', 'B']
                       >>> dependencies = ['A depends on B', 'B depends on A']
                       >>> result = create_task_dag(tasks, dependencies)
                       >>> print(result)
                       {'task_ids': ['A', 'B'], 'edge_sources': ['B', 'A'],
                           'edge_destinations': ['A', 'B'], 'is_valid': False}
                       
                       Using the provided inputs: Using
                           {identify_task_dependencies_output}, Create a DAG
                           representing the tasks and their dependencies""",
            agent=agent,
            expected_output="""{
                               task_ids: str  # List of unique task identifiers
                               used in the DAG
                               edge_sources: str  # List of source task
                               identifiers for each directed edge in the DAG
                               edge_destinations: str  # List of destination
                               task identifiers for each directed edge in the
                               DAG
                               is_valid: bool  # Indicates whether the
                               constructed DAG is acyclic and complete
                           }""",
            output_pydantic=create_task_dag_output
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.create_task_dag_agent()],
            tasks=[self.create_task_dag_task()],
            verbose=True
        )
