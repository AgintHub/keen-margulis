# format_dependency_pairs PRD

## Description
Formats a list of dependency tuples into human‑readable strings of the form "parent -> child".


## Conceptual Info

Transforms raw dependency tuples into concise string representations for reporting and further processing.

## Docstring

### Summary
Converts a list of dependency tuples into formatted strings.

### Parameters

- **dependencies** (List[tuple]): A list of tuples where each tuple contains two task names (parent, child).

### Returns

List[str]: A list of strings, each representing a dependency pair in the form 'parent -> child'.

### Raises

- ValueError: Raised when the input list is empty or contains non‑tuple elements.
- TypeError: Raised when the input is not a list.

### Examples

```python
>>> format_dependency_pairs([('Task1', 'Task2'), ('Task3', 'Task4')])
["Task1 -> Task2", "Task3 -> Task4"]
```

```python
>>> format_dependency_pairs([('A', 'B')])
["A -> B"]
```
