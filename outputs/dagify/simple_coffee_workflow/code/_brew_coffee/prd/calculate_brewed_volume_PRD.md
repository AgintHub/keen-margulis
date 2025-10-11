# calculate_brewed_volume PRD

## Description
Calculates the number of coffee cups that can be brewed from a given amount of coffee grounds.


## Conceptual Info

The shim determines how many standard cups of coffee can be produced from a specified amount of coffee grounds, enabling downstream logic to anticipate volume and resource usage.

## Docstring

### Summary
Returns the number of standard cups of coffee that can be brewed from the given coffee amount in grams.

### Parameters

- **coffee_amount** (str): String representation of the coffee grounds weight in grams.

### Returns

int: Integer count of coffee cups that can be brewed.

### Raises

- ValueError: Raised when the coffee_amount cannot be converted to a positive numeric value.
- TypeError: Raised when coffee_amount is not a string.

### Examples

```python
>>> calculate_brewed_volume('7.5')
1
```

```python
>>> calculate_brewed_volume('15')
2
```
