# extract_account_balance PRD

## Description
Extracts the account balance from the provided raw account data.


## Conceptual Info

This shim is responsible for extracting the account balance from raw account data fetched from a data connection. It plays a crucial role in the account data collection process.

## Docstring

### Summary
Extracts the account balance from raw account data.

### Parameters

- **data** (str): The raw account data containing the account balance information.

### Returns

float: The extracted account balance.

### Raises

- ValueError: If the raw data is malformed or missing required balance information.
- TypeError: If the input data is not of type str.

### Examples

```python
>>> raw_data = '{"account_balance": 1234.56, "other_info": "some data"}'
>>> balance = extract_account_balance(data=raw_data)
1234.56
```

```python
>>> raw_data = '{\"account_balance\": 7890.12, \"other_info\": \"some other data\"}'
>>> balance = extract_account_balance(data=raw_data)
7890.12
```
