# _validate_dag - Complete PRD Documentation

## Overview
PRDs for nodes in the '_validate_dag' module.

## Table of Contents

- [parse_dag_structure](#parse_dag_structure)

- [validate_dag_format](#validate_dag_format)

- [build_graph_from_edges](#build_graph_from_edges)

- [check_dag_acyclicity](#check_dag_acyclicity)

- [validate_dag_wellformedness](#validate_dag_wellformedness)



---

## parse_dag_structure

### Description
Parses the input DAG structure string into a format that can be used for further processing.

### Conceptual Info

This shim function is responsible for parsing the input DAG structure string into a usable format for further validation and processing in the workflow.

### Docstring

**Summary:** Parses the input DAG structure string into a suitable format for further processing.

**Parameters:**

- dag_structure (str): The input DAG structure as a string that needs to be parsed.
**Returns:** str - The parsed DAG structure in a format that can be used for further processing, such as validation and graph construction.

**Raises:**

- ValueError: If the input DAG structure string is malformed or cannot be parsed.
- TypeError: If the input is not a string.
**Examples:**

```python
>>> dag_structure = '{ "nodes": ["A", "B"], "edges": [["A", "B"]] }'
>>> parsed_dag = parse_dag_structure(dag_structure=dag_structure)
>>> print(parsed_dag)
'[("A", "B")]'
```

```python
>>> dag_structure = 'A -> B; B -> C'
>>> parsed_dag = parse_dag_structure(dag_structure=dag_structure)
>>> print(parsed_dag)
'[("A", "B"), ("B", "C")]'
```



---

## validate_dag_format

### Description
Validates the format of a DAG structure represented as a string of edges.

### Conceptual Info

This shim node is responsible for validating the format of a DAG (Directed Acyclic Graph) structure represented as a string of edges. It ensures that the input DAG structure conforms to expected formatting rules.

### Docstring

**Summary:** Validates the format of the input DAG structure represented by the given edges.

**Parameters:**

- parsed_edges (str): A string representing the edges of the DAG structure to be validated.
**Returns:** str - A message indicating whether the DAG format is valid or not.

**Raises:**

- ValueError: If the input DAG structure is not well-formed or does not conform to expected formatting rules.
- TypeError: If the input type is not a string.
**Examples:**

```python
>>> validate_dag_format(parsed_edges='A->B,B->C,C->D')
>>> validate_dag_format(parsed_edges='A->B,B->C,C->D,A->D')
'DAG format is valid'
```

```python
>>> validate_dag_format(parsed_edges='A->B,B->C,C->A')
'DAG format is invalid: cyclic detected'
```



---

## build_graph_from_edges

### Description
Constructs a graph representation from a given list of edges.

### Conceptual Info

This shim function is responsible for transforming a list of edges into a graph representation, which is crucial for further analysis such as checking for acyclicity and validating the well-formedness of the graph.

### Docstring

**Summary:** Builds a graph representation from a given list of edges.

**Parameters:**

- edges (str): A string representing the list of edges in the graph, where edges are typically represented as pairs of nodes.
**Returns:** str - A string representing the constructed graph.

**Raises:**

- ValueError: If the input edges string is malformed or cannot be parsed correctly.
- TypeError: If the input edges is not a string.
**Examples:**

```python
>>> edges = '[(1, 2), (2, 3), (3, 4)]'
>>> graph = build_graph_from_edges(edges=edges)
'Graph with nodes: [1, 2, 3, 4] and edges: [(1, 2), (2, 3), (3, 4)]'
```

```python
>>> edges = '[(A, B), (B, C)]'
>>> graph = build_graph_from_edges(edges=edges)
'Graph with nodes: [A, B, C] and edges: [(A, B), (B, C)]'
```



---

## check_dag_acyclicity

### Description
Checks if a given DAG represented as a graph is acyclic.

### Conceptual Info

This shim function checks if a Directed Acyclic Graph (DAG) represented as a graph is acyclic, playing a crucial role in validating workflow structures.

### Docstring

**Summary:** Checks if a given DAG is acyclic by analyzing its graph representation.

**Parameters:**

- graph (str): The input graph representation as a string that needs to be checked for acyclicity.
**Returns:** bool - True if the DAG is acyclic, False otherwise.

**Raises:**

- ValueError: If the input graph is not a valid representation of a DAG.
- TypeError: If the input graph is not of type string.
**Examples:**

```python
>>> graph_repr = 'A->B; B->C; C->D'
>>> is_acyclic = check_dag_acyclicity(graph=graph_repr)
True
```

```python
>>> graph_repr = 'A->B; B->C; C->A'
>>> is_acyclic = check_dag_acyclicity(graph=graph_repr)
False
```



---

## validate_dag_wellformedness

### Description
Checks if the provided DAG representation is valid and properly formed.

### Conceptual Info

This shim validates the well-formedness of a given DAG representation, ensuring it adheres to expected structural requirements.

### Docstring

**Summary:** Validates the well-formedness of a DAG representation.

**Parameters:**

- graph (str): The input graph representation as a string.
**Returns:** bool - True if the DAG is well-formed, False otherwise.

**Raises:**

- ValueError: If the input graph string is malformed or cannot be parsed.
- TypeError: If the input is not a string.
**Examples:**

```python
>>> graph_str = '{'nodes': ['A', 'B'], 'edges': [('A', 'B')]}'
>>> validate_dag_wellformedness(graph=graph_str)
True
```

```python
>>> graph_str = '{'nodes': ['A', 'B'], 'edges': [('A', 'C')]}'
>>> validate_dag_wellformedness(graph=graph_str)
False
```

