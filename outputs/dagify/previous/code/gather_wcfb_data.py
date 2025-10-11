from ._gather_wcfb_data.collect_business_operations_data import collect_business_operations_data
from ._gather_wcfb_data.fetch_customer_feedback_sources import fetch_customer_feedback_sources
from ._gather_wcfb_data.process_customer_feedback_data import process_customer_feedback_data
from ._gather_wcfb_data.gather_market_trend_metrics import gather_market_trend_metrics
from ._gather_wcfb_data.aggregate_market_trends import aggregate_market_trends
from ._gather_wcfb_data.validate_data_collection_success import validate_data_collection_success

from pydantic import BaseModel, Field


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


def gather_wcfb_data(general_input: str, **kwargs) -> GatherWcfbDataOutput:
    """
    Gathers data necessary for WCFB analysis from business operations, customer
    feedback, and market trends.

    Returns
    -------
    Tuple[str, List[str], List[float]]
        A tuple containing business operations data, customer feedback data,
        and market trends data.

    Raises
    ------
    DataCollectionError
        If there's an issue collecting data from any of the sources.

    Examples
    --------
    >>> gather_wcfb_data()
    ('Business operations data', ['Customer feedback 1', 'Customer feedback 2'],
    [1.2, 3.4, 5.6])

    >>> business_ops_data, customer_feedback, market_trends = gather_wcfb_data()
    business_ops_data: 'Business operations data'
    customer_feedback: ['Customer feedback 1', 'Customer feedback 2']
    market_trends: [1.2, 3.4, 5.6]

    """
    business_ops_data: str = collect_business_operations_data(input_context=general_input)
    customer_feedback_raw: list = fetch_customer_feedback_sources()
    customer_feedback_processed: str = process_customer_feedback_data(feedback_list=customer_feedback_raw)
    market_trends_raw: list = gather_market_trend_metrics()
    market_trends_aggregated: float = aggregate_market_trends(trends_data=market_trends_raw)
    validate_data_collection_success(business_data=business_ops_data, feedback_data=customer_feedback_processed, trends_data=market_trends_aggregated)
    return GatherWcfbDataOutput(
        business_operations_data=business_ops_data,
        customer_feedback_data=customer_feedback_processed,
        market_trends_data=market_trends_aggregated,
    )