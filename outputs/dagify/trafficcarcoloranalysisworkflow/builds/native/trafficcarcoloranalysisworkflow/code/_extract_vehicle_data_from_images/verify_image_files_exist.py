import os


def verify_image_files_exist(image_paths: str) -> str:
    """
    Verifies the existence of image files based on provided paths.

    Parameters
    ----------
    image_paths : str
        A string containing the paths to the image files to be verified,
        potentially comma-separated or in a specific format.

    Returns
    -------
    str
        A string indicating the result of the verification process. The
        exact format may vary based on implementation requirements.

    Raises
    ------
    FileNotFoundError
        When one or more of the specified image files do not exist.
    TypeError
        If the input is not a string or does not contain valid file paths.

    Examples
    --------
    >>> verify_image_files_exist(image_paths='/path/to/image1.jpg,/path/to/image
    2.jpg')
    'All image files exist.'

    >>> verify_image_files_exist(image_paths='/path/to/nonexistent.jpg')
    'Error: One or more image files do not exist.'

    """
    if not isinstance(image_paths, str):
        raise TypeError("Input must be a string containing file paths")
    
    if not image_paths.strip():
        raise TypeError("Input does not contain valid file paths")
    
    paths = [path.strip() for path in image_paths.split(',') if path.strip()]
    
    if not paths:
        raise TypeError("Input does not contain valid file paths")
    
    missing_files = []
    for path in paths:
        if not os.path.isfile(path):
            missing_files.append(path)
    
    if missing_files:
        raise FileNotFoundError(f"One or more image files do not exist: {', '.join(missing_files)}")
    
    return "All image files exist."