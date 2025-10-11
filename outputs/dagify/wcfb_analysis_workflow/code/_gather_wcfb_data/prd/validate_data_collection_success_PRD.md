# validate_data_collection_success PRD

## Description
Validates the success of data collection for business operations, customer feedback, and market trends.


## Conceptual Info

This shim node is responsible for validating the success of data collection processes for business operations, customer feedback, and market trends. It ensures that the collected data is valid and consistent before proceeding with further processing.

## Docstring

### Summary
Validates the data collection success for business operations, customer feedback, and market trends.

### Parameters

- **business_data** (str): Data related to business operations that needs to be validated.
- **feedback_data** (str): Processed customer feedback data that needs to be validated.
- **trends_data** (str): Aggregated market trends data that needs to be validated.

### Returns

str: Output indicating whether the data collection was successful. It should return 'success' if all data is valid, otherwise, it should return an appropriate error message.

### Raises

- ValueError: If any of the input data is invalid or inconsistent.
- TypeError: If the input data types are not as expected.

### Examples

```python
>>> validate_data_collection_success(business_data='valid_business_data', feedback_data='valid_feedback_data', trends_data='valid_trends_data')
'success'
```

```python
>>> validate_data_collection_success(business_data='invalid_business_data', feedback_data='valid_feedback_data', trends_data='valid_trends_data')
'error: invalid business data'
```
