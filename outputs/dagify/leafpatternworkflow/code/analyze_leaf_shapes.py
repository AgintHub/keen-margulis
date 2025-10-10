from ._analyze_leaf_shapes.validate_input_lengths import validate_input_lengths
from ._analyze_leaf_shapes.preprocess_leaf_images import preprocess_leaf_images
from ._analyze_leaf_shapes.normalize_characteristics import normalize_characteristics
from ._analyze_leaf_shapes.extract_shape_categories import extract_shape_categories
from ._analyze_leaf_shapes.count_shape_categories import count_shape_categories

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


def analyze_leaf_shapes(collect_leaf_data_input: CollectLeafDataOutput, **kwargs) -> AnalyzeLeafShapesOutput:
    """
    Analyze leaf shapes and categorize them into different types based on the
    collected leaf data.

    Parameters
    ----------
    leaf_images : List[str]
        List of image file names or URLs of leaves collected by the
        'collect_leaf_data' node.
    leaf_characteristics : List[str]
        List of characteristic descriptions for each leaf collected by the
        'collect_leaf_data' node.

    Returns
    -------
    Tuple[List[str], List[int]]
        A tuple containing a list of shape categories for the leaves and a
        list of counts of leaves in each shape category.

    Raises
    ------
    ValueError
        If the input lists 'leaf_images' and 'leaf_characteristics' are of
        different lengths.

    Examples
    --------
    >>> leaf_images = ['leaf1.jpg', 'leaf2.jpg', 'leaf3.jpg']
    >>> leaf_characteristics = ['oval', 'lanceolate', 'cordate']
    >>> leaf_shape_categories, shape_category_counts =
    analyze_leaf_shapes(leaf_images, leaf_characteristics)
    (['oval', 'lanceolate', 'cordate'], [1, 1, 1])

    >>> leaf_images = ['leaf4.jpg', 'leaf5.jpg']
    >>> leaf_characteristics = ['elliptical', 'lanceolate']
    >>> leaf_shape_categories, shape_category_counts =
    analyze_leaf_shapes(leaf_images, leaf_characteristics)
    (['elliptical', 'lanceolate'], [1, 1])

    """
    validate_input_lengths(images=collect_leaf_data_input.leaf_images, characteristics=collect_leaf_data_input.leaf_characteristics)
    
    processed_images: List[str] = preprocess_leaf_images(images=collect_leaf_data_input.leaf_images)
    normalized_characteristics: List[str] = normalize_characteristics(characteristics=collect_leaf_data_input.leaf_characteristics)
    
    shape_categories: List[str] = extract_shape_categories(images=processed_images, characteristics=normalized_characteristics)
    category_counts: List[int] = count_shape_categories(categories=shape_categories)
    
    return AnalyzeLeafShapesOutput(
        leaf_shape_categories=shape_categories,
        shape_category_counts=category_counts
    )