# close_data_connection PRD

## Description
Closes an established data connection to release system resources.


## Conceptual Info

The close_data_connection shim is responsible for terminating an active data connection, ensuring that system resources are properly released and made available for other tasks.

## Docstring

### Summary
Closes an established data connection and returns the status of the operation.

### Parameters

- **connection** (str): A string representing the established data connection to be closed.

### Returns

str: A string indicating the result or status of closing the data connection, such as 'success' or an error message.

### Raises

- ValueError: If the input 'connection' is not a valid or recognized connection string.
- TypeError: If the 'connection' parameter is not of type string.

### Examples

```python
>>> close_data_connection(connection='active_connection_string')
'success'
```

```python
>>> close_data_connection(connection='invalid_connection')
'error: invalid connection'
```
