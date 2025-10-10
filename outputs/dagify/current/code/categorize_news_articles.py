from ._categorize_news_articles.validate_input import validate_input
from ._categorize_news_articles.normalize_article_titles import normalize_article_titles
from ._categorize_news_articles.assign_categories import assign_categories
from ._categorize_news_articles.get_unique_categories import get_unique_categories

from pydantic import BaseModel, Field
from typing import List


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


class CategorizeNewsArticlesOutput(BaseModel):
    """Pydantic model for categorize_news_articles node outputs."""
    article_titles: List[str] = (
        Field(..., description = (
            "List of article titles that were filtered and are now categorized.")
        )
    )
    categories: List[str] = (
        Field(..., description = (
            "List of category labels corresponding to each article in `article_titles`; indices match.")
        )
    )
    unique_category_count: int = (
        Field(..., description = (
            "Total number of distinct categories identified.")
        )
    )
    article_count: int = (
        Field(..., description = (
            "Total number of articles processed by this node.")
        )
    )
    is_successful: bool = (
        Field(..., description = (
            "Indicates whether the categorization succeeded without errors.")
        )
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
    filtered_article_ids: List[str] = filter_news_articles_input.filtered_article_ids
    
    validate_input(filtered_article_ids=filtered_article_ids)
    
    normalized_titles: List[str] = normalize_article_titles(article_ids=filtered_article_ids)
    
    categories: List[str] = assign_categories(article_titles=normalized_titles)
    
    unique_categories: List[str] = get_unique_categories(categories=categories)
    
    unique_category_count: int = len(unique_categories)
    article_count: int = len(normalized_titles)
    
    return CategorizeNewsArticlesOutput(
        article_titles=normalized_titles,
        categories=categories,
        unique_category_count=unique_category_count,
        article_count=article_count,
        is_successful=True
    )