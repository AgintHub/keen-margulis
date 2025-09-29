from ._generate_stock_insights.validate_input_data import validate_input_data
from ._generate_stock_insights.analyze_trend_signals import analyze_trend_signals
from ._generate_stock_insights.analyze_technical_indicators import analyze_technical_indicators
from ._generate_stock_insights.assess_risk_factors import assess_risk_factors
from ._generate_stock_insights.generate_investment_recommendations import generate_investment_recommendations
from ._generate_stock_insights.calculate_risk_assessment import calculate_risk_assessment
from ._generate_stock_insights.calculate_confidence_score import calculate_confidence_score

from pydantic import BaseModel, Field
from typing import List


class AnalyzeStockTrendsOutput(BaseModel):
    """Pydantic model for analyze_stock_trends node outputs."""
    trend_analysis: List[str] = (
        Field(..., description="List of identified trends and patterns")
    )
    anomaly_detected: bool = (
        Field(..., description="Whether any anomalies were detected")
    )


class CalculateStockMetricsOutput(BaseModel):
    """Pydantic model for calculate_stock_metrics node outputs."""
    moving_averages: List[float] = (
        Field(..., description="Moving averages for the stock prices.")
    )
    rsi_values: List[float] = (
        Field(..., description="Relative Strength Index values.")
    )
    volatility: float = (
        Field(..., description="Stock price volatility measure.")
    )


class GenerateStockInsightsOutput(BaseModel):
    """Pydantic model for generate_stock_insights node outputs."""
    investment_recommendations: List[str] = (
        Field(..., description="List of investment recommendations based on the analysis")
    )
    risk_assessment: str = (
        Field(..., description="Assessment of the investment risk")
    )
    confidence_score: float = (
        Field(..., description="Confidence score in the investment recommendations")
    )


def generate_stock_insights(analyze_stock_trends_input: AnalyzeStockTrendsOutput, calculate_stock_metrics_input: CalculateStockMetricsOutput, **kwargs) -> GenerateStockInsightsOutput:
    """
    Generate investment recommendations, risk assessment, and confidence score
    based on stock trend analysis and metrics.

    Parameters
    ----------
    trend_analysis : List[str]
        List of identified trends and patterns from stock data analysis.
    anomaly_detected : bool
        Whether any anomalies were detected in the stock data.
    moving_averages : List[float]
        Moving averages for the stock prices.
    rsi_values : List[float]
        Relative Strength Index values for the stock.
    volatility : float
        Stock price volatility measure.

    Returns
    -------
    Tuple[List[str], str, float]
        A tuple containing investment recommendations, risk assessment, and
        confidence score.

    Raises
    ------
    ValueError
        If input data is inconsistent or missing required fields.

    Examples
    --------
    >>> trend_analysis = ['uptrend', 'bullish']
    >>> anomaly_detected = False
    >>> moving_averages = [100.0, 120.0]
    >>> rsi_values = [30.0, 40.0]
    >>> volatility = 0.05
    >>> generate_stock_insights(trend_analysis, anomaly_detected,
    moving_averages, rsi_values, volatility)
    (['Buy', 'Hold'], 'Low', 0.8)

    >>> trend_analysis = ['downtrend']
    >>> anomaly_detected = True
    >>> moving_averages = [80.0, 70.0]
    >>> rsi_values = [70.0, 80.0]
    >>> volatility = 0.1
    >>> generate_stock_insights(trend_analysis, anomaly_detected,
    moving_averages, rsi_values, volatility)
    (['Sell'], 'High', 0.6)

    """
    validate_input_data(trends=analyze_stock_trends_input.trend_analysis, 
                         moving_averages=calculate_stock_metrics_input.moving_averages,
                         rsi_values=calculate_stock_metrics_input.rsi_values,
                         volatility=calculate_stock_metrics_input.volatility)
    
    trend_signals: List[str] = analyze_trend_signals(trends=analyze_stock_trends_input.trend_analysis)
    
    technical_signals: List[str] = analyze_technical_indicators(moving_averages=calculate_stock_metrics_input.moving_averages,
                                                                  rsi_values=calculate_stock_metrics_input.rsi_values)
    
    risk_factors: List[str] = assess_risk_factors(anomaly_detected=analyze_stock_trends_input.anomaly_detected,
                                                    volatility=calculate_stock_metrics_input.volatility,
                                                    rsi_values=calculate_stock_metrics_input.rsi_values)
    
    investment_recommendations: List[str] = generate_investment_recommendations(trend_signals=trend_signals,
                                                                                 technical_signals=technical_signals,
                                                                                 risk_factors=risk_factors)
    
    risk_assessment: str = calculate_risk_assessment(risk_factors=risk_factors,
                                                       volatility=calculate_stock_metrics_input.volatility,
                                                       anomaly_detected=analyze_stock_trends_input.anomaly_detected)
    
    confidence_score: float = calculate_confidence_score(trend_analysis=analyze_stock_trends_input.trend_analysis,
                                                           moving_averages=calculate_stock_metrics_input.moving_averages,
                                                           rsi_values=calculate_stock_metrics_input.rsi_values,
                                                           volatility=calculate_stock_metrics_input.volatility,
                                                           anomaly_detected=analyze_stock_trends_input.anomaly_detected)
    
    return GenerateStockInsightsOutput(
        investment_recommendations=investment_recommendations,
        risk_assessment=risk_assessment,
        confidence_score=confidence_score
    )