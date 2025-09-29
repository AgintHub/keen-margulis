from ._analyze_pawn_structure.validate_input import validate_input
from ._analyze_pawn_structure.extract_pawn_positions import extract_pawn_positions
from ._analyze_pawn_structure.identify_pawn_chains import identify_pawn_chains
from ._analyze_pawn_structure.analyze_pawn_chains import analyze_pawn_chains
from ._analyze_pawn_structure.find_isolated_pawns import find_isolated_pawns
from ._analyze_pawn_structure.find_passed_pawns import find_passed_pawns

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


class AnalyzePawnStructureOutput(BaseModel):
    """Pydantic model for analyze_pawn_structure node outputs."""
    pawn_chain_analysis: List[str] = (
        Field(..., description = (
            "Analysis of pawn chains and their implications.")
        )
    )
    isolated_pawns: List[str] = (
        Field(..., description="Positions of isolated pawns.")
    )
    passed_pawns: List[str] = (
        Field(..., description="Positions of passed pawns.")
    )


def analyze_pawn_structure(parse_chess_position_input: ParseChessPositionOutput, **kwargs) -> AnalyzePawnStructureOutput:
    """
    Analyze the pawn structure from the parsed chess position.

    Parameters
    ----------
    piece_positions : List[str]
        Positions of all pieces on the board, provided by the
        parse_chess_position node.
    side_to_move : str
        Side to move (white or black), provided by the parse_chess_position
        node.

    Returns
    -------
    Tuple[List[str], List[str], List[str]]
        A tuple containing the analysis of pawn chains, positions of
        isolated pawns, and positions of passed pawns.

    Raises
    ------
    ValueError
        If the piece_positions list is empty or if side_to_move is not
        'white' or 'black'.

    Examples
    --------
    >>> piece_positions = ['e2', 'e4', 'd4', 'c3']
    >>> side_to_move = 'white'
    >>> result = analyze_pawn_structure(piece_positions, side_to_move)
    (['Pawn chain on d4 and c3 is strong'], ['b2'], ['e4'])

    >>> piece_positions = ['e7', 'd5', 'c6']
    >>> side_to_move = 'black'
    >>> result = analyze_pawn_structure(piece_positions, side_to_move)
    (['Pawn chain on d5 and c6 is flexible'], ['a7'], ['d5'])

    """
    validate_input(piece_positions=parse_chess_position_input.piece_positions, side_to_move=parse_chess_position_input.side_to_move)
    
    pawn_positions: List[str] = extract_pawn_positions(piece_positions=parse_chess_position_input.piece_positions, side=parse_chess_position_input.side_to_move)
    
    pawn_chains: List[str] = identify_pawn_chains(pawn_positions=pawn_positions)
    chain_analysis: List[str] = analyze_pawn_chains(pawn_chains=pawn_chains)
    
    isolated_pawn_positions: List[str] = find_isolated_pawns(pawn_positions=pawn_positions)
    
    passed_pawn_positions: List[str] = find_passed_pawns(pawn_positions=pawn_positions, all_piece_positions=parse_chess_position_input.piece_positions, side=parse_chess_position_input.side_to_move)
    
    return AnalyzePawnStructureOutput(
        pawn_chain_analysis=chain_analysis,
        isolated_pawns=isolated_pawn_positions,
        passed_pawns=passed_pawn_positions
    )