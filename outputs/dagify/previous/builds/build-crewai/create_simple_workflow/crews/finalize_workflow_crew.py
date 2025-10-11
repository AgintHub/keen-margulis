from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task
from .models import finalize_workflow_output

@CrewBase
class finalize_workflow_crew:
    """Crew for finalize_workflow operations."""

    @agent
    def finalize_workflow_agent(self):
        return Agent(
            role="Finalize Workflow Specialist",
            goal="""Finalize the workflow DAG""",
            backstory="""The finalize_workflow node takes a validated DAG, checks
                         for any remaining inconsistencies such as missing
                         dependencies or cycles, applies necessary adjustments,
                         and produces a clean, ordered representation ready for
                         execution.""",
            verbose=True
        )


    @task
    def finalize_workflow_task(self):
        """Task for finalize_workflow."""
        agent = self.finalize_workflow_agent()
        return Task(
            description="""Simulate the Python function `finalize_workflow`.
                       
                       Function specification:
                       Finalize a workflow DAG by validating its structure,
                           resolving missing dependencies, removing cycles, and
                           ordering tasks.
                       
                       Parameters
                       ----------
                       task_ids : List[str]
                           Unique identifiers of all tasks in the DAG.
                       edge_sources : List[str]
                           Source task identifiers for each directed edge.
                       edge_destinations : List[str]
                           Destination task identifiers for each directed edge.
                       is_valid : bool
                           Result of the validation step (True if the DAG passed
                           all checks).
                       node_count : int
                           Total number of nodes in the DAG.
                       edge_count : int
                           Total number of directed edges in the DAG.
                       cycles_detected : List[str]
                           List of cycle identifiers found during validation.
                       missing_dependencies : List[str]
                           List of node names that reference non‑existent
                           dependencies.
                       errors : List[str]
                           Detailed error messages from the validation step.
                       
                       Returns
                       -------
                       Dict[str, Any]
                           A dictionary containing the finalized DAG
                           representation and
                           metadata: dag_representation (str), is_valid (bool),
                           adjustments_made (bool), adjusted_task_order
                           (List[str]),
                           missing_dependencies (List[str]), cycles_detected
                           (List[str]),
                           warnings (List[str]), and summary (str).
                       
                       Raises
                       ------
                       ValueError
                           If any required input lists are empty or lengths of
                           edge_sources and
                           edge_destinations mismatch.
                       
                       Examples
                       --------
                       >>> dag = finalize_workflow(
                       
                       ...     task_ids=['A', 'B', 'C'],
                       
                       ...     edge_sources=['A', 'B'],
                       
                       ...     edge_destinations=['B', 'C'],
                       
                       ...     is_valid=True,
                       
                       ...     node_count=3,
                       
                       ...     edge_count=2,
                       
                       ...     cycles_detected=[],
                       
                       ...     missing_dependencies=[],
                       
                       ...     errors=[]
                       
                       >>> )
                       {'dag_representation': 'A -> B -> C', 'is_valid': True,
                           'adjustments_made': False, 'adjusted_task_order':
                           ['A', 'B', 'C'], 'missing_dependencies': [],
                           'cycles_detected': [], 'warnings': [], 'summary':
                           'DAG finalized successfully.'}
                       
                       >>> dag = finalize_workflow(
                       
                       ...     task_ids=['A', 'B', 'C'],
                       
                       ...     edge_sources=['A', 'B', 'C'],
                       
                       ...     edge_destinations=['B', 'C', 'A'],
                       
                       ...     is_valid=False,
                       
                       ...     node_count=3,
                       
                       ...     edge_count=3,
                       
                       ...     cycles_detected=['A->B->C->A'],
                       
                       ...     missing_dependencies=[],
                       
                       ...     errors=['Cycle detected']
                       
                       >>> )
                       {'dag_representation': 'A -> B -> C', 'is_valid': False,
                           'adjustments_made': True, 'adjusted_task_order':
                           ['A', 'B', 'C'], 'missing_dependencies': [],
                           'cycles_detected': ['A->B->C->A'], 'warnings':
                           ['Cycle removed: A->B->C->A'], 'summary': 'DAG
                           finalized with cycle removal.'}
                       
                       Using the provided inputs: Using {validate_dag_output},
                           Finalize the workflow DAG""",
            agent=agent,
            expected_output="""{
                               dag_representation: str  # String representation
                               of the finalized DAG, e.g., serialized adjacency
                               list or other format.
                               is_valid: bool  # Whether the finalized DAG is
                               valid and acyclic.
                               adjustments_made: bool  # Whether any adjustments
                               were made to the DAG during finalization.
                               adjusted_task_order: str  # Ordered list of task
                               identifiers in the finalized DAG.
                               missing_dependencies: str  # List of task
                               identifiers that have missing or unresolved
                               dependencies.
                               cycles_detected: str  # List of detected cycles
                               in the DAG, if any.
                               warnings: str  # Any warnings or notes about
                               potential issues.
                               summary: str  # Short textual summary of the
                               finalized workflow.
                           }""",
            output_pydantic=finalize_workflow_output
        )


    @crew
    # @traceable
    def crew(self):
        """Create the crew instance."""
        return Crew(
            agents=[self.finalize_workflow_agent()],
            tasks=[self.finalize_workflow_task()],
            verbose=True
        )
