import json


def validate_input_lists(image_paths: str, image_timestamps: str) -> str:
    """
    Validates input lists for image paths and timestamps, checking for
    consistency and correct formatting.

    Parameters
    ----------
    image_paths : str
        A list of file paths to captured traffic images, expected to be in a
        string format that can be parsed into a list.
    image_timestamps : str
        A list of timestamps for when each image was captured, expected to
        be in a string format that can be parsed into a list and in the same
        order as image_paths.

    Returns
    -------
    str
        A message indicating whether the input lists are valid. Returns
        'valid' if both lists are of the same length and correctly
        formatted, otherwise returns an error message.

    Raises
    ------
    ValueError
        When the input lists are not of the same length or are not correctly
        formatted.
    TypeError
        When the input types are not as expected (e.g., not strings that can
        be parsed into lists).

    Examples
    --------
    >>> validate_input_lists(image_paths='["path1", "path2"]',
    image_timestamps='["timestamp1", "timestamp2"]')
    'valid'

    >>> validate_input_lists(image_paths='["path1", "path2"]',
    image_timestamps='["timestamp1"]')
    'Error: Input lists are not of the same length.'

    """
    
    try:
        if not isinstance(image_paths, str) or not isinstance(image_timestamps, str):
            raise TypeError("Input types are not as expected (e.g., not strings that can be parsed into lists).")
        
        parsed_image_paths = json.loads(image_paths)
        parsed_image_timestamps = json.loads(image_timestamps)
        
        if not isinstance(parsed_image_paths, list) or not isinstance(parsed_image_timestamps, list):
            raise ValueError("Input strings are not correctly formatted as lists.")
        
        if len(parsed_image_paths) != len(parsed_image_timestamps):
            raise ValueError("Input lists are not of the same length.")
        
        return "valid"
        
    except json.JSONDecodeError:
        raise ValueError("Input strings are not correctly formatted as lists.")
    except ValueError as e:
        return f"Error: {str(e)}"
    except TypeError as e:
        raise TypeError(str(e))