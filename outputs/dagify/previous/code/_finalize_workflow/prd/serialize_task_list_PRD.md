# serialize_task_list PRD

## Description
Serializes a list of task identifiers into a single comma-separated string.


## Conceptual Info

This shim turns a list of task names into a compact string that can be stored or transmitted, maintaining the order of the tasks.

## Docstring

### Summary
Converts a list of task identifiers into a single comma-separated string.

### Parameters

- **tasks** (List[str]): A list of task identifiers to serialize.

### Returns

str: A string containing the task identifiers joined by commas, preserving the input order.

### Raises

- TypeError: If the input is not a list.
- ValueError: If any element in the list is not a string.

### Examples

```python
>>> output = serialize_task_list(['step1', 'step2', 'step3'])
'step1,step2,step3'
```

```python
>>> output = serialize_task_list(['taskC', 'taskA', 'taskB'])
'taskC,taskA,taskB'
```
