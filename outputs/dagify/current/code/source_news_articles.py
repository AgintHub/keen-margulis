from ._source_news_articles.get_predefined_news_sources import get_predefined_news_sources
from ._source_news_articles.fetch_articles_from_source import fetch_articles_from_source
from ._source_news_articles.extract_urls import extract_urls
from ._source_news_articles.extract_titles import extract_titles
from ._source_news_articles.extract_texts import extract_texts
from ._source_news_articles.extract_source_names import extract_source_names
from ._source_news_articles.handle_fetch_error import handle_fetch_error
from ._source_news_articles.validate_collected_data import validate_collected_data

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


def source_news_articles(general_input: str, **kwargs) -> SourceNewsArticlesOutput:
    """
    Collects news articles from a predefined list of sources, returning metadata
    and content for each article.

    Returns
    -------
    dict
        A dictionary containing the following keys: - `article_urls`:
        List[str] - `article_titles`: List[str] - `article_texts`: List[str]
        - `article_sources`: List[str] - `article_count`: int -
        `fetch_successful`: bool

    Raises
    ------
    ConnectionError
        Raised when the network connection to a news source fails.
    ValueError
        Raised if the fetched data is empty or cannot be parsed.

    Examples
    --------
    >>> result = source_news_articles()
    >>> print(result['article_count'])
    5

    >>> result = source_news_articles()
    >>> print(result['article_urls'])
    ['https://example.com/article1', 'https://example.org/news/2',
    'https://news.com/story3']

    """
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
            
        except Exception as e:
            fetch_success = handle_fetch_error(error=e, source=source)
    
    validated_data: dict = validate_collected_data(
        urls=collected_urls,
        titles=collected_titles, 
        texts=collected_texts,
        sources=collected_sources
    )
    
    total_count: int = len(validated_data['urls'])
    
    return SourceNewsArticlesOutput(
        article_urls=validated_data['urls'],
        article_titles=validated_data['titles'],
        article_texts=validated_data['texts'],
        article_sources=validated_data['sources'],
        article_count=total_count,
        fetch_successful=fetch_success and total_count > 0
    )