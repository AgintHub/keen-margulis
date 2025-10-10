# validate_and_clean_metrics_data PRD

## Description
Validates and cleans the raw metrics data fetched from various sources.


## Conceptual Info

This shim node is responsible for validating and cleaning the raw metrics data fetched from various sources, ensuring it is in a consistent and usable format for further processing.

## Docstring

### Summary
Validates and cleans raw metrics data.

### Parameters

- **raw_data** (str): Input string representing a list of dictionaries containing raw metrics data.

### Returns

List[dict]: List of dictionaries containing validated and cleaned metrics data.

### Raises

- ValueError: If the input string is not a valid representation of a list of dictionaries.
- TypeError: If the input is not a string or if the dictionaries within the list contain incorrect types.

### Examples

```python
>>> raw_data = '[{"metric": "value1"}, {"metric": "value2"}]'
>>> validated_data = validate_and_clean_metrics_data(raw_data=raw_data)
>>> print(validated_data)
[{'metric': 'value1'}, {'metric': 'value2'}]
```

```python
>>> raw_data = '[{"metric": "value1"}, {"wrong_metric": "value2"}]'
>>> try:
...     validated_data = validate_and_clean_metrics_data(raw_data=raw_data)
>>> except ValueError as e:
...     print(e)
"Invalid data: missing required 'metric' key"
```
