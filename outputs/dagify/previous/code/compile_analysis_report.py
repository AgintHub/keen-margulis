from ._compile_analysis_report.validate_input_parameters import validate_input_parameters
from ._compile_analysis_report.count_sentiment_categories import count_sentiment_categories
from ._compile_analysis_report.generate_sentiment_summary import generate_sentiment_summary
from ._compile_analysis_report.generate_trend_summary import generate_trend_summary
from ._compile_analysis_report.generate_full_report import generate_full_report
from ._compile_analysis_report.validate_report_completion import validate_report_completion

from pydantic import BaseModel, Field
from typing import List


class AnalyzeSentimentOutput(BaseModel):
    """Pydantic model for analyze_sentiment node outputs."""
    article_index: List[int] = (
        Field(..., description = (
            "The sequential index of each article in the input list.")
        )
    )
    sentiment_category: List[str] = (
        Field(..., description = (
            "Sentiment category for each article, one of 'positive', 'negative', or 'neutral'.")
        )
    )
    sentiment_confidence: List[float] = (
        Field(..., description = (
            "Confidence score (0.0 to 1.0) for the assigned sentiment.")
        )
    )


class IdentifyTrendsOutput(BaseModel):
    """Pydantic model for identify_trends node outputs."""
    trending_topics: List[str] = (
        Field(..., description = (
            "List of topics that show a trend across the news articles.")
        )
    )
    sentiment_trends: List[str] = (
        Field(..., description = (
            "Sentiment trend for each corresponding trending topic, e.g., 'increasing positive', 'decreasing negative', or 'stable neutral'.")
        )
    )
    overall_trend_summary: str = (
        Field(..., description = (
            "A concise textual summary of the overall trend patterns identified.")
        )
    )


class CompileAnalysisReportOutput(BaseModel):
    """Pydantic model for compile_analysis_report node outputs."""
    report_text: str = (
        Field(..., description = (
            "Full textual analysis report combining sentiment and trend insights.")
        )
    )
    sentiment_summary: str = (
        Field(..., description = (
            "Brief summary of overall sentiment distribution (positive/negative/neutral).")
        )
    )
    trend_summary: str = (
        Field(..., description = (
            "Brief summary of key trends identified across articles.")
        )
    )
    sentiment_per_article: List[str] = (
        Field(..., description = (
            "Sentiment category for each article in the order processed.")
        )
    )
    trend_topics: List[str] = (
        Field(..., description = (
            "List of trending topics or themes identified in the articles.")
        )
    )
    article_count: int = (
        Field(..., description = (
            "Total number of articles included in the analysis.")
        )
    )
    is_valid: bool = (
        Field(..., description = (
            "Flag indicating whether the report was generated successfully.")
        )
    )


def compile_analysis_report(analyze_sentiment_input: AnalyzeSentimentOutput, identify_trends_input: IdentifyTrendsOutput, **kwargs) -> CompileAnalysisReportOutput:
    """
    Generate a comprehensive analysis report from sentiment and trend data.

    Parameters
    ----------
    sentiment_category : List[str]
        Sentiment label for each article ('positive', 'negative',
        'neutral').
    sentiment_confidence : List[float]
        Confidence score (0.0–1.0) for each article's sentiment.
    trending_topics : List[str]
        List of topics that exhibit a trend across the articles.
    sentiment_trends : List[str]
        Sentiment trend description for each corresponding trending topic.
    overall_trend_summary : str
        Concise textual summary of the overall trend patterns identified.

    Returns
    -------
    Dict[str, Any]
        Dictionary containing the full report text, sentiment and trend
        summaries, per‑article sentiment list, trend topics list, article
        count, and validity flag.

    Raises
    ------
    ValueError
        If the lengths of `sentiment_category` and `sentiment_confidence` do
        not match, or if `trending_topics` and `sentiment_trends` differ in
        length.
    TypeError
        If any input parameter is of an unexpected type.

    Examples
    --------
    >>> sentiment_category = ['positive', 'neutral', 'negative'],
    >>> sentiment_confidence = [0.92, 0.85, 0.78],
    >>> trending_topics = ['Climate Action', 'Tech Innovation'],
    >>> sentiment_trends = ['decreasing positive', 'increasing positive'],
    >>> overall_trend_summary = 'The overall sentiment is shifting from positive
    to more neutral, with rising excitement around tech.'
    >>> report = compile_analysis_report(sentiment_category,
    sentiment_confidence, trending_topics, sentiment_trends,
    overall_trend_summary)
    {
      'report_text': 'Analysis Report:\n\nSentiment:\n- Positive: 1\n- Neutral:
    1\n- Negative: 1\n\nTrends:\n- Climate Action: decreasing positive\n- Tech
    Innovation: increasing positive\n\nOverall Trend: The overall sentiment is
    shifting from positive to more neutral, with rising excitement around
    tech.',
      'sentiment_summary': '1 positive, 1 neutral, 1 negative',
      'trend_summary': 'Climate Action shows decreasing positivity while Tech
    Innovation is gaining traction.',
      'sentiment_per_article': ['positive', 'neutral', 'negative'],
      'trend_topics': ['Climate Action', 'Tech Innovation'],
      'article_count': 3,
      'is_valid': True
    }

    """
    validate_input_parameters(sentiment_data=analyze_sentiment_input, trends_data=identify_trends_input)
    
    sentiment_counts: dict = count_sentiment_categories(sentiment_categories=analyze_sentiment_input.sentiment_category)
    
    sentiment_summary_text: str = generate_sentiment_summary(sentiment_counts=sentiment_counts)
    
    trend_summary_text: str = generate_trend_summary(trending_topics=identify_trends_input.trending_topics, sentiment_trends=identify_trends_input.sentiment_trends)
    
    full_report_text: str = generate_full_report(sentiment_summary=sentiment_summary_text, trend_summary=trend_summary_text, overall_trend_summary=identify_trends_input.overall_trend_summary, sentiment_counts=sentiment_counts, trending_topics=identify_trends_input.trending_topics, sentiment_trends=identify_trends_input.sentiment_trends)
    
    article_count: int = len(analyze_sentiment_input.sentiment_category)
    
    is_valid_report: bool = validate_report_completion(report_text=full_report_text, article_count=article_count)
    
    return CompileAnalysisReportOutput(
        report_text=full_report_text,
        sentiment_summary=sentiment_summary_text,
        trend_summary=trend_summary_text,
        sentiment_per_article=analyze_sentiment_input.sentiment_category,
        trend_topics=identify_trends_input.trending_topics,
        article_count=article_count,
        is_valid=is_valid_report
    )