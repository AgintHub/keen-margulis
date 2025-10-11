# extract_requirements PRD

## Description
Extracts a list of key requirements from a parsed user intent dictionary.


## Conceptual Info

The shim analyzes the structure of a parsed user intent to pull out actionable requirement statements, which are later used to identify domain context and generate objective statements.

## Docstring

### Summary
Extracts key requirement statements from the parsed intent dictionary.

### Parameters

- **parsed_intent** (dict): A dictionary representation of the user input that has already been parsed by the `parse_user_input` function.

### Returns

list[str]: A list of strings, each representing a distinct requirement derived from the parsed intent.

### Raises

- TypeError: Raised if `parsed_intent` is not a dictionary.
- ValueError: Raised if no valid requirements can be extracted from the input.

### Examples

```python
>>> parsed_user_intent = {
...     'intent': 'Book a flight',
...     'entities': {
...         'destination': 'New York',
...         'departure_date': '2025-08-15',
...         'return_date': '2025-08-20' }
>>> } 
>>> requirements = extract_requirements(parsed_user_intent)
['Destination: New York', 'Departure date: 2025-08-15', 'Return date: 2025-08-20']
```

```python
>>> extract_requirements({})
ValueError: No requirements extracted from the parsed intent.
```
