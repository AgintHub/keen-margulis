# _refine_dag - Complete PRD Documentation

## Overview
PRDs for nodes in the '_refine_dag' module.

## Table of Contents

- [validate_dag_input](#validate_dag_input)

- [build_adjacency_graph](#build_adjacency_graph)

- [verify_dag_acyclicity](#verify_dag_acyclicity)

- [compute_topological_levels](#compute_topological_levels)

- [calculate_concurrency_stats](#calculate_concurrency_stats)

- [reorder_edges_by_topology](#reorder_edges_by_topology)



---

## validate_dag_input

### Description
Validates that the provided DAG node and edge lists represent a well‑formed DAG with no cycles or invalid references.

### Conceptual Info

The shim ensures that DAG inputs supplied to higher‑level orchestration functions are syntactically and semantically correct before any graph operations are performed.

### Docstring

**Summary:** Validate DAG node and edge specifications and return a success message or raise errors.

**Parameters:**

- dag_nodes (str): JSON string representing a list of unique task identifiers, e.g. '["A", "B", "C"]'.
- dag_edges (str): JSON string representing a list of directed edges in the form 'source->target', e.g. '["A->B", "B->C"]'.
**Returns:** str - A string such as "Validation succeeded" confirming that the DAG input is valid.

**Raises:**

- ValueError: If the node list contains duplicates, if an edge references an unknown node, or if the graph contains a cycle.
- TypeError: If either dag_nodes or dag_edges is not a string or cannot be parsed as JSON.
**Examples:**

```python
>>> output = validate_dag_input(dag_nodes='["A", "B", "C"]', dag_edges='["A->B", "B->C"]')
"Validation succeeded"
```

```python
>>> try:
...     validate_dag_input(dag_nodes='["A", "B"]', dag_edges='["A->B", "B->A"]')
>>> except ValueError as e:
...     print(e)
"Cycle detected: A->B->A"
```



---

## build_adjacency_graph

### Description
Constructs an adjacency graph representation from a list of node identifiers and dependency edges.

### Conceptual Info

The build_adjacency_graph shim takes raw DAG information and transforms it into a graph structure that the rest of the system can consume for validation, topology analysis, and execution planning.

### Docstring

**Summary:** Builds an adjacency graph from a list of node identifiers and dependency edges.

**Parameters:**

- dag_nodes (str): Comma‑separated string of unique task identifiers.
- dag_edges (str): Comma‑separated string of directed edges in the format 'source->target'.
**Returns:** str - A string representation of a dictionary mapping each node id to a list of its downstream node ids.

**Raises:**

- ValueError: Raised when an edge references a node not present in dag_nodes or when the edge format is invalid.
- TypeError: Raised when dag_nodes or dag_edges are not of type str.
**Examples:**

```python
>>> dag_nodes = "A,B,C"
>>> dag_edges = "A->B,B->C"
>>> graph_str = build_adjacency_graph(dag_nodes, dag_edges)
>>> print(graph_str)
'{'A': ['B'], 'B': ['C'], 'C': []}'
```

```python
>>> dag_nodes = "X,Y"
>>> dag_edges = ""
>>> print(build_adjacency_graph(dag_nodes, dag_edges))
'{'X': [], 'Y': []}'
```



---

## verify_dag_acyclicity

### Description
Checks whether a directed graph defined by adjacency data and node list contains cycles, returning a boolean.

### Conceptual Info

This shim determines the acyclicity of a directed graph represented by an adjacency map and a list of nodes, a core prerequisite for DAG construction and validation in workflow orchestration.

### Docstring

**Summary:** Verify that a directed graph has no cycles and return a boolean result.

**Parameters:**

- adjacency_data (str): JSON string representing a dictionary that maps each node identifier to a list of its successor nodes.
- dag_nodes (str): JSON string representing a list of all node identifiers that comprise the graph.
**Returns:** bool - True if the graph contains no directed cycles; False otherwise.

**Raises:**

- ValueError: Raised when the JSON cannot be parsed or the graph data is inconsistent (e.g., missing nodes, self‑loops).
- TypeError: Raised when either adjacency_data or dag_nodes is not a string.
**Examples:**

```python
>>> adjacency = '{"A":["B"],"B":["C"],"C":[]}'
>>> nodes = '["A","B","C"]'
>>> print(verify_dag_acyclicity(adjacency, nodes))
True
```

```python
>>> adjacency = '{"A":["B"],"B":["A"]}'
>>> nodes = '["A","B"]'
>>> print(verify_dag_acyclicity(adjacency, nodes))
False
```



---

## compute_topological_levels

### Description
Computes the topological level of each node in a DAG, returning a mapping of node identifiers to integer levels for use in concurrency analysis and edge reordering.

### Conceptual Info

The shim determines the depth of each task in a directed acyclic graph, enabling downstream components to compute concurrency metrics and reorder edges according to the DAG topology.

### Docstring

**Summary:** Return a mapping of each node in the DAG to its topological level.

**Parameters:**

- adjacency_data (dict): A mapping where keys are node identifiers and values are lists of successor node identifiers representing directed edges.
- dag_nodes (list[str]): Ordered list of all node identifiers present in the DAG.
**Returns:** dict - A dictionary mapping each node identifier (str) to an integer topological level (0 for source nodes).

**Raises:**

- ValueError: If the DAG contains nodes referenced in adjacency_data that are not present in dag_nodes, or if dag_nodes is empty.
- TypeError: If adjacency_data is not a dict or dag_nodes is not a list of strings.
**Examples:**

```python
>>> adjacency = {"A": ["B"], "B": ["C"], "C": []}
>>> nodes = ["A", "B", "C"]
>>> print(compute_topological_levels(adjacency, nodes))
{"A": 0, "B": 1, "C": 2}
```

```python
>>> adjacency = {"X": ["Y", "Z"], "Y": ["W"], "Z": ["W"], "W": []}
>>> nodes = ["X", "Y", "Z", "W"]
>>> print(compute_topological_levels(adjacency, nodes))
{"X": 0, "Y": 1, "Z": 1, "W": 2}
```



---

## calculate_concurrency_stats

### Description
Calculates whether a directed acyclic graph has concurrent tasks and reports the maximum concurrency level based on its topological level structure.

### Conceptual Info

This shim computes concurrency metrics for a DAG, determining if concurrent execution is possible and the maximum number of tasks that can run simultaneously, based on the provided topological level mapping.

### Docstring

**Summary:** Determine concurrency availability and maximum concurrency from a DAG's topological level structure.

**Parameters:**

- level_structure (str): JSON string representing a dictionary mapping each node identifier to its topological level (an integer).
**Returns:** str - A JSON string containing two keys: 'is_concurrent' (bool) indicating if any level contains more than one node, and 'max_concurrency' (int) representing the highest node count observed across all levels.

**Raises:**

- ValueError: Raised if the JSON cannot be parsed or required structure is missing.
- TypeError: Raised if the input is not a string.
**Examples:**

```python
>>> level_structure = '{"A":0, "B":0, "C":1, "D":1}'
>>> print(calculate_concurrency_stats(level_structure))
"{\"is_concurrent\": true, \"max_concurrency\": 2}"
```

```python
>>> level_structure = '{"X":0, "Y":0, "Z":0}'
>>> print(calculate_concurrency_stats(level_structure))
"{\"is_concurrent\": true, \"max_concurrency\": 3}"
```



---

## reorder_edges_by_topology

### Description
Reorders a list of DAG edges according to their topological levels, returning the edges sorted by source task level.

### Conceptual Info

This shim reorders raw DAG edges so that execution can be staged level‑by‑level, supporting concurrency analysis downstream.

### Docstring

**Summary:** Reorders edges by topological source levels.

**Parameters:**

- dag_edges (str): A comma‑separated string of edges formatted as 'source->target'.
- level_structure (str): A JSON string mapping each node to its topological level (int).
**Returns:** List[str] - Edges sorted in ascending order of the source node's level.

**Raises:**

- ValueError: If the input strings cannot be parsed or an edge references an undefined node.
- TypeError: If either argument is not a string.
**Examples:**

```python
>>> edges = 'A->B,B->C,D->E'
>>> levels = '{"A":0,"B":1,"C":2,"D":0,"E":1}'
>>> result = reorder_edges_by_topology(dag_edges=edges, level_structure=levels)
>>> print(result)
['A->B', 'D->E', 'B->C']
```

```python
>>> edges = 'X->Y,Y->Z,Z->W'
>>> levels = '{"X":0,"Y":1,"Z":2,"W":3}'
>>> print(reorder_edges_by_topology(dag_edges=edges, level_structure=levels))
['X->Y', 'Y->Z', 'Z->W']
```

