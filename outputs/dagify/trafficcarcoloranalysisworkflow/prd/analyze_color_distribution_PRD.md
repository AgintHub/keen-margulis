# analyze_color_distribution PRD

## Description
Analyze the distribution of vehicle colors observed during rush hour


## Conceptual Info

This node analyzes the distribution of vehicle colors observed during rush hour, calculating their frequency, identifying the most common colors, and providing statistical measures of the color distribution.

## Docstring

### Summary
Analyze vehicle color distribution from extracted vehicle data.

### Parameters

- **vehicle_colors** (List[str]): List of detected vehicle colors from the extract_vehicle_data_from_images node.
- **vehicle_confidence_scores** (List[float]): Confidence scores for the detected vehicle colors (same order as vehicle_colors).

### Returns

Tuple[List[float], List[str], List[float]]: A tuple containing the frequency of each observed vehicle color, the list of most common vehicle colors observed, and statistical measures (mean, median, std dev) of color distribution.

### Raises

- ValueError: If the input lists (vehicle_colors and vehicle_confidence_scores) are of different lengths.
- TypeError: If the input types are not as expected (List[str] for vehicle_colors and List[float] for vehicle_confidence_scores).

### Examples

```python
>>> vehicle_colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
>>> vehicle_confidence_scores = [0.8, 0.9, 0.7, 0.6, 0.95, 0.85]
>>> color_frequencies, most_common_colors, color_distribution_stats = analyze_color_distribution(vehicle_colors, vehicle_confidence_scores)
([0.3333333333333333, 0.5, 0.16666666666666666], ['blue'], [0.8166666666666667, 0.875, 0.10246950860768163])
```

```python
>>> vehicle_colors = ['black', 'white', 'black', 'white', 'black']
>>> vehicle_confidence_scores = [0.9, 0.8, 0.85, 0.7, 0.95]
>>> color_frequencies, most_common_colors, color_distribution_stats = analyze_color_distribution(vehicle_colors, vehicle_confidence_scores)
([0.6, 0.4], ['black'], [0.8833333333333333, 0.9, 0.08164965809277261])
```
