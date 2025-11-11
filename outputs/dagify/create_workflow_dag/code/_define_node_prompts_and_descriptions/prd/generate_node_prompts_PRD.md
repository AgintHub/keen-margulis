# generate_node_prompts PRD

## Description
Generates a list of prompts for nodes in a DAG based on the node context.


## Conceptual Info

The generate_node_prompts shim function generates a list of prompts for nodes in a DAG based on the provided node context. This function plays a crucial role in defining node prompts and descriptions for the DAG.

## Docstring

### Summary
Generates a list of prompts for nodes in a DAG based on the node context.

### Parameters

- **dag_nodes** (str): List of node names in the DAG.
- **node_context** (str): Node context used to generate prompts.

### Returns

List[str]: List of generated prompts for the nodes in the DAG.

### Raises

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.

### Examples

```python
>>> generate_node_prompts(dag_nodes=['node1', 'node2'], node_context='example_context')
['prompt1', 'prompt2']
```

```python
>>> generate_node_prompts(dag_nodes=['node3', 'node4'], node_context='another_context')
['prompt3', 'prompt4']
```
