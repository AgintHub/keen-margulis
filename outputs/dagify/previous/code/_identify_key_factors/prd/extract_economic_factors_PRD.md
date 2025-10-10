# extract_economic_factors PRD

## Description
Extracts a list of primary economic factors that influenced a specified historical event from provided contextual data.


## Conceptual Info

The shim serves as a specialized extraction routine that parses supplied historical datasets to identify and return economic variables relevant to a given historical event, enabling downstream analytical modules to focus on economic dimensions of historical analysis.

## Docstring

### Summary
Extracts primary economic factors from historical data for a given event.

### Parameters

- **historical_data** (dict): A dictionary containing contextual data about the event, expected to include an 'economic_factors' key with a list of strings.
- **event** (str): The name or title of the historical event for which economic factors are to be extracted.

### Returns

List[str]: A list of economic factor descriptions that were identified within the provided historical data for the specified event.

### Raises

- ValueError: Raised when the 'economic_factors' key is missing from historical_data or when no factors are found for the given event.
- TypeError: Raised when historical_data is not a dictionary or event is not a string.

### Examples

```python
>>> result = extract_economic_factors(historical_data={'economic_factors': ['inflation', 'unemployment']}, event='Great Depression')
>>> print(result)
['inflation', 'unemployment']
```

```python
>>> result = extract_economic_factors(historical_data={'economic_factors': []}, event='Great Depression')
>>> print(result)
[]
```
