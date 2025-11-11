# define_node_prompts_and_descriptions PRD

## Description
Specify the prompts and descriptions for each node in the DAG.


## Conceptual Info

This node generates prompts and descriptions for each node in the DAG based on the structure defined by the parent node.

## Docstring

### Summary
Generate node prompts and descriptions from the DAG structure.

### Parameters

- **dag_nodes** (List[str]): List of node names from the DAG structure.
- **dag_edges** (List[str]): List of edges in the DAG, represented as 'node1->node2'.
- **root_nodes** (List[str]): List of root node names in the DAG.
- **is_valid_dag** (bool): Whether the constructed DAG is valid.

### Returns

dict: A dictionary containing lists of node names, prompts, and descriptions.

### Raises

- ValueError: If the input DAG structure is invalid or empty.

### Examples

```python
>>> node_names = ['A', 'B', 'C']
>>> node_prompts = ['Task A', 'Task B', 'Task C']
>>> node_descriptions = ['Description A', 'Description B', 'Description C']
>>> result = define_node_prompts_and_descriptions(node_names, node_prompts, node_descriptions)
{'node_names': ['A', 'B', 'C'], 'node_prompts': ['Task A', 'Task B', 'Task C'], 'node_descriptions': ['Description A', 'Description B', 'Description C']}
```
