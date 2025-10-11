# format_win_loss_record PRD

## Description
Formats the win/loss record into a string representation.


## Conceptual Info

This shim node is responsible for formatting the win/loss record of a team into a string representation, typically used in sports analytics.

## Docstring

### Summary
Formats the win and loss counts into a string representation.

### Parameters

- **wins** (str): The number of wins as a string.
- **losses** (str): The number of losses as a string.

### Returns

str: The formatted win/loss record (e.g., '20-10').

### Raises

- ValueError: If either wins or losses cannot be converted to a non-negative integer.
- TypeError: If wins or losses are not strings.

### Examples

```python
>>> format_win_loss_record(wins='20', losses='10')
'20-10'
```

```python
>>> format_win_loss_record(wins='0', losses='5')
'0-5'
```
