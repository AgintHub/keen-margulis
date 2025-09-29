from ._parse_chess_position.validate_fen_notation import validate_fen_notation
from ._parse_chess_position.split_fen_components import split_fen_components
from ._parse_chess_position.extract_piece_positions import extract_piece_positions
from ._parse_chess_position.parse_side_to_move import parse_side_to_move
from ._parse_chess_position.parse_castling_rights import parse_castling_rights
from ._parse_chess_position.parse_en_passant_square import parse_en_passant_square

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
    validated_fen: str = validate_fen_notation(fen=general_input)
    fen_parts: List[str] = split_fen_components(fen=validated_fen)
    piece_positions: List[str] = extract_piece_positions(board_section=fen_parts[0])
    side_to_move: str = parse_side_to_move(side_section=fen_parts[1])
    castling_rights: List[bool] = parse_castling_rights(castling_section=fen_parts[2])
    en_passant_square: str = parse_en_passant_square(en_passant_section=fen_parts[3])
    return ParseChessPositionOutput(
        piece_positions=piece_positions,
        castling_rights=castling_rights,
        en_passant_square=en_passant_square,
        side_to_move=side_to_move
    )