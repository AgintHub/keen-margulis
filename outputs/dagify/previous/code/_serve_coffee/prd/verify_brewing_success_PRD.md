# verify_brewing_success PRD

## Description
Verifies whether the brewing process was successful and returns a status string.


## Conceptual Info

This shim checks the brewing success flag and provides a human‑readable status message, allowing downstream nodes to act accordingly.

## Docstring

### Summary
Check brewing success and return a status message.

### Parameters

- **brewed_success** (bool): Boolean indicating if the brewing process completed successfully.

### Returns

str: A message: 'Brewing succeeded' when brewed_success is True, otherwise 'Brewing failed'.

### Raises

- ValueError: If brewed_success is None.
- TypeError: If brewed_success is not a boolean.

### Examples

```python
>>> verify_brewing_success(brewed_success=True)
'Brewing succeeded'
```

```python
>>> verify_brewing_success(brewed_success=False)
'Brewing failed'
```
