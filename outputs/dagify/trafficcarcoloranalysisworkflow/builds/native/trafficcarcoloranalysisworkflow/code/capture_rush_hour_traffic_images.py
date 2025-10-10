from ._capture_rush_hour_traffic_images.initialize_camera_devices import initialize_camera_devices
from ._capture_rush_hour_traffic_images.determine_rush_hour_timing import determine_rush_hour_timing
from ._capture_rush_hour_traffic_images.capture_traffic_images import capture_traffic_images
from ._capture_rush_hour_traffic_images.save_images_to_storage import save_images_to_storage
from ._capture_rush_hour_traffic_images.generate_timestamps import generate_timestamps
from ._capture_rush_hour_traffic_images.validate_capture_results import validate_capture_results

from ._capture_rush_hour_traffic_images.initialize_camera_devices import initialize_camera_devices
from ._capture_rush_hour_traffic_images.determine_rush_hour_timing import determine_rush_hour_timing
from ._capture_rush_hour_traffic_images.capture_traffic_images import capture_traffic_images
from ._capture_rush_hour_traffic_images.save_images_to_storage import save_images_to_storage
from ._capture_rush_hour_traffic_images.generate_timestamps import generate_timestamps
from ._capture_rush_hour_traffic_images.validate_capture_results import validate_capture_results

from ._capture_rush_hour_traffic_images.initialize_camera_devices import initialize_camera_devices
from ._capture_rush_hour_traffic_images.determine_rush_hour_timing import determine_rush_hour_timing
from ._capture_rush_hour_traffic_images.capture_traffic_images import capture_traffic_images
from ._capture_rush_hour_traffic_images.save_images_to_storage import save_images_to_storage
from ._capture_rush_hour_traffic_images.generate_timestamps import generate_timestamps
from ._capture_rush_hour_traffic_images.validate_capture_results import validate_capture_results

from pydantic import BaseModel, Field
from typing import List


class CaptureRushHourTrafficImagesOutput(BaseModel):
    """Pydantic model for capture_rush_hour_traffic_images node outputs."""
    image_paths: List[str] = (
        Field(..., description="List of file paths to captured traffic images")
    )
    image_timestamps: List[str] = (
        Field(..., description = (
            "Timestamps for when each image was captured (same order as image_paths)")
        )
    )


def capture_rush_hour_traffic_images(general_input: str, **kwargs) -> CaptureRushHourTrafficImagesOutput:
    """
    Captures images of traffic during rush hour and returns file paths and
    timestamps.

    Returns
    -------
    Tuple[List[str], List[str]]
        A tuple containing a list of image file paths and a list of
        corresponding timestamps.

    Raises
    ------
    IOError
        If there's an issue capturing or saving the images.
    ValueError
        If the captured images or timestamps are invalid or empty.

    Examples
    --------
    >>> image_paths, image_timestamps = capture_rush_hour_traffic_images()
    (['path/to/image1.jpg', 'path/to/image2.jpg'], ['2023-03-01 08:00:00',
    '2023-03-01 08:01:00'])

    """
    camera_devices: List[str] = initialize_camera_devices(input_config=general_input)
    rush_hour_schedule: dict = determine_rush_hour_timing(location=general_input)
    
    captured_images: List[bytes] = capture_traffic_images(
        cameras=camera_devices,
        schedule=rush_hour_schedule,
        focus_settings="vehicle_features",
        lighting_optimization=True
    )
    
    saved_paths: List[str] = save_images_to_storage(
        image_data=captured_images,
        output_directory="traffic_images",
        file_format="jpg"
    )
    
    capture_timestamps: List[str] = generate_timestamps(
        image_count=len(saved_paths),
        capture_start_time=rush_hour_schedule["start_time"]
    )
    
    validate_capture_results(paths=saved_paths, timestamps=capture_timestamps)
    
    return CaptureRushHourTrafficImagesOutput(
        image_paths=saved_paths,
        image_timestamps=capture_timestamps
    )