from typing import List


def extract_shape_categories(images: str, characteristics: str) -> List[str]:
    """
    Extract shape categories from leaf images and their characteristics.

    Parameters
    ----------
    images : List[str]
        List of image file names or URLs of leaves.
    characteristics : List[str]
        List of characteristic descriptions for each leaf.

    Returns
    -------
    List[str]
        List of shape categories for the leaves.

    Raises
    ------
    ValueError
        When the lengths of images and characteristics lists do not match.
    TypeError
        When the input types are not as expected (e.g., not lists or not
        strings).

    Examples
    --------
    >>> images = ['leaf1.jpg', 'leaf2.jpg']
    >>> characteristics = ['oval', 'lanceolate']
    >>> shape_categories = extract_shape_categories(images, characteristics)
    ['oval', 'lanceolate']

    >>> images = ['leaf3.jpg']
    >>> characteristics = ['heart-shaped']
    >>> shape_categories = extract_shape_categories(images, characteristics)
    ['heart-shaped']

    """
    if not isinstance(images, list) or not isinstance(characteristics, list):
        raise TypeError("Both images and characteristics must be lists")
    
    if not all(isinstance(img, str) for img in images):
        raise TypeError("All items in images list must be strings")
    
    if not all(isinstance(char, str) for char in characteristics):
        raise TypeError("All items in characteristics list must be strings")
    
    if len(images) != len(characteristics):
        raise ValueError("The lengths of images and characteristics lists do not match")
    
    shape_categories = []
    for characteristic in characteristics:
        characteristic = characteristic.strip().lower()
        if 'oval' in characteristic:
            shape_categories.append('oval')
        elif 'lanceolate' in characteristic:
            shape_categories.append('lanceolate')
        elif 'heart' in characteristic:
            shape_categories.append('heart-shaped')
        else:
            shape_categories.append(characteristic)
    
    return shape_categories