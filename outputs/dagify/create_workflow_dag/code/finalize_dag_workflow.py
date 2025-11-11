from ._finalize_dag_workflow.validate_input_consistency import validate_input_consistency
from ._finalize_dag_workflow.raise_value_error import raise_value_error
from ._finalize_dag_workflow.validate_dag_structure import validate_dag_structure
from ._finalize_dag_workflow.evaluate_prompt_quality import evaluate_prompt_quality
from ._finalize_dag_workflow.evaluate_description_completeness import evaluate_description_completeness
from ._finalize_dag_workflow.calculate_workflow_efficiency import calculate_workflow_efficiency
from ._finalize_dag_workflow.identify_validation_issues import identify_validation_issues
from ._finalize_dag_workflow.determine_overall_validity import determine_overall_validity
from ._finalize_dag_workflow.format_validation_details import format_validation_details

from pydantic import BaseModel, Field
from typing import List


class DefineNodePromptsAndDescriptionsOutput(BaseModel):
    """Pydantic model for define_node_prompts_and_descriptions node outputs."""
    node_names: List[str] = (
        Field(..., description="List of all node names in the DAG.")
    )
    node_prompts: List[str] = (
        Field(..., description = (
            "List of prompts corresponding to each node name.")
        )
    )
    node_descriptions: List[str] = (
        Field(..., description = (
            "List of descriptions corresponding to each node name.")
        )
    )


class FinalizeDagWorkflowOutput(BaseModel):
    """Pydantic model for finalize_dag_workflow node outputs."""
    is_valid: bool = (
        Field(..., description = (
            "Whether the DAG workflow is valid and effective")
        )
    )
    validation_details: str = (
        Field(..., description = (
            "List of details or issues found during validation")
        )
    )
    efficiency_score: float = (
        Field(..., description = (
            "A score indicating the efficiency of the workflow, ranging from 0 to 1")
        )
    )


def finalize_dag_workflow(define_node_prompts_and_descriptions_input: DefineNodePromptsAndDescriptionsOutput, **kwargs) -> FinalizeDagWorkflowOutput:
    """
    Finalize the DAG workflow by validating its correctness and effectiveness.

    Parameters
    ----------
    node_names : List[str]
        List of node names in the DAG
    node_prompts : List[str]
        List of prompts corresponding to each node name
    node_descriptions : List[str]
        List of descriptions corresponding to each node name

    Returns
    -------
    Dict[str, Any]
        A dictionary containing the validation result, details, and
        efficiency score

    Raises
    ------
    ValueError
        If the input node names, prompts, or descriptions are invalid or
        inconsistent

    Examples
    --------
    >>> node_names = ['node1', 'node2', 'node3']
    >>> node_prompts = ['prompt1', 'prompt2', 'prompt3']
    >>> node_descriptions = ['description1', 'description2', 'description3']
    >>> result = finalize_dag_workflow(node_names, node_prompts,
    node_descriptions)
    {'is_valid': True, 'validation_details': [], 'efficiency_score': 0.8}

    """
    input_validation_result: bool = validate_input_consistency(
        node_names=define_node_prompts_and_descriptions_input.node_names,
        node_prompts=define_node_prompts_and_descriptions_input.node_prompts,
        node_descriptions=define_node_prompts_and_descriptions_input.node_descriptions
    )
    
    if not input_validation_result:
        raise_value_error(message="Input node names, prompts, or descriptions are invalid or inconsistent")
    
    dag_structure_validation: bool = validate_dag_structure(
        node_names=define_node_prompts_and_descriptions_input.node_names
    )
    
    prompt_quality_score: float = evaluate_prompt_quality(
        node_prompts=define_node_prompts_and_descriptions_input.node_prompts
    )
    
    description_completeness_score: float = evaluate_description_completeness(
        node_descriptions=define_node_prompts_and_descriptions_input.node_descriptions
    )
    
    workflow_efficiency_score: float = calculate_workflow_efficiency(
        node_names=define_node_prompts_and_descriptions_input.node_names,
        node_prompts=define_node_prompts_and_descriptions_input.node_prompts,
        node_descriptions=define_node_prompts_and_descriptions_input.node_descriptions
    )
    
    validation_issues: List[str] = identify_validation_issues(
        dag_valid=dag_structure_validation,
        prompt_score=prompt_quality_score,
        description_score=description_completeness_score
    )
    
    is_workflow_valid: bool = determine_overall_validity(
        dag_valid=dag_structure_validation,
        validation_issues=validation_issues
    )
    
    validation_details_str: str = format_validation_details(validation_issues=validation_issues)
    
    return FinalizeDagWorkflowOutput(
        is_valid=is_workflow_valid,
        validation_details=validation_details_str,
        efficiency_score=workflow_efficiency_score
    )