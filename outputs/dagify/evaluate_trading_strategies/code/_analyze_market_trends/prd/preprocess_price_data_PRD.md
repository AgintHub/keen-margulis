# preprocess_price_data PRD

## Description
Preprocesses raw stock price data by validating, filtering invalid entries, and sorting the remaining prices.


## Conceptual Info

The shim preprocess_price_data serves to sanitize and normalize raw price inputs so that downstream analysis functions receive clean, reliable numeric data.

## Docstring

### Summary
Preprocesses raw stock price data by validating the input list, filtering out non‑numeric or negative entries, sorting the remaining values, and returning the cleaned list.

### Parameters

- **prices** (List[float]): A list of raw stock prices to be cleaned. Each element should represent a price as a float.

### Returns

List[float]: A list containing only valid, non‑negative stock prices sorted in ascending order.

### Raises

- TypeError: Raised if `prices` is not a list.
- ValueError: Raised if any element in `prices` cannot be cast to float or if the list is empty after cleaning.

### Examples

```python
>>> preprocess_price_data([100.0, 101.5, 99.3])
[99.3, 100.0, 101.5]
```

```python
>>> preprocess_price_data([100.0, -5.0, 102.0])
[100.0, 102.0]
```
