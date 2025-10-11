# Generated Pydantic models for CrewAI task outputs
from typing import List, Dict, Any, Optional
from pydantic import BaseModel

class create_task_dag_output(BaseModel):
    """Create a DAG representing the tasks and their dependencies"""

    task_ids: str  # List of unique task identifiers used in the DAG
    # List of source task identifiers for each directed edge in
    # the DAG
    edge_sources: str
    # List of destination task identifiers for each directed
    # edge in the DAG
    edge_destinations: str
    # Indicates whether the constructed DAG is acyclic and
    # complete
    is_valid: bool

class decompose_objective_into_tasks_output(BaseModel):
    """Break down the workflow objective into individual tasks"""

    # List of task descriptions that represent the decomposed
    # workflow objective
    tasks: List[str]
    task_count: int  # Number of tasks identified in the decomposition

class define_workflow_objective_output(BaseModel):
    """Define the objective of the workflow"""

    # The primary goal of the workflow expressed as a concise
    # statement.
    workflow_objective: str

class finalize_workflow_output(BaseModel):
    """Finalize the workflow DAG"""

    # String representation of the finalized DAG, e.g.,
    # serialized adjacency list or other format.
    dag_representation: str
    is_valid: bool  # Whether the finalized DAG is valid and acyclic.
    # Whether any adjustments were made to the DAG during
    # finalization.
    adjustments_made: bool
    # Ordered list of task identifiers in the finalized DAG.
    adjusted_task_order: str
    # List of task identifiers that have missing or unresolved
    # dependencies.
    missing_dependencies: str
    cycles_detected: str  # List of detected cycles in the DAG, if any.
    warnings: str  # Any warnings or notes about potential issues.
    summary: str  # Short textual summary of the finalized workflow.

class identify_task_dependencies_output(BaseModel):
    """Identify dependencies between tasks"""

    tasks: List[str]  # List of identified task names.
    # List of dependency relationships in the format TaskA
    # depends on TaskB.
    dependencies: List[str]
    # Indicates whether any dependencies were identified.
    dependency_exists: bool

class validate_dag_output(BaseModel):
    """Validate the created DAG for correctness and acyclicity"""

    is_valid: bool  # Indicates whether the DAG passes all validation checks.
    node_count: int  # Total number of nodes present in the DAG.
    edge_count: int  # Total number of directed edges in the DAG.
    # List of cycle identifiers or descriptions found in the DAG
    # (empty if none).
    cycles_detected: str
    # List of node names that reference non‑existent
    # dependencies (empty if none).
    missing_dependencies: str
    errors: str  # Detailed error messages for any validation failures.

