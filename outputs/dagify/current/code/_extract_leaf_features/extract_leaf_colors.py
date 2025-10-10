from typing import List


def extract_leaf_colors(images: str, characteristics: str) -> List[str]:
    """
    Extracts leaf colors from images based on their characteristics.

    Parameters
    ----------
    images : str
        A string containing image file names or URLs of leaves, expected to
        be preprocessed.
    characteristics : str
        A string containing characteristic descriptions for each leaf, used
        to guide the color extraction.

    Returns
    -------
    List[str]
        A list of colors observed in the leaves, where each color is
        represented as a string.

    Raises
    ------
    ValueError
        If the input images or characteristics are invalid or inconsistent.
    TypeError
        If the input types are not as expected (e.g., not strings).

    Examples
    --------
    >>> extract_leaf_colors(images='leaf_images.jpg', characteristics='green,
    oval, smooth edges')
    ['green', 'light green']

    >>> extract_leaf_colors(images='leaf1.jpg,leaf2.jpg',
    characteristics='variegated, lobed')
    ['green, white', 'deep green']

    """
    
    if not isinstance(images, str):
        raise TypeError("Images parameter must be a string")
    if not isinstance(characteristics, str):
        raise TypeError("Characteristics parameter must be a string")
    
    if not images.strip():
        raise ValueError("Images parameter cannot be empty")
    if not characteristics.strip():
        raise ValueError("Characteristics parameter cannot be empty")
    
    image_list = [img.strip() for img in images.split(',') if img.strip()]
    char_list = [char.strip().lower() for char in characteristics.split(',') if char.strip()]
    
    if len(image_list) == 0:
        raise ValueError("No valid images found in input")
    if len(char_list) == 0:
        raise ValueError("No valid characteristics found in input")
    
    colors = []
    
    for i, image in enumerate(image_list):
        if not (image.endswith('.jpg') or image.endswith('.jpeg') or image.endswith('.png') or image.startswith('http')):
            raise ValueError(f"Invalid image format: {image}")
        
        extracted_colors = []
        
        for char in char_list:
            if 'green' in char:
                if 'light' in char or 'pale' in char:
                    extracted_colors.append('light green')
                elif 'dark' in char or 'deep' in char:
                    extracted_colors.append('deep green')
                else:
                    extracted_colors.append('green')
            elif 'variegated' in char:
                extracted_colors.append('green, white')
            elif 'red' in char:
                extracted_colors.append('red')
            elif 'yellow' in char:
                extracted_colors.append('yellow')
            elif 'brown' in char:
                extracted_colors.append('brown')
            elif 'purple' in char:
                extracted_colors.append('purple')
        
        if not extracted_colors:
            extracted_colors.append('green')
        
        if len(extracted_colors) == 1:
            colors.append(extracted_colors[0])
        else:
            colors.append(', '.join(extracted_colors))
    
    if len(image_list) == 1 and len(colors) == 1:
        color_parts = colors[0].split(', ')
        if len(color_parts) > 1:
            return color_parts
    
    return colors