# validate_input_lengths PRD

## Description
Validates that the evaluations and risks lists have equal length and correct types before strategy selection.


## Conceptual Info

This shim ensures data integrity by checking that the number of strategy evaluations matches the number of associated risk assessments before any downstream calculations are performed.

## Docstring

### Summary
Checks that the provided evaluations and risks lists are of equal length and contain appropriate element types.

### Parameters

- **evaluations** (List[str]): A list of evaluation strings for each trading strategy.
- **risks** (List[float]): A list of risk scores corresponding to each evaluation.

### Returns

str: A confirmation string "Input lengths validated" when inputs are correct.

### Raises

- ValueError: Raised when the lengths of evaluations and risks differ.
- TypeError: Raised when evaluations is not a list of strings or risks is not a list of floats.

### Examples

```python
>>> validate_input_lengths(evaluations=['win', 'draw', 'loss'], risks=[0.1, 0.2, 0.3])
"Input lengths validated"
```

```python
>>> validate_input_lengths(evaluations=['win', 'draw'], risks=[0.1, 0.2, 0.3])
ValueError: evaluations and risks must have the same length
```
