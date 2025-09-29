# format_threat_descriptions PRD

## Description
Converts a list of attacking chess piece identifiers into a concise, human‑readable threat description string.


## Conceptual Info

This shim formats raw attacking piece data into a readable threat description for display and downstream analysis.

## Docstring

### Summary
Formats a list of attacking chess piece identifiers into a human‑readable threat description string.

### Parameters

- **attacking_pieces** (List[str]): A list of strings describing attacking pieces in standard algebraic notation (e.g., 'Nf6', 'Qxe5').

### Returns

str: A single string summarizing all attacking pieces, or a message indicating no active threats.

### Raises

- ValueError: Raised when the input list is empty.
- TypeError: Raised when the input is not a list of strings.

### Examples

```python
>>> format_threat_descriptions(['Nf6', 'Qxe5'])
'Threats from: Nf6, Qxe5'
```

```python
>>> format_threat_descriptions([])
'No active threats'
```
