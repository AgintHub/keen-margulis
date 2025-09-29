from pydantic import BaseModel, Field
from typing import List


class EvaluateMaterialBalanceOutput(BaseModel):
    """Pydantic model for evaluate_material_balance node outputs."""
    material_score: float = (
        Field(..., description="Material score indicating advantage")
    )
    piece_counts: int = (
        Field(..., description="Count of each piece type for both sides")
    )


class AnalyzePawnStructureOutput(BaseModel):
    """Pydantic model for analyze_pawn_structure node outputs."""
    pawn_chain_analysis: List[str] = (
        Field(..., description="Analysis of pawn chains and their implications.")
    )
    isolated_pawns: List[str] = (
        Field(..., description="Positions of isolated pawns.")
    )
    passed_pawns: List[str] = (
        Field(..., description="Positions of passed pawns.")
    )


class AssessKingSafetyOutput(BaseModel):
    """Pydantic model for assess_king_safety node outputs."""
    king_safety_score: float = (
        Field(..., description="Score indicating king safety")
    )
    threats: str = Field(..., description="Potential threats to the kings")


class SynthesizeAnalysisOutput(BaseModel):
    """Pydantic model for synthesize_analysis node outputs."""
    overall_evaluation: str = (
        Field(..., description="Overall assessment of the position")
    )
    strategic_recommendations: List[str] = (
        Field(..., description="Strategic recommendations based on the analysis")
    )
    tactical_opportunities: List[str] = (
        Field(..., description="Tactical opportunities or threats identified")
    )


def synthesize_analysis(evaluate_material_balance_input: EvaluateMaterialBalanceOutput, analyze_pawn_structure_input: AnalyzePawnStructureOutput, assess_king_safety_input: AssessKingSafetyOutput, **kwargs) -> SynthesizeAnalysisOutput:
    """
    Synthesizes findings from various analyses into a comprehensive evaluation
    of the chess position.

    Parameters
    ----------
    material_balance : dict
        Output from evaluate_material_balance containing material_score and
        piece_counts.
    pawn_structure_analysis : dict
        Output from analyze_pawn_structure containing pawn_chain_analysis,
        isolated_pawns, and passed_pawns.
    king_safety_assessment : dict
        Output from assess_king_safety containing king_safety_score and
        threats.

    Returns
    -------
    dict
        A dictionary containing overall_evaluation,
        strategic_recommendations, and tactical_opportunities.

    Raises
    ------
    ValueError
        If any of the input analyses are missing or malformed.

    Examples
    --------
    >>> material_balance = {'material_score': 0.5, 'piece_counts': [1, 2, 3, 4,
    5, 6]}
    >>> pawn_structure_analysis = {'pawn_chain_analysis': ['strong'],
    'isolated_pawns': ['e4'], 'passed_pawns': ['d5']}
    >>> king_safety_assessment = {'king_safety_score': 0.8, 'threats':
    ['checkmate']}
    >>> synthesize_analysis(material_balance, pawn_structure_analysis,
    king_safety_assessment)
    {'overall_evaluation': 'White has a slight advantage',
    'strategic_recommendations': ['Control the center', 'Develop pieces'],
    'tactical_opportunities': ['Attack weak pawns']}

    """
    return SynthesizeAnalysisOutput(
        overall_evaluation="",
        strategic_recommendations=[],
        tactical_opportunities=[],
    )