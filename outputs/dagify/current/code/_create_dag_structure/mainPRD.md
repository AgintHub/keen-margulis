# _create_dag_structure - Complete PRD Documentation

## Overview
PRDs for nodes in the '_create_dag_structure' module.

## Table of Contents

- [parse_dependency_string](#parse_dependency_string)

- [extract_unique_nodes](#extract_unique_nodes)

- [format_edges_for_output](#format_edges_for_output)

- [detect_cycles_in_graph](#detect_cycles_in_graph)

- [find_root_nodes](#find_root_nodes)

- [validate_dag_structure](#validate_dag_structure)



---

## parse_dependency_string

### Description
Parses a dependency string into a list of tuples representing the dependencies.

### Conceptual Info

The parse_dependency_string shim function takes a string representing dependencies between tasks and parses it into a structured format that can be used for further processing.

### Docstring

**Summary:** Parses a dependency string into a list of tuples representing the dependencies.

**Parameters:**

- dependency_string (str): Input string representing the dependencies, where each dependency is represented as 'subtask_id_1 -> subtask_id_2'.
**Returns:** List[tuple] - List of tuples representing the dependencies, where each tuple contains two strings representing the dependent and independent tasks.

**Raises:**

- ValueError: When the input string is not in the correct format.
- TypeError: When the input is not a string.
**Examples:**

```python
>>> parse_dependency_string('A -> B, C -> D')
[('A', 'B'), ('C', 'D')]
```

```python
>>> parse_dependency_string('E -> F, G -> H, I -> J')
[('E', 'F'), ('G', 'H'), ('I', 'J')]
```



---

## extract_unique_nodes

### Description
Extracts a list of unique nodes from a given set of dependencies.

### Conceptual Info

The extract_unique_nodes shim function takes a set of dependencies as input and returns a list of unique nodes present in those dependencies.

### Docstring

**Summary:** Extracts a list of unique nodes from a given set of dependencies.

**Parameters:**

- dependencies (List[tuple]): A list of tuples, where each tuple represents a dependency between two nodes.
**Returns:** List[str] - A list of unique node names extracted from the dependencies.

**Raises:**

- TypeError: When the input dependencies are not in the expected format.
- ValueError: When the input dependencies are invalid or malformed.
**Examples:**

```python
>>> dependencies = [('A', 'B'), ('B', 'C'), ('A', 'C')]
>>> extract_unique_nodes(dependencies=dependencies)
['A', 'B', 'C']
```

```python
>>> dependencies = [('Node1', 'Node2'), ('Node2', 'Node3'), ('Node1', 'Node3')]
>>> extract_unique_nodes(dependencies=dependencies)
['Node1', 'Node2', 'Node3']
```



---

## format_edges_for_output

### Description
Formats a list of parsed dependencies into a list of strings representing edges in a DAG.

### Conceptual Info

The format_edges_for_output shim function takes a list of parsed dependencies and formats them into a list of strings representing edges in a DAG. This is necessary to provide a standardized output format for the create_dag_structure function.

### Docstring

**Summary:** Formats a list of parsed dependencies into a list of strings representing edges in a DAG.

**Parameters:**

- dependencies (str): A string representation of a list of parsed dependencies, where each dependency is a tuple of two node names.
**Returns:** List[str] - A list of strings representing edges in a DAG, where each edge is in the format 'node1->node2'.

**Raises:**

- ValueError: When the input dependencies are invalid or malformed.
- TypeError: When the input dependencies are not of the correct type.
**Examples:**

```python
>>> format_edges_for_output(dependencies=[('A', 'B'), ('B', 'C')])
['A->B', 'B->C']
```

```python
>>> format_edges_for_output(dependencies=[('D', 'E'), ('E', 'F')])
['D->E', 'E->F']
```



---

## detect_cycles_in_graph

### Description
This shim detects whether a cycle exists in a graph represented by a list of nodes and their dependencies.

### Conceptual Info

The detect_cycles_in_graph shim is crucial for validating the structure of a Directed Acyclic Graph (DAG), ensuring it does not contain cycles which would prevent a valid topological sorting.

### Docstring

**Summary:** Detects whether a cycle exists in a graph given its nodes and dependencies.

**Parameters:**

- nodes (List[str]): List of node names in the graph.
- dependencies (List[tuple]): List of dependencies where each dependency is a tuple of two node names (node1, node2) indicating node1 -> node2.
**Returns:** bool - True if a cycle is detected in the graph, False otherwise.

**Raises:**

- ValueError: If the input graph structure is invalid (e.g., a node references a non-existent node).
- TypeError: If the input types do not match the expected types (list of str for nodes and list of tuples for dependencies).
**Examples:**

```python
>>> detect_cycles_in_graph(['A', 'B', 'C'], [('A', 'B'), ('B', 'C')])
False
```

```python
>>> detect_cycles_in_graph(['A', 'B', 'C'], [('A', 'B'), ('B', 'C'), ('C', 'A')])
True
```



---

## find_root_nodes

### Description
This shim identifies the root nodes in a directed acyclic graph (DAG) given its nodes and dependencies.

### Conceptual Info

The find_root_nodes shim is crucial for constructing a valid DAG by identifying nodes with no incoming edges, which are the starting points of the graph.

### Docstring

**Summary:** Finds the root nodes in a DAG given its nodes and dependencies.

**Parameters:**

- nodes (List[str]): A list of node names in the DAG.
- dependencies (List[tuple]): A list of dependencies between nodes, where each dependency is a tuple of two node names.
**Returns:** List[str] - A list of root node names in the DAG.

**Raises:**

- ValueError: If the input nodes or dependencies are invalid (e.g., a node has no dependencies but is not a root node).
- TypeError: If the input types are incorrect (e.g., nodes is not a list of strings, dependencies is not a list of tuples).
**Examples:**

```python
>>> nodes = ['A', 'B', 'C']
>>> dependencies = [('A', 'B'), ('B', 'C')]
>>> root_nodes = find_root_nodes(nodes, dependencies)
['A']
```

```python
>>> nodes = ['X', 'Y', 'Z']
>>> dependencies = [('X', 'Y'), ('Y', 'Z'), ('Z', 'X')]
>>> try:
...     root_nodes = find_root_nodes(nodes, dependencies)
>>> except ValueError as e:
...     print(e)
Dependencies form a cycle, making it impossible to create a valid DAG
```



---

## validate_dag_structure

### Description
Validates the structure of a Directed Acyclic Graph (DAG) given its nodes, edges, and root nodes.

### Conceptual Info

The validate_dag_structure shim function checks if a given DAG structure, represented by its nodes, edges, and root nodes, is valid. A valid DAG should not contain cycles and should have at least one root node.

### Docstring

**Summary:** Validates the structure of a Directed Acyclic Graph (DAG) given its nodes, edges, and root nodes.

**Parameters:**

- nodes (str): A string of comma-separated node names in the DAG
- edges (str): A string of comma-separated edges in the DAG, represented as 'node1->node2'
- roots (str): A string of comma-separated root node names in the DAG
**Returns:** bool - True if the DAG structure is valid, False otherwise

**Raises:**

- ValueError: When input validation fails
- TypeError: When input types are incorrect
**Examples:**

```python
>>> validate_dag_structure(nodes='A,B,C', edges='A->B,B->C', roots='A')
True
```

```python
>>> validate_dag_structure(nodes='A,B,C', edges='A->B,B->C,A->C', roots='A')
False
```

