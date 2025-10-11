from ._analyze_business_operations.validate_input_data import validate_input_data
from ._analyze_business_operations.parse_business_operations_data import parse_business_operations_data
from ._analyze_business_operations.identify_strengths import identify_strengths
from ._analyze_business_operations.identify_weaknesses import identify_weaknesses
from ._analyze_business_operations.calculate_efficiency_metrics import calculate_efficiency_metrics

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


class AnalyzeBusinessOperationsOutput(BaseModel):
    """Pydantic model for analyze_business_operations node outputs."""
    strengths: List[str] = (
        Field(..., description="List of business operation strengths")
    )
    weaknesses: List[str] = (
        Field(..., description="List of business operation weaknesses")
    )
    efficiency_metrics: List[float] = (
        Field(..., description="List of efficiency metrics for business operations")
    )


def analyze_business_operations(gather_wcfb_data_input: GatherWcfbDataOutput, **kwargs) -> AnalyzeBusinessOperationsOutput:
    """
    Analyzes business operations data to identify areas of strength and
    weakness.

    Parameters
    ----------
    business_operations_data : str
        Data related to business operations gathered from the
        'gather_wcfb_data' node.

    Returns
    -------
    Tuple[List[str], List[str], List[float]]
        A tuple containing a list of business operation strengths, a list of
        business operation weaknesses, and a list of efficiency metrics for
        business operations.

    Raises
    ------
    ValueError
        If the input 'business_operations_data' is empty or not in the
        expected format.

    Examples
    --------
    >>> business_operations_data = '{"sales": 1000, "expenses": 500,
    "productivity": 0.8}'
    >>> strengths, weaknesses, efficiency_metrics =
    analyze_business_operations(business_operations_data)
    >>> print(strengths, weaknesses, efficiency_metrics)
    ['High sales'] ['High expenses'] [0.8]

    >>> business_operations_data = '{"sales": 800, "expenses": 600,
    "productivity": 0.7}'
    >>> strengths, weaknesses, efficiency_metrics =
    analyze_business_operations(business_operations_data)
    >>> print(strengths, weaknesses, efficiency_metrics)
    ['Moderate sales'] ['High expenses'] [0.7]

    """
    validate_input_data(data=gather_wcfb_data_input.business_operations_data)
    parsed_data: dict = parse_business_operations_data(data=gather_wcfb_data_input.business_operations_data)
    
    strengths_list: List[str] = identify_strengths(parsed_data=parsed_data)
    weaknesses_list: List[str] = identify_weaknesses(parsed_data=parsed_data)
    efficiency_metrics_list: List[float] = calculate_efficiency_metrics(parsed_data=parsed_data)
    
    return AnalyzeBusinessOperationsOutput(
        strengths=strengths_list,
        weaknesses=weaknesses_list,
        efficiency_metrics=efficiency_metrics_list
    )