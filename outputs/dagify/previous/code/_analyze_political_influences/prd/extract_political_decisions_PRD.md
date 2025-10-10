# extract_political_decisions PRD

## Description
This shim extracts a list of key political decisions from a string of political factors for downstream analysis.


## Conceptual Info

The extract_political_decisions shim is responsible for parsing a textual description of political factors and isolating distinct political decisions that have directly shaped historical events or periods. This extracted list feeds into subsequent nodes that analyze policy influence and leadership impact.

## Docstring

### Summary
Extracts key political decisions from a textual description of political factors.

### Parameters

- **political_factors** (str): A free‑form string containing political factors, typically a comma‑separated list or paragraph describing events, reforms, or decisions.

### Returns

List[str]: A list of strings, each representing a distinct political decision identified within the input.

### Raises

- ValueError: Raised when the input string is empty or contains no discernible decisions.
- TypeError: Raised when the input is not a string.

### Examples

```python
>>> extract_political_decisions('Political factors include the enactment of the 1964 Civil Rights Act, the establishment of the Department of Energy, and the decision to withdraw from the Soviet-led space race.')
['enactment of the 1964 Civil Rights Act', 'establishment of the Department of Energy', 'decision to withdraw from the Soviet-led space race']
```

```python
>>> extract_political_decisions('Factors: economic sanctions, election reforms, and policy shifts.')
['economic sanctions', 'election reforms', 'policy shifts']
```
