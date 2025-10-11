# _finalize_workflow - Complete PRD Documentation

## Overview
PRDs for nodes in the '_finalize_workflow' module.

## Table of Contents

- [parse_cycles_from_string](#parse_cycles_from_string)

- [parse_missing_dependencies_from_string](#parse_missing_dependencies_from_string)

- [remove_cycles_from_dag](#remove_cycles_from_dag)

- [generate_cycle_removal_warnings](#generate_cycle_removal_warnings)

- [resolve_missing_dependencies](#resolve_missing_dependencies)

- [generate_dependency_warnings](#generate_dependency_warnings)

- [topological_sort_tasks](#topological_sort_tasks)

- [generate_dag_representation](#generate_dag_representation)

- [check_final_dag_validity](#check_final_dag_validity)

- [generate_summary](#generate_summary)

- [serialize_task_list](#serialize_task_list)

- [serialize_dependencies_list](#serialize_dependencies_list)

- [serialize_cycles_list](#serialize_cycles_list)

- [serialize_warnings_list](#serialize_warnings_list)



---

## parse_cycles_from_string

### Description
Parse a string representation of cycles into a list of cycle identifiers or descriptions.

### Conceptual Info

This shim converts the `cycles_detected` string from `ValidateDagOutput` into a list of cycle identifiers or descriptions so that downstream nodes can perform cycle removal and generate warnings.

### Docstring

**Summary:** Parse a string of cycle identifiers or descriptions into a list of individual cycles.

**Parameters:**

- cycles_str (str): The string representation of cycles. It may contain comma‑separated cycle names, newline‑separated names, or be an empty string if no cycles are present.
**Returns:** list[str] - A list of cycle identifiers or descriptions extracted from the input string. The list is empty if the input is an empty string.

**Raises:**

- ValueError: Raised when the input string contains malformed entries that cannot be parsed into distinct cycle identifiers.
- TypeError: Raised if the provided `cycles_str` is not of type `str`.
**Examples:**

```python
>>> cycles = parse_cycles_from_string('cycleA, cycleB, cycleC')
['cycleA', 'cycleB', 'cycleC']
```

```python
>>> cycles = parse_cycles_from_string('')
[]
```



---

## parse_missing_dependencies_from_string

### Description
Parses a comma‑separated string of missing dependency names and returns a list of cleaned dependency identifiers.

### Conceptual Info

This shim extracts and normalizes missing dependency identifiers from a comma‑separated string representation provided by the DAG validation step.

### Docstring

**Summary:** Parses a string of missing dependency names and returns them as a list of cleaned strings.

**Parameters:**

- deps_str (str): Comma‑separated string of missing dependency names, possibly with surrounding whitespace.
**Returns:** List[str] - A list of dependency names with whitespace trimmed; an empty list if the input is empty or contains only whitespace.

**Raises:**

- ValueError: If the input string contains invalid characters (e.g., non‑printable characters).
- TypeError: If deps_str is not of type str.
**Examples:**

```python
>>> parse_missing_dependencies_from_string('task_a, task_b, task_c')
['task_a', 'task_b', 'task_c']
```

```python
>>> parse_missing_dependencies_from_string('   ')
[]
```



---

## remove_cycles_from_dag

### Description
Removes specified cycles from the DAG and returns a status message indicating the number of cycles removed.

### Conceptual Info

The remove_cycles_from_dag shim is responsible for processing a list of cycle identifiers, eliminating those cycles from the underlying DAG structure, and returning a human‑readable message that reflects the operation performed. It serves as a bridge between the cycle detection phase and the subsequent DAG finalization steps.

### Docstring

**Summary:** Removes cycles from the DAG and returns a status message.

**Parameters:**

- cycles (list[str]): A list of string identifiers describing cycles to be removed from the DAG. Each string should represent a distinct cycle (e.g., "A->B->C->A").
**Returns:** str - A status message indicating how many cycles were removed (e.g., "Removed 3 cycle(s) from the DAG.").

**Raises:**

- ValueError: If the cycles list is empty or None.
- TypeError: If the cycles argument is not a list of strings.
**Examples:**

```python
>>> result = remove_cycles_from_dag(['A->B->C->A'])
>>> print(result)
"Removed 1 cycle(s) from the DAG."
```

```python
>>> result = remove_cycles_from_dag(['X->Y->Z->X', 'M->N->M'])
>>> print(result)
"Removed 2 cycle(s) from the DAG."
```



---

## generate_cycle_removal_warnings

### Description
Creates human‑readable warnings describing cycles that were removed from a directed acyclic graph.

### Conceptual Info

This shim translates a list of removed cycle identifiers into user‑friendly warning messages, ensuring downstream components are informed of the adjustments made to the workflow graph.

### Docstring

**Summary:** Generate human‑readable warnings for cycles removed from a DAG.

**Parameters:**

- cycles (str): A comma‑separated string where each element represents a cycle (e.g., "A->B->A, C->D->E->C").
**Returns:** str - A single string containing one warning per cycle, formatted as "Warning: removed cycle [cycle]".

**Raises:**

- ValueError: Raised when `cycles` is an empty string or contains only whitespace.
- TypeError: Raised when `cycles` is not a string.
**Examples:**

```python
>>> warnings = generate_cycle_removal_warnings('A->B->A, C->D->E->C')
>>> print(warnings)
"Warning: removed cycle A->B->A\nWarning: removed cycle C->D->E->C"
```

```python
>>> warnings = generate_cycle_removal_warnings('X->Y->Z->X')
>>> print(warnings)
"Warning: removed cycle X->Y->Z->X"
```



---

## resolve_missing_dependencies

### Description
Resolves missing dependencies in a workflow by updating the graph and returning a summary string.

### Conceptual Info

This shim is responsible for reconciling missing dependency references in a directed acyclic graph (DAG). When the validation step identifies tasks that refer to non‑existent nodes, this function attempts to add the missing nodes or adjust edges to satisfy those dependencies, then reports which dependencies were successfully handled.

### Docstring

**Summary:** Resolve missing dependencies in a DAG and return a summary string.

**Parameters:**

- missing_deps (str): A comma‑separated string of dependency identifiers that were found missing during DAG validation.
**Returns:** str - A summary string in the format 'Resolved dependencies: <dep1>, <dep2>, ...'. If no dependencies were resolved, returns an empty string.

**Raises:**

- ValueError: Raised when `missing_deps` is an empty string or contains only whitespace.
- TypeError: Raised when `missing_deps` is not a string.
**Examples:**

```python
>>> result = resolve_missing_dependencies('A,B,C')
'Resolved dependencies: A, B, C'
```

```python
>>> try:
...     resolve_missing_dependencies('')
>>> except ValueError as e:
...     print(e)
'missing_deps must be a non‑empty comma‑separated string'
```



---

## generate_dependency_warnings

### Description
Generates warning messages for each missing dependency supplied as a comma‑separated string.

### Conceptual Info

This shim transforms a comma‑separated list of missing dependency names into human‑readable warning messages that are later included in workflow validation reports.

### Docstring

**Summary:** Creates a newline‑separated string of warnings for each missing dependency provided as a comma‑separated string.

**Parameters:**

- missing_deps (str): A comma‑separated string of task identifiers that are missing dependencies.
**Returns:** str - A string containing a warning for each missing dependency, one per line.

**Raises:**

- ValueError: If missing_deps is an empty string or None.
- TypeError: If missing_deps is not of type str.
**Examples:**

```python
>>> generate_dependency_warnings('task1,task2')
Warning: task1 has missing dependencies.\nWarning: task2 has missing dependencies.
```

```python
>>> generate_dependency_warnings('taskA')
Warning: taskA has missing dependencies.
```



---

## topological_sort_tasks

### Description
Computes an ordered list of task identifiers for a DAG given node and edge counts.

### Conceptual Info

The topological_sort_tasks shim is responsible for translating raw DAG metrics (node and edge counts) into a deterministic ordering of tasks, which later steps use for serialization, validation, and dependency resolution.

### Docstring

**Summary:** Generate a topological ordering of task identifiers based on node and edge counts.

**Parameters:**

- node_count (str): Total number of nodes in the DAG, expressed as a string that can be parsed into an integer.
- edge_count (str): Total number of directed edges in the DAG, expressed as a string that can be parsed into an integer.
**Returns:** str - A string representation of a list of task identifiers sorted in topological order. The list contains one identifier per node.

**Raises:**

- ValueError: Raised when node_count or edge_count is negative or represents an infeasible DAG configuration.
- TypeError: Raised when either node_count or edge_count is not convertible to an integer.
**Examples:**

```python
>>> topological_sort_tasks(node_count='3', edge_count='2')
['task1', 'task2', 'task3']
```

```python
>>> topological_sort_tasks(node_count='2', edge_count='1')
['taskA', 'taskB']
```



---

## generate_dag_representation

### Description
Creates a string representation of a directed acyclic graph from a serialized task order.

### Conceptual Info

The shim turns a serialized list of task identifiers into a textual DAG representation that can be used by downstream nodes such as `finalize_workflow`. It is responsible for interpreting the task order string, validating its format, and producing a concise, machine‑readable description of the graph structure.

### Docstring

**Summary:** Generate a string representation of a DAG from a comma‑separated task order.

**Parameters:**

- task_order (str): Comma‑separated list of task identifiers representing a topological ordering of the DAG.
**Returns:** str - A string describing the DAG, formatted as an adjacency list where each task points to its successors. Example: ``"A->B, B->C, C->"``.

**Raises:**

- ValueError: If `task_order` is an empty string or contains malformed entries (e.g., consecutive commas or trailing commas).
- TypeError: If `task_order` is not of type `str`.
**Examples:**

```python
>>> generate_dag_representation('A,B,C')
"A->B, B->C, C->"
```

```python
>>> generate_dag_representation('X')
"X->"
```



---

## check_final_dag_validity

### Description
Determines the final validity of a DAG based on its original validity and whether adjustments were made.

### Conceptual Info

This shim evaluates whether a Directed Acyclic Graph (DAG) remains valid after optional corrective operations. It accepts the original validation status and a flag indicating if any adjustments were applied, returning a single boolean that indicates the overall validity.

### Docstring

**Summary:** Return the final validity of a DAG based on its original validity and whether adjustments were made.

**Parameters:**

- is_originally_valid (bool): Indicates if the DAG was valid before any adjustments were attempted.
- adjustments_made (bool): True if any corrective changes (e.g., cycle removal or missing dependency resolution) were applied to the DAG.
**Returns:** bool - True if the DAG is considered valid after adjustments; False otherwise.

**Raises:**

- ValueError: Raised when either input is not of boolean type.
- TypeError: Raised when inputs are of incorrect type (not bool).
**Examples:**

```python
>>> check_final_dag_validity(True, False)
True
```

```python
>>> check_final_dag_validity(False, True)
True
```

```python
>>> check_final_dag_validity(False, False)
False
```



---

## generate_summary

### Description
Generates a short textual summary of the workflow based on its validity, whether adjustments were made, and if cycles were removed.

### Conceptual Info

The shim encapsulates the logic for creating a concise human‑readable description of the finalized workflow’s state. It takes three boolean flags indicating whether the workflow is valid, whether any adjustments were performed during finalization, and whether cycles were removed, and produces a single string that summarizes these conditions in natural language.

### Docstring

**Summary:** Create a summary string for a finalized workflow.

**Parameters:**

- is_valid (bool): True if the finalized workflow is valid (acyclic and all dependencies resolved).
- adjustments_made (bool): True if any adjustments (e.g., cycle removal or dependency resolution) were applied during finalization.
- cycles_removed (bool): True if one or more cycles were detected and removed from the original DAG.
**Returns:** str - A human‑readable summary stating the workflow’s validity, whether adjustments were made, and if cycles were removed.

**Raises:**

- TypeError: Raised when any of the arguments is not a bool.
- ValueError: Raised if any boolean argument is None.
**Examples:**

```python
>>> generate_summary(is_valid=True, adjustments_made=False, cycles_removed=False)
"The workflow is valid. No adjustments were made."
```

```python
>>> generate_summary(is_valid=False, adjustments_made=True, cycles_removed=True)
"The workflow is invalid. Adjustments were made: cycles removed."
```



---

## serialize_task_list

### Description
Serializes a list of task identifiers into a single comma-separated string.

### Conceptual Info

This shim turns a list of task names into a compact string that can be stored or transmitted, maintaining the order of the tasks.

### Docstring

**Summary:** Converts a list of task identifiers into a single comma-separated string.

**Parameters:**

- tasks (List[str]): A list of task identifiers to serialize.
**Returns:** str - A string containing the task identifiers joined by commas, preserving the input order.

**Raises:**

- TypeError: If the input is not a list.
- ValueError: If any element in the list is not a string.
**Examples:**

```python
>>> output = serialize_task_list(['step1', 'step2', 'step3'])
'step1,step2,step3'
```

```python
>>> output = serialize_task_list(['taskC', 'taskA', 'taskB'])
'taskC,taskA,taskB'
```



---

## serialize_dependencies_list

### Description
Serializes a list of dependency names into a single comma‑separated string for workflow output.

### Conceptual Info

The shim converts a list of task dependencies into a human‑readable string that can be embedded in the FinalizeWorkflowOutput model. It is used after parsing missing dependencies or cycles to produce a concise representation for logs, warnings, or display.

### Docstring

**Summary:** Return a comma‑separated string representation of the input dependency list.

**Parameters:**

- deps (List[str]): A list of dependency names to be serialized.
**Returns:** str - A single string containing all dependency names joined by commas. If the list is empty, an empty string is returned.

**Raises:**

- TypeError: If the `deps` argument is not a list.
- ValueError: If any element in `deps` is not a string.
**Examples:**

```python
>>> serialize_dependencies_list(['task_a', 'task_b', 'task_c'])
'task_a, task_b, task_c'
```

```python
>>> serialize_dependencies_list([])
''
```



---

## serialize_cycles_list

### Description
Serializes a list of cycle identifiers into a comma-separated string.

### Conceptual Info

This shim takes a list of cycle identifiers discovered during DAG validation and produces a single string representation suitable for storage or display in downstream nodes.

### Docstring

**Summary:** Serializes a list of cycle identifiers into a comma-separated string.

**Parameters:**

- cycles (List[str]): A list of cycle identifiers to serialize.
**Returns:** str - A comma-separated string representation of the cycles.

**Raises:**

- ValueError: Raised when the list contains non-string elements or is empty.
- TypeError: Raised when the input is not a list.
**Examples:**

```python
>>> serialize_cycles_list(['cycle1', 'cycle2', 'cycle3'])
'cycle1, cycle2, cycle3'
```

```python
>>> serialize_cycles_list('not a list')
Traceback (most recent call last):\n  File "<stdin>", line 1, in <module>\nTypeError: cycles must be a list of strings.
```



---

## serialize_warnings_list

### Description
Converts a list of warning messages into a single string, with each warning separated by a newline.

### Conceptual Info

This shim serializes a collection of warning strings so that they can be embedded in workflow summaries or logs.

### Docstring

**Summary:** Serialize a list of warning messages into a single newline‑separated string.

**Parameters:**

- warnings (List[str]): List of warning messages to be serialized.
**Returns:** str - A string containing all warning messages separated by newlines. If the input list is empty, an empty string is returned.

**Raises:**

- TypeError: If the input is not a list or if any element is not a string.
- ValueError: If any warning message is an empty string.
**Examples:**

```python
>>> warnings = ['Low disk space', 'Deprecated API used']
>>> result = serialize_warnings_list(warnings)
>>> print(result)
"Low disk space\nDeprecated API used"
```

```python
>>> warnings = ['All good']
>>> result = serialize_warnings_list(warnings)
>>> print(result)
"All good"
```

