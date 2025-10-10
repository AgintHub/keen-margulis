from ._generate_trading_signals.validate_input_lengths import validate_input_lengths
from ._generate_trading_signals.validate_input_types import validate_input_types
from ._generate_trading_signals.process_recommended_strategies import process_recommended_strategies
from ._generate_trading_signals.calculate_signal_confidence import calculate_signal_confidence

from ._generate_trading_signals.validate_input_lengths import validate_input_lengths
from ._generate_trading_signals.validate_input_types import validate_input_types
from ._generate_trading_signals.process_recommended_strategies import process_recommended_strategies
from ._generate_trading_signals.calculate_signal_confidence import calculate_signal_confidence

from pydantic import BaseModel, Field
from typing import List


class EvaluateTradingStrategiesOutput(BaseModel):
    """Pydantic model for evaluate_trading_strategies node outputs."""
    strategy_evaluations: List[str] = (
        Field(..., description="Evaluations of different trading strategies")
    )
    recommended_strategies: List[str] = (
        Field(..., description = (
            "Recommended trading strategies based on the evaluations")
        )
    )


class GenerateTradingSignalsOutput(BaseModel):
    """Pydantic model for generate_trading_signals node outputs."""
    trading_signals: List[str] = (
        Field(..., description="Generated trading signals")
    )
    signal_confidence: List[float] = (
        Field(..., description = (
            "Confidence levels for the generated trading signals")
        )
    )


def generate_trading_signals(evaluate_trading_strategies_input: EvaluateTradingStrategiesOutput, **kwargs) -> GenerateTradingSignalsOutput:
    """
    Generate trading signals and their confidence levels based on recommended
    strategies.

    Parameters
    ----------
    strategy_evaluations : List[str]
        Evaluations of different trading strategies from the parent node
        'evaluate_trading_strategies'.
    recommended_strategies : List[str]
        Recommended trading strategies based on the evaluations from the
        parent node 'evaluate_trading_strategies'.

    Returns
    -------
    Tuple[List[str], List[float]]
        A tuple containing a list of generated trading signals and a list of
        their corresponding confidence levels.

    Raises
    ------
    ValueError
        If the input lists 'strategy_evaluations' and
        'recommended_strategies' are of different lengths.
    TypeError
        If the input lists contain elements of incorrect types.

    Examples
    --------
    >>> strategy_evaluations = ['good', 'bad', 'neutral']
    >>> recommended_strategies = ['buy', 'sell', 'hold']
    >>> trading_signals, signal_confidence =
    generate_trading_signals(strategy_evaluations, recommended_strategies)
    (['buy', 'sell', 'hold'], [0.8, 0.7, 0.9])

    >>> strategy_evaluations = ['excellent', 'poor']
    >>> recommended_strategies = ['buy', 'sell']
    >>> trading_signals, signal_confidence =
    generate_trading_signals(strategy_evaluations, recommended_strategies)
    (['buy', 'sell'], [0.9, 0.6])

    """
    validate_input_lengths(evaluations=evaluate_trading_strategies_input.strategy_evaluations, strategies=evaluate_trading_strategies_input.recommended_strategies)
    validate_input_types(evaluations=evaluate_trading_strategies_input.strategy_evaluations, strategies=evaluate_trading_strategies_input.recommended_strategies)
    
    trading_signals: List[str] = process_recommended_strategies(strategies=evaluate_trading_strategies_input.recommended_strategies)
    confidence_levels: List[float] = calculate_signal_confidence(evaluations=evaluate_trading_strategies_input.strategy_evaluations, strategies=evaluate_trading_strategies_input.recommended_strategies)
    
    return GenerateTradingSignalsOutput(
        trading_signals=trading_signals,
        signal_confidence=confidence_levels
    )