# _parse_chess_position - Complete PRD Documentation

## Overview
PRDs for nodes in the '_parse_chess_position' module.

## Table of Contents

- [validate_fen_notation](#validate_fen_notation)

- [split_fen_components](#split_fen_components)

- [extract_piece_positions](#extract_piece_positions)

- [parse_side_to_move](#parse_side_to_move)

- [parse_castling_rights](#parse_castling_rights)

- [parse_en_passant_square](#parse_en_passant_square)



---

## validate_fen_notation

### Description
Validates a FEN string, ensuring it follows the standard chess notation format, and returns a canonical form if valid.

### Conceptual Info

This shim ensures that any FEN string passed to the chess parsing pipeline is syntactically and semantically correct, providing a clean, canonical representation for downstream functions.

### Docstring

**Summary:** Validate a FEN string according to the FEN specification and return the canonical form if valid.

**Parameters:**

- fen (str): The FEN string to be validated.
**Returns:** str - The canonical FEN string if the input is valid.

**Raises:**

- ValueError: Raised when the FEN string is syntactically or semantically invalid.
- TypeError: Raised when the input is not a string.
**Examples:**

```python
>>> validate_fen_notation('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
```

```python
>>> validate_fen_notation('invalid fen')
ValueError: Invalid FEN string
```



---

## split_fen_components

### Description
Splits a validated FEN string into its six component fields and returns them as a list of strings.

### Conceptual Info

This shim takes a validated FEN string and splits it into its constituent parts so that downstream parsers can operate on each field separately.

### Docstring

**Summary:** Splits a FEN string into its six components.

**Parameters:**

- fen (str): A validated FEN string containing exactly six fields separated by spaces.
**Returns:** LIST_STR - A list of six strings representing the FEN components in the order: board, active color, castling rights, en passant target, half‑move clock, and full‑move number.

**Raises:**

- TypeError: If the input is not a string.
- ValueError: If the input string does not contain exactly six space‑separated parts.
**Examples:**

```python
>>> split_fen_components('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
["rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR", "w", "KQkq", "-", "0", "1"]
```

```python
>>> split_fen_components('8/8/8/8/8/8/8/8 w - - 0 1')
["8/8/8/8/8/8/8/8", "w", "-", "-", "0", "1"]
```



---

## extract_piece_positions

### Description
Extracts a list of piece positions from the board section of a FEN string.

### Conceptual Info

The shim parses the board section of a FEN string to enumerate all pieces present on the board along with their board coordinates.

### Docstring

**Summary:** Extract a list of piece positions from a FEN board section string.

**Parameters:**

- board_section (str): The board section of a FEN string (e.g., "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR").
**Returns:** list[str] - A list of strings, each formatted as "<square> <piece>", enumerating all pieces on the board from a8 to h1.

**Raises:**

- TypeError: If board_section is not a string.
- ValueError: If board_section does not contain exactly 8 ranks separated by slashes or contains invalid characters.
**Examples:**

```python
>>> extract_piece_positions('8/8/8/8/8/8/8/8')
[]
```

```python
>>> extract_piece_positions('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
["a8 r", "b8 n", "c8 b", "d8 q", "e8 k", "f8 b", "g8 n", "h8 r", "a7 p", "b7 p", "c7 p", "d7 p", "e7 p", "f7 p", "g7 p", "h7 p", "a2 P", "b2 P", "c2 P", "d2 P", "e2 P", "f2 P", "g2 P", "h2 P", "a1 R", "b1 N", "c1 B", "d1 Q", "e1 K", "f1 B", "g1 N", "h1 R"]
```



---

## parse_side_to_move

### Description
Parses the side-to-move section of a FEN string and returns the side to move as 'w' or 'b'.

### Conceptual Info

The parse_side_to_move shim extracts and validates the side-to-move field from a FEN string, ensuring that only the characters 'w' or 'b' are accepted and returned for downstream processing of a chess position.

### Docstring

**Summary:** Parse the side-to-move field of a FEN string, returning 'w' for white or 'b' for black.

**Parameters:**

- side_section (str): A single-character string from a FEN that indicates which side should move next; expected to be 'w' or 'b'.
**Returns:** str - The character 'w' if white is to move or 'b' if black is to move.

**Raises:**

- ValueError: Raised when side_section is not 'w' or 'b', indicating an invalid side-to-move value.
- TypeError: Raised when side_section is not of type str.
**Examples:**

```python
>>> parse_side_to_move('w')
'w'
```

```python
>>> parse_side_to_move('b')
'b'
```



---

## parse_castling_rights

### Description
Parses the castling rights section of a FEN string into a list of booleans indicating the availability of kingside and queenside castling for both white and black.

### Conceptual Info

This shim converts the castling portion of a FEN string (e.g., 'KQkq' or '-') into a standardized list of booleans, enabling downstream logic to quickly assess castling availability.

### Docstring

**Summary:** Parse the castling rights field of a FEN string into a list of booleans.

**Parameters:**

- castling_section (str): The castling rights segment of a FEN string, typically one of 'KQkq', 'Kkq', 'Qq', or '-'.
**Returns:** List[bool] - A list of four booleans: [white_kingside, white_queenside, black_kingside, black_queenside] where True indicates the right is available.

**Raises:**

- ValueError: If the input string contains invalid characters or length greater than 4.
- TypeError: If castling_section is not a string.
**Examples:**

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



---

## parse_en_passant_square

### Description
Parses the en passant square from the FEN en passant field and returns it as a string or '-' if none.

### Conceptual Info

This shim extracts the en passant square from the fourth component of a FEN string, performing minimal validation and returning the raw square notation or a placeholder when no en passant move is available.

### Docstring

**Summary:** Parse the en passant field of a FEN string and return the square or '-' if none.

**Parameters:**

- en_passant_section (str): The en passant section of a FEN string (fourth component). Expected to be either a two-character square notation like "e3" or a single hyphen '-' indicating no en passant square.
**Returns:** str - The square notation of the en passant square, or '-' if no en passant move exists.

**Raises:**

- TypeError: Raised if en_passant_section is not a string.
- ValueError: Raised if en_passant_section is not a valid two-character square or '-'.
**Examples:**

```python
>>> parse_en_passant_square('e3')
'e3'
```

```python
>>> parse_en_passant_square('-')
'-'
```

```python
>>> parse_en_passant_square('z9')
Traceback (most recent call last):
  ...
ValueError: Invalid en passant square: z9
```

