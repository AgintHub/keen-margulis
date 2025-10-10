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
    return SourceNewsArticlesOutput(
        article_urls=[],
        article_titles=[],
        article_texts=[],
        article_sources=[],
        article_count=0,
        fetch_successful=False,
    )