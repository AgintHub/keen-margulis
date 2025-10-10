import json


def parse_market_data_params(input_string: str, kwargs: str) -> str:
    """
    Parses input string and keyword arguments into a dictionary of market data
    parameters.

    Parameters
    ----------
    input_string : str
        The input string containing market data parameters in a specific
        format.
    kwargs : str
        Additional keyword arguments containing market data parameters.

    Returns
    -------
    str
        A JSON string representing a dictionary with keys 'assets',
        'start_date', and 'end_date'.

    Raises
    ------
    ValueError
        If the input string or keyword arguments are invalid or missing
        required parameters.
    TypeError
        If the input types are incorrect or cannot be parsed.

    Examples
    --------
    >>> parse_market_data_params(input_string='assets:AAPL,GOOG;start_date:2022-
    01-01;end_date:2022-12-31', kwargs='{}')
    >>> parse_market_data_params(input_string='assets:MSFT;start_date:2023-01-
    01;end_date:2023-06-30', kwargs='{"assets": ["MSFT"]}')
    >>> parse_market_data_params(input_string='', kwargs='{"assets": ["AAPL",
    "GOOG"], "start_date": "2022-01-01", "end_date": "2022-12-31"}')
    {"assets": ["AAPL", "GOOG"], "start_date": "2022-01-01", "end_date":
    "2022-12-31"}

    """
    
    result = {}
    
    try:
        kwargs_dict = json.loads(kwargs) if kwargs.strip() else {}
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in kwargs")
    
    if not isinstance(kwargs_dict, dict):
        raise TypeError("kwargs must be a valid JSON object")
    
    result.update(kwargs_dict)
    
    if input_string.strip():
        try:
            pairs = input_string.split(';')
            for pair in pairs:
                if ':' not in pair:
                    raise ValueError(f"Invalid format in input_string: {pair}")
                key, value = pair.split(':', 1)
                key = key.strip()
                value = value.strip()
                
                if key == 'assets':
                    assets = [asset.strip() for asset in value.split(',') if asset.strip()]
                    result['assets'] = assets
                elif key in ['start_date', 'end_date']:
                    result[key] = value
                else:
                    result[key] = value
        except Exception as e:
            raise ValueError(f"Failed to parse input_string: {str(e)}")
    
    required_fields = ['assets', 'start_date', 'end_date']
    for field in required_fields:
        if field not in result:
            raise ValueError(f"Missing required parameter: {field}")
    
    if not isinstance(result['assets'], list):
        raise TypeError("assets must be a list")
    
    if not result['assets']:
        raise ValueError("assets cannot be empty")
    
    return json.dumps(result)