from ._analyze_color_distribution.validate_input_lengths import validate_input_lengths
from ._analyze_color_distribution.validate_input_types import validate_input_types
from ._analyze_color_distribution.get_unique_colors import get_unique_colors
from ._analyze_color_distribution.count_color_occurrences import count_color_occurrences
from ._analyze_color_distribution.calculate_frequencies import calculate_frequencies
from ._analyze_color_distribution.find_most_common_colors import find_most_common_colors
from ._analyze_color_distribution.calculate_mean import calculate_mean
from ._analyze_color_distribution.calculate_median import calculate_median
from ._analyze_color_distribution.calculate_std_deviation import calculate_std_deviation

from ._analyze_color_distribution.validate_input_lengths import validate_input_lengths
from ._analyze_color_distribution.validate_input_types import validate_input_types
from ._analyze_color_distribution.get_unique_colors import get_unique_colors
from ._analyze_color_distribution.count_color_occurrences import count_color_occurrences
from ._analyze_color_distribution.calculate_frequencies import calculate_frequencies
from ._analyze_color_distribution.find_most_common_colors import find_most_common_colors
from ._analyze_color_distribution.calculate_mean import calculate_mean
from ._analyze_color_distribution.calculate_median import calculate_median
from ._analyze_color_distribution.calculate_std_deviation import calculate_std_deviation

from ._analyze_color_distribution.validate_input_lengths import validate_input_lengths
from ._analyze_color_distribution.validate_input_types import validate_input_types
from ._analyze_color_distribution.get_unique_colors import get_unique_colors
from ._analyze_color_distribution.count_color_occurrences import count_color_occurrences
from ._analyze_color_distribution.calculate_frequencies import calculate_frequencies
from ._analyze_color_distribution.find_most_common_colors import find_most_common_colors
from ._analyze_color_distribution.calculate_mean import calculate_mean
from ._analyze_color_distribution.calculate_median import calculate_median
from ._analyze_color_distribution.calculate_std_deviation import calculate_std_deviation

from pydantic import BaseModel, Field
from typing import List


class ExtractVehicleDataFromImagesOutput(BaseModel):
    """Pydantic model for extract_vehicle_data_from_images node outputs."""
    vehicle_colors: List[str] = (
        Field(..., description="List of detected vehicle colors")
    )
    vehicle_confidence_scores: List[float] = (
        Field(..., description = (
            "Confidence scores for the detected vehicle colors (same order as vehicle_colors)")
        )
    )


class AnalyzeColorDistributionOutput(BaseModel):
    """Pydantic model for analyze_color_distribution node outputs."""
    color_frequencies: List[float] = (
        Field(..., description="Frequency of each observed vehicle color")
    )
    most_common_colors: List[str] = (
        Field(..., description="List of most common vehicle colors observed")
    )
    color_distribution_stats: List[float] = (
        Field(..., description = (
            "Statistical measures (mean, median, std dev) of color distribution")
        )
    )


def analyze_color_distribution(extract_vehicle_data_from_images_input: ExtractVehicleDataFromImagesOutput, **kwargs) -> AnalyzeColorDistributionOutput:
    """
    Analyze vehicle color distribution from extracted vehicle data.

    Parameters
    ----------
    vehicle_colors : List[str]
        List of detected vehicle colors from the
        extract_vehicle_data_from_images node.
    vehicle_confidence_scores : List[float]
        Confidence scores for the detected vehicle colors (same order as
        vehicle_colors).

    Returns
    -------
    Tuple[List[float], List[str], List[float]]
        A tuple containing the frequency of each observed vehicle color, the
        list of most common vehicle colors observed, and statistical
        measures (mean, median, std dev) of color distribution.

    Raises
    ------
    ValueError
        If the input lists (vehicle_colors and vehicle_confidence_scores)
        are of different lengths.
    TypeError
        If the input types are not as expected (List[str] for vehicle_colors
        and List[float] for vehicle_confidence_scores).

    Examples
    --------
    >>> vehicle_colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
    >>> vehicle_confidence_scores = [0.8, 0.9, 0.7, 0.6, 0.95, 0.85]
    >>> color_frequencies, most_common_colors, color_distribution_stats =
    analyze_color_distribution(vehicle_colors, vehicle_confidence_scores)
    ([0.3333333333333333, 0.5, 0.16666666666666666], ['blue'],
    [0.8166666666666667, 0.875, 0.10246950860768163])

    >>> vehicle_colors = ['black', 'white', 'black', 'white', 'black']
    >>> vehicle_confidence_scores = [0.9, 0.8, 0.85, 0.7, 0.95]
    >>> color_frequencies, most_common_colors, color_distribution_stats =
    analyze_color_distribution(vehicle_colors, vehicle_confidence_scores)
    ([0.6, 0.4], ['black'], [0.8833333333333333, 0.9, 0.08164965809277261])

    """
    vehicle_colors = extract_vehicle_data_from_images_input.vehicle_colors
    vehicle_confidence_scores = extract_vehicle_data_from_images_input.vehicle_confidence_scores
    
    validate_input_lengths(colors=vehicle_colors, scores=vehicle_confidence_scores)
    validate_input_types(colors=vehicle_colors, scores=vehicle_confidence_scores)
    
    unique_colors: List[str] = get_unique_colors(colors=vehicle_colors)
    color_counts: List[int] = count_color_occurrences(colors=vehicle_colors, unique_colors=unique_colors)
    color_frequencies: List[float] = calculate_frequencies(counts=color_counts, total=len(vehicle_colors))
    
    most_common_colors: List[str] = find_most_common_colors(unique_colors=unique_colors, counts=color_counts)
    
    mean_score: float = calculate_mean(scores=vehicle_confidence_scores)
    median_score: float = calculate_median(scores=vehicle_confidence_scores)
    std_dev_score: float = calculate_std_deviation(scores=vehicle_confidence_scores)
    color_distribution_stats: List[float] = [mean_score, median_score, std_dev_score]
    
    return AnalyzeColorDistributionOutput(
        color_frequencies=color_frequencies,
        most_common_colors=most_common_colors,
        color_distribution_stats=color_distribution_stats
    )