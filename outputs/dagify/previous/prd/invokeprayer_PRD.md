# invokeprayer PRD

## Description
Step to invoke the prayer based on the prepared intention.


## Conceptual Info

This node invokes a prayer based on a prepared intention, generating the actual prayer invocation and assessing the connection status during the prayer.

## Docstring

### Summary
Invokes a prayer based on the prepared intention and returns the prayer invocation and connection status.

### Parameters

- **prayer_intention** (str): The intention or focus of the prayer, as prepared in the previous step.
- **is_ready** (bool): Whether the person is ready to pray, indicating their preparedness.

### Returns

Tuple[str, str]: A tuple containing the prayer invocation (str) and the connection status (str).

### Raises

- ValueError: If the prayer intention is empty or if the person is not ready to pray.

### Examples

```python
>>> invokeprayer(prayer_intention='Seeking guidance', is_ready=True)
('Dear higher power, guide me...', 'Connected')
```

```python
>>> invokeprayer(prayer_intention='', is_ready=False)
ValueError: Prayer intention cannot be empty and person must be ready to pray.
```
