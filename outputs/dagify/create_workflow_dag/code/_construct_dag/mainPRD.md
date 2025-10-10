# _construct_dag - Complete PRD Documentation

## Overview
PRDs for nodes in the '_construct_dag' module.

## Table of Contents

- [validate_inputs](#validate_inputs)

- [parse_dependency_map](#parse_dependency_map)

- [extract_task_list](#extract_task_list)

- [validate_dag_consistency](#validate_dag_consistency)

- [build_dag_edges](#build_dag_edges)

- [format_digraph](#format_digraph)



---

## validate_inputs

### Description
Validates the inputs for constructing a DAG, checking dependency map and node outputs for correctness.

### Conceptual Info

This shim node is responsible for validating the inputs required for constructing a Directed Acyclic Graph (DAG). It checks the dependency map and node outputs to ensure they are correctly formatted and consistent.

### Docstring

**Summary:** Validates the dependency map and node outputs for DAG construction.

**Parameters:**

- dependency_map (str): A string representing the dependency map between tasks.
- node_outputs (str): A string containing output structures for each node.
**Returns:** str - A string indicating the result of the validation.

**Raises:**

- ValueError: If the dependency map or node outputs are invalid or inconsistent.
- TypeError: If the input types are incorrect.
**Examples:**

```python
>>> validate_inputs(dependency_map='task1:task2,task3', node_outputs='task1:out1,task2:out2')
>>> print(output)
'Validation successful'
```

```python
>>> validate_inputs(dependency_map='invalid_map', node_outputs='task1:out1')
>>> print(output)
'Validation failed: Invalid dependency map'
```



---

## parse_dependency_map

### Description
Parses a given dependency map string into a list of tuples representing task dependencies.

### Conceptual Info

This shim function is crucial for converting a string representation of task dependencies into a structured format that can be used for constructing a Directed Acyclic Graph (DAG) in workflow management systems.

### Docstring

**Summary:** Parses a dependency map string into a list of tuples, where each tuple represents a dependency between tasks.

**Parameters:**

- dependency_map (str): A string representing the dependency map between tasks.
**Returns:** List[tuple] - A list of tuples, where each tuple contains information about task dependencies.

**Raises:**

- ValueError: If the input dependency map string is malformed or cannot be parsed.
- TypeError: If the input is not a string.
**Examples:**

```python
>>> dependency_map_str = 'task1:task2,task3;task2:task4'
>>> parsed_dependencies = parse_dependency_map(dependency_map=dependency_map_str)
[('task1', ['task2', 'task3']), ('task2', ['task4'])]
```

```python
>>> dependency_map_str = 'A:B,C;B:D'
>>> parsed_dependencies = parse_dependency_map(dependency_map=dependency_map_str)
[('A', ['B', 'C']), ('B', ['D'])]
```



---

## extract_task_list

### Description
Extracts a list of tasks from the given dependency map and node outputs.

### Conceptual Info

This shim is responsible for extracting a list of tasks based on the dependency map and node outputs provided.

### Docstring

**Summary:** Extracts a list of tasks from the given dependency map and node outputs.

**Parameters:**

- dependency_map (str): A string representing the dependency map between tasks.
- node_outputs (str): A string containing output structures for each node.
**Returns:** List[str] - A list of task names extracted from the dependency map and node outputs.

**Raises:**

- ValueError: If the input dependency map or node outputs are invalid or malformed.
- TypeError: If the input types are not as expected (e.g., not strings).
**Examples:**

```python
>>> dependency_map = 'task1:task2,task3;task2:task4'
>>> node_outputs = 'task1:out1;task2:out2;task3:out3'
>>> extract_task_list(dependency_map=dependency_map, node_outputs=node_outputs)
['task1', 'task2', 'task3', 'task4']
```

```python
>>> dependency_map = 'A:B,C;B:D'
>>> node_outputs = 'A:1;B:2;C:3;D:4'
>>> extract_task_list(dependency_map=dependency_map, node_outputs=node_outputs)
['A', 'B', 'C', 'D']
```



---

## validate_dag_consistency

### Description
Validates the consistency of a Directed Acyclic Graph (DAG) given task list, dependencies, and node outputs.

### Conceptual Info

This shim node plays a crucial role in ensuring the integrity of the DAG structure by validating its consistency against the provided task list, dependencies, and node outputs.

### Docstring

**Summary:** Validates the DAG consistency by checking if the task list, dependencies, and node outputs are coherent.

**Parameters:**

- task_list (str): A string representing the list of tasks in the DAG.
- dependencies (str): A string representing the dependencies between tasks in the DAG.
- node_outputs (str): A string representing the outputs of each node in the DAG.
**Returns:** str - A string indicating whether the DAG is consistent. Returns 'DAG is consistent' if valid, otherwise raises an exception.

**Raises:**

- ValueError: If the task list, dependencies, or node outputs are invalid or inconsistent.
- TypeError: If the input types are not as expected (e.g., not strings).
**Examples:**

```python
>>> validate_dag_consistency(task_list='task1,task2,task3', dependencies='task1->task2,task2->task3', node_outputs='task1:out1,task2:out2,task3:out3')
'DAG is consistent'
```

```python
>>> validate_dag_consistency(task_list='task1,task2', dependencies='task1->task2,task2->task3', node_outputs='task1:out1,task2:out2')
ValueError: Inconsistent DAG structure detected.
```



---

## build_dag_edges

### Description
This shim node generates a list of edges representing the DAG structure based on the provided dependencies.

### Conceptual Info

The build_dag_edges shim is crucial for constructing the Directed Acyclic Graph (DAG) structure by generating edges based on task dependencies.

### Docstring

**Summary:** Generates a list of edges for the DAG based on the provided dependencies.

**Parameters:**

- dependencies (List[tuple]): A list of tuples representing the dependencies between tasks.
**Returns:** List[str] - A list of strings representing the edges in the DAG, where each edge is in the format 'task1 -> task2'.

**Raises:**

- ValueError: If the dependencies are malformed or inconsistent.
- TypeError: If the input dependencies are not a list of tuples.
**Examples:**

```python
>>> dependencies = [('A', 'B'), ('B', 'C'), ('A', 'C')]
>>> dag_edges = build_dag_edges(dependencies=dependencies)
['A -> B', 'B -> C', 'A -> C']
```

```python
>>> dependencies = [('task1', 'task2'), ('task2', 'task3')]
>>> dag_edges = build_dag_edges(dependencies=dependencies)
['task1 -> task2', 'task2 -> task3']
```



---

## format_digraph

### Description
Formats the given edges into a digraph structure.

### Conceptual Info

This shim function is responsible for taking a list of edges representing a directed graph and formatting them into a string that represents the digraph structure.

### Docstring

**Summary:** Formats the given edges into a digraph structure represented as a string.

**Parameters:**

- edges (str): A string representing the edges of the digraph, expected to be in a format that can be processed into a digraph structure.
**Returns:** str - A string representing the formatted digraph structure.

**Raises:**

- ValueError: If the input edges cannot be properly formatted into a digraph.
- TypeError: If the input edges are not of the expected type.
**Examples:**

```python
>>> format_digraph(edges='A->B;B->C')
'digraph { A -> B; B -> C }'
```

```python
>>> format_digraph(edges='X->Y;Y->Z;Z->X')
'digraph { X -> Y; Y -> Z; Z -> X }'
```

