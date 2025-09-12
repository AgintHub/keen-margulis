from ._analyze_chart_performance.validate_chart_data import validate_chart_data
from ._analyze_chart_performance.analyze_performance_trends import analyze_performance_trends
from ._analyze_chart_performance.extract_peak_positions import extract_peak_positions

from pydantic import BaseModel, Field
from typing import List


class GatherTaylorSwiftDataOutput(BaseModel):
    """Pydantic model for gather_taylor_swift_data node outputs."""
    album_names: List[str] = Field(..., description="List of Taylor Swift's album names")
    release_dates: List[str] = Field(..., description="List of release dates corresponding to the albums")
    song_lyrics: List[str] = Field(..., description="List of song lyrics from Taylor Swift's discography")
    chart_performance: List[int] = Field(..., description="List of chart performance metrics for Taylor Swift's songs")


class AnalyzeChartPerformanceOutput(BaseModel):
    """Pydantic model for analyze_chart_performance node outputs."""
    chart_trends: List[str] = Field(..., description="List of trends observed in chart performance")
    peak_positions: List[int] = Field(..., description="List of peak chart positions for each song")


def analyze_chart_performance(gather_taylor_swift_data_input: GatherTaylorSwiftDataOutput, **kwargs) -> AnalyzeChartPerformanceOutput:
    """
    Analyze chart performance data to identify trends and peak positions.

    Parameters
    ----------
    chart_performance_data : List[int]
        List of chart performance metrics for Taylor Swift's songs, obtained
        from the 'gather_taylor_swift_data' node.

    Returns
    -------
    {'chart_trends': List[str], 'peak_positions': List[int]}
        A dictionary containing a list of trends observed in chart
        performance and a list of peak chart positions for each song.

    Raises
    ------
    ValueError
        If the input chart performance data is empty or malformed.

    Examples
    --------
    >>> chart_performance_data = [10, 5, 1, 8, 3]
    >>> result = analyze_chart_performance(chart_performance_data)
    >>> print(result)
    {'chart_trends': ['Increasing trend', 'Decreasing trend'], 'peak_positions':
    [1, 3, 5, 8, 10]}

    >>> chart_performance_data = [20, 15, 10, 5]
    >>> result = analyze_chart_performance(chart_performance_data)
    >>> print(result)
    {'chart_trends': ['Decreasing trend'], 'peak_positions': [5, 10, 15, 20]}

    """
    chart_data: List[int] = gather_taylor_swift_data_input.chart_performance
    
    validated_data: List[int] = validate_chart_data(data=chart_data)
    
    trend_analysis: List[str] = analyze_performance_trends(chart_positions=validated_data)
    
    peak_positions: List[int] = extract_peak_positions(chart_positions=validated_data)
    
    return AnalyzeChartPerformanceOutput(
        chart_trends=trend_analysis,
        peak_positions=peak_positions
    )