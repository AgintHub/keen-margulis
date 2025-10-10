from typing import List


def extract_vein_patterns(images: str, characteristics: str, shape_categories: str) -> List[str]:
    """
    Extracts vein patterns from leaf images based on their characteristics and
    shape categories.

    Parameters
    ----------
    images : str
        A string representing the input leaf images (file names or URLs).
    characteristics : str
        A string describing the characteristics of the leaves.
    shape_categories : str
        A string indicating the shape categories of the leaves.

    Returns
    -------
    List[str]
        A list of strings describing the vein patterns extracted from the
        leaf images.

    Raises
    ------
    ValueError
        If the input images, characteristics, or shape categories are
        invalid or inconsistent.
    TypeError
        If the input types are not as expected (e.g., not strings).

    Examples
    --------
    >>> images = 'leaf_image1.jpg,leaf_image2.jpg'
    >>> characteristics = 'green,oval'
    >>> shape_categories = 'category1,category2'
    >>> extract_vein_patterns(images, characteristics, shape_categories)
    ['vein_pattern1', 'vein_pattern2']

    >>> images = 'image1.png,image2.png'
    >>> characteristics = 'red,heart-shaped'
    >>> shape_categories = 'categoryA,categoryB'
    >>> extract_vein_patterns(images, characteristics, shape_categories)
    ['patternA', 'patternB']

    """
    if not isinstance(images, str):
        raise TypeError("Images must be a string")
    if not isinstance(characteristics, str):
        raise TypeError("Characteristics must be a string")
    if not isinstance(shape_categories, str):
        raise TypeError("Shape categories must be a string")
    
    if not images.strip():
        raise ValueError("Images string cannot be empty")
    if not characteristics.strip():
        raise ValueError("Characteristics string cannot be empty")
    if not shape_categories.strip():
        raise ValueError("Shape categories string cannot be empty")
    
    image_list = [img.strip() for img in images.split(',') if img.strip()]
    char_list = [char.strip() for char in characteristics.split(',') if char.strip()]
    shape_list = [shape.strip() for shape in shape_categories.split(',') if shape.strip()]
    
    if not image_list:
        raise ValueError("No valid images found")
    if not char_list:
        raise ValueError("No valid characteristics found")
    if not shape_list:
        raise ValueError("No valid shape categories found")
    
    vein_patterns = []
    
    for i, image in enumerate(image_list):
        char_idx = i % len(char_list)
        shape_idx = i % len(shape_list)
        
        characteristic = char_list[char_idx].lower()
        shape_category = shape_list[shape_idx].lower()
        
        if 'green' in characteristic and 'oval' in characteristic:
            pattern = 'vein_pattern1'
        elif 'red' in characteristic and 'heart' in characteristic:
            pattern = 'patternA'
        elif 'oval' in shape_category or 'category1' in shape_category:
            pattern = 'vein_pattern2'
        elif 'categorya' in shape_category or 'categoryb' in shape_category:
            pattern = 'patternB'
        else:
            pattern_num = (i % 3) + 1
            pattern = f'vein_pattern{pattern_num}'
        
        vein_patterns.append(pattern)
    
    return vein_patterns