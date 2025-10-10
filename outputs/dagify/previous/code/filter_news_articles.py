from pydantic import BaseModel, Field
from typing import List


class SourceNewsArticlesOutput(BaseModel):
    """Pydantic model for source_news_articles node outputs."""
    article_urls: List[str] = (
        Field(..., description="List of URLs for the news articles collected.")
    )
    article_titles: List[str] = (
        Field(..., description="Headlines of the news articles collected.")
    )
    article_texts: List[str] = (
        Field(..., description="Full text content of each news article.")
    )
    article_sources: List[str] = (
        Field(..., description="Names of the sources from which each article was retrieved.")
    )
    article_count: int = (
        Field(..., description="Total number of news articles collected.")
    )
    fetch_successful: bool = (
        Field(..., description="Indicates whether the fetch operation succeeded.")
    )


class FilterNewsArticlesOutput(BaseModel):
    """Pydantic model for filter_news_articles node outputs."""
    filtered_article_ids: List[str] = (
        Field(..., description="List of article identifiers or titles that passed the relevance and duplication filters.")
    )
    removed_article_ids: List[str] = (
        Field(..., description="List of article identifiers or titles that were excluded due to irrelevance or duplication.")
    )
    filter_success: bool = (
        Field(..., description="Indicates whether the filtering operation completed successfully without errors.")
    )


def filter_news_articles(source_news_articles_input: SourceNewsArticlesOutput, **kwargs) -> FilterNewsArticlesOutput:
    """
    Filter out irrelevant or duplicate news articles from a collected set.

    Parameters
    ----------
    article_titles : List[str]
        Headlines of the news articles collected by the source_news_articles
        node.
    article_texts : List[str]
        Full text content of each news article.
    article_count : int
        Total number of articles provided. Used to validate that titles and
        texts lists are consistent.

    Returns
    -------
    Tuple[List[str], List[str], bool]
        A tuple containing (filtered_article_ids, removed_article_ids,
        filter_success).

    Raises
    ------
    ValueError
        Raised if the lengths of article_titles and article_texts do not
        match article_count, indicating malformed input.
    RuntimeError
        Raised if an internal filtering error occurs, such as failure to
        compute similarity scores.

    Examples
    --------
    >>> filtered, removed, success = filter_news_articles(

    ...     article_titles=['A', 'B', 'C'],

    ...     article_texts=['text A', 'text B', 'text C'],

    ...     article_count=3

    >>> )
    >>> print(filtered, removed, success)
    (['A', 'B', 'C'], [], True)

    >>> filtered, removed, success = filter_news_articles(

    ...     article_titles=['A', 'B', 'C', 'B'],

    ...     article_texts=['text A', 'text B', 'text C', 'text B'],

    ...     article_count=4

    >>> )
    >>> print(filtered, removed, success)
    (['A', 'B', 'C'], ['B'], True)

    """
    return FilterNewsArticlesOutput(
        filtered_article_ids=[],
        removed_article_ids=[],
        filter_success=False,
    )