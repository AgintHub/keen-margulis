# verify_filter_readiness PRD

## Description
Verifies that the filter is ready to receive the expected amount of grounds based on the cup count.


## Conceptual Info

Ensures the coffee filter is prepared to hold the correct quantity of grounds for the desired number of cups.

## Docstring

### Summary
Verifies that the filter can accommodate the expected amount of coffee grounds based on the cup count.

### Parameters

- **expected_amount** (str): The expected amount of coffee grounds in grams, provided as a string that can be parsed to a float.
- **cup_count** (str): The desired number of cups to brew, provided as a string that can be parsed to an integer.

### Returns

bool: True if the filter can handle the specified amount of grounds for the given cup count, otherwise False.

### Raises

- ValueError: Raised when the parsed amount or cup count is not a positive number.
- TypeError: Raised when either expected_amount or cup_count is not a string.

### Examples

```python
>>> ready = verify_filter_readiness(expected_amount='50', cup_count='5')
>>> print(ready)
True
```

```python
>>> ready = verify_filter_readiness(expected_amount='10', cup_count='10')
>>> print(ready)
False
```
