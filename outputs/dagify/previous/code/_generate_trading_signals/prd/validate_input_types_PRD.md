# validate_input_types PRD

## Description
Validates that the input evaluations and strategies are of the correct type.


## Conceptual Info

This shim node is responsible for validating the data types of input evaluations and strategies, ensuring they are List[str] as expected by downstream processing.

## Docstring

### Summary
Validates the input types of evaluations and strategies, raising exceptions for invalid types.

### Parameters

- **evaluations** (List[str]): A list of strategy evaluations to be validated.
- **strategies** (List[str]): A list of recommended strategies to be validated.

### Returns

str: A success message if both inputs are valid List[str].

### Raises

- TypeError: If either evaluations or strategies is not a List[str].

### Examples

```python
>>> validate_input_types(evaluations=['eval1', 'eval2'], strategies=['strat1', 'strat2'])
'Input types are valid.'
```

```python
>>> validate_input_types(evaluations='not a list', strategies=['strat1', 'strat2'])
TypeError: Evaluations must be a List[str]
```
