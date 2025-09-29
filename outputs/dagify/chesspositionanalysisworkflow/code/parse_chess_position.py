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


def parse_chess_position(general_input: str, **kwargs) -> ParseChessPositionOutput:
    """
    Parses a given chess position in standard algebraic notation (FEN) into a
    structured format.

    Parameters
    ----------
    fen_notation : str
        The chess position in FEN notation to be parsed.

    Returns
    -------
    dict
        A dictionary containing piece positions, castling rights, en passant
        square, and side to move.

    Raises
    ------
    ValueError
        If the input FEN notation is invalid or malformed.

    Examples
    --------
    >>> fen_notation = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0
    1'
    >>> parse_chess_position(fen_notation)
    {'piece_positions': ['e2', 'e4', ...], 'castling_rights': [true, true],
    'en_passant_square': 'e3', 'side_to_move': 'white'}

    >>> fen_notation = '8/8/8/8/8/8/8/8 b - - 0 1'
    >>> parse_chess_position(fen_notation)
    {'piece_positions': [], 'castling_rights': [false, false],
    'en_passant_square': None, 'side_to_move': 'black'}

    """
    return ParseChessPositionOutput(
        piece_positions=[],
        castling_rights=[],
        en_passant_square="",
        side_to_move="",
    )