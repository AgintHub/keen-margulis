import logging
from typing import List

from pydantic import BaseModel, Field

from ._filter_news_articles.validate_input_consistency import validate_input_consistency
from ._filter_news_articles.detect_duplicate_articles import detect_duplicate_articles
from ._filter_news_articles.identify_irrelevant_articles import identify_irrelevant_articles
from ._filter_news_articles.combine_removal_indices import combine_removal_indices
from ._filter_news_articles.get_remaining_indices import get_remaining_indices
from ._filter_news_articles.extract_article_ids import extract_article_ids


logger = logging.getLogger(__name__)

class SourceNewsArticlesOutput(BaseModel):
    article_urls: List[str] = (
        Field(..., description='List of URLs for the news articles collected.')
    )
    article_titles: List[str] = (
        Field(..., description='Headlines of the news articles collected.')
    )
    article_texts: List[str] = (
        Field(..., description='Full text content of each news article.')
    )
    article_sources: List[str] = (
        Field(..., description='Names of the sources from which each article was retrieved.')
    )
    article_count: int = (
        Field(..., description='Total number of news articles collected.')
    )
    fetch_successful: bool = (
        Field(..., description='Indicates whether the fetch operation succeeded.')
    )

class FilterNewsArticlesOutput(BaseModel):
    filtered_article_ids: List[str] = (
        Field(..., description='List of article identifiers or titles that passed the relevance and duplication filters.')
    )
    removed_article_ids: List[str] = (
        Field(..., description='List of article identifiers or titles that were excluded due to irrelevance or duplication.')
    )
    filter_success: bool = (
        Field(..., description='Indicates whether the filtering operation completed successfully without errors.')
    )

def filter_news_articles(source_news_articles_input: SourceNewsArticlesOutput, **kwargs) -> FilterNewsArticlesOutput:
    """
    Filter news articles to remove irrelevant or duplicate entries.

    Parameters
    ----------
    source_news_articles_input : SourceNewsArticlesOutput
        Validated output from the source_news_articles node.

    Returns
    -------
    FilterNewsArticlesOutput
        Output containing filtered and removed article ids, and a success
        flag.

    Raises
    ------
    ValueError
        Raised when input validation fails.
    RuntimeError
        Raised when internal filtering logic encounters an unexpected error.

    Examples
    --------
    >>> from filter_news_articles import filter_news_articles,
    SourceNewsArticlesOutput, FilterNewsArticlesOutput
    >>> # Sample input with three articles
    >>> input_data = SourceNewsArticlesOutput(
    ...     article_urls=['url1', 'url2', 'url3'],
    ...     article_titles=['Title A', 'Title B', 'Title C'],
    ...     article_texts=['text A', 'text B', 'text C'],
    ...     article_sources=['Source X', 'Source Y', 'Source Z'],
    ...     article_count=3,
    ...     fetch_successful=True
    >>> )
    >>> output = filter_news_articles(input_data)
    >>> print(output)
    FilterNewsArticlesOutput(filtered_article_ids=['Title A', 'Title B', 'Title
    C'], removed_article_ids=[], filter_success=True)

    >>> # Sample input with a duplicate title
    >>> input_data = SourceNewsArticlesOutput(
    ...     article_urls=['url1', 'url2', 'url3'],
    ...     article_titles=['Title A', 'Title B', 'Title B'],
    ...     article_texts=['text A', 'text B', 'text B'],
    ...     article_sources=['Source X', 'Source Y', 'Source Y'],
    ...     article_count=3,
    ...     fetch_successful=True
    >>> )
    >>> output = filter_news_articles(input_data)
    >>> print(output)
    FilterNewsArticlesOutput(filtered_article_ids=['Title A', 'Title B'],
    removed_article_ids=['Title B'], filter_success=True)

    """
    try:
        validate_input_consistency(
            titles=source_news_articles_input.article_titles,
            texts=source_news_articles_input.article_texts,
            count=source_news_articles_input.article_count
        )
    except Exception as e:
        logger.error('Input validation failed: %s', e)
        raise ValueError(f'Input validation error: {e}')
    try:
        duplicate_indices = detect_duplicate_articles(
            titles=source_news_articles_input.article_titles,
            texts=source_news_articles_input.article_texts
        )
        irrelevant_indices = identify_irrelevant_articles(
            titles=source_news_articles_input.article_titles,
            texts=source_news_articles_input.article_texts
        )
        removed_indices = combine_removal_indices(duplicates=duplicate_indices, irrelevant=irrelevant_indices)
        filtered_indices = get_remaining_indices(
            total_count=source_news_articles_input.article_count,
            removed_indices=removed_indices
        )
        filtered_ids = extract_article_ids(
            titles=source_news_articles_input.article_titles,
            indices=filtered_indices
        )
        removed_ids = extract_article_ids(
            titles=source_news_articles_input.article_titles,
            indices=removed_indices
        )
        return FilterNewsArticlesOutput(
            filtered_article_ids=filtered_ids,
            removed_article_ids=removed_ids,
            filter_success=True
        )
    except Exception as e:
        logger.exception('Filtering failed: %s', e)
        return FilterNewsArticlesOutput(
            filtered_article_ids=[],
            removed_article_ids=[],
            filter_success=False
        )