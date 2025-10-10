# _create_task_dag - Complete PRD Documentation

## Overview
PRDs for nodes in the '_create_task_dag' module.

## Table of Contents

- [parse_dependency_strings](#parse_dependency_strings)

- [validate_task_references](#validate_task_references)

- [extract_edge_sources](#extract_edge_sources)

- [extract_edge_destinations](#extract_edge_destinations)

- [check_dag_acyclicity](#check_dag_acyclicity)

- [format_task_list](#format_task_list)

- [format_edge_list](#format_edge_list)



---

## parse_dependency_strings

### Description
Parses a string of dependency relationships into a list of task source‑destination pairs.

### Conceptual Info

The shim extracts structured dependency pairs from a plain text description, enabling downstream DAG construction and validation.

### Docstring

**Summary:** Parse a multiline string of dependency relationships and return them as a list of tuples.

**Parameters:**

- dependencies (str): A string containing dependency descriptions, one per line. Each line must follow the format "SourceTask depends on TargetTask" or "SourceTask,TargetTask".
**Returns:** List[Tuple[str, str]] - A list of tuples where each tuple contains the source task name and the target task name.

**Raises:**

- ValueError: Raised if a line in the input string does not conform to an expected dependency format.
- TypeError: Raised if the input `dependencies` is not of type `str`.
**Examples:**

```python
>>> parse_dependency_strings('TaskA depends on TaskB\nTaskB depends on TaskC')
[('TaskA', 'TaskB'), ('TaskB', 'TaskC')]
```

```python
>>> parse_dependency_strings('Task1,Task2\nTask3,Task4')
[('Task1', 'Task2'), ('Task3', 'Task4')]
```



---

## validate_task_references

### Description
Checks that every task referenced in the parsed dependencies exists in the provided task list and reports any missing references.

### Conceptual Info

Validates that all tasks referenced in dependency tuples are defined in the task list, preventing dangling references before DAG construction.

### Docstring

**Summary:** Validate that every task in `parsed_dependencies` exists in `tasks`. If any reference is missing, a `ValueError` is raised.

**Parameters:**

- tasks (List[str]): A list of all task identifiers that are considered valid.
- parsed_dependencies (List[Tuple[str, str]]): A list of dependency tuples in the form (source_task, target_task).
**Returns:** str - A message stating that all references are valid, or a list of missing task identifiers.

**Raises:**

- ValueError: If any task in a dependency tuple is not present in `tasks`.
- TypeError: If the input arguments are not of the expected types (`list` of `str` and `list` of `tuple`).
**Examples:**

```python
>>> validate_task_references(
    tasks=['TaskA', 'TaskB', 'TaskC'],
    parsed_dependencies=[('TaskA', 'TaskB'), ('TaskB', 'TaskC')]
)
'All task references are valid.'
```

```python
>>> try:
...     validate_task_references(
    	tasks=['TaskA', 'TaskB'],
    	parsed_dependencies=[('TaskA', 'TaskC')]
    )
>>> except ValueError as e:
...     print(e)
"Missing task reference(s) found: TaskC"
```



---

## extract_edge_sources

### Description
Extracts a list of source task identifiers from a string representation of parsed dependency pairs.

### Conceptual Info

The shim isolates the logic for extracting source task names from a dependency string, enabling reuse in DAG construction and simplifying unit tests.

### Docstring

**Summary:** Parse a string of dependency tuples and return the list of source task identifiers.

**Parameters:**

- parsed_dependencies (str): A string containing comma‑separated tuples in the form "('TaskA', 'TaskB'), ('TaskC', 'TaskD')" or a similar format where each tuple represents a dependency "source" → "destination".
**Returns:** List[str] - A list of the source task identifiers extracted from each dependency tuple.

**Raises:**

- TypeError: If `parsed_dependencies` is not a string.
- ValueError: If the input string cannot be parsed into a sequence of valid two‑element tuples or if any tuple is malformed.
**Examples:**

```python
>>> output = extract_edge_sources("('TaskA', 'TaskB'), ('TaskC', 'TaskD')")
['TaskA', 'TaskC']
```

```python
>>> output = extract_edge_sources("('Deploy', 'Test'), ('Build', 'Deploy')")
['Deploy', 'Build']
```



---

## extract_edge_destinations

### Description
Extracts the destination task identifiers from a string representation of parsed dependency tuples.

### Conceptual Info

This shim serves as the bridge between parsed dependency data and the DAG construction logic by isolating the extraction of destination nodes from dependency tuples.

### Docstring

**Summary:** Extracts destination task identifiers from a string representation of parsed dependency tuples.

**Parameters:**

- parsed_dependencies (str): String representation of parsed dependency tuples, each tuple containing a source and destination task identifier.
**Returns:** LIST_STR - A list of destination task identifiers (e.g., ['TaskB', 'TaskC']) extracted from the parsed dependencies.

**Raises:**

- ValueError: Raised when the input string cannot be parsed into a list of tuple pairs.
- TypeError: Raised when the input is not a string.
**Examples:**

```python
>>> deps = "[(\'TaskA\', \'TaskB\'), (\'TaskB\', \'TaskC\')]"
>>> print(extract_edge_destinations(deps))
['TaskB', 'TaskC']
```

```python
>>> deps = "[]"
>>> print(extract_edge_destinations(deps))
[]
```



---

## check_dag_acyclicity

### Description
Checks whether a directed graph defined by tasks and edge lists contains any cycles, returning a boolean result.

### Conceptual Info

This shim determines the acyclicity of a task dependency DAG by examining the list of tasks and the corresponding source–destination edge pairs.

### Docstring

**Summary:** Determine if a directed graph, specified by tasks and edge lists, contains a cycle.

**Parameters:**

- tasks (List[str]): A list of unique task identifiers that form the nodes of the graph.
- edge_sources (List[str]): A list of source task identifiers for each directed edge in the graph.
- edge_destinations (List[str]): A list of destination task identifiers for each directed edge in the graph.
**Returns:** bool - Returns True if the graph contains no cycles (is acyclic); otherwise returns False.

**Raises:**

- TypeError: Raised when any of the arguments is not a list of strings.
- ValueError: Raised when the lengths of edge_sources and edge_destinations differ, or when a source/destination is not present in tasks.
**Examples:**

```python
>>> check_dag_acyclicity([
...     "A", "B", "C"
>>> ], [
...     "A", "B"
>>> ], [
...     "B", "C"
>>> ])
True
```

```python
>>> check_dag_acyclicity([
...     "A", "B", "C"
>>> ], [
...     "A", "B", "C"
>>> ], [
...     "B", "C", "A"
>>> ])
False
```



---

## format_task_list

### Description
Converts a list of task names into a formatted string representation.

### Conceptual Info

Provides a human-readable string representation of task identifiers for DAG construction and validation.

### Docstring

**Summary:** Formats a list of task names into a standardized string for downstream DAG processing.

**Parameters:**

- tasks (list): A list of task names to format.
**Returns:** str - A string containing the task names formatted as a list.

**Raises:**

- ValueError: Raised when the input list is empty or contains non-string elements.
- TypeError: Raised when the input is not a list or iterable.
**Examples:**

```python
>>> result = format_task_list(['TaskA', 'TaskB', 'TaskC'])
>>> print(result)
['TaskA', 'TaskB', 'TaskC']
```

```python
>>> format_task_list([])
ValueError: Input list cannot be empty.
```



---

## format_edge_list

### Description
Formats a list of edge identifiers into a comma-separated string representation.

### Conceptual Info

Converts a list of directed edge identifiers into a compact string for serialization or display, ensuring consistent formatting across the system.

### Docstring

**Summary:** Create a comma‑separated string from a list of edge identifiers.

**Parameters:**

- edges (List[str]): A list of edge identifiers to format.
**Returns:** str - A single string containing all edge identifiers separated by commas, with no additional whitespace or delimiters.

**Raises:**

- TypeError: Raised when `edges` is not a list.
- ValueError: Raised when any element in `edges` is not a string.
**Examples:**

```python
>>> format_edge_list(['taskA', 'taskB', 'taskC'])
'taskA,taskB,taskC'
```

```python
>>> format_edge_list([])
''
```

```python
>>> format_edge_list(['single'])
'single'
```

