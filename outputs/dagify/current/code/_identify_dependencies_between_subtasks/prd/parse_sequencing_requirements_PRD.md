# parse_sequencing_requirements PRD

## Description
Parses sequencing requirements from a string into a list of dependencies.


## Conceptual Info

The parse_sequencing_requirements shim function takes a string describing sequencing requirements and returns a list of dependencies.

## Docstring

### Summary
Parses sequencing requirements from a string into a list of dependencies.

### Parameters

- **sequencing_requirements** (str): Input string containing sequencing requirements.

### Returns

List[str]: List of parsed dependencies.

### Raises

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.

### Examples

```python
>>> parse_sequencing_requirements('Task A must be completed before Task B')
['Task A -> Task B']
```

```python
>>> parse_sequencing_requirements('Task C and Task D are independent')
[]
```
