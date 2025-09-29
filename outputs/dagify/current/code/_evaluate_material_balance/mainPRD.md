# _evaluate_material_balance - Complete PRD Documentation

## Overview
PRDs for nodes in the '_evaluate_material_balance' module.

## Table of Contents

- [validate_piece_positions](#validate_piece_positions)

- [extract_white_pieces](#extract_white_pieces)

- [extract_black_pieces](#extract_black_pieces)

- [count_pieces_by_type](#count_pieces_by_type)

- [calculate_material_value](#calculate_material_value)

- [compute_material_score](#compute_material_score)

- [combine_piece_counts](#combine_piece_counts)



---

## validate_piece_positions

### Description
Validates a list of chess position strings, ensuring each is a legal coordinate and normalizes formatting.

### Conceptual Info

The shim acts as a gatekeeper for position data, ensuring downstream functions receive well-formed coordinates.

### Docstring

**Summary:** Validate and normalize a list of chess board position strings.

**Parameters:**

- piece_positions (List[str]): A list of strings each representing a square on the chessboard (e.g., 'e4', 'A1').
**Returns:** List[str] - The input list with each position converted to lowercase and trimmed; positions are guaranteed to be valid squares.

**Raises:**

- TypeError: If `piece_positions` is not a list or contains non-string elements.
- ValueError: If any string does not match a valid chess coordinate (files a-h and ranks 1-8).
**Examples:**

```python
>>> validate_piece_positions(['E4', 'a1', 'H8'])
['e4', 'a1', 'h8']
```

```python
>>> try:
...     validate_piece_positions(['e9', 'b2'])
>>> except ValueError as e:
...     print(e)
Invalid chess position: e9
```



---

## extract_white_pieces

### Description
Extracts and returns a list of white piece identifiers from a list of chess piece positions.

### Conceptual Info

This shim isolates the logic for filtering white chess pieces from a mixed list of piece positions, enabling downstream evaluation nodes to work with a clean subset.

### Docstring

**Summary:** Return a list of chess piece positions that represent white pieces.

**Parameters:**

- piece_positions (List[str]): A list of strings where each string encodes a board square followed by a piece identifier (e.g., 'e4N', 'd3q'). White pieces are represented by uppercase letters.
**Returns:** List[str] - All input strings whose piece identifier is uppercase, preserving the original order.

**Raises:**

- ValueError: If any element of `piece_positions` is not a string or does not contain at least a file, rank, and a piece identifier.
- TypeError: If `piece_positions` is not a list or its elements are not strings.
**Examples:**

```python
>>> extract_white_pieces(['e4N', 'd3Q', 'a1k', 'c5P'])
['e4N', 'd3Q', 'c5P']
```

```python
>>> extract_white_pieces(['b2p', 'g8R', 'h7q'])
['g8R']
```



---

## extract_black_pieces

### Description
Extracts black piece positions from a list of chess piece positions.

### Conceptual Info

This shim isolates the logic for filtering black chess pieces from a given set of piece positions, allowing the rest of the material balance evaluation to operate on a clean subset of data.

### Docstring

**Summary:** Extracts the positions of all black pieces from the given list of chess piece positions.

**Parameters:**

- piece_positions (List[str]): A list of chess piece position strings, e.g., ['e4', 'B5', 'c6', 'D1'].
**Returns:** List[str] - A list containing only the positions of black pieces.

**Raises:**

- TypeError: Raised when `piece_positions` is not a list or contains non-string elements.
- ValueError: Raised when any element in `piece_positions` is an empty string or does not conform to expected format.
**Examples:**

```python
>>> extract_black_pieces(['e4', 'B5', 'c6', 'D1'])
['e4', 'c6']
```

```python
>>> extract_black_pieces([])
[]
```



---

## count_pieces_by_type

### Description
Counts the number of each chess piece type from a list of piece symbols and returns a list of counts in the order king, queen, rook, bishop, knight, pawn.

### Conceptual Info

This shim aggregates the quantity of each chess piece type for a single side, providing a foundation for material evaluation and board analysis.

### Docstring

**Summary:** Counts chess pieces by type.

**Parameters:**

- pieces (List[str]): A list of piece symbols (e.g., 'K', 'Q', 'R', 'B', 'N', 'P') representing the pieces of one side.
**Returns:** List[int] - A list of six integers: [king_count, queen_count, rook_count, bishop_count, knight_count, pawn_count].

**Raises:**

- TypeError: Raised if `pieces` is not a list.
- ValueError: Raised if any element in `pieces` is not a valid chess piece symbol.
**Examples:**

```python
>>> count_pieces_by_type(['K', 'P', 'P', 'Q', 'R', 'B', 'N', 'P'])
[1, 1, 1, 1, 1, 3]
```

```python
>>> count_pieces_by_type([])
[0, 0, 0, 0, 0, 0]
```



---

## calculate_material_value

### Description
Computes the material value of a side based on piece counts.

### Conceptual Info

This shim calculates a numeric value representing the material advantage of a chess side by weighting each piece type with standard chess piece values and summing the result based on the provided counts.

### Docstring

**Summary:** Calculates the material value of a side based on the counts of each piece type.

**Parameters:**

- piece_counts (List[int]): A list of integers representing the number of each piece type in the order [pawn, knight, bishop, rook, queen, king].
**Returns:** float - The total material value as a float. Positive values indicate an advantage for the side, while negative values indicate a disadvantage.

**Raises:**

- ValueError: Raised when the input list is not exactly six elements long.
- TypeError: Raised when any element in the list is not an integer.
- ValueError: Raised when any count is negative.
**Examples:**

```python
>>> calculate_material_value(piece_counts=[8, 2, 2, 2, 1, 1])
39.0
```

```python
>>> calculate_material_value(piece_counts=[0, 2, 2, 2, 1, 1])
17.0
```



---

## compute_material_score

### Description
Calculates the material score by subtracting black's material value from white's material value.

### Conceptual Info

The shim computes a numeric score representing the material advantage of the white side over the black side by comparing their aggregated material values.

### Docstring

**Summary:** Return the material score as a float by subtracting the black material value from the white material value.

**Parameters:**

- white_value (float): Total material value of the white side, as returned by calculate_material_value.
- black_value (float): Total material value of the black side, as returned by calculate_material_value.
**Returns:** float - The material score (white_value minus black_value). A positive value indicates a white advantage, zero indicates parity, and negative indicates a black advantage.

**Raises:**

- TypeError: Raised when either `white_value` or `black_value` is not of type float.
- ValueError: Raised when either `white_value` or `black_value` is negative, since material values should be non‑negative.
**Examples:**

```python
>>> compute_material_score(white_value=9.0, black_value=5.0)
4.0
```

```python
>>> compute_material_score(white_value=6.0, black_value=6.0)
0.0
```



---

## combine_piece_counts

### Description
Combines two lists of piece counts (white and black) into a single list by summing corresponding piece type counts.

### Conceptual Info

This shim aggregates the counts of each chess piece type from both the white and black sides to provide a unified view of material distribution.

### Docstring

**Summary:** Combine piece counts from two sides of a chess position.

**Parameters:**

- white_counts (List[int]): List of integers representing the count of each piece type for white, ordered consistently with `black_counts`.
- black_counts (List[int]): List of integers representing the count of each piece type for black, ordered consistently with `white_counts`.
**Returns:** List[int] - A list of integers where each element is the sum of the corresponding elements from `white_counts` and `black_counts`.

**Raises:**

- TypeError: Raised if either `white_counts` or `black_counts` is not a list or contains non-integer elements.
- ValueError: Raised if `white_counts` and `black_counts` are of different lengths.
**Examples:**

```python
>>> combine_piece_counts(white_counts=[5, 2, 1, 0, 0, 0],
...                       black_counts=[3, 1, 2, 0, 0, 0])
[8, 3, 3, 0, 0, 0]
```

```python
>>> combine_piece_counts(white_counts=[0, 0, 0, 0, 0, 0],
...                       black_counts=[1, 1, 1, 1, 1, 1])
[1, 1, 1, 1, 1, 1]
```

