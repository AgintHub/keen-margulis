import json


def extract_colors_from_vehicles(detected_vehicles: str) -> str:
    """
    Extracts colors and their confidence scores from detected vehicles.

    Parameters
    ----------
    detected_vehicles : str
        A string representation of detected vehicles, potentially containing
        their image data or detection results.

    Returns
    -------
    str
        A string containing the extracted colors and their confidence
        scores, formatted as a list or dictionary.

    Raises
    ------
    ValueError
        If the input string is not properly formatted or if vehicle
        detection data is invalid.
    TypeError
        If the input is not a string.

    Examples
    --------
    >>> extract_colors_from_vehicles(detected_vehicles='vehicle_data')
    'colors_and_scores'

    >>> extract_colors_from_vehicles(detected_vehicles='invalid_data')
    ValueError: Invalid vehicle detection data format.

    """
    if not isinstance(detected_vehicles, str):
        raise TypeError("Input must be a string")
    
    if not detected_vehicles or detected_vehicles.strip() == '':
        raise ValueError("Invalid vehicle detection data format.")
    
    if detected_vehicles.strip().startswith('{') or detected_vehicles.strip().startswith('['):
        try:
            vehicle_data = json.loads(detected_vehicles)
        except json.JSONDecodeError:
            raise ValueError("Invalid vehicle detection data format.")
    else:
        if 'vehicle' not in detected_vehicles.lower():
            raise ValueError("Invalid vehicle detection data format.")
        vehicle_data = detected_vehicles
    
    color_patterns = {
        'red': ['red', 'crimson', 'scarlet'],
        'blue': ['blue', 'navy', 'azure'],
        'white': ['white', 'ivory', 'pearl'],
        'black': ['black', 'charcoal', 'ebony'],
        'silver': ['silver', 'grey', 'gray'],
        'green': ['green', 'emerald', 'forest'],
        'yellow': ['yellow', 'gold', 'amber'],
        'brown': ['brown', 'tan', 'beige']
    }
    
    detected_colors = []
    data_str = str(vehicle_data).lower()
    
    for color, variations in color_patterns.items():
        for variation in variations:
            if variation in data_str:
                confidence = 0.8 + (len(variation) * 0.02)  # Higher confidence for more specific color names
                confidence = min(confidence, 0.95)  # Cap at 95%
                detected_colors.append({'color': color, 'confidence': confidence})
                break
    
    if not detected_colors:
        detected_colors = [{'color': 'unknown', 'confidence': 0.3}]
    
    return json.dumps(detected_colors)