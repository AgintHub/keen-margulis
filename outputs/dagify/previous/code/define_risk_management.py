from pydantic import BaseModel, Field
from typing import List


class AssessRiskOutput(BaseModel):
    """Pydantic model for assess_risk node outputs."""
    risk_levels: List[float] = (
        Field(..., description="List of risk levels associated with potential trades.")
    )
    risk_factors: List[str] = (
        Field(..., description="List of factors contributing to the risk assessment.")
    )


class DefineRiskManagementOutput(BaseModel):
    """Pydantic model for define_risk_management node outputs."""
    stop_loss_levels: List[float] = (
        Field(..., description="List of stop-loss levels for trades.")
    )
    position_sizing: List[float] = (
        Field(..., description="List of position sizes for trades.")
    )


def define_risk_management(assess_risk_input: AssessRiskOutput, **kwargs) -> DefineRiskManagementOutput:
    """
    Defines risk management strategies based on risk assessment.

    Parameters
    ----------
    risk_levels : List[float]
        List of risk levels associated with potential trades from the
        'assess_risk' node.
    risk_factors : List[str]
        List of factors contributing to the risk assessment from the
        'assess_risk' node.

    Returns
    -------
    {'stop_loss_levels': List[float], 'position_sizing': List[float]}
        A dictionary containing lists of stop-loss levels and position sizes
        for trades.

    Raises
    ------
    ValueError
        If risk_levels or risk_factors are empty or not of the correct type.

    Examples
    --------
    >>> risk_levels = [0.5, 0.7, 0.3]
    >>> risk_factors = ['market_volatility', 'economic_indicators']
    >>> result = define_risk_management(risk_levels, risk_factors)
    {'stop_loss_levels': [0.4, 0.6, 0.2], 'position_sizing': [0.1, 0.2, 0.3]}

    >>> risk_levels = [0.2, 0.9]
    >>> risk_factors = ['geopolitical_events']
    >>> result = define_risk_management(risk_levels, risk_factors)
    {'stop_loss_levels': [0.1, 0.8], 'position_sizing': [0.05, 0.15]}

    """
    return DefineRiskManagementOutput(
        stop_loss_levels=[],
        position_sizing=[],
    )