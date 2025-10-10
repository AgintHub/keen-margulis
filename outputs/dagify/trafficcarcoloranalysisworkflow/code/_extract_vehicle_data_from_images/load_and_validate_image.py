import os
import base64
from PIL import Image


def load_and_validate_image(image_path: str) -> str:
    """
    Loads an image from a file path and validates it.

    Parameters
    ----------
    image_path : str
        The file path to the image that needs to be loaded and validated.

    Returns
    -------
    str
        A string representation of the loaded and validated image data.

    Raises
    ------
    FileNotFoundError
        If the image file at the specified path does not exist.
    ValueError
        If the image file is corrupted or cannot be validated.
    TypeError
        If the image_path is not a string.

    Examples
    --------
    >>> image_data =
    load_and_validate_image(image_path='path/to/valid/image.jpg')
    'image_data_string'

    >>> load_and_validate_image(image_path='path/to/nonexistent/image.jpg')
    FileNotFoundError: Image file not found at path/to/nonexistent/image.jpg

    """
    
    if not isinstance(image_path, str):
        raise TypeError("image_path must be a string")
    
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found at {image_path}")
    
    try:
        with Image.open(image_path) as img:
            img.verify()
        
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
            encoded_string = base64.b64encode(image_data).decode('utf-8')
            return encoded_string
    except Exception as e:
        raise ValueError(f"Image file is corrupted or cannot be validated: {str(e)}")