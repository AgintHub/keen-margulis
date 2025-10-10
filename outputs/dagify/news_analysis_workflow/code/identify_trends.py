from ._identify_trends.validate_summaries import validate_summaries
from ._identify_trends.preprocess_summaries import preprocess_summaries
from ._identify_trends.extract_topics_from_summaries import extract_topics_from_summaries
from ._identify_trends.identify_recurring_topics import identify_recurring_topics
from ._identify_trends.analyze_sentiment_per_topic import analyze_sentiment_per_topic
from ._identify_trends.calculate_sentiment_trends import calculate_sentiment_trends
from ._identify_trends.generate_overall_trend_summary import generate_overall_trend_summary

from pydantic import BaseModel, Field
from typing import List


class SummarizeNewsArticlesOutput(BaseModel):
    """Pydantic model for summarize_news_articles node outputs."""
    summary_count: int = (
        Field(..., description="Number of article summaries generated")
    )
    summaries: List[str] = (
        Field(..., description = (
            "Concise summaries for each news article, ordered as input")
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


def identify_trends(summarize_news_articles_input: SummarizeNewsArticlesOutput, **kwargs) -> IdentifyTrendsOutput:
    """
    Analyzes a list of article summaries to detect recurring topics and
    sentiment trends.

    Parameters
    ----------
    summaries : List[str]
        A list of concise summaries for each news article, produced by the
        `summarize_news_articles` node.

    Returns
    -------
    Dict[str, Any]
        Dictionary containing: - `trending_topics`: List of topics that
        recur across the summaries. - `sentiment_trends`: List of sentiment
        trend descriptors corresponding to each trending topic. -
        `overall_trend_summary`: A short narrative summarizing the overall
        trend patterns.

    Raises
    ------
    ValueError
        Raised if `summaries` is empty or contains non‑string elements.

    Examples
    --------
    >>> summaries = [
    ...     "The stock market saw a steady rise in technology shares after the
    earnings report.",
    ...     "Technology stocks continued to climb, reflecting investor
    confidence in AI.",
    ...     "Economic indicators suggest a slowing growth in manufacturing, but
    tech remains strong.",
    >>> ]
    >>> result = identify_trends(summaries)
    >>> print(result['trending_topics'])
    >>> print(result['sentiment_trends'])
    >>> print(result['overall_trend_summary'])
    [
      'technology',
      'manufacturing'
    ]
    [
      'increasing positive',
      'stable neutral'
    ]
    'Technology shows a growing positive trend while manufacturing sentiment
    remains stable.'

    >>> summaries = [
    ...     "Climate change policies gain traction in Europe.",
    ...     "Europe sees increased investment in green energy.",
    ...     "Green initiatives remain a hot topic across EU countries.",
    >>> ]
    >>> print(identify_trends(summaries)['trending_topics'])
    [
      'climate change',
      'green energy'
    ]

    """
    summaries: List[str] = summarize_news_articles_input.summaries
    
    validate_summaries(summaries=summaries)
    
    preprocessed_summaries: List[str] = preprocess_summaries(summaries=summaries)
    
    extracted_topics: List[List[str]] = extract_topics_from_summaries(summaries=preprocessed_summaries)
    
    trending_topics: List[str] = identify_recurring_topics(topic_lists=extracted_topics)
    
    topic_sentiments: List[List[str]] = analyze_sentiment_per_topic(summaries=preprocessed_summaries, topics=trending_topics)
    
    sentiment_trends: List[str] = calculate_sentiment_trends(topic_sentiments=topic_sentiments)
    
    overall_summary: str = generate_overall_trend_summary(topics=trending_topics, trends=sentiment_trends)
    
    return IdentifyTrendsOutput(
        trending_topics=trending_topics,
        sentiment_trends=sentiment_trends,
        overall_trend_summary=overall_summary
    )