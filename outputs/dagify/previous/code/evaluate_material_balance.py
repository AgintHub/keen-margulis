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


class EvaluateMaterialBalanceOutput(BaseModel):
    """Pydantic model for evaluate_material_balance node outputs."""
    material_score: float = (
        Field(..., description="Material score indicating advantage")
    )
    piece_counts: int = (
        Field(..., description="Count of each piece type for both sides")
    )


def evaluate_material_balance(parse_chess_position_input: ParseChessPositionOutput, **kwargs) -> EvaluateMaterialBalanceOutput:
    """
    Evaluates the material balance in a chess position based on piece positions.

    Parameters
    ----------
    piece_positions : List[str]
        Positions of all pieces on the board, obtained from
        parse_chess_position.

    Returns
    -------
    Tuple[float, List[int]]
        A tuple containing the material score (float) and the count of each
        piece type for both sides (List[int]).

    Raises
    ------
    ValueError
        If the input piece_positions are invalid or not in the expected
        format.

    Examples
    --------
    >>> piece_positions = ['e2', 'e4', 'Nb1', 'c3']
    >>> result = evaluate_material_balance(piece_positions)
    (0.5, [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0])

    >>> piece_positions = ['d2', 'd4', 'd7', 'd5']
    >>> result = evaluate_material_balance(piece_positions)
    (0.0, [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0])

    """
    return EvaluateMaterialBalanceOutput(
        material_score=0.0,
        piece_counts=0,
    )