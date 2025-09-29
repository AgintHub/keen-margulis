from pydantic import BaseModel, Field
from typing import List


class ParseChessPositionOutput(BaseModel):
    """Pydantic model for parse_chess_position node outputs."""
    piece_positions: List[str] = (
        Field(..., description="Positions of all pieces on the board")
    )
    castling_rights: List[bool] = (
        Field(..., description="Castling rights for both white and black")
    )
    en_passant_square: str = (
        Field(..., description="En passant square if available")
    )
    side_to_move: str = Field(..., description="Side to move (white or black)")


class AssessKingSafetyOutput(BaseModel):
    """Pydantic model for assess_king_safety node outputs."""
    king_safety_score: float = (
        Field(..., description="Score indicating king safety")
    )
    threats: str = Field(..., description="Potential threats to the kings")


def assess_king_safety(parse_chess_position_input: ParseChessPositionOutput, **kwargs) -> AssessKingSafetyOutput:
    """
    Assess king safety based on position and threats.

    Parameters
    ----------
    piece_positions : List[str]
        Positions of all pieces on the board from parse_chess_position.
    castling_rights : List[bool]
        Castling rights for both white and black from parse_chess_position.
    en_passant_square : str
        En passant square if available from parse_chess_position.
    side_to_move : str
        Side to move (white or black) from parse_chess_position.

    Returns
    -------
    Tuple[float, List[str]]
        A tuple containing the king safety score and a list of potential
        threats.

    Raises
    ------
    ValueError
        If piece_positions is not a valid list of chess positions.

    Examples
    --------
    >>> piece_positions = ['e1', 'e8', 'e2', 'e7']
    >>> castling_rights = [True, False]
    >>> en_passant_square = 'e3'
    >>> side_to_move = 'white'
    >>> result = assess_king_safety(piece_positions, castling_rights,
    en_passant_square, side_to_move)
    (0.7, ['Queen on d5', 'Knight on f3'])

    >>> piece_positions = ['e1', 'e8', 'd4', 'd5']
    >>> castling_rights = [False, True]
    >>> en_passant_square = None
    >>> side_to_move = 'black'
    >>> result = assess_king_safety(piece_positions, castling_rights,
    en_passant_square, side_to_move)
    (0.4, ['Rook on e1', 'Bishop on c4'])

    """
    return AssessKingSafetyOutput(
        king_safety_score=0.0,
        threats="",
    )