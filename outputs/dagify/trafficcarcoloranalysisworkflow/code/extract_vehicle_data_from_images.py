from ._extract_vehicle_data_from_images.validate_input_lists import validate_input_lists
from ._extract_vehicle_data_from_images.verify_image_files_exist import verify_image_files_exist
from ._extract_vehicle_data_from_images.load_and_validate_image import load_and_validate_image
from ._extract_vehicle_data_from_images.detect_vehicles_in_image import detect_vehicles_in_image
from ._extract_vehicle_data_from_images.extract_colors_from_vehicles import extract_colors_from_vehicles
from ._extract_vehicle_data_from_images.get_color_names import get_color_names
from ._extract_vehicle_data_from_images.get_confidence_values import get_confidence_values

from pydantic import BaseModel, Field
from typing import List


class CaptureRushHourTrafficImagesOutput(BaseModel):
    """Pydantic model for capture_rush_hour_traffic_images node outputs."""
    image_paths: List[str] = (
        Field(..., description="List of file paths to captured traffic images")
    )
    image_timestamps: List[str] = (
        Field(..., description="Timestamps for when each image was captured (same order as image_paths)")
    )


class ExtractVehicleDataFromImagesOutput(BaseModel):
    """Pydantic model for extract_vehicle_data_from_images node outputs."""
    vehicle_colors: List[str] = (
        Field(..., description="List of detected vehicle colors")
    )
    vehicle_confidence_scores: List[float] = (
        Field(..., description="Confidence scores for the detected vehicle colors (same order as vehicle_colors)")
    )


def extract_vehicle_data_from_images(capture_rush_hour_traffic_images_input: CaptureRushHourTrafficImagesOutput, **kwargs) -> ExtractVehicleDataFromImagesOutput:
    """
    Extracts vehicle color data from a list of image paths using computer
    vision.

    Parameters
    ----------
    image_paths : List[str]
        List of file paths to the images captured during rush hour traffic.
    image_timestamps : List[str]
        Timestamps for when each image was captured (same order as
        image_paths).

    Returns
    -------
    Tuple[List[str], List[float]]
        A tuple containing a list of detected vehicle colors and their
        corresponding confidence scores.

    Raises
    ------
    ValueError
        If the input lists (image_paths and image_timestamps) are of
        different lengths.
    FileNotFoundError
        If any of the image paths in image_paths do not exist.
    Exception
        If there's an issue processing an image (e.g., due to corruption or
        unsupported format).

    Examples
    --------
    >>> image_paths = ['/path/to/image1.jpg', '/path/to/image2.jpg']
    >>> image_timestamps = ['2023-04-01 08:00:00', '2023-04-01 08:01:00']
    >>> vehicle_colors, vehicle_confidence_scores =
    extract_vehicle_data_from_images(image_paths, image_timestamps)
    (['red', 'blue'], [0.9, 0.85])

    >>> image_paths = ['/path/to/image3.jpg']
    >>> image_timestamps = ['2023-04-01 08:02:00']
    >>> vehicle_colors, vehicle_confidence_scores =
    extract_vehicle_data_from_images(image_paths, image_timestamps)
    (['black'], [0.95])

    """
    validate_input_lists(image_paths=capture_rush_hour_traffic_images_input.image_paths, image_timestamps=capture_rush_hour_traffic_images_input.image_timestamps)
    verify_image_files_exist(image_paths=capture_rush_hour_traffic_images_input.image_paths)
    
    all_vehicle_colors: List[str] = []
    all_confidence_scores: List[float] = []
    
    for image_path in capture_rush_hour_traffic_images_input.image_paths:
        image_data = load_and_validate_image(image_path=image_path)
        detected_vehicles = detect_vehicles_in_image(image_data=image_data)
        colors_and_scores = extract_colors_from_vehicles(detected_vehicles=detected_vehicles)
        vehicle_colors: List[str] = get_color_names(colors_and_scores=colors_and_scores)
        confidence_scores: List[float] = get_confidence_values(colors_and_scores=colors_and_scores)
        all_vehicle_colors.extend(vehicle_colors)
        all_confidence_scores.extend(confidence_scores)
    
    return ExtractVehicleDataFromImagesOutput(
        vehicle_colors=all_vehicle_colors,
        vehicle_confidence_scores=all_confidence_scores
    )