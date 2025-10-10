# create_workflow_dag - Complete PRD Documentation

## Overview
PRDs for nodes in the 'create_workflow_dag' module.

## Table of Contents

- [define_objective](#define_objective)

- [decompose_objective](#decompose_objective)

- [identify_dependencies](#identify_dependencies)

- [define_node_outputs](#define_node_outputs)

- [construct_dag](#construct_dag)

- [validate_dag](#validate_dag)

- [finalize_workflow](#finalize_workflow)



---

## define_objective

### Description
Clearly define the objective or task description that the workflow needs to achieve

### Conceptual Info

This node is responsible for defining the objective or task description that the workflow is intended to achieve. It serves as the initial step in creating a workflow DAG.

### Docstring

**Summary:** Defines the objective or task description for the workflow.

**Returns:** str - The defined objective or task description.

**Raises:**

- ValueError: If the objective is not provided or is empty.
**Examples:**

```python
>>> define_objective()
"Create a workflow to process customer orders"
```

```python
>>> define_objective()
"Design a data pipeline for real-time analytics"
```



---

## decompose_objective

### Description
Decompose the objective into smaller, manageable tasks or steps

### Conceptual Info

This node takes the defined objective from its parent node 'define_objective' and breaks it down into smaller, manageable tasks or steps.

### Docstring

**Summary:** Decomposes the given objective into a list of tasks or steps.

**Parameters:**

- objective (str): The defined objective or task description obtained from the 'define_objective' node.
**Returns:** List[str] - A list of decomposed tasks or steps derived from the objective.

**Raises:**

- ValueError: If the objective is empty or not a string.
**Examples:**

```python
>>> decompose_objective(objective='Create a workflow DAG')
['Define objective', 'Decompose objective', 'Identify dependencies', 'Construct DAG']
```

```python
>>> decompose_objective(objective='Develop a machine learning model')
['Collect data', 'Preprocess data', 'Train model', 'Evaluate model']
```



---

## identify_dependencies

### Description
Identify dependencies between the decomposed tasks

### Conceptual Info

This node analyzes the decomposed tasks from the 'decompose_objective' node to identify dependencies between them, producing a dependency map.

### Docstring

**Summary:** Identify dependencies between decomposed tasks.

**Parameters:**

- task_list (List[str]): List of decomposed tasks or steps from the 'decompose_objective' node.
**Returns:** List[str] - List representing the dependency map between tasks.

**Raises:**

- ValueError: If the task_list is empty or malformed.
**Examples:**

```python
>>> task_list = ['task1', 'task2', 'task3']
>>> dependency_map = identify_dependencies(task_list)
['task1->task2', 'task2->task3']
```

```python
>>> task_list = ['init', 'process', 'finalize']
>>> dependency_map = identify_dependencies(task_list)
['init->process', 'process->finalize']
```



---

## define_node_outputs

### Description
Define the output structure for each node or task

### Conceptual Info

This node defines the output structure for each task or node in the workflow DAG.

### Docstring

**Summary:** Defines the output structure for each node based on the decomposed tasks.

**Parameters:**

- task_list (List[str]): List of decomposed tasks or steps from the decompose_objective node.
**Returns:** List[str] - A list of output structures for each node in the workflow DAG.

**Raises:**

- ValueError: If the task_list is empty or not a list.
**Examples:**

```python
>>> task_list = ['task1', 'task2']
>>> node_outputs = define_node_outputs(task_list)
['{"task": "task1", "output_type": "str"}', '{"task": "task2", "output_type": "int"}']
```

```python
>>> task_list = ['data_ingestion', 'data_processing']
>>> node_outputs = define_node_outputs(task_list)
['{"task": "data_ingestion", "output_type": "DataFrame"}', '{"task": "data_processing", "output_type": "DataFrame"}']
```



---

## construct_dag

### Description
Construct the workflow DAG using the decomposed tasks and their dependencies

### Conceptual Info

This node constructs a Directed Acyclic Graph (DAG) representing the workflow based on the decomposed tasks, their dependencies, and output structures.

### Docstring

**Summary:** Constructs the workflow DAG using the task list, dependency map, and node outputs.

**Parameters:**

- task_list (List[str]): List of decomposed tasks or steps derived from the objective.
- dependency_map (List[str]): List representing the dependency map between tasks.
- node_outputs (List[str]): List containing output structures for each node.
**Returns:** str - The constructed workflow DAG structure represented as a string.

**Raises:**

- ValueError: If the task list, dependency map, or node outputs are inconsistent or malformed.
**Examples:**

```python
>>> task_list = ['task1', 'task2', 'task3']
>>> dependency_map = [('task1', 'task2'), ('task2', 'task3')]
>>> node_outputs = [{'task1': 'output1'}, {'task2': 'output2'}, {'task3': 'output3'}]
>>> dag_structure = construct_dag(task_list, dependency_map, node_outputs)
digraph G { task1 -> task2; task2 -> task3; }
```

```python
>>> task_list = ['A', 'B', 'C']
>>> dependency_map = [('A', 'B'), ('B', 'C')]
>>> node_outputs = [{'A': 'resultA'}, {'B': 'resultB'}, {'C': 'resultC'}]
>>> dag_structure = construct_dag(task_list, dependency_map, node_outputs)
digraph G { A -> B; B -> C; }
```



---

## validate_dag

### Description
Validate the constructed workflow DAG for correctness and acyclicity

### Conceptual Info

This node validates the constructed workflow DAG for correctness and ensures it is acyclic.

### Docstring

**Summary:** Validate the constructed workflow DAG for correctness and acyclicity.

**Parameters:**

- dag_structure (str): The constructed workflow DAG structure from the construct_dag node.
**Returns:** bool - Whether the DAG is valid and acyclic.

**Raises:**

- ValueError: If the DAG structure is malformed or contains cycles.
**Examples:**

```python
>>> validate_dag('A->B;B->C')
True
```

```python
>>> validate_dag('A->B;B->A')
False
```



---

## finalize_workflow

### Description
Finalize the workflow by ensuring all nodes are connected and the DAG is valid

### Conceptual Info

This node finalizes the workflow DAG by ensuring all nodes are connected and the DAG is valid, based on the validation result from its parent node.

### Docstring

**Summary:** Finalize the workflow DAG based on validation results.

**Parameters:**

- validation_result (bool): The validation result from the validate_dag node indicating whether the DAG is valid and acyclic.
**Returns:** str - The finalized workflow DAG as a string representation.

**Raises:**

- ValueError: If the validation result is False, indicating the DAG is not valid or contains cycles.
**Examples:**

```python
>>> finalize_workflow(validation_result=True)
'valid_dag_structure'
```

```python
>>> finalize_workflow(validation_result=False)
ValueError: 'DAG is not valid or contains cycles'
```

