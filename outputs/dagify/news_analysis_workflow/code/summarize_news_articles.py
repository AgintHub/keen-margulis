import logging
from typing import List
from pydantic import BaseModel, Field
from ._summarize_news_articles.get_article_texts import get_article_texts
from ._summarize_news_articles.validate_input_lists import validate_input_lists
from ._summarize_news_articles.preprocess_article_text import preprocess_article_text
from ._summarize_news_articles.generate_concise_summary import generate_concise_summary
from ._categorize_news_articles import CategorizeNewsArticlesOutput


class SummarizeNewsArticlesOutput(BaseModel):
    summary_count: int = (
        Field(..., description="Number of article summaries generated")
    )
    summaries: List[str] = (
        Field(..., description="Concise summaries for each news article, ordered as input")
    )

def summarize_news_articles(categorize_news_articles_input: CategorizeNewsArticlesOutput, **kwargs) -> SummarizeNewsArticlesOutput:
    """
    Generate concise one‑sentence summaries of news articles.

    Parameters
    ----------
    categorize_news_articles_input : CategorizeNewsArticlesOutput
        Output from the categorization node containing article titles and
        associated metadata.

    Returns
    -------
    SummarizeNewsArticlesOutput
        Structured output with the count of summaries and the list of
        summary strings.

    Raises
    ------
    ValueError
        Raised when no article titles are provided or when title and text
        counts mismatch.
    TypeError
        Raised when input types are not as expected.

    Examples
    --------
    >>> output = summarize_news_articles(categorize_news_articles_input)
    >>> print(output.summary_count)
    >>> print(output.summaries)
    2
    ['Economy grew 3% driven by consumer spending and tech investment.',
    'Championship final ended with a dramatic tie‑breaker.']

    """
    logger = logging.getLogger(__name__)
    article_titles = categorize_news_articles_input.article_titles
    if not article_titles:
        logger.error("No article titles provided")
        raise ValueError("No article titles provided")
    article_texts = get_article_texts(titles=article_titles)
    if not article_texts or len(article_texts) != len(article_titles):
        logger.error("Mismatch between article titles and texts")
        raise ValueError("Mismatch between article titles and texts")
    validate_input_lists(titles=article_titles, texts=article_texts)
    summaries: List[str] = []
    for title, text in zip(article_titles, article_texts):
        processed_text = preprocess_article_text(text=text)
        summary = generate_concise_summary(title=title, text=processed_text)
        summaries.append(summary)
    return SummarizeNewsArticlesOutput(summary_count=len(summaries), summaries=summaries)