# retrieve_leagues_for_sport PRD

## Description
Returns the list of major league names for a given sport using a provided mapping dictionary.


## Conceptual Info

This shim provides the core lookup logic for mapping a sport name to its major professional leagues. It decouples the lookup from higher‑level orchestration and allows the mapping dictionary to be supplied by configuration or a separate node.

## Docstring

### Summary
Retrieves a list of league names for the given sport based on a mapping dictionary.

### Parameters

- **sport** (str): The name of the sport to look up, e.g., "soccer".
- **mapping** (dict): A dictionary where keys are sport names and values are lists of league names.

### Returns

List[str]: A list of league names corresponding to the requested sport.

### Raises

- ValueError: Raised if the sport is not present in the mapping dictionary.
- TypeError: Raised if sport is not a string or mapping is not a dict.

### Examples

```python
>>> mapping = {
...     "soccer": ["Premier League", "La Liga"],
...     "basketball": ["NBA", "EuroLeague"],
>>> }
>>> print(retrieve_leagues_for_sport("soccer", mapping))
["Premier League", "La Liga"]
```

```python
>>> try:
...     retrieve_leagues_for_sport("cricket", mapping)
>>> except ValueError as e:
...     print(str(e))
"Sport 'cricket' not found in mapping dictionary."
```
