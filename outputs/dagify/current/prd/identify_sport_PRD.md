# identify_sport PRD

## Description
Identify the sport of interest


## Conceptual Info

Collects user input to determine which sport to analyze, serving as the foundational data for all subsequent nodes in the sports workflow.

## Docstring

### Summary
Prompts the user to specify a sport of interest and returns the selected sport name as a string.

### Returns

str: The selected sport name.

### Raises

- ValueError: Raised if the user provides an empty or whitespace-only input.

### Examples

```python
>>> sport = identify_sport()
'soccer'
```

```python
>>> sport = identify_sport()
'basketball'
```
