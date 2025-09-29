# validate_and_clean_price_data PRD

## Description
Validates and cleans raw price data fetched from various market data sources.


## Conceptual Info

This shim node is responsible for validating and cleaning raw price data fetched from various market data sources before it's processed further.

## Docstring

### Summary
Validates and cleans raw price data by checking for missing values, outliers, and data format consistency.

### Parameters

- **raw_data** (str): Input raw price data as a string representation of a list of dictionaries.

### Returns

List[dict]: List of dictionaries containing validated and cleaned price data.

### Raises

- ValueError: When input data is malformed or contains invalid values.
- TypeError: When input data type is not a string representation of a list of dictionaries.

### Examples

```python
>>> raw_price_data = '[{"date": "2022-01-01", "price": 100.0}, {"date": "2022-01-02", "price": 105.0}]'
>>> validated_data = validate_and_clean_price_data(raw_data=raw_price_data)
[{"date": "2022-01-01", "price": 100.0}, {"date": "2022-01-02", "price": 105.0}]
```

```python
>>> raw_price_data = '[{"date": "2022-01-01"}, {"date": "2022-01-02", "price": 105.0}]'
>>> validated_data = validate_and_clean_price_data(raw_data=raw_price_data)
ValueError: Missing 'price' value for date '2022-01-01'
```
