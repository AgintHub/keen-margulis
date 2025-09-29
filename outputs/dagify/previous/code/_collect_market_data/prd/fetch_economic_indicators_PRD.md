# fetch_economic_indicators PRD

## Description
Fetches economic indicators from the provided data sources and returns them as a list of floats.


## Conceptual Info

This shim node is responsible for retrieving economic indicators from specified data sources, playing a crucial role in the market data collection process.

## Docstring

### Summary
Fetches economic indicators from given data sources and returns them as a list of floats.

### Parameters

- **sources** (str): A string representing the data sources to fetch economic indicators from.

### Returns

List[float]: A list of economic indicators fetched from the given sources.

### Raises

- ValueError: If the input sources are invalid or cannot be processed.
- TypeError: If the input type is not a string.

### Examples

```python
>>> fetch_economic_indicators(sources='https://example.com/economic_data')
>>> fetch_economic_indicators(sources='database://economic_indicators')
[1.2, 3.4, 5.6]
```
