from ._examine_customer_feedback.parse_feedback_data import parse_feedback_data
from ._examine_customer_feedback.validate_feedback_input import validate_feedback_input
from ._examine_customer_feedback.analyze_sentiment_scores import analyze_sentiment_scores
from ._examine_customer_feedback.calculate_overall_satisfaction import calculate_overall_satisfaction
from ._examine_customer_feedback.filter_negative_feedback import filter_negative_feedback
from ._examine_customer_feedback.filter_positive_feedback import filter_positive_feedback
from ._examine_customer_feedback.extract_common_complaints import extract_common_complaints
from ._examine_customer_feedback.extract_positive_themes import extract_positive_themes

from pydantic import BaseModel, Field
from typing import List


class GatherWcfbDataOutput(BaseModel):
    """Pydantic model for gather_wcfb_data node outputs."""
    business_operations_data: str = (
        Field(..., description="Data related to business operations")
    )
    customer_feedback_data: str = (
        Field(..., description="List of customer feedback comments")
    )
    market_trends_data: float = (
        Field(..., description="List of market trend metrics")
    )


class ExamineCustomerFeedbackOutput(BaseModel):
    """Pydantic model for examine_customer_feedback node outputs."""
    customer_satisfaction_score: float = (
        Field(..., description="Overall customer satisfaction score")
    )
    common_complaints: List[str] = (
        Field(..., description="List of common customer complaints")
    )
    positive_feedback_themes: List[str] = (
        Field(..., description="List of themes from positive customer feedback")
    )


def examine_customer_feedback(gather_wcfb_data_input: GatherWcfbDataOutput, **kwargs) -> ExamineCustomerFeedbackOutput:
    """
    Analyze customer feedback data to extract insights.

    Parameters
    ----------
    customer_feedback_data : List[str]
        List of customer feedback comments from the gather_wcfb_data node.

    Returns
    -------
    Tuple[float, List[str], List[str]]
        A tuple containing the overall customer satisfaction score, a list
        of common customer complaints, and a list of themes from positive
        customer feedback.

    Raises
    ------
    ValueError
        If customer_feedback_data is empty or not a list of strings.

    Examples
    --------
    >>> customer_feedback_data = ['Great service!', 'Slow delivery.', 'Excellent
    product!']
    >>> result = examine_customer_feedback(customer_feedback_data)
    >>> print(result)
    (0.8, ['Slow delivery.'], ['Great service!', 'Excellent product!'])

    >>> customer_feedback_data = ['Good product.', 'Bad customer support.',
    'Fast shipping!']
    >>> result = examine_customer_feedback(customer_feedback_data)
    >>> print(result)
    (0.7, ['Bad customer support.'], ['Good product.', 'Fast shipping!'])

    """
    feedback_list: List[str] = parse_feedback_data(feedback_data=gather_wcfb_data_input.customer_feedback_data)
    
    validate_feedback_input(feedback_data=feedback_list)
    
    sentiment_scores: List[float] = analyze_sentiment_scores(feedback_list=feedback_list)
    
    overall_satisfaction: float = calculate_overall_satisfaction(sentiment_scores=sentiment_scores)
    
    negative_feedback: List[str] = filter_negative_feedback(feedback_list=feedback_list, sentiment_scores=sentiment_scores)
    
    positive_feedback: List[str] = filter_positive_feedback(feedback_list=feedback_list, sentiment_scores=sentiment_scores)
    
    complaints: List[str] = extract_common_complaints(negative_feedback=negative_feedback)
    
    themes: List[str] = extract_positive_themes(positive_feedback=positive_feedback)
    
    return ExamineCustomerFeedbackOutput(
        customer_satisfaction_score=overall_satisfaction,
        common_complaints=complaints,
        positive_feedback_themes=themes
    )