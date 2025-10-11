from ._collect_leaf_data.identify_leaf_data_sources import identify_leaf_data_sources
from ._collect_leaf_data.gather_raw_leaf_data import gather_raw_leaf_data
from ._collect_leaf_data.extract_leaf_images import extract_leaf_images
from ._collect_leaf_data.process_and_validate_images import process_and_validate_images
from ._collect_leaf_data.extract_leaf_characteristics import extract_leaf_characteristics
from ._collect_leaf_data.validate_characteristics import validate_characteristics

from ._collect_leaf_data.identify_leaf_data_sources import identify_leaf_data_sources
from ._collect_leaf_data.gather_raw_leaf_data import gather_raw_leaf_data
from ._collect_leaf_data.extract_leaf_images import extract_leaf_images
from ._collect_leaf_data.process_and_validate_images import process_and_validate_images
from ._collect_leaf_data.extract_leaf_characteristics import extract_leaf_characteristics
from ._collect_leaf_data.validate_characteristics import validate_characteristics

from ._collect_leaf_data.identify_leaf_data_sources import identify_leaf_data_sources
from ._collect_leaf_data.gather_raw_leaf_data import gather_raw_leaf_data
from ._collect_leaf_data.extract_leaf_images import extract_leaf_images
from ._collect_leaf_data.process_and_validate_images import process_and_validate_images
from ._collect_leaf_data.extract_leaf_characteristics import extract_leaf_characteristics
from ._collect_leaf_data.validate_characteristics import validate_characteristics

from pydantic import BaseModel, Field
from typing import List


class CollectLeafDataOutput(BaseModel):
    """Pydantic model for collect_leaf_data node outputs."""
    leaf_images: List[str] = (
        Field(..., description="List of image file names or URLs of leaves")
    )
    leaf_characteristics: List[str] = (
        Field(..., description = (
            "List of characteristic descriptions for each leaf")
        )
    )


def collect_leaf_data(general_input: str, **kwargs) -> CollectLeafDataOutput:
    """
    Collects leaf images and their characteristics, returning lists of image
    file names/URLs and characteristic descriptions.

    Returns
    -------
    Tuple[List[str], List[str]]
        A tuple containing a list of leaf image file names/URLs and a list
        of characteristic descriptions for each leaf.

    Raises
    ------
    Exception
        If there's an issue collecting or processing the leaf data.

    Examples
    --------
    >>> leaf_images, leaf_characteristics = collect_leaf_data()
    (['leaf1.jpg', 'leaf2.jpg'], ['Ovate with smooth edges', 'Lanceolate with
    serrated edges'])

    >>> leaf_data = collect_leaf_data(); print(leaf_data[0]);
    print(leaf_data[1])
    ['leaf1.jpg', 'leaf2.jpg']
    ['Ovate with smooth edges', 'Lanceolate with serrated edges']

    """
    data_sources: List[str] = identify_leaf_data_sources(input_context=general_input)
    raw_leaf_data: List[dict] = gather_raw_leaf_data(sources=data_sources)
    image_files: List[str] = extract_leaf_images(raw_data=raw_leaf_data)
    processed_images: List[str] = process_and_validate_images(images=image_files)
    characteristic_data: List[str] = extract_leaf_characteristics(raw_data=raw_leaf_data)
    validated_characteristics: List[str] = validate_characteristics(characteristics=characteristic_data)
    return CollectLeafDataOutput(
        leaf_images=processed_images,
        leaf_characteristics=validated_characteristics
    )