# _finalize_workflow - Complete PRD Documentation

## Overview
PRDs for nodes in the '_finalize_workflow' module.

## Table of Contents

- [validate_dag_edges](#validate_dag_edges)

- [extract_nodes_from_edges](#extract_nodes_from_edges)

- [check_dag_completeness](#check_dag_completeness)

- [determine_adjustments](#determine_adjustments)

- [generate_dag_summary](#generate_dag_summary)

- [log_finalization_results](#log_finalization_results)



---

## validate_dag_edges

### Description
Validates a list of directed edges for syntax, uniqueness, and acyclicity, returning a cleaned list of edges.

### Conceptual Info

The validate_dag_edges shim ensures that the edges supplied to the workflow refinement process conform to the expected syntax and represent an acyclic graph, providing a safe set of edges for subsequent processing.

### Docstring

**Summary:** Validate a list of directed edges, ensuring each edge is formatted correctly, unique, and that the resulting graph is acyclic. Returns a cleaned list of edges or raises an error if validation fails.

**Parameters:**

- edges (list[str]): A list of edge strings formatted as 'NodeA->NodeB'.
- logger (logging.Logger): Logger instance used for debug and error logging.
**Returns:** List[str] - A list of validated edge strings, deduplicated and in the same order as the first appearance.

**Raises:**

- ValueError: Raised when an edge is malformed, refers to an undefined node, or if the edge set introduces a cycle.
- TypeError: Raised when the `edges` argument is not a list of strings or the `logger` is not a logging.Logger instance.
**Examples:**

```python
>>> edges = ['Task1->Task2', 'Task2->Task3']
>>> validated = validate_dag_edges(edges, logger)
>>> print(validated)
['Task1->Task2', 'Task2->Task3']
```

```python
>>> edges = ['Task1->Task2', 'Task2->Task1']
>>> validate_dag_edges(edges, logger)
ValueError: Cyclic dependency detected in edges.
```



---

## extract_nodes_from_edges

### Description
Extracts a set of unique node names from a comma‑separated string of directed DAG edges in the format 'NodeA->NodeB'.

### Conceptual Info

This shim is responsible for parsing DAG edge definitions and identifying all participating nodes to support downstream DAG validation and optimization.

### Docstring

**Summary:** Extracts node names from a string of DAG edges.

**Parameters:**

- edges (str): A comma‑separated string of directed edges formatted as 'NodeA->NodeB'.
**Returns:** set - A set of unique node names found in the input edges.

**Raises:**

- ValueError: If any edge does not contain the '->' separator or the input string is empty but not None.
- TypeError: If the input `edges` is not a string.
**Examples:**

```python
>>> edges = 'TaskA->TaskB,TaskB->TaskC,TaskC->TaskD'
>>> nodes = extract_nodes_from_edges(edges)
>>> print(nodes)
{'TaskA', 'TaskB', 'TaskC', 'TaskD'}
```

```python
>>> edges = ''
>>> nodes = extract_nodes_from_edges(edges)
>>> print(nodes)
{}
```



---

## check_dag_completeness

### Description
Determines whether a directed graph with the given number of nodes and edges is complete (contains the maximum possible edges).

### Conceptual Info

This shim verifies that the DAG is fully defined by ensuring the number of edges equals the maximum possible for a directed graph of the specified node count, indicating that every potential task relationship has been specified.

### Docstring

**Summary:** Check if a directed graph is complete based on node and edge counts.

**Parameters:**

- node_count (int): The number of unique nodes in the DAG.
- edge_count (int): The number of directed edges present in the DAG.
**Returns:** bool - True when edge_count equals node_count * (node_count - 1) (i.e., the graph is complete), otherwise False.

**Raises:**

- ValueError: Raised if edge_count is negative or greater than the maximum possible for the given node_count.
- TypeError: Raised if node_count or edge_count are not integers.
**Examples:**

```python
>>> check_dag_completeness(3, 6)
True
```

```python
>>> check_dag_completeness(4, 10)
False
```

```python
>>> check_dag_completeness(-1, 5)
ValueError: edge_count cannot be negative
```



---

## determine_adjustments

### Description
Determines which nodes need adjustment based on concurrency and acyclicity flags.

### Conceptual Info

This shim is responsible for deciding which workflow nodes must be modified when the DAG is either intended to run concurrently or must remain acyclic. The function receives the concurrency and acyclicity flags, validates them, and returns a list of node identifiers that require adjustment.

### Docstring

**Summary:** Return a list of node names that require adjustment based on the `is_concurrent` and `is_acyclic` flags.

**Parameters:**

- is_concurrent (str): Flag indicating whether the DAG should allow concurrent execution. Expected values: 'True' or 'False'.
- is_acyclic (str): Flag indicating whether the DAG is acyclic. Expected values: 'True' or 'False'.
**Returns:** LIST_STR - A list of node names (strings) that need to be adjusted. If no adjustments are necessary, an empty list is returned.

**Raises:**

- ValueError: Raised when either `is_concurrent` or `is_acyclic` is not one of the accepted string values ('True', 'False').
- TypeError: Raised when either `is_concurrent` or `is_acyclic` is not a string.
**Examples:**

```python
>>> determine_adjustments("True", "True")
[]
```

```python
>>> determine_adjustments("False", "True")
["Task1", "Task2"]
```



---

## generate_dag_summary

### Description
Creates a concise, human‑readable summary of a directed acyclic graph based on node and edge counts, acyclicity, and concurrency status.

### Conceptual Info

This shim generates a natural‑language description of a DAG’s structure and properties, allowing downstream components to report or log the DAG state without needing to parse raw metrics.

### Docstring

**Summary:** Generate a concise, human‑readable summary of a directed acyclic graph based on its node count, edge count, acyclicity, and concurrency status.

**Parameters:**

- node_count (int): Total number of nodes in the DAG.
- edge_count (int): Total number of directed edges in the DAG.
- is_acyclic (bool): True if the DAG contains no cycles; False otherwise.
- is_concurrent (bool): True if the DAG is configured to allow concurrent execution of independent tasks; False otherwise.
**Returns:** str - A string summarizing the DAG, e.g., "The DAG contains 5 nodes and 4 directed edges, is acyclic, and does not support concurrent execution."

**Raises:**

- ValueError: Raised when node_count or edge_count is negative or not an integer.
- TypeError: Raised when any input parameter is of an incorrect type.
**Examples:**

```python
>>> summary = generate_dag_summary(node_count=5, edge_count=4, is_acyclic=True, is_concurrent=False)
"The DAG contains 5 nodes and 4 directed edges, is acyclic, and does not support concurrent execution."
```

```python
>>> summary = generate_dag_summary(node_count=10, edge_count=9, is_acyclic=True, is_concurrent=True)
"The DAG contains 10 nodes and 9 directed edges, is acyclic, and supports concurrent execution."
```



---

## log_finalization_results

### Description
Logs the finalization summary and adjustments of a workflow DAG and returns a concise message.

### Conceptual Info

This shim abstracts the logging of workflow DAG finalization details, allowing downstream components to capture and record the outcome without depending on a concrete logging implementation.

### Docstring

**Summary:** Logs the finalization summary and list of adjustments for a workflow DAG and returns a formatted string containing both.

**Parameters:**

- logger (str): Name of the logger to use for outputting the finalization results.
- summary (str): Human‑readable summary of the finalized DAG.
- adjustments (List[str]): List of node names that were adjusted during finalization.
**Returns:** str - A single string in the form "Log summary: {summary}. Adjustments made: {adjustments}" where adjustments are comma‑separated.

**Raises:**

- ValueError: If `summary` is an empty string or `adjustments` contains non‑string elements.
- TypeError: If any argument is of an incorrect type.
**Examples:**

```python
>>> result = log_finalization_results(logger='root', summary='All tasks completed.', adjustments=['NodeA', 'NodeB'])
>>> print(result)
"Log summary: All tasks completed. Adjustments made: NodeA, NodeB"
```

```python
>>> result = log_finalization_results(logger='workflow', summary='DAG is acyclic.', adjustments=[])
>>> print(result)
"Log summary: DAG is acyclic. Adjustments made: "
```

