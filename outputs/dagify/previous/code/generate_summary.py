from pydantic import BaseModel, Field
from typing import List


class ExtractThemesOutput(BaseModel):
    """Pydantic model for extract_themes node outputs."""
    themes: List[str] = Field(..., description="Top 5 thematic words in descending order of frequency.")
    theme_scores: List[float] = Field(..., description="Normalized frequency score for each theme (count / total word count).")


class TrendOverTimeOutput(BaseModel):
    """Pydantic model for trend_over_time node outputs."""
    years: List[int] = Field(..., description="Chronological list of years with songs.")
    avg_sentiment: List[float] = Field(..., description="Average sentiment for each year.")


class GenerateSummaryOutput(BaseModel):
    """Pydantic model for generate_summary node outputs."""
    summary_text: str = Field(..., description="Plain\u2011text summary of the analysis.")


def generate_summary(extract_themes_input: ExtractThemesOutput, trend_over_time_input: TrendOverTimeOutput, **kwargs) -> GenerateSummaryOutput:
    """
    Create a concise paragraph summarizing key lyrical themes and sentiment
    trends.

    Parameters
    ----------
    themes : List[str]
        Top 5 thematic words in descending frequency order.
    theme_scores : List[float]
        Normalized frequency score for each corresponding theme (sum of all
        scores should equal 1).
    years : List[int]
        Chronological list of release years for which sentiment averages
        have been computed.
    avg_sentiment : List[float]
        Average sentiment score for each year, aligned with the `years`
        list. Scores range from -1 (very negative) to +1 (very positive).

    Returns
    -------
    str
        A single paragraph that lists the top themes, summarizes the
        sentiment trend over time, and notes any significant pattern shifts.

    Raises
    ------
    ValueError
        If `themes` and `theme_scores` lists are of unequal length, or if
        any of the input lists are empty.
    TypeError
        If any of the parameters is not of the expected type.

    Examples
    --------
    >>> generate_summary(
    ...     themes=["love", "heartbreak", "growth", "rebellion", "dreams"],
    ...     theme_scores=[0.28, 0.22, 0.18, 0.12, 0.10],
    ...     years=[2013, 2014, 2015, 2016, 2017],
    ...     avg_sentiment=[0.15, 0.08, 0.02, -0.04, -0.10]
    >>> )
    "The analysis highlights love and heartbreak as the dominant lyrical themes,
    followed by growth, rebellion, and dreams. Sentiment shifts from mildly
    positive in 2013 to increasingly negative by 2017, indicating a noticeable
    downturn in overall lyrical mood during the latter years."

    >>> generate_summary(
    ...     themes=["hope", "rain", "silence", "journey", "home"],
    ...     theme_scores=[0.30, 0.20, 0.15, 0.12, 0.10],
    ...     years=[2012, 2013, 2014],
    ...     avg_sentiment=[0.05, 0.10, 0.15]"
                ")
    "The prevailing themes are hope, rain, silence, journey, and home. The
    sentiment trend shows a steady improvement from 2012 to 2014, suggesting an
    increasingly optimistic tone over time."

    """
    return GenerateSummaryOutput(
        summary_text="",
    )