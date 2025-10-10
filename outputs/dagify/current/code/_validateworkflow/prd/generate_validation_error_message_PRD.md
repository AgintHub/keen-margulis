# generate_validation_error_message PRD

## Description
This shim generates a detailed error message based on the validation results of node connectivity, schema validity, and execution path validity.


## Conceptual Info

This shim plays a crucial role in providing informative error messages during the validation of workflows, helping users identify and rectify issues related to node connectivity, schema validity, and execution path validity.

## Docstring

### Summary
Generates a validation error message based on the given validation results.

### Parameters

- **connectivity_valid** (str): A boolean string indicating whether the node connectivity is valid ('True' or 'False').
- **schema_valid** (str): A boolean string indicating whether the node schema is valid ('True' or 'False').
- **execution_path_valid** (str): A boolean string indicating whether the execution path is valid ('True' or 'False').

### Returns

str: A detailed error message indicating which validation checks failed.

### Raises

- ValueError: If any of the input boolean strings are not 'True' or 'False'.

### Examples

```python
>>> generate_validation_error_message(connectivity_valid='False', schema_valid='True', execution_path_valid='False')
'Validation failed due to invalid connectivity and execution path.'
```

```python
>>> generate_validation_error_message(connectivity_valid='True', schema_valid='False', execution_path_valid='True')
'Validation failed due to invalid schema.'
```
