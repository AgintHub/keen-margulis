# collect_account_data PRD

## Description
Gather account data including balance and positions


## Conceptual Info

This node is responsible for collecting account data, including the current balance and positions, to provide a snapshot of the current trading account status.

## Docstring

### Summary
Collects and returns account data including balance and positions.

### Returns

Dict[str, Union[float, List[str]]]: A dictionary containing the account balance as a float and positions as a list of strings.

### Raises

- ConnectionError: If there's an issue connecting to the data source.
- DataRetrievalError: If there's an error retrieving account data.

### Examples

```python
>>> account_data = collect_account_data()
{'account_balance': 10000.0, 'positions': ['AAPL', 'GOOG']}
```

```python
>>> account_data = collect_account_data()
>>> print(account_data['account_balance'])
>>> print(account_data['positions'])
10000.0
['AAPL', 'GOOG']
```
