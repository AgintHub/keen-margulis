import logging
from typing import List
from pydantic import BaseModel, Field


def compile_analysis_report(
    """
    Generates a summarized analysis report from sentiment and trend data.

    Parameters
    ----------
    analyze_sentiment_input : AnalyzeSentimentOutput
        Output of the analyze_sentiment node, including sentiment categories
        and confidence scores.
    identify_trends_input : IdentifyTrendsOutput
        Output of the identify_trends node, including trending topics and
        sentiment trends.

    Returns
    -------
    CompileAnalysisReportOutput
        Structured output containing the completed analysis report,
        summaries, and validation status.

    Raises
    ------
    ValueError
        Raised if input validation fails or if inconsistencies are found in
        the inputs.
    TypeError
        Raised if input parameters are of unexpected types.

    Examples
    --------
    >>> analyze_output = AnalyzeSentimentOutput(
    ...     article_index=[0, 1],
    ...     sentiment_category=['positive', 'neutral'],
    ...     sentiment_confidence=[0.95, 0.78]
    >>> )
    >>> trends_output = IdentifyTrendsOutput(
    ...     trending_topics=['AI', 'Climate Change'],
    ...     sentiment_trends=['increasing positive', 'stable neutral'],
    ...     overall_trend_summary='AI topics are gaining positivity while
    climate sentiment remains neutral.'
    >>> )
    >>> result = compile_analysis_report(
    ...     analyze_sentiment_input=analyze_output,
    ...     identify_trends_input=trends_output
    >>> )
    >>> print(result.report_text)
    Full analysis report combining sentiment and trend insights.

    """
    analyze_sentiment_input: 'AnalyzeSentimentOutput',
    identify_trends_input: 'IdentifyTrendsOutput',
    **kwargs: dict
) -> 'CompileAnalysisReportOutput':
    logger = logging.getLogger(__name__)

    try:
        if not analyze_sentiment_input or not identify_trends_input:
            raise ValueError("Input data for sentiment analysis and trends cannot be empty.")

        sentiment_count = {
            "positive": analyze_sentiment_input.sentiment_category.count("positive"),
            "negative": analyze_sentiment_input.sentiment_category.count("negative"),
            "neutral": analyze_sentiment_input.sentiment_category.count("neutral")
        }

        sentiment_summary = (
            f"Sentiment Distribution: Positive={sentiment_count['positive']}, "
            f"Neutral={sentiment_count['neutral']}, Negative={sentiment_count['negative']}"
        )

        trend_summary = (
            identify_trends_input.overall_trend_summary or
            "No notable trends were identified in the input data."
        )

        full_report = (
            f"Analysis Report\n\n"
            f"--- Sentiment Summary ---\n{sentiment_summary}\n\n"
            f"--- Trends ---\n"
            f"Topics: {', '.join(identify_trends_input.trending_topics)}\n"
            f"Details: {trend_summary}\n"
        )

        return CompileAnalysisReportOutput(
            report_text=full_report,
            sentiment_summary=sentiment_summary,
            trend_summary=trend_summary,
            sentiment_per_article=analyze_sentiment_input.sentiment_category,
            trend_topics=identify_trends_input.trending_topics,
            article_count=len(analyze_sentiment_input.sentiment_category),
            is_valid=True
        )

    except ValueError as e:
        logger.error("Input validation failed: %s", e)
        return CompileAnalysisReportOutput(
            report_text="", trend_summary="", sentiment_summary="",
            sentiment_per_article=[], trend_topics=[], article_count=0, is_valid=False
        )
    except Exception as e:
        logger.error("Unhandled error during report compilation: %s", e)
        return CompileAnalysisReportOutput(
            report_text="", trend_summary="", sentiment_summary="",
            sentiment_per_article=[], trend_topics=[], article_count=0, is_valid=False
        )