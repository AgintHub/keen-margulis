from typing import List


import re


def preprocess_leaf_images(images: str) -> List[str]:
    """
    Preprocesses a list of leaf image file names or URLs.

    Parameters
    ----------
    images : str
        List of image file names or URLs to be preprocessed, separated by
        commas or in a list format.

    Returns
    -------
    List[str]
        List of preprocessed image file names or URLs, potentially
        transformed for analysis.

    Raises
    ------
    ValueError
        If the input list is empty or contains invalid image file names or
        URLs.
    TypeError
        If the input is not a string or a list of strings.

    Examples
    --------
    >>> preprocess_leaf_images(images='image1.jpg,image2.jpg')
    ['preprocessed_image1.jpg', 'preprocessed_image2.jpg']

    >>> preprocess_leaf_images(images=['image1.jpg', 'image2.jpg'])
    ['preprocessed_image1.jpg', 'preprocessed_image2.jpg']

    """
    
    if not isinstance(images, str):
        raise TypeError("If the input is not a string or a list of strings.")
    
    if not images or not images.strip():
        raise ValueError("If the input list is empty or contains invalid image file names or URLs.")
    
    image_list = [img.strip() for img in images.split(',')]
    image_list = [img for img in image_list if img]
    
    if not image_list:
        raise ValueError("If the input list is empty or contains invalid image file names or URLs.")
    
    valid_extensions = r'\.(jpg|jpeg|png|gif|bmp|tiff|webp)$'
    
    for img in image_list:
        if not img:
            raise ValueError("If the input list is empty or contains invalid image file names or URLs.")
        
        is_url = img.startswith(('http://', 'https://'))
        is_file = re.search(valid_extensions, img.lower())
        
        if not (is_url or is_file):
            raise ValueError("If the input list is empty or contains invalid image file names or URLs.")
    
    preprocessed_images = []
    for img in image_list:
        if img.startswith(('http://', 'https://')):
            parts = img.split('/')
            filename = parts[-1]
            base_url = '/'.join(parts[:-1])
            preprocessed_name = f"{base_url}/preprocessed_{filename}"
        else:
            preprocessed_name = f"preprocessed_{img}"
        preprocessed_images.append(preprocessed_name)
    
    return preprocessed_images