from typing import List


import os
import base64
import hashlib


def save_images_to_storage(image_data: str, output_directory: str, file_format: str) -> List[str]:
    """
    Saves image data to storage, returning a list of saved file paths.

    Parameters
    ----------
    image_data : str
        The image data to be saved, expected to be in bytes format but
        passed as str
    output_directory : str
        The directory path where images will be saved
    file_format : str
        The file format for the images (e.g., 'jpg', 'png')

    Returns
    -------
    List[str]
        A list of file paths where the images were saved

    Raises
    ------
    ValueError
        If the output directory is invalid or inaccessible
    TypeError
        If image_data is not of type str or if output_directory or
        file_format are not strings

    Examples
    --------
    >>> save_images_to_storage(image_data='image1_bytes',
    output_directory='/tmp/images', file_format='jpg')
    >>> save_images_to_storage(image_data='image2_bytes',
    output_directory='/tmp/images', file_format='png')
    ['/tmp/images/image1.jpg', '/tmp/images/image2.png']

    >>> save_images_to_storage(image_data=['image_bytes1', 'image_bytes2'],
    output_directory='/tmp/images', file_format='jpg')
    ['/tmp/images/image1.jpg', '/tmp/images/image2.jpg']

    """
    
    if not isinstance(image_data, str):
        raise TypeError("image_data must be of type str")
    if not isinstance(output_directory, str):
        raise TypeError("output_directory must be of type str")
    if not isinstance(file_format, str):
        raise TypeError("file_format must be of type str")
    
    if not os.path.exists(output_directory):
        try:
            os.makedirs(output_directory, exist_ok=True)
        except OSError:
            raise ValueError("output directory is invalid or inaccessible")
    
    if not os.access(output_directory, os.W_OK):
        raise ValueError("output directory is invalid or inaccessible")
    
    try:
        image_bytes = base64.b64decode(image_data)
    except Exception:
        image_bytes = image_data.encode('utf-8')
    
    file_hash = hashlib.md5(image_bytes).hexdigest()[:8]
    filename = f"image_{file_hash}.{file_format.lstrip('.')}"
    filepath = os.path.join(output_directory, filename)
    
    with open(filepath, 'wb') as f:
        f.write(image_bytes)
    
    return [filepath]