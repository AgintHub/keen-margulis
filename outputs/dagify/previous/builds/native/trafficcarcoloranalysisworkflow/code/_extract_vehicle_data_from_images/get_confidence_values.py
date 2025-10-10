from typing import List


def get_confidence_values(colors_and_scores: str) -> List[float]:
    """
    Extracts confidence scores from a string containing color and confidence
    information.

    Parameters
    ----------
    colors_and_scores : str
        Input string containing color information along with their
        confidence scores, formatted in a way that can be parsed to extract
        confidence scores.

    Returns
    -------
    List[float]
        A list of floating-point numbers representing the confidence scores
        for the detected colors.

    Raises
    ------
    ValueError
        If the input string is not in the expected format or if confidence
        scores cannot be extracted.
    TypeError
        If the input is not a string.

    Examples
    --------
    >>> colors_and_scores = 'red:0.8,blue:0.9,green:0.7'
    >>> confidence_scores = get_confidence_values(colors_and_scores)
    [0.8, 0.9, 0.7]

    >>> colors_and_scores = 'yellow:0.95,black:0.85'
    >>> confidence_scores = get_confidence_values(colors_and_scores)
    [0.95, 0.85]

    """
    if not isinstance(colors_and_scores, str):
        raise TypeError("Input must be a string")
    
    if not colors_and_scores.strip():
        raise ValueError("Input string cannot be empty")
    
    confidence_scores = []
    
    try:
        color_pairs = colors_and_scores.split(',')
        
        for pair in color_pairs:
            pair = pair.strip()
            if ':' not in pair:
                raise ValueError(f"Invalid format in pair: {pair}")
            
            color, score_str = pair.split(':', 1)
            
            if not color.strip() or not score_str.strip():
                raise ValueError(f"Empty color or score in pair: {pair}")
            
            try:
                score = float(score_str.strip())
                confidence_scores.append(score)
            except ValueError:
                raise ValueError(f"Invalid confidence score format: {score_str}")
                
    except Exception as e:
        if isinstance(e, (ValueError, TypeError)):
            raise
        raise ValueError("Input string is not in the expected format")
    
    return confidence_scores