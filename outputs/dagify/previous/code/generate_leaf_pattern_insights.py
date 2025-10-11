from ._generate_leaf_pattern_insights.validate_input_data import validate_input_data
from ._generate_leaf_pattern_insights.identify_common_patterns import identify_common_patterns
from ._generate_leaf_pattern_insights.combine_pattern_lists import combine_pattern_lists
from ._generate_leaf_pattern_insights.identify_pattern_variations import identify_pattern_variations
from ._generate_leaf_pattern_insights.combine_variation_lists import combine_variation_lists
from ._generate_leaf_pattern_insights.generate_insights_summary import generate_insights_summary

from ._generate_leaf_pattern_insights.validate_input_data import validate_input_data
from ._generate_leaf_pattern_insights.identify_common_patterns import identify_common_patterns
from ._generate_leaf_pattern_insights.combine_pattern_lists import combine_pattern_lists
from ._generate_leaf_pattern_insights.identify_pattern_variations import identify_pattern_variations
from ._generate_leaf_pattern_insights.combine_variation_lists import combine_variation_lists
from ._generate_leaf_pattern_insights.generate_insights_summary import generate_insights_summary

from ._generate_leaf_pattern_insights.validate_input_data import validate_input_data
from ._generate_leaf_pattern_insights.identify_common_patterns import identify_common_patterns
from ._generate_leaf_pattern_insights.combine_pattern_lists import combine_pattern_lists
from ._generate_leaf_pattern_insights.identify_pattern_variations import identify_pattern_variations
from ._generate_leaf_pattern_insights.combine_variation_lists import combine_variation_lists
from ._generate_leaf_pattern_insights.generate_insights_summary import generate_insights_summary

from pydantic import BaseModel, Field
from typing import List


class ExtractLeafFeaturesOutput(BaseModel):
    """Pydantic model for extract_leaf_features node outputs."""
    leaf_vein_patterns: List[str] = (
        Field(..., description="Descriptions of vein patterns for each leaf")
    )
    leaf_colors: List[str] = (
        Field(..., description="List of colors observed in the leaves")
    )


class GenerateLeafPatternInsightsOutput(BaseModel):
    """Pydantic model for generate_leaf_pattern_insights node outputs."""
    common_leaf_patterns: List[str] = (
        Field(..., description="List of common patterns observed in the leaves")
    )
    leaf_pattern_variations: List[str] = (
        Field(..., description="List of variations observed in leaf patterns")
    )
    insights_summary: str = (
        Field(..., description="Summary of key insights on leaf patterns")
    )


def generate_leaf_pattern_insights(extract_leaf_features_input: ExtractLeafFeaturesOutput, **kwargs) -> GenerateLeafPatternInsightsOutput:
    """
    Generate insights on leaf patterns based on extracted features such as vein
    patterns and colors.

    Parameters
    ----------
    leaf_vein_patterns : List[str]
        Descriptions of vein patterns for each leaf, extracted by the parent
        node 'extract_leaf_features'
    leaf_colors : List[str]
        List of colors observed in the leaves, extracted by the parent node
        'extract_leaf_features'

    Returns
    -------
    Tuple[List[str], List[str], str]
        A tuple containing a list of common leaf patterns, a list of leaf
        pattern variations, and a summary of key insights on leaf patterns.

    Raises
    ------
    ValueError
        If the input lists 'leaf_vein_patterns' or 'leaf_colors' are empty
        or not provided.

    Examples
    --------
    >>> leaf_vein_patterns = ['parallel', 'net-like', 'parallel']
    >>> leaf_colors = ['green', 'green', 'yellow']
    >>> common_leaf_patterns, leaf_pattern_variations, insights_summary =
    generate_leaf_pattern_insights(leaf_vein_patterns, leaf_colors)
    (['parallel', 'net-like'], ['green', 'yellow'], 'Key insights: Parallel vein
    patterns are common, with variations in color.')

    >>> leaf_vein_patterns = ['net-like', 'net-like', 'net-like']
    >>> leaf_colors = ['green', 'variegated', 'green']
    >>> common_leaf_patterns, leaf_pattern_variations, insights_summary =
    generate_leaf_pattern_insights(leaf_vein_patterns, leaf_colors)
    (['net-like'], ['variegated'], 'Key insights: Net-like vein patterns are
    predominant, with some variation in leaf color.')

    """
    validate_input_data(vein_patterns=extract_leaf_features_input.leaf_vein_patterns, colors=extract_leaf_features_input.leaf_colors)
    
    common_vein_patterns: List[str] = identify_common_patterns(patterns=extract_leaf_features_input.leaf_vein_patterns)
    common_color_patterns: List[str] = identify_common_patterns(patterns=extract_leaf_features_input.leaf_colors)
    
    all_common_patterns: List[str] = combine_pattern_lists(vein_patterns=common_vein_patterns, color_patterns=common_color_patterns)
    
    vein_variations: List[str] = identify_pattern_variations(patterns=extract_leaf_features_input.leaf_vein_patterns)
    color_variations: List[str] = identify_pattern_variations(patterns=extract_leaf_features_input.leaf_colors)
    
    all_variations: List[str] = combine_variation_lists(vein_variations=vein_variations, color_variations=color_variations)
    
    insights_text: str = generate_insights_summary(common_patterns=all_common_patterns, variations=all_variations, vein_patterns=extract_leaf_features_input.leaf_vein_patterns, colors=extract_leaf_features_input.leaf_colors)
    
    return GenerateLeafPatternInsightsOutput(
        common_leaf_patterns=all_common_patterns,
        leaf_pattern_variations=all_variations,
        insights_summary=insights_text
    )