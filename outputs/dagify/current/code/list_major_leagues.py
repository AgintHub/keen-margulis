from ._list_major_leagues.validate_sport_input import validate_sport_input
from ._list_major_leagues.get_sport_league_mapping import get_sport_league_mapping
from ._list_major_leagues.retrieve_leagues_for_sport import retrieve_leagues_for_sport
from ._list_major_leagues.curate_prominent_leagues import curate_prominent_leagues

from pydantic import BaseModel, Field
from typing import List


class IdentifySportOutput(BaseModel):
    """Pydantic model for identify_sport node outputs."""
    selected_sport: str = (
        Field(..., description = (
            "The name of the sport identified or specified by the user")
        )
    )


class ListMajorLeaguesOutput(BaseModel):
    """Pydantic model for list_major_leagues node outputs."""
    league_names: List[str] = (
        Field(..., description = (
            "List of major professional leagues for the identified sport")
        )
    )


def list_major_leagues(identify_sport_input: IdentifySportOutput, **kwargs) -> ListMajorLeaguesOutput:
    """
    Enumerates the major professional leagues for a specified sport.

    Parameters
    ----------
    selected_sport : str
        The name of the sport for which to retrieve major professional
        leagues. Must be a non-empty string and match one of the supported
        sports.

    Returns
    -------
    List[str]
        A list of league names (strings) representing the top professional
        leagues associated with the input sport.

    Raises
    ------
    ValueError
        Raised if `selected_sport` is an empty string or if the sport is not
        recognized in the internal league mapping.

    Examples
    --------
    >>> league_names = list_major_leagues(selected_sport="basketball")
    ["NBA", "EuroLeague", "NBL", "CBA", "Liga ACB"]

    >>> league_names = list_major_leagues(selected_sport="soccer")
    ["Premier League", "La Liga", "Bundesliga", "Serie A", "Ligue 1"]

    """
    selected_sport: str = identify_sport_input.selected_sport
    
    validated_sport: str = validate_sport_input(sport_name=selected_sport)
    
    league_mapping: dict = get_sport_league_mapping()
    
    major_leagues: List[str] = retrieve_leagues_for_sport(sport=validated_sport, mapping=league_mapping)
    
    curated_leagues: List[str] = curate_prominent_leagues(leagues=major_leagues, sport=validated_sport)
    
    return ListMajorLeaguesOutput(league_names=curated_leagues)