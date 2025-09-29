# validate_and_clean_volume_data PRD

## Description
Validates and cleans raw volume data fetched from various sources.


## Conceptual Info

This shim node is responsible for validating and cleaning raw volume data fetched from various market data sources. It ensures that the data is consistent and ready for further processing.

## Docstring

### Summary
Validate and clean raw volume data to ensure it is consistent and usable for further processing.

### Parameters

- **raw_data** (str): Raw volume data fetched from various sources, expected to be a string representation of a list of dictionaries.

### Returns

List[dict]: A list of dictionaries containing validated and cleaned volume data.

### Raises

- ValueError: If the input raw_data is not a valid string representation of a list of dictionaries.
- TypeError: If the input raw_data cannot be parsed into a list of dictionaries.

### Examples

```python
>>> raw_data = '[{"date": "2022-01-01", "volume": 1000}, {"date": "2022-01-02", "volume": 2000}]'
>>> validated_data = validate_and_clean_volume_data(raw_data=raw_data)
[{"date": "2022-01-01", "volume": 1000}, {"date": "2022-01-02", "volume": 2000}]
```

```python
>>> raw_data = '[{"date": "2022-01-01"}, {"volume": 2000}]'
>>> validated_data = validate_and_clean_volume_data(raw_data=raw_data)
ValueError: Invalid data structure in input raw_data
```
