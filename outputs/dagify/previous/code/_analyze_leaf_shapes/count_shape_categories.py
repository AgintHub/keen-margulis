from typing import List


def count_shape_categories(categories: str) -> List[int]:
    """
    Counts the occurrences of each shape category in the given list of
    categories.

    Parameters
    ----------
    categories : str
        A string representing the shape categories, expected to be a list or
        a string that can be parsed into a list of categories.

    Returns
    -------
    List[int]
        A list of integers where each integer represents the count of a
        unique shape category in the input.

    Raises
    ------
    ValueError
        If the input categories are not in an expected format or if there's
        an issue parsing the categories.
    TypeError
        If the input categories are not of type str or if the parsed
        categories are not as expected.

    Examples
    --------
    >>> count_shape_categories(categories='category1,category2,category1')
    [2, 1]

    >>> count_shape_categories(categories='oval, lance, oval, round')
    [2, 1, 1]

    """
    if not isinstance(categories, str):
        raise TypeError("Input categories must be of type str")
    
    if not categories.strip():
        raise ValueError("Input categories string is empty or contains only whitespace")
    
    try:
        category_list = [cat.strip() for cat in categories.split(',')]
        category_list = [cat for cat in category_list if cat]  # Remove empty strings
        
        if not category_list:
            raise ValueError("No valid categories found after parsing")
        
        unique_categories = []
        counts = []
        
        for category in category_list:
            if category in unique_categories:
                index = unique_categories.index(category)
                counts[index] += 1
            else:
                unique_categories.append(category)
                counts.append(1)
        
        return counts
    
    except Exception as e:
        if isinstance(e, (ValueError, TypeError)):
            raise
        raise ValueError("Error parsing categories") from e