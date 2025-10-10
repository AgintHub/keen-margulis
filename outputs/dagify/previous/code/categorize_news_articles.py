import logging
from typing import List
from pydantic import BaseModel, Field
from ._categorize_news_articles.normalize_article_titles import normalize_article_titles
from ._categorize_news_articles.assign_categories import assign_categories
from ._categorize_news_articles.get_unique_categories import get_unique_categories


class FilterNewsArticlesOutput(BaseModel):
    filtered_article_ids: List[str] = (
        Field(..., description="List of article titles that passed filtering.")
    )
    removed_article_ids: List[str] = (
        Field(..., description="List of article titles that were removed.")
    )
    filter_success: bool = (
        Field(..., description="Indicates whether filtering succeeded.")
    )

class CategorizeNewsArticlesOutput(BaseModel):
    article_titles: List[str] = (
        Field(..., description="List of article titles that were categorized.")
    )
    categories: List[str] = Field(..., description="Category for each article.")
    unique_category_count: int = (
        Field(..., description="Number of distinct categories.")
    )
    article_count: int = Field(..., description="Total articles processed.")
    is_successful: bool = (
        Field(..., description="Indicates success of categorization.")
    )

def categorize_news_articles(filter_news_articles_input: FilterNewsArticlesOutput, **kwargs) -> CategorizeNewsArticlesOutput:
    """
    Categorizes news article titles by topic.

    Parameters
    ----------
    filter_news_articles_input : FilterNewsArticlesOutput
        Output from the filtering step containing the list of article titles
        to be categorized.

    Returns
    -------
    CategorizeNewsArticlesOutput
        Structured output containing categorized titles, category list, and
        statistics.

    Raises
    ------
    ValueError
        Raised when `filtered_article_ids` is empty or not a list of
        strings.
    RuntimeError
        Raised when the prior filtering step failed or an internal error
        occurs during categorization.

    Examples
    --------
    >>> filtered = FilterNewsArticlesOutput(**{
    ...     'filtered_article_ids': ['Economic growth forecast', 'Parliament
    passes new law', 'Local community event'],
    ...     'removed_article_ids': [],
    ...     'filter_success': True
    >>> })
    >>> result = categorize_news_articles(filtered)
    >>> print(result)
    CategorizeNewsArticlesOutput(article_titles=['Economic growth forecast',
    'Parliament passes new law', 'Local community event'],
    categories=['Economics', 'Politics', 'Social Issues'],
    unique_category_count=3, article_count=3, is_successful=True)

    """
    logger = logging.getLogger(__name__)
    try:
        if not filter_news_articles_input.filter_success:
            logger.error("Filtering failed; cannot categorize.")
            raise RuntimeError("Previous filtering step failed.")
        titles = filter_news_articles_input.filtered_article_ids
        if not titles:
            logger.error("No titles provided for categorization.")
            raise ValueError("filtered_article_ids must be non-empty.")
        normalized_titles = normalize_article_titles(article_ids=titles)
        categories = assign_categories(article_titles=normalized_titles)
        unique_categories = get_unique_categories(categories=categories)
        return CategorizeNewsArticlesOutput(
            article_titles=normalized_titles,
            categories=categories,
            unique_category_count=len(unique_categories),
            article_count=len(normalized_titles),
            is_successful=True
        )
    except Exception as e:
        logger.exception("Categorization failed: %s", e)
        return CategorizeNewsArticlesOutput(
            article_titles=[],
            categories=[],
            unique_category_count=0,
            article_count=0,
            is_successful=False
        )