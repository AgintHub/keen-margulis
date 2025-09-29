from ._generate_trading_signals.validate_trading_parameters import validate_trading_parameters
from ._generate_trading_signals.validate_trading_opportunities import validate_trading_opportunities
from ._generate_trading_signals.parse_trading_opportunities import parse_trading_opportunities
from ._generate_trading_signals.calculate_signal_details import calculate_signal_details
from ._generate_trading_signals.format_trading_signal import format_trading_signal

from pydantic import BaseModel, Field
from typing import List


class DetermineTradingParametersOutput(BaseModel):
    """Pydantic model for determine_trading_parameters node outputs."""
    risk_tolerance: float = (
        Field(..., description="Risk tolerance level between 0 and 1")
    )
    position_sizing: float = (
        Field(..., description="Position sizing strategy as a proportion of account balance")
    )


class IdentifyTradingOpportunitiesOutput(BaseModel):
    """Pydantic model for identify_trading_opportunities node outputs."""
    trading_opportunities: List[str] = (
        Field(..., description="List of potential trading opportunities")
    )


class GenerateTradingSignalsOutput(BaseModel):
    """Pydantic model for generate_trading_signals node outputs."""
    trading_signals: List[str] = (
        Field(..., description="List of trading signals")
    )


def generate_trading_signals(determine_trading_parameters_input: DetermineTradingParametersOutput, identify_trading_opportunities_input: IdentifyTradingOpportunitiesOutput, **kwargs) -> GenerateTradingSignalsOutput:
    """
    Generate trading signals including buy/sell orders based on trading
    parameters and opportunities.

    Parameters
    ----------
    trading_parameters : dict
        Dictionary containing risk tolerance and position sizing strategy,
        output of 'determine_trading_parameters' node.
    trading_opportunities : List[str]
        List of potential trading opportunities, output of
        'identify_trading_opportunities' node.

    Returns
    -------
    List[str]
        List of trading signals generated based on the input parameters.

    Raises
    ------
    ValueError
        If trading parameters are invalid or trading opportunities are
        empty.

    Examples
    --------
    >>> trading_parameters = {'risk_tolerance': 0.5, 'position_sizing': 0.2}
    >>> trading_opportunities = ['buy AAPL', 'sell GOOG']
    >>> generate_trading_signals(trading_parameters, trading_opportunities)
    ['buy AAPL at 150', 'sell GOOG at 2000']

    >>> trading_parameters = {'risk_tolerance': 0.3, 'position_sizing': 0.1}
    >>> trading_opportunities = ['buy MSFT', 'sell AMZN']
    >>> generate_trading_signals(trading_parameters, trading_opportunities)
    ['buy MSFT at 200', 'sell AMZN at 3000']

    """
    validated_parameters: dict = validate_trading_parameters(risk_tolerance=determine_trading_parameters_input.risk_tolerance, position_sizing=determine_trading_parameters_input.position_sizing)
    validated_opportunities: List[str] = validate_trading_opportunities(opportunities=identify_trading_opportunities_input.trading_opportunities)
    
    parsed_opportunities: List[dict] = parse_trading_opportunities(opportunities=validated_opportunities)
    
    signal_list: List[str] = []
    for opportunity in parsed_opportunities:
        signal_details: dict = calculate_signal_details(opportunity=opportunity, risk_tolerance=validated_parameters['risk_tolerance'], position_sizing=validated_parameters['position_sizing'])
        formatted_signal: str = format_trading_signal(signal_details=signal_details)
        signal_list.append(formatted_signal)
    
    return GenerateTradingSignalsOutput(trading_signals=signal_list)