from pydantic import BaseModel, Field
from typing import List


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


class CategorizeNewsArticlesOutput(BaseModel):
    """Pydantic model for categorize_news_articles node outputs."""
    article_titles: List[str] = (
        Field(..., description="List of article titles that were filtered and are now categorized.")
    )
    categories: List[str] = (
        Field(..., description="List of category labels corresponding to each article in `article_titles`; indices match.")
    )
    unique_category_count: int = (
        Field(..., description="Total number of distinct categories identified.")
    )
    article_count: int = (
        Field(..., description="Total number of articles processed by this node.")
    )
    is_successful: bool = (
        Field(..., description="Indicates whether the categorization succeeded without errors.")
    )


def categorize_news_articles(filter_news_articles_input: FilterNewsArticlesOutput, **kwargs) -> CategorizeNewsArticlesOutput:
    """
    Assigns topical categories to a list of filtered news article titles.

    Parameters
    ----------
    filtered_article_ids : List[str]
        List of article identifiers or titles that passed the relevance and
        duplication filters.

    Returns
    -------
    Dict[str, Any]
        Dictionary containing `article_titles`, `categories`,
        `unique_category_count`, `article_count`, and `is_successful`.

    Raises
    ------
    ValueError
        Raised if `filtered_article_ids` is empty or not a list of strings.

    Examples
    --------
    >>> categorized = categorize_news_articles(['Economic growth forecast',
    'Parliament passes new law', 'Local community event'])
    {
      'article_titles': ['Economic growth forecast', 'Parliament passes new
    law', 'Local community event'],
      'categories': ['Economics', 'Politics', 'Social Issues'],
      'unique_category_count': 3,
      'article_count': 3,
      'is_successful': True
    }

    >>> categorize_news_articles([])
    ValueError: filtered_article_ids must be a non-empty list of strings.

    """
    return CategorizeNewsArticlesOutput(
        article_titles=[],
        categories=[],
        unique_category_count=0,
        article_count=0,
        is_successful=False,
    )