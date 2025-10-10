from ._filter_news_articles.validate_input_consistency import validate_input_consistency
from ._filter_news_articles.detect_duplicate_articles import detect_duplicate_articles
from ._filter_news_articles.identify_irrelevant_articles import identify_irrelevant_articles
from ._filter_news_articles.combine_removal_indices import combine_removal_indices
from ._filter_news_articles.get_remaining_indices import get_remaining_indices
from ._filter_news_articles.extract_article_ids import extract_article_ids

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
        Field(..., description = (
            "Names of the sources from which each article was retrieved.")
        )
    )
    article_count: int = (
        Field(..., description="Total number of news articles collected.")
    )
    fetch_successful: bool = (
        Field(..., description = (
            "Indicates whether the fetch operation succeeded.")
        )
    )


class FilterNewsArticlesOutput(BaseModel):
    """Pydantic model for filter_news_articles node outputs."""
    filtered_article_ids: List[str] = (
        Field(..., description = (
            "List of article identifiers or titles that passed the relevance and duplication filters.")
        )
    )
    removed_article_ids: List[str] = (
        Field(..., description = (
            "List of article identifiers or titles that were excluded due to irrelevance or duplication.")
        )
    )
    filter_success: bool = (
        Field(..., description = (
            "Indicates whether the filtering operation completed successfully without errors.")
        )
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
    validate_input_consistency(titles=source_news_articles_input.article_titles, texts=source_news_articles_input.article_texts, count=source_news_articles_input.article_count)
    
    duplicate_indices: List[int] = detect_duplicate_articles(titles=source_news_articles_input.article_titles, texts=source_news_articles_input.article_texts)
    irrelevant_indices: List[int] = identify_irrelevant_articles(titles=source_news_articles_input.article_titles, texts=source_news_articles_input.article_texts)
    
    removed_indices: List[int] = combine_removal_indices(duplicates=duplicate_indices, irrelevant=irrelevant_indices)
    filtered_indices: List[int] = get_remaining_indices(total_count=source_news_articles_input.article_count, removed_indices=removed_indices)
    
    filtered_ids: List[str] = extract_article_ids(titles=source_news_articles_input.article_titles, indices=filtered_indices)
    removed_ids: List[str] = extract_article_ids(titles=source_news_articles_input.article_titles, indices=removed_indices)
    
    return FilterNewsArticlesOutput(
        filtered_article_ids=filtered_ids,
        removed_article_ids=removed_ids,
        filter_success=True
    )