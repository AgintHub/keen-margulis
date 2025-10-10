# _validateworkflow - Complete PRD Documentation

## Overview
PRDs for nodes in the '_validateworkflow' module.

## Table of Contents

- [validate_input_type_and_empty](#validate_input_type_and_empty)

- [validate_node_names_are_strings](#validate_node_names_are_strings)

- [analyze_node_dependencies](#analyze_node_dependencies)

- [check_for_circular_dependencies](#check_for_circular_dependencies)

- [validate_node_connectivity](#validate_node_connectivity)

- [validate_node_schemas](#validate_node_schemas)

- [validate_execution_path](#validate_execution_path)

- [generate_validation_error_message](#generate_validation_error_message)



---

## validate_input_type_and_empty

### Description
Validates that the input is a non-empty list of strings.

### Conceptual Info

This shim node validates the input connected_nodes to ensure it is a non-empty list of strings, which is crucial for subsequent workflow validation steps.

### Docstring

**Summary:** Validates that the input connected_nodes is a non-empty list of strings.

**Parameters:**

- connected_nodes (List[str]): List of connected node names to be validated.
**Returns:** str - Output indicating the validation result or an error message.

**Raises:**

- ValueError: If the input list is empty.
- TypeError: If the input is not a list or if any element in the list is not a string.
**Examples:**

```python
>>> validate_input_type_and_empty(connected_nodes=['node1', 'node2'])
'Validation successful'
```

```python
>>> validate_input_type_and_empty(connected_nodes=[])
ValueError: Input list is empty
```

```python
>>> validate_input_type_and_empty(connected_nodes=['node1', 2])
TypeError: All elements in the list must be strings
```



---

## validate_node_names_are_strings

### Description
Validates that the provided connected node names are strings.

### Conceptual Info

This shim function is responsible for validating that all connected node names provided to it are indeed strings. It plays a crucial role in ensuring data consistency and preventing potential errors downstream in the workflow validation process.

### Docstring

**Summary:** Validates that all connected node names are strings.

**Parameters:**

- connected_nodes (List[str]): A list of node names to be validated as strings.
**Returns:** str - A message indicating whether the validation was successful or not.

**Raises:**

- TypeError: If any of the node names in the list are not strings.
**Examples:**

```python
>>> validate_node_names_are_strings(connected_nodes=['node1', 'node2'])
'Validation successful'
```

```python
>>> validate_node_names_are_strings(connected_nodes=['node1', 2])
TypeError: All node names must be strings.
```



---

## analyze_node_dependencies

### Description
Analyzes node dependencies from a list of connected node names and returns a dictionary representing the dependency graph.

### Conceptual Info

This shim analyzes the dependencies between nodes in a workflow represented by a list of connected node names. It returns a dictionary that maps each node to its dependencies, which is crucial for validating the workflow's structure and detecting potential issues like circular dependencies.

### Docstring

**Summary:** Analyzes node dependencies from a list of connected node names and returns a dictionary representing the dependency graph.

**Parameters:**

- connected_nodes (str): A JSON string representing a list of connected node names.
**Returns:** str - A JSON string representing a dictionary where keys are node names and values are lists of their dependencies.

**Raises:**

- ValueError: If the input is not a valid JSON string or if the parsed list contains non-string node names.
- TypeError: If the input is not a string.
**Examples:**

```python
>>> import json
>>> connected_nodes = json.dumps(['node1', 'node2', 'node3'])
>>> result = analyze_node_dependencies(connected_nodes=connected_nodes)
>>> print(result)
"{'node1': ['node2'], 'node2': ['node3'], 'node3': []}"
```

```python
>>> import json
>>> connected_nodes = json.dumps(['A', 'B', 'C'])
>>> result = analyze_node_dependencies(connected_nodes=connected_nodes)
>>> print(result)
"{'A': ['B'], 'B': ['C'], 'C': []}"
```



---

## check_for_circular_dependencies

### Description
Checks if there are circular dependencies in the given node dependencies.

### Conceptual Info

This shim function analyzes the given node dependencies to detect any circular references, which could indicate potential issues in workflow execution.

### Docstring

**Summary:** Checks for circular dependencies in the provided node dependency structure.

**Parameters:**

- dependencies (str): A string representation of the node dependencies, expected to be parseable into a dependency graph.
**Returns:** bool - Returns True if the dependency graph is free of circular dependencies, False otherwise.

**Raises:**

- ValueError: If the input dependencies string is malformed or cannot be parsed into a valid dependency graph.
- TypeError: If the input type is not a string.
**Examples:**

```python
>>> check_for_circular_dependencies(dependencies='A->B, B->C, C->A')
>>> check_for_circular_dependencies(dependencies='A->B, B->C, C->D')
False
```

```python
>>> check_for_circular_dependencies(dependencies='A->B, B->A')
False
```

```python
>>> check_for_circular_dependencies(dependencies='A->B, B->C')
True
```



---

## validate_node_connectivity

### Description
Validates the connectivity of nodes in a workflow based on their connections.

### Conceptual Info

This shim function is responsible for validating the connectivity between nodes in a workflow. It takes a string representation of connected nodes as input and returns a boolean indicating whether the connectivity is valid.

### Docstring

**Summary:** Validates node connectivity in a workflow based on the provided connected nodes.

**Parameters:**

- connected_nodes (str): A string representing the connected nodes in the workflow.
**Returns:** bool - A boolean value indicating whether the node connectivity is valid.

**Raises:**

- ValueError: If the input string is not properly formatted or contains invalid node connections.
- TypeError: If the input is not a string.
**Examples:**

```python
>>> validate_node_connectivity(connected_nodes='node1,node2,node3')
True
```

```python
>>> validate_node_connectivity(connected_nodes='invalid_node')
False
```



---

## validate_node_schemas

### Description
Validate the schemas of nodes in a workflow based on their connectivity.

### Conceptual Info

This shim node is responsible for validating the schemas of nodes within a workflow. It takes the names of connected nodes as input and returns a boolean indicating whether their schemas are valid.

### Docstring

**Summary:** Validate the schemas of nodes based on their connectivity.

**Parameters:**

- connected_nodes (str): A string representing the names of connected nodes in the workflow.
**Returns:** bool - A boolean value indicating whether the schemas of the connected nodes are valid.

**Raises:**

- ValueError: If the input 'connected_nodes' is not a valid string or is empty.
- TypeError: If the input 'connected_nodes' is not of type string.
**Examples:**

```python
>>> validate_node_schemas(connected_nodes='node1,node2,node3')
True
```

```python
>>> validate_node_schemas(connected_nodes='invalid_node')
False
```



---

## validate_execution_path

### Description
Validates the execution path of connected nodes in a workflow.

### Conceptual Info

This shim function validates the execution path of a given set of connected nodes in a workflow, ensuring that the sequence of nodes can be executed without any logical or structural issues.

### Docstring

**Summary:** Validates the execution path of connected nodes.

**Parameters:**

- connected_nodes (List[str]): A list of connected node names to validate.
**Returns:** bool - True if the execution path is valid, False otherwise.

**Raises:**

- ValueError: If the input list is empty or contains invalid node names.
- TypeError: If the input is not a list of strings.
**Examples:**

```python
>>> validate_execution_path(connected_nodes=['node1', 'node2', 'node3'])
True
```

```python
>>> validate_execution_path(connected_nodes=['node1', 'invalid_node', 'node3'])
False
```



---

## generate_validation_error_message

### Description
This shim generates a detailed error message based on the validation results of node connectivity, schema validity, and execution path validity.

### Conceptual Info

This shim plays a crucial role in providing informative error messages during the validation of workflows, helping users identify and rectify issues related to node connectivity, schema validity, and execution path validity.

### Docstring

**Summary:** Generates a validation error message based on the given validation results.

**Parameters:**

- connectivity_valid (str): A boolean string indicating whether the node connectivity is valid ('True' or 'False').
- schema_valid (str): A boolean string indicating whether the node schema is valid ('True' or 'False').
- execution_path_valid (str): A boolean string indicating whether the execution path is valid ('True' or 'False').
**Returns:** str - A detailed error message indicating which validation checks failed.

**Raises:**

- ValueError: If any of the input boolean strings are not 'True' or 'False'.
**Examples:**

```python
>>> generate_validation_error_message(connectivity_valid='False', schema_valid='True', execution_path_valid='False')
'Validation failed due to invalid connectivity and execution path.'
```

```python
>>> generate_validation_error_message(connectivity_valid='True', schema_valid='False', execution_path_valid='True')
'Validation failed due to invalid schema.'
```

