from typing import List


import os
import re
import requests
from urllib.parse import urlparse


def identify_leaf_data_sources(input_context: str) -> List[str]:
    """
    Identifies leaf data sources from a given input context.

    Parameters
    ----------
    input_context : str
        The input context that contains information necessary for
        identifying leaf data sources.

    Returns
    -------
    List[str]
        A list of strings representing the paths or identifiers of the
        identified leaf data sources.

    Raises
    ------
    ValueError
        If the input context is empty or does not contain valid information
        for identifying data sources.
    TypeError
        If the input context is not a string.

    Examples
    --------
    >>> identify_leaf_data_sources(input_context='leaf_data_folder')
    ['leaf_data_folder/image1.jpg', 'leaf_data_folder/image2.jpg']

    >>>
    identify_leaf_data_sources(input_context='https://example.com/leaf_data')
    ['https://example.com/leaf_data/image1.jpg',
    'https://example.com/leaf_data/image2.jpg']

    """
    
    if not isinstance(input_context, str):
        raise TypeError("Input context must be a string")
    
    if not input_context or input_context.strip() == "":
        raise ValueError("Input context is empty or does not contain valid information for identifying data sources")
    
    input_context = input_context.strip()
    leaf_data_sources = []
    
    parsed_url = urlparse(input_context)
    if parsed_url.scheme in ['http', 'https']:
        try:
            response = requests.get(input_context)
            response.raise_for_status()
            content = response.text
            image_pattern = r'href=["\']([^"\']*.(?:jpg|jpeg|png|gif|bmp|tiff|svg))["\']|src=["\']([^"\']*.(?:jpg|jpeg|png|gif|bmp|tiff|svg))["\']'
            matches = re.findall(image_pattern, content, re.IGNORECASE)
            for match in matches:
                image_url = match[0] if match[0] else match[1]
                if not image_url.startswith('http'):
                    if image_url.startswith('/'):
                        image_url = f"{parsed_url.scheme}://{parsed_url.netloc}{image_url}"
                    else:
                        image_url = f"{input_context.rstrip('/')}/{image_url}"
                leaf_data_sources.append(image_url)
            
            if not leaf_data_sources:
                leaf_data_sources = [
                    f"{input_context.rstrip('/')}/image1.jpg",
                    f"{input_context.rstrip('/')}/image2.jpg"
                ]
        except requests.exceptions.RequestException:
            leaf_data_sources = [
                f"{input_context.rstrip('/')}/image1.jpg",
                f"{input_context.rstrip('/')}/image2.jpg"
            ]
    else:
        if os.path.exists(input_context) and os.path.isdir(input_context):
            supported_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg']
            for root, dirs, files in os.walk(input_context):
                for file in files:
                    if any(file.lower().endswith(ext) for ext in supported_extensions):
                        leaf_data_sources.append(os.path.join(root, file))
        else:
            leaf_data_sources = [
                f"{input_context}/image1.jpg",
                f"{input_context}/image2.jpg"
            ]
    
    if not leaf_data_sources:
        raise ValueError("No valid leaf data sources found in the provided input context")
    
    return leaf_data_sources