# parse_castling_rights PRD

## Description
Parses the castling rights section of a FEN string into a list of booleans indicating the availability of kingside and queenside castling for both white and black.


## Conceptual Info

This shim converts the castling portion of a FEN string (e.g., 'KQkq' or '-') into a standardized list of booleans, enabling downstream logic to quickly assess castling availability.

## Docstring

### Summary
Parse the castling rights field of a FEN string into a list of booleans.

### Parameters

- **castling_section** (str): The castling rights segment of a FEN string, typically one of 'KQkq', 'Kkq', 'Qq', or '-'.

### Returns

List[bool]: A list of four booleans: [white_kingside, white_queenside, black_kingside, black_queenside] where True indicates the right is available.

### Raises

- ValueError: If the input string contains invalid characters or length greater than 4.
- TypeError: If castling_section is not a string.

### Examples

```python
>>> parse_castling_rights('KQkq')
[True, True, True, True]
```

```python
>>> parse_castling_rights('-')
[False, False, False, False]
```

```python
>>> parse_castling_rights('Kq')
[True, False, False, True]
```
