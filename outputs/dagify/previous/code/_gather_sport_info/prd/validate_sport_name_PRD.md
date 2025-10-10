# validate_sport_name PRD

## Description
Validates a given sport name against a predefined list and returns the canonical form.


## Conceptual Info

The shim is responsible for ensuring that the sport name provided by the user or upstream nodes is recognized and mapped to a standard, canonical form before further processing. It acts as a gatekeeper, preventing invalid or misspelled sport names from propagating through the system.

## Docstring

### Summary
Validate a sport name against a known list and return its canonical form.

### Parameters

- **sport_name** (str): The sport name to be validated. Can be a full name or abbreviation.

### Returns

str: The canonical sport name that matches an entry in the supported sports list.

### Raises

- TypeError: Raised if sport_name is not a string.
- ValueError: Raised if sport_name does not match any known sport.

### Examples

```python
>>> validate_sport_name('soccer')
'Football'
```

```python
>>> validate_sport_name('basketball')
'Basketball'
```
