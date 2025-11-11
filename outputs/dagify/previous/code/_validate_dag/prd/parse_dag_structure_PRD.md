# parse_dag_structure PRD

## Description
Parses the input DAG structure string into a format that can be used for further processing.


## Conceptual Info

This shim function is responsible for parsing the input DAG structure string into a usable format for further validation and processing in the workflow.

## Docstring

### Summary
Parses the input DAG structure string into a suitable format for further processing.

### Parameters

- **dag_structure** (str): The input DAG structure as a string that needs to be parsed.

### Returns

str: The parsed DAG structure in a format that can be used for further processing, such as validation and graph construction.

### Raises

- ValueError: If the input DAG structure string is malformed or cannot be parsed.
- TypeError: If the input is not a string.

### Examples

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
