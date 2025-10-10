from pydantic import BaseModel, Field
from typing import List


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


class SummarizeNewsArticlesOutput(BaseModel):
    """Pydantic model for summarize_news_articles node outputs."""
    summary_count: int = (
        Field(..., description="Number of article summaries generated")
    )
    summaries: List[str] = (
        Field(..., description="Concise summaries for each news article, ordered as input")
    )


def summarize_news_articles(categorize_news_articles_input: CategorizeNewsArticlesOutput, **kwargs) -> SummarizeNewsArticlesOutput:
    """
    Generate concise summaries for a collection of news articles.

    Parameters
    ----------
    article_titles : List[str]
        List of article titles corresponding to the articles to be
        summarized.
    article_texts : List[str]
        Full text content of each article in the same order as
        `article_titles`.

    Returns
    -------
    Tuple[int, List[str]]
        A tuple where the first element is the number of summaries generated
        and the second element is a list of summary strings ordered to match
        the input articles.

    Raises
    ------
    ValueError
        If either `article_titles` or `article_texts` is empty, or if the
        two lists have different lengths.
    TypeError
        If the inputs are not of the expected list-of-strings types.

    Examples
    --------
    >>> summaries = summarize_news_articles(
    ...     article_titles=["Economy grows 3%", "Championship ends in
    tie‑breaker"],
    ...     article_texts=[
    ...         "The economy grew by 3% last quarter, driven largely by consumer
    spending and investment in technology sectors.",
    ...         "In an unexpected turn, the championship final concluded with a
    dramatic tie‑breaker, sending the crowd into a frenzy."
    >>> ]
    >>> )
    (2, ['Economy grew 3% driven by consumer spending and tech investment.',
    'Championship final ended with a dramatic tie‑breaker.'])

    >>> summaries = summarize_news_articles(article_titles=[], article_texts=[])
    ValueError: No articles provided.

    """
    return SummarizeNewsArticlesOutput(
        summary_count=0,
        summaries=[],
    )