from ._extract_leaf_features.validate_input_consistency import validate_input_consistency
from ._extract_leaf_features.preprocess_leaf_images import preprocess_leaf_images
from ._extract_leaf_features.extract_vein_patterns import extract_vein_patterns
from ._extract_leaf_features.extract_leaf_colors import extract_leaf_colors

from pydantic import BaseModel, Field
from typing import List


class CollectLeafDataOutput(BaseModel):
    """Pydantic model for collect_leaf_data node outputs."""
    leaf_images: List[str] = (
        Field(..., description="List of image file names or URLs of leaves")
    )
    leaf_characteristics: List[str] = (
        Field(..., description="List of characteristic descriptions for each leaf")
    )


class AnalyzeLeafShapesOutput(BaseModel):
    """Pydantic model for analyze_leaf_shapes node outputs."""
    leaf_shape_categories: List[str] = (
        Field(..., description="List of shape categories for the leaves")
    )
    shape_category_counts: List[int] = (
        Field(..., description="Counts of leaves in each shape category")
    )


class ExtractLeafFeaturesOutput(BaseModel):
    """Pydantic model for extract_leaf_features node outputs."""
    leaf_vein_patterns: List[str] = (
        Field(..., description="Descriptions of vein patterns for each leaf")
    )
    leaf_colors: List[str] = (
        Field(..., description="List of colors observed in the leaves")
    )


def extract_leaf_features(collect_leaf_data_input: CollectLeafDataOutput, analyze_leaf_shapes_input: AnalyzeLeafShapesOutput, **kwargs) -> ExtractLeafFeaturesOutput:
    """
    Extracts features from leaf images, including vein patterns and colors,
    using data from collect_leaf_data and analyze_leaf_shapes.

    Parameters
    ----------
    leaf_images : List[str]
        List of image file names or URLs of leaves from collect_leaf_data.
    leaf_characteristics : List[str]
        List of characteristic descriptions for each leaf from
        collect_leaf_data.
    leaf_shape_categories : List[str]
        List of shape categories for the leaves from analyze_leaf_shapes.
    shape_category_counts : List[int]
        Counts of leaves in each shape category from analyze_leaf_shapes.

    Returns
    -------
    Tuple[List[str], List[str]]
        A tuple containing a list of descriptions of vein patterns for each
        leaf and a list of colors observed in the leaves.

    Raises
    ------
    ValueError
        If leaf_images or leaf_characteristics are empty or mismatched in
        length.
    TypeError
        If the input lists are not of the expected types.

    Examples
    --------
    >>> leaf_images = ['leaf1.jpg', 'leaf2.jpg']
    >>> leaf_characteristics = ['characteristic1', 'characteristic2']
    >>> leaf_shape_categories = ['shape1', 'shape2']
    >>> shape_category_counts = [1, 2]
    >>> result = extract_leaf_features(leaf_images, leaf_characteristics,
    leaf_shape_categories, shape_category_counts)
    (['vein pattern 1', 'vein pattern 2'], ['color1', 'color2'])

    >>> leaf_images = ['leaf3.jpg']
    >>> leaf_characteristics = ['characteristic3']
    >>> leaf_shape_categories = ['shape3']
    >>> shape_category_counts = [3]
    >>> result = extract_leaf_features(leaf_images, leaf_characteristics,
    leaf_shape_categories, shape_category_counts)
    (['vein pattern 3'], ['color3'])

    """
    validate_input_consistency(leaf_images=collect_leaf_data_input.leaf_images, leaf_characteristics=collect_leaf_data_input.leaf_characteristics)
    
    processed_images: List[str] = preprocess_leaf_images(images=collect_leaf_data_input.leaf_images)
    
    vein_patterns: List[str] = extract_vein_patterns(
        images=processed_images, 
        characteristics=collect_leaf_data_input.leaf_characteristics,
        shape_categories=analyze_leaf_shapes_input.leaf_shape_categories
    )
    
    leaf_colors: List[str] = extract_leaf_colors(
        images=processed_images,
        characteristics=collect_leaf_data_input.leaf_characteristics
    )
    
    return ExtractLeafFeaturesOutput(
        leaf_vein_patterns=vein_patterns,
        leaf_colors=leaf_colors
    )