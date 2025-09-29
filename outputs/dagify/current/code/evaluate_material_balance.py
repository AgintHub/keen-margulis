from ._evaluate_material_balance.validate_piece_positions import validate_piece_positions
from ._evaluate_material_balance.extract_white_pieces import extract_white_pieces
from ._evaluate_material_balance.extract_black_pieces import extract_black_pieces
from ._evaluate_material_balance.count_pieces_by_type import count_pieces_by_type
from ._evaluate_material_balance.calculate_material_value import calculate_material_value
from ._evaluate_material_balance.compute_material_score import compute_material_score
from ._evaluate_material_balance.combine_piece_counts import combine_piece_counts

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
    validated_positions: List[str] = validate_piece_positions(piece_positions=parse_chess_position_input.piece_positions)
    
    white_pieces: List[str] = extract_white_pieces(piece_positions=validated_positions)
    black_pieces: List[str] = extract_black_pieces(piece_positions=validated_positions)
    
    white_piece_counts: List[int] = count_pieces_by_type(pieces=white_pieces)
    black_piece_counts: List[int] = count_pieces_by_type(pieces=black_pieces)
    
    white_material_value: float = calculate_material_value(piece_counts=white_piece_counts)
    black_material_value: float = calculate_material_value(piece_counts=black_piece_counts)
    
    material_score: float = compute_material_score(white_value=white_material_value, black_value=black_material_value)
    
    combined_piece_counts: List[int] = combine_piece_counts(white_counts=white_piece_counts, black_counts=black_piece_counts)
    
    return EvaluateMaterialBalanceOutput(
        material_score=material_score,
        piece_counts=combined_piece_counts
    )