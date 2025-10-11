# parse_cycles_from_string PRD

## Description
Parse a string representation of cycles into a list of cycle identifiers or descriptions.


## Conceptual Info

This shim converts the `cycles_detected` string from `ValidateDagOutput` into a list of cycle identifiers or descriptions so that downstream nodes can perform cycle removal and generate warnings.

## Docstring

### Summary
Parse a string of cycle identifiers or descriptions into a list of individual cycles.

### Parameters

- **cycles_str** (str): The string representation of cycles. It may contain comma‑separated cycle names, newline‑separated names, or be an empty string if no cycles are present.

### Returns

list[str]: A list of cycle identifiers or descriptions extracted from the input string. The list is empty if the input is an empty string.

### Raises

- ValueError: Raised when the input string contains malformed entries that cannot be parsed into distinct cycle identifiers.
- TypeError: Raised if the provided `cycles_str` is not of type `str`.

### Examples

```python
>>> cycles = parse_cycles_from_string('cycleA, cycleB, cycleC')
['cycleA', 'cycleB', 'cycleC']
```

```python
>>> cycles = parse_cycles_from_string('')
[]
```
