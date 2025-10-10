# prompt_user_for_sport PRD

## Description
Prompts the user to specify a sport and returns the entered string.


## Conceptual Info

This shim function provides a simple interface for obtaining a user's sport preference, acting as a placeholder for future, more sophisticated input mechanisms.

## Docstring

### Summary
Prompts the user to enter a sport name and returns the raw string provided by the user.

### Parameters

- **message** (str): The prompt message displayed to the user.

### Returns

str: The string entered by the user.

### Raises

- TypeError: Raised if the message argument is not a string.

### Examples

```python
>>> response = prompt_user_for_sport(message='Please specify a sport of interest: ')
>>> print(response)
'Soccer'
```

```python
>>> response = prompt_user_for_sport(message='Enter your favorite sport: ')
>>> print(response)
'Basketball'
```
