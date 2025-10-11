# check_coffee_maker_status PRD

## Description
Determines the coffee maker's status string based on filter readiness and grounds presence.


## Conceptual Info

The shim encapsulates the logic that translates the internal state of the coffee maker—specifically whether the filter is prepared and whether grounds have been loaded—into a user‑friendly status string. It is a single‑point interface for status reporting, decoupling status determination from the lower‑level hardware checks.

## Docstring

### Summary
Return a status string based on filter readiness and ground loading.

### Parameters

- **filter_prepared** (bool): True if the filter is properly prepared and ready for use.
- **grounds_loaded** (bool): True if coffee grounds have been loaded into the filter.

### Returns

str: A status string describing the current state of the coffee maker.

### Raises

- ValueError: Raised when an invalid combination of filter_prepared and grounds_loaded is detected, such as both being False.
- TypeError: Raised if either argument is not a boolean.

### Examples

```python
>>> status = check_coffee_maker_status(filter_prepared=True, grounds_loaded=True)
'ready'
```

```python
>>> status = check_coffee_maker_status(filter_prepared=False, grounds_loaded=True)
'error: filter not prepared'
```
