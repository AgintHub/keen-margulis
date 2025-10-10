import logging
from typing import List
from ._identify_trends.validate_summaries import validate_summaries
from ._identify_trends.preprocess_summaries import preprocess_summaries
from ._identify_trends.extract_topics_from_summaries import extract_topics_from_summaries
from ._identify_trends.identify_recurring_topics import identify_recurring_topics
from ._identify_trends.analyze_sentiment_per_topic import analyze_sentiment_per_topic
from ._identify_trends.calculate_sentiment_trends import calculate_sentiment_trends
from ._identify_trends.generate_overall_trend_summary import generate_overall_trend_summary


logger = logging.getLogger(__name__)

def identify_trends(summarize_news_articles_input: SummarizeNewsArticlesOutput, **kwargs) -> IdentifyTrendsOutput:
    """
    Identifies trending topics and sentiment trajectories from article
    summaries.

    Parameters
    ----------
    summarize_news_articles_input : SummarizeNewsArticlesOutput
        Pydantic model containing the list of article summaries produced by
        the summarize_news_articles node.
    kwargs : dict
        Optional keyword arguments for extensibility.

    Returns
    -------
    IdentifyTrendsOutput
        Pydantic model with trending topics, sentiment trends, and an
        overall summary.

    Raises
    ------
    ValueError
        If the summaries list is empty or contains non-string items.
    RuntimeError
        If any helper function fails during processing.

    Examples
    --------
    >>> from your_module import identify_trends
    --

    """
    summaries: List[str] = summarize_news_articles_input.summaries
    if not isinstance(summaries, list) or not summaries:
        raise ValueError("summaries must be a non‑empty list of strings")
    if not all(isinstance(item, str) for item in summaries):
        raise ValueError("all items in summaries must be strings")
    try:
        validate_summaries(summaries=summaries)
    except Exception as e:
        logger.exception("Summaries validation failed")
        raise RuntimeError("Failed to validate summaries") from e
    try:
        preprocessed: List[str] = preprocess_summaries(summaries=summaries)
        extracted: List[List[str]] = extract_topics_from_summaries(summaries=preprocessed)
        trending: List[str] = identify_recurring_topics(topic_lists=extracted)
        topic_sentiments: List[List[str]] = analyze_sentiment_per_topic(summaries=preprocessed, topics=trending)
        sentiment_trends: List[str] = calculate_sentiment_trends(topic_sentiments=topic_sentiments)
        overall: str = generate_overall_trend_summary(topics=trending, trends=sentiment_trends)
    except Exception as e:
        logger.exception("Trend identification processing failed")
        raise RuntimeError("Error during trend identification") from e
    return IdentifyTrendsOutput(
        trending_topics=trending,
        sentiment_trends=sentiment_trends,
        overall_trend_summary=overall
    )