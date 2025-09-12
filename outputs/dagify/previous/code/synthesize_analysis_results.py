from ._synthesize_analysis_results.validate_analysis_inputs import validate_analysis_inputs
from ._synthesize_analysis_results.analyze_sentiment_patterns import analyze_sentiment_patterns
from ._synthesize_analysis_results.analyze_thematic_patterns import analyze_thematic_patterns
from ._synthesize_analysis_results.analyze_performance_patterns import analyze_performance_patterns
from ._synthesize_analysis_results.synthesize_cross_analysis_insights import synthesize_cross_analysis_insights
from ._synthesize_analysis_results.generate_recommendations import generate_recommendations
from ._synthesize_analysis_results.format_overall_insights import format_overall_insights

from pydantic import BaseModel, Field
from typing import List


class AnalyzeLyricsSentimentOutput(BaseModel):
    """Pydantic model for analyze_lyrics_sentiment node outputs."""
    sentiment_scores: List[float] = Field(..., description="List of sentiment scores for each song")
    average_sentiment: float = Field(..., description="Average sentiment score across all songs")


class IdentifyCommonThemesOutput(BaseModel):
    """Pydantic model for identify_common_themes node outputs."""
    themes: List[str] = Field(..., description="List of common themes found in the lyrics")
    theme_frequencies: List[int] = Field(..., description="Frequency of occurrence for each theme")


class AnalyzeChartPerformanceOutput(BaseModel):
    """Pydantic model for analyze_chart_performance node outputs."""
    chart_trends: List[str] = Field(..., description="List of trends observed in chart performance")
    peak_positions: List[int] = Field(..., description="List of peak chart positions for each song")


class SynthesizeAnalysisResultsOutput(BaseModel):
    """Pydantic model for synthesize_analysis_results node outputs."""
    overall_insights: str = Field(..., description="Summary of key insights from the analysis")
    recommendations: List[str] = Field(..., description="List of recommendations based on the analysis findings")


def synthesize_analysis_results(analyze_lyrics_sentiment_input: AnalyzeLyricsSentimentOutput, identify_common_themes_input: IdentifyCommonThemesOutput, analyze_chart_performance_input: AnalyzeChartPerformanceOutput, **kwargs) -> SynthesizeAnalysisResultsOutput:
    """
    Synthesizes analysis results to draw conclusions about Taylor Swift's music
    and impact.

    Parameters
    ----------
    sentiment_analysis_results : dict
        Results from sentiment analysis, including sentiment scores and
        average sentiment.
    theme_identification_results : dict
        Results from theme identification, including common themes and their
        frequencies.
    chart_performance_analysis_results : dict
        Results from chart performance analysis, including chart trends and
        peak positions.

    Returns
    -------
    dict
        A dictionary containing overall insights and recommendations based
        on the analysis.

    Raises
    ------
    ValueError
        If any of the input analysis results are missing or malformed.

    Examples
    --------
    >>> sentiment_analysis_results = {'sentiment_scores': [0.8, 0.7],
    'average_sentiment': 0.75}
    >>> theme_identification_results = {'themes': ['love', 'heartbreak'],
    'theme_frequencies': [10, 5]}
    >>> chart_performance_analysis_results = {'chart_trends': ['increasing
    popularity'], 'peak_positions': [1, 2]}
    >>> result = synthesize_analysis_results(sentiment_analysis_results,
    theme_identification_results, chart_performance_analysis_results)
    {'overall_insights': 'Taylor Swift\'s music is generally positive with
    themes of love and heartbreak, and has shown increasing popularity on
    charts.', 'recommendations': ['Continue producing music with positive
    themes.', 'Explore more themes beyond love and heartbreak.']}

    """
    validate_analysis_inputs(sentiment_input=analyze_lyrics_sentiment_input, themes_input=identify_common_themes_input, chart_input=analyze_chart_performance_input)
    
    sentiment_insights: str = analyze_sentiment_patterns(sentiment_scores=analyze_lyrics_sentiment_input.sentiment_scores, average_sentiment=analyze_lyrics_sentiment_input.average_sentiment)
    
    theme_insights: str = analyze_thematic_patterns(themes=identify_common_themes_input.themes, frequencies=identify_common_themes_input.theme_frequencies)
    
    chart_insights: str = analyze_performance_patterns(trends=analyze_chart_performance_input.chart_trends, peak_positions=analyze_chart_performance_input.peak_positions)
    
    combined_insights: str = synthesize_cross_analysis_insights(sentiment_insights=sentiment_insights, theme_insights=theme_insights, chart_insights=chart_insights)
    
    recommendations: List[str] = generate_recommendations(sentiment_data=analyze_lyrics_sentiment_input, theme_data=identify_common_themes_input, chart_data=analyze_chart_performance_input)
    
    overall_insights: str = format_overall_insights(combined_insights=combined_insights)
    
    return SynthesizeAnalysisResultsOutput(
        overall_insights=overall_insights,
        recommendations=recommendations
    )