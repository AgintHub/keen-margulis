# _connectnodes - Complete PRD Documentation

## Overview
PRDs for nodes in the '_connectnodes' module.

## Table of Contents

- [validate_node_names](#validate_node_names)

- [check_cyclic_dependency](#check_cyclic_dependency)

- [establish_dag_connection](#establish_dag_connection)



---

## validate_node_names

### Description
Validates the names of two nodes to ensure they are properly formatted and valid for connection.

### Conceptual Info

This shim function is responsible for validating the names of two nodes before they are connected in a DAG.

### Docstring

**Summary:** Validates the names of two nodes to ensure they are valid for connection.

**Parameters:**

- node1_name (str): The name of the first node to be validated.
- node2_name (str): The name of the second node to be validated.
**Returns:** str - A string indicating the validation result of the node names.

**Raises:**

- ValueError: If either node name is empty or contains invalid characters.
- TypeError: If either node name is not a string.
**Examples:**

```python
>>> validate_node_names(node1_name='valid_node1', node2_name='valid_node2')
'Node names are valid'
```

```python
>>> validate_node_names(node1_name='', node2_name='valid_node2')
ValueError: 'Node name cannot be empty'
```



---

## check_cyclic_dependency

### Description
Checks if there's a cyclic dependency between two given nodes in a directed graph.

### Conceptual Info

This shim function is crucial for validating the structural integrity of a directed acyclic graph (DAG) when connecting nodes. It ensures that adding an edge between two nodes does not introduce a cycle, which is essential for maintaining the DAG property.

### Docstring

**Summary:** Checks if connecting two nodes creates a cyclic dependency in a DAG.

**Parameters:**

- node1_name (str): The name of the first node.
- node2_name (str): The name of the second node.
**Returns:** str - A message indicating whether a cyclic dependency exists.

**Raises:**

- ValueError: If either node name is invalid or empty.
- TypeError: If node names are not strings.
**Examples:**

```python
>>> check_cyclic_dependency(node1_name='nodeA', node2_name='nodeB')
>>> check_cyclic_dependency(node1_name='nodeC', node2_name='nodeD')
'No cyclic dependency detected.'
```

```python
>>> check_cyclic_dependency(node1_name='nodeE', node2_name='nodeF')
'Cyclic dependency detected.'
```



---

## establish_dag_connection

### Description
Establishes a connection between two nodes in a Directed Acyclic Graph (DAG) and returns the result as a list of connected node names.

### Conceptual Info

This shim function is responsible for establishing a connection between two nodes in a Directed Acyclic Graph (DAG). It takes the names of two nodes as input and returns a list representing the result of the connection.

### Docstring

**Summary:** Establishes a DAG connection between two nodes and returns the connected node names.

**Parameters:**

- node1 (str): The name of the first node to be connected.
- node2 (str): The name of the second node to be connected.
**Returns:** List[str] - A list of connected node names after establishing the DAG connection.

**Raises:**

- ValueError: If the input node names are invalid or if the connection would result in a cyclic dependency.
- TypeError: If the input node names are not strings.
**Examples:**

```python
>>> establish_dag_connection(node1='nodeA', node2='nodeB')
['nodeA', 'nodeB']
```

```python
>>> establish_dag_connection(node1='task1', node2='task2')
['task1', 'task2']
```

