from typing import List


import re


def process_and_validate_images(images: str) -> List[str]:
    """
    Processes and validates image file names or URLs, returning a list of valid
    images.

    Parameters
    ----------
    images : str
        A string containing image file names or URLs to be processed,
        separated by commas or another delimiter.

    Returns
    -------
    List[str]
        A list of processed and validated image file names or URLs.

    Raises
    ------
    ValueError
        If the input string is empty or contains invalid image file names or
        URLs.
    TypeError
        If the input is not a string.

    Examples
    --------
    >>> process_and_validate_images(images='image1.jpg,image2.png')
    ['image1.jpg', 'image2.png']

    >>> process_and_validate_images(images='invalid_image')
    []

    """
    
    if not isinstance(images, str):
        raise TypeError("Input must be a string")
    
    if not images.strip():
        raise ValueError("Input string is empty")
    
    image_list = re.split(r'[,;\n\s]+', images.strip())
    
    image_list = [img.strip() for img in image_list if img.strip()]
    
    valid_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg'}
    
    valid_images = []
    
    for img in image_list:
        if img.startswith(('http://', 'https://')):
            if re.match(r'^https?://[^\s/$.?#].[^\s]*$', img):
                if any(img.lower().endswith(ext) for ext in valid_extensions) or '.' not in img.split('/')[-1]:
                    valid_images.append(img)
        else:
            if '.' in img and any(img.lower().endswith(ext) for ext in valid_extensions):
                valid_images.append(img)
    
    return valid_images