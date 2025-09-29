# _assess_king_safety - Complete PRD Documentation

## Overview
PRDs for nodes in the '_assess_king_safety' module.

## Table of Contents

- [validate_piece_positions](#validate_piece_positions)

- [find_king_positions](#find_king_positions)

- [get_current_side_king](#get_current_side_king)

- [identify_attacking_pieces](#identify_attacking_pieces)

- [evaluate_castling_safety](#evaluate_castling_safety)

- [evaluate_pawn_shield](#evaluate_pawn_shield)

- [calculate_threat_proximity](#calculate_threat_proximity)

- [evaluate_en_passant_threat](#evaluate_en_passant_threat)

- [calculate_final_safety_score](#calculate_final_safety_score)

- [format_threat_descriptions](#format_threat_descriptions)



---

## validate_piece_positions

### Description
Validate chess piece positions for syntax and legality, returning a cleaned list of positions.

### Conceptual Info

This shim ensures that the piece positions supplied to the chess engine are syntactically correct and represent legal squares on a chessboard, providing a sanitized list for downstream analysis.

### Docstring

**Summary:** Validate and sanitize chess piece positions, returning a list of legal squares.

**Parameters:**

- positions (List[str]): List of chess position strings (e.g., ['e4', 'd5']) to be validated.
**Returns:** List[str] - A list containing only valid chess positions.

**Raises:**

- ValueError: Raised when a position string is not a valid chess square (e.g., 'e9', 'z3').
- TypeError: Raised when the input is not a list of strings.
**Examples:**

```python
>>> validate_piece_positions(['e4', 'd5'])
['e4', 'd5']
```

```python
>>> validate_piece_positions(['e9'])
ValueError: Invalid chess position: e9
```



---

## find_king_positions

### Description
Finds the board positions of the white and black kings from a list of piece position strings.

### Conceptual Info

The shim extracts king locations from a validated list of chess piece positions, ensuring both white and black kings are present and correctly identified.

### Docstring

**Summary:** Returns the positions of the white and black kings in the given board representation.

**Parameters:**

- piece_positions (List[str]): A list of strings, each describing a piece on the board in the form "<PieceLetter><Square>", e.g., "Ke1" for the white king on e1.
**Returns:** List[str] - A list of two strings containing the king squares, e.g., ["e1", "e8"]. The first element corresponds to the white king, the second to the black king.

**Raises:**

- TypeError: Raised if `piece_positions` is not a list of strings.
- ValueError: Raised if no king or more than one king of either color is found.
**Examples:**

```python
>>> positions = ["Ke1", "Qd8", "Ke8", "Nb5"]
>>> find_king_positions(piece_positions=positions)
["e1", "e8"]
```

```python
>>> positions = ["Ke1", "Qd8", "Nb5"]
>>> find_king_positions(piece_positions=positions)
ValueError: No king found for black side.
```



---

## get_current_side_king

### Description
Return the king position belonging to the side to move given the two king positions.

### Conceptual Info

Provides the current side's king location based on parsed board positions, enabling subsequent safety assessments.

### Docstring

**Summary:** Return the king square belonging to the side specified to move.

**Parameters:**

- king_positions (List[str]): A list containing exactly two elements: the square notation of the white king and the black king, e.g., ['e1', 'e8'].
- side_to_move (str): The side to move; must be either 'white' or 'black'.
**Returns:** str - The square notation (e.g., 'e1' or 'e8') of the king belonging to the side to move.

**Raises:**

- ValueError: Raised when the side_to_move is not 'white' or 'black', or when king_positions does not contain the expected king for the given side.
- TypeError: Raised when king_positions is not a list of strings or side_to_move is not a string.
**Examples:**

```python
>>> king_positions = ['e1', 'e8']
>>> side_to_move = 'white'
>>> print(get_current_side_king(king_positions, side_to_move))
'e1'
```

```python
>>> king_positions = ['e1', 'e8']
>>> side_to_move = 'black'
>>> print(get_current_side_king(king_positions, side_to_move))
'e8'
```



---

## identify_attacking_pieces

### Description
This shim returns a list of piece identifiers from piece_positions that are attacking the specified target king, taking into account the side to move.

### Conceptual Info

The identify_attacking_pieces shim is responsible for analyzing a board state represented by piece positions and determining which pieces pose an immediate threat to a given king. It abstracts the chess engine logic of attack detection, enabling higher-level safety assessments without requiring a full engine integration.

### Docstring

**Summary:** Return a list of pieces from the provided board representation that are attacking the specified king square.

**Parameters:**

- piece_positions (List[str]): A list of strings representing all pieces on the board in the form of "<piece><square>" (e.g., "Ke1", "Qg5").
- target_king (str): The board square of the king to evaluate, expressed as a two‑character coordinate (e.g., "e1").
- side_to_move (str): The side that is to move, either "white" or "black".
**Returns:** List[str] - A list of strings, each describing a piece that is attacking the target king. The format matches the input representation.

**Raises:**

- ValueError: Raised when side_to_move is not one of "white" or "black", or when target_king is not a valid square.
- TypeError: Raised when any input parameter has an incorrect type.
**Examples:**

```python
>>> pieces = ["Ke1", "Qd4", "Ra8", "Bh3", "Ng6", "pd2", "pb7", "pc7"]
>>> attacking = identify_attacking_pieces(piece_positions=pieces, target_king="e1", side_to_move="black")
>>> print(attacking)
["Qd4", "Bh3"]
```

```python
>>> pieces = ["Ke8", "Qa7", "Nc6", "Pf7", "Pg6"]
>>> attacking = identify_attacking_pieces(piece_positions=pieces, target_king="e8", side_to_move="white")
>>> print(attacking)
["Qa7", "Nc6"]
```



---

## evaluate_castling_safety

### Description
Evaluates a numeric bonus based on the given castling rights and the side to move, indicating how safe castling is for that side.

### Conceptual Info

This shim is used within the king safety assessment pipeline to provide a quantitative measure of how favorable castling is for the current side, based on the available castling rights. The returned bonus influences the overall safety score of the king.

### Docstring

**Summary:** Computes a castling safety bonus from castling rights and the side to move.

**Parameters:**

- castling_rights (str): A four‑character string representing castling rights in standard chess notation (e.g., 'KQkq', 'KQ', 'kq', or '--').
- side_to_move (str): The side to move, either 'white' or 'black'.
**Returns:** float - A non‑negative float bonus; higher values indicate safer castling opportunities.

**Raises:**

- ValueError: Raised when `castling_rights` is not a 4‑character string or contains invalid characters.
- TypeError: Raised when either `castling_rights` or `side_to_move` is not of type `str`.
**Examples:**

```python
>>> evaluate_castling_safety(castling_rights='KQkq', side_to_move='white')
1.0
```

```python
>>> evaluate_castling_safety(castling_rights='kq', side_to_move='black')
0.5
```



---

## evaluate_pawn_shield

### Description
Calculates a numeric score that quantifies the effectiveness of the pawn shield protecting the king for the side to move.

### Conceptual Info

The evaluate_pawn_shield shim is responsible for evaluating how well a king’s pawn shield protects it from direct attacks. It interprets the board state, locates the king and friendly pawns, and returns a float score that is used by higher‑level safety calculations.

### Docstring

**Summary:** Return a float score representing the pawn shield strength for the king of the side to move.

**Parameters:**

- piece_positions (str): Comma‑separated list of piece descriptors in the format "<piece>@<square>", e.g., "P@e2,p@d3".
- king_position (str): Algebraic notation of the king’s square (e.g., "e1" for White king).
- side_to_move (str): The side whose pawn shield is being evaluated, either "white" or "black".
**Returns:** float - A score in the range 0.0 to 1.0 indicating how well the king is protected by its pawns.

**Raises:**

- ValueError: Raised when the input strings cannot be parsed into a valid board representation or contain illegal piece descriptors.
- TypeError: Raised when any of the input arguments is not of type str.
**Examples:**

```python
>>> score = evaluate_pawn_shield('P@e2,P@d2,P@f2', 'e1', 'white')
>>> print(round(score, 2))
0.87
```

```python
>>> score = evaluate_pawn_shield('P@e2,P@d3,P@f3', 'e1', 'white')
>>> print(round(score, 2))
0.65
```



---

## calculate_threat_proximity

### Description
Calculates a numeric threat proximity score for a king based on the positions of attacking pieces.

### Conceptual Info

The shim is responsible for translating the list of attacking piece coordinates and the king's coordinate into a single numeric value that quantifies how close the king is to being captured. This score is used downstream to compute overall king safety.

### Docstring

**Summary:** Returns a threat proximity score for a king given the positions of attacking pieces.

**Parameters:**

- attacking_pieces (str): Comma‑separated chess board coordinates (e.g., "b3,d4,f5") of all pieces that attack the king.
- king_position (str): The chess board coordinate of the king being evaluated (e.g., "e1").
**Returns:** float - A float in the inclusive range [0.0, 1.0] where 0.0 means no immediate threat and 1.0 indicates that the king is under direct attack.

**Raises:**

- ValueError: Raised when either `attacking_pieces` or `king_position` cannot be parsed into valid board coordinates.
- TypeError: Raised when input types are not strings.
**Examples:**

```python
>>> score = calculate_threat_proximity(attacking_pieces='b3,d4,f5', king_position='e1')
>>> print(score)
0.42
```

```python
>>> score = calculate_threat_proximity(attacking_pieces='h8', king_position='e1')
>>> print(score)
0.05
```



---

## evaluate_en_passant_threat

### Description
Evaluates the threat posed by an en passant square on the current king's safety and returns a numeric threat score.

### Conceptual Info

The shim calculates a float score that quantifies the potential danger of an en passant capture to the king, integrating this metric into overall king safety assessment.

### Docstring

**Summary:** Computes a numeric score representing how much an en passant square threatens the king’s safety.

**Parameters:**

- en_passant_square (str): Algebraic notation of the en passant square (e.g., 'e3') or an empty string if no en passant is available.
- king_position (str): Algebraic notation of the king’s current position (e.g., 'e1').
**Returns:** float - A non‑negative float where a higher value indicates a greater threat to the king from the en passant square.

**Raises:**

- ValueError: If `en_passant_square` is not a valid algebraic square or is not applicable for the given king position.
- TypeError: If either `en_passant_square` or `king_position` is not a string.
**Examples:**

```python
>>> >>> evaluate_en_passant_threat('e3', 'e1')
>>> 0.0
0.0
```

```python
>>> >>> evaluate_en_passant_threat('d4', 'e1')
>>> 0.5
0.5
```



---

## calculate_final_safety_score

### Description
Calculates a numeric king safety score from individual safety component values.

### Conceptual Info

This shim aggregates four numeric safety metrics into a single float representing the overall king safety, enabling downstream modules to make safety‑based decisions.

### Docstring

**Summary:** Compute the final king safety score from individual safety component scores.

**Parameters:**

- castling_bonus (float): Bonus score for having castled. Non‑negative floating‑point value.
- pawn_shield (float): Score reflecting the strength of the pawn shield around the king. Non‑negative floating‑point value.
- threat_proximity (float): Score that increases with proximity of enemy pieces to the king. Non‑negative floating‑point value.
- en_passant_threat (float): Score indicating threat from a potential en passant capture. Non‑negative floating‑point value.
**Returns:** float - The weighted sum of the input scores, representing overall king safety.

**Raises:**

- TypeError: If any argument is not of type float.
- ValueError: If any argument is negative.
**Examples:**

```python
>>> calculate_final_safety_score(1.5, 2.0, 0.8, 0.3)
4.6
```

```python
>>> calculate_final_safety_score(0.0, 1.2, 0.5, 0.0)
1.7
```



---

## format_threat_descriptions

### Description
Converts a list of attacking chess piece identifiers into a concise, human‑readable threat description string.

### Conceptual Info

This shim formats raw attacking piece data into a readable threat description for display and downstream analysis.

### Docstring

**Summary:** Formats a list of attacking chess piece identifiers into a human‑readable threat description string.

**Parameters:**

- attacking_pieces (List[str]): A list of strings describing attacking pieces in standard algebraic notation (e.g., 'Nf6', 'Qxe5').
**Returns:** str - A single string summarizing all attacking pieces, or a message indicating no active threats.

**Raises:**

- ValueError: Raised when the input list is empty.
- TypeError: Raised when the input is not a list of strings.
**Examples:**

```python
>>> format_threat_descriptions(['Nf6', 'Qxe5'])
'Threats from: Nf6, Qxe5'
```

```python
>>> format_threat_descriptions([])
'No active threats'
```

