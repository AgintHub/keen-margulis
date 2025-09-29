from ._assess_king_safety.validate_piece_positions import validate_piece_positions
from ._assess_king_safety.find_king_positions import find_king_positions
from ._assess_king_safety.get_current_side_king import get_current_side_king
from ._assess_king_safety.identify_attacking_pieces import identify_attacking_pieces
from ._assess_king_safety.evaluate_castling_safety import evaluate_castling_safety
from ._assess_king_safety.evaluate_pawn_shield import evaluate_pawn_shield
from ._assess_king_safety.calculate_threat_proximity import calculate_threat_proximity
from ._assess_king_safety.evaluate_en_passant_threat import evaluate_en_passant_threat
from ._assess_king_safety.calculate_final_safety_score import calculate_final_safety_score
from ._assess_king_safety.format_threat_descriptions import format_threat_descriptions

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
    validated_positions: List[str] = validate_piece_positions(positions=parse_chess_position_input.piece_positions)
    
    king_positions: List[str] = find_king_positions(piece_positions=validated_positions)
    
    current_side_king: str = get_current_side_king(king_positions=king_positions, side_to_move=parse_chess_position_input.side_to_move)
    
    attacking_pieces: List[str] = identify_attacking_pieces(piece_positions=validated_positions, target_king=current_side_king, side_to_move=parse_chess_position_input.side_to_move)
    
    castling_safety_bonus: float = evaluate_castling_safety(castling_rights=parse_chess_position_input.castling_rights, side_to_move=parse_chess_position_input.side_to_move)
    
    pawn_shield_score: float = evaluate_pawn_shield(piece_positions=validated_positions, king_position=current_side_king, side_to_move=parse_chess_position_input.side_to_move)
    
    threat_proximity_score: float = calculate_threat_proximity(attacking_pieces=attacking_pieces, king_position=current_side_king)
    
    en_passant_threat: float = evaluate_en_passant_threat(en_passant_square=parse_chess_position_input.en_passant_square, king_position=current_side_king)
    
    final_safety_score: float = calculate_final_safety_score(castling_bonus=castling_safety_bonus, pawn_shield=pawn_shield_score, threat_proximity=threat_proximity_score, en_passant_threat=en_passant_threat)
    
    threat_descriptions: str = format_threat_descriptions(attacking_pieces=attacking_pieces)
    
    return AssessKingSafetyOutput(king_safety_score=final_safety_score, threats=threat_descriptions)