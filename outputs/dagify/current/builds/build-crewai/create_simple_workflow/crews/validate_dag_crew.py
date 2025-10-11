from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task
from .models import validate_dag_output

@CrewBase
class validate_dag_crew:
    """Crew for validate_dag operations."""

    @agent
    def validate_dag_agent(self):
        return Agent(
            role="Validate Dag Specialist",
            goal="""Validate the created DAG for correctness and acyclicity""",
            backstory="""The validate_dag node verifies that a workflow DAG is
                         well‑formed, acyclic, and internally consistent. It
                         acts as a safety net before the workflow is finalized,
                         catching missing dependencies and logical cycles that
                         could cause runtime failures.""",
            verbose=True
        )


    @task
    def validate_dag_task(self):
        """Task for validate_dag."""
        agent = self.validate_dag_agent()
        return Task(
            description="""Simulate the Python function `validate_dag`.
                       
                       Function specification:
                       Validates a Directed Acyclic Graph (DAG) representation
                           for correctness, acyclicity, and missing
                           dependencies.
                       
                       Parameters
                       ----------
                       task_ids : List[str]
                           List of unique identifiers for all tasks in the
                           workflow.
                       edge_sources : List[str]
                           List of task identifiers representing the source of
                           each directed
                           edge.
                       edge_destinations : List[str]
                           List of task identifiers representing the destination
                           of each
                           directed edge.
                       is_valid_input : bool
                           (Optional) A flag from `create_task_dag` indicating
                           preliminary
                           validity. It is used only as a hint; full validation
                           is performed
                           regardless.
                       
                       Returns
                       -------
                       dict
                           Dictionary containing validation results: -
                           `is_valid` (bool):
                           Overall validity. - `node_count` (int): Number of
                           nodes. -
                           `edge_count` (int): Number of directed edges. -
                           `cycles_detected`
                           (List[str]): Descriptions of any detected cycles. -
                           `missing_dependencies` (List[str]): Tasks that
                           reference undefined
                           dependencies. - `errors` (List[str]): Human‑readable
                           error messages
                           for all failures.
                       
                       Raises
                       ------
                       ValueError
                           If `edge_sources` and `edge_destinations` lists are
                           not of the same
                           length.
                       ValueError
                           If `task_ids` contains duplicate identifiers.
                       
                       Examples
                       --------
                       >>> task_ids = ['A', 'B', 'C']
                       >>> edge_sources = ['A', 'B']
                       >>> edge_destinations = ['B', 'C']
                       >>> result = validate_dag(task_ids, edge_sources,
                           edge_destinations)
                       >>> print(result)
                       {'is_valid': True, 'node_count': 3, 'edge_count': 2,
                           'cycles_detected': [], 'missing_dependencies': [],
                           'errors': []}
                       
                       >>> task_ids = ['A', 'B', 'C']
                       >>> edge_sources = ['A', 'B', 'C']
                       >>> edge_destinations = ['B', 'C', 'A']
                       >>> result = validate_dag(task_ids, edge_sources,
                           edge_destinations)
                       >>> print(result)
                       {'is_valid': False, 'node_count': 3, 'edge_count': 3,
                           'cycles_detected': ['A -> B -> C -> A'],
                           'missing_dependencies': [], 'errors': ['Cycle
                           detected: A -> B -> C -> A']}
                       
                       Using the provided inputs: Using
                           {create_task_dag_output}, Validate the created DAG
                           for correctness and acyclicity""",
            agent=agent,
            expected_output="""{
                               is_valid: bool  # Indicates whether the DAG
                               passes all validation checks.
                               node_count: int  # Total number of nodes present
                               in the DAG.
                               edge_count: int  # Total number of directed edges
                               in the DAG.
                               cycles_detected: str  # List of cycle identifiers
                               or descriptions found in the DAG (empty if none).
                               missing_dependencies: str  # List of node names
                               that reference non‑existent dependencies (empty
                               if none).
                               errors: str  # Detailed error messages for any
                               validation failures.
                           }""",
            output_pydantic=validate_dag_output
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.validate_dag_agent()],
            tasks=[self.validate_dag_task()],
            verbose=True
        )
