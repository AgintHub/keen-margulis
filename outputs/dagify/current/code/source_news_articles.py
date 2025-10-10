import logging
from typing import List
from pydantic import BaseModel, Field

from ._source_news_articles.get_predefined_news_sources import get_predefined_news_sources
from ._source_news_articles.fetch_articles_from_source import fetch_articles_from_source
from ._source_news_articles.extract_urls import extract_urls
from ._source_news_articles.extract_titles import extract_titles
from ._source_news_articles.extract_texts import extract_texts
from ._source_news_articles.extract_source_names import extract_source_names
from ._source_news_articles.handle_fetch_error import handle_fetch_error
from ._source_news_articles.validate_collected_data import validate_collected_data


class SourceNewsArticlesOutput(BaseModel):
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
        Field(..., description="Indicates whether the fetch operation succeeded for at least one source.")
    )

logger = logging.getLogger(__name__)

def source_news_articles(general_input: str | None = None, **kwargs) -> SourceNewsArticlesOutput:
    """
    Retrieve news articles from a set of predefined sources, returning
    structured metadata and content.

    Parameters
    ----------
    general_input : str | None
        Optional textual input that can be used to influence source
        selection or filtering. Currently unused but kept for compatibility.
    kwargs : dict
        Additional keyword arguments forwarded to downstream helpers.

    Returns
    -------
    SourceNewsArticlesOutput
        Model containing article URLs, titles, texts, source names, count,
        and a success flag.

    Raises
    ------
    ValueError
        Raised when an unexpected type is passed or collected data cannot be
        validated.

    Examples
    --------
    >>> result = source_news_articles()
    >>> print(result.article_count)
    7

    """
    if general_input is not None and not isinstance(general_input, str):
        logger.error("general_input must be a string if provided")
        raise ValueError("general_input must be a string if provided")

    source_list: List[str] = get_predefined_news_sources()
    collected_urls: List[str] = []
    collected_titles: List[str] = []
    collected_texts: List[str] = []
    collected_sources: List[str] = []

    fetch_success: bool = True

    for source in source_list:
        try:
            article_data: dict = fetch_articles_from_source(source=source)
            urls: List[str] = extract_urls(data=article_data)
            titles: List[str] = extract_titles(data=article_data)
            texts: List[str] = extract_texts(data=article_data)
            sources: List[str] = extract_source_names(data=article_data, source=source)
            collected_urls.extend(urls)
            collected_titles.extend(titles)
            collected_texts.extend(texts)
            collected_sources.extend(sources)
            logger.info("Fetched %d articles from %s", len(urls), source)
        except Exception as e:
            logger.exception("Error fetching articles from %s: %s", source, e)
            fetch_success = handle_fetch_error(error=e, source=source)

    validated_data: dict = validate_collected_data(
        urls=collected_urls,
        titles=collected_titles,
        texts=collected_texts,
        sources=collected_sources
    )

    total_count: int = len(validated_data["urls"]) if validated_data else 0

    return SourceNewsArticlesOutput(
        article_urls=validated_data["urls"],
        article_titles=validated_data["titles"],
        article_texts=validated_data["texts"],
        article_sources=validated_data["sources"],
        article_count=total_count,
        fetch_successful=fetch_success and total_count > 0
    )