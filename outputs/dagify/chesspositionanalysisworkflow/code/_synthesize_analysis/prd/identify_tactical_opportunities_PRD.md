# identify_tactical_opportunities PRD

## Description
Identify tactical opportunities in a chess position from pawn weaknesses, passed pawns and king threats.


## Conceptual Info

This shim analyzes pawn structure weaknesses (isolated pawns), passed pawn possibilities, and direct king threats to generate actionable tactical ideas such as forks, pins, and mating nets. It acts as the tactical analysis layer within the broader synthesis pipeline.

## Docstring

### Summary
Return a list of tactical opportunities based on pawn weaknesses, passed pawns, and king threats.

### Parameters

- **pawn_weaknesses** (str): Comma‑separated list of squares containing isolated or otherwise weakened pawns.
- **passed_pawns** (str): Comma‑separated list of squares of passed pawns.
- **king_threats** (str): Comma‑separated list of squares or patterns representing direct threats to the king (e.g., potential checks, mating nets).

### Returns

List[str]: A list of descriptive strings, each describing a distinct tactical opportunity that can be pursued from the given position.

### Raises

- TypeError: Raised when any of the input parameters is not of type `str`.
- ValueError: Raised when any of the input strings is empty or cannot be parsed into a list of squares.

### Examples

```python
>>> opportunities = identify_tactical_opportunities(
...     pawn_weaknesses='c3, e5',
...     passed_pawns='g4',
...     king_threats='h7'"
              ")
>>> print(opportunities)
['Fork on c3', 'Pawn push g4+ leading to mate in 2', 'Pin on h7']
```

```python
>>> opportunities = identify_tactical_opportunities(
...     pawn_weaknesses='b2',
...     passed_pawns='h2, h3',
...     king_threats='f7'"
              ")
>>> print(opportunities)
['Double attack on b2', 'Advance h2 to h3 opening a discovered attack', 'Check on f7 from h5']
```
