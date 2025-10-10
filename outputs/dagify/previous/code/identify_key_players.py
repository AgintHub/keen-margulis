from ._identify_key_players.validate_inputs import validate_inputs
from ._identify_key_players.fetch_top_players_for_sport import fetch_top_players_for_sport
from ._identify_key_players.filter_active_players import filter_active_players
from ._identify_key_players.map_players_to_leagues import map_players_to_leagues
from ._identify_key_players.select_best_players import select_best_players
from ._identify_key_players.extract_player_names import extract_player_names
from ._identify_key_players.extract_player_leagues import extract_player_leagues

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


class IdentifyKeyPlayersOutput(BaseModel):
    """Pydantic model for identify_key_players node outputs."""
    player_names: List[str] = (
        Field(..., description="Names of the 3-5 key players")
    )
    player_leagues: List[str] = (
        Field(..., description="Leagues corresponding to each player")
    )


def identify_key_players(identify_sport_input: IdentifySportOutput, list_major_leagues_input: ListMajorLeaguesOutput, **kwargs) -> IdentifyKeyPlayersOutput:
    """
    Retrieve 3–5 prominent active players for a specified sport along with the
    league each player belongs to.

    Parameters
    ----------
    selected_sport : str
        The sport for which key players should be identified (e.g.,
        'soccer', 'basketball').
    league_names : List[str]
        A list of major professional leagues associated with the sport,
        obtained from the `list_major_leagues` node.

    Returns
    -------
    Tuple[List[str], List[str]]
        A tuple containing two lists: the first list holds the names of 3‑5
        key players, and the second list holds the corresponding league
        names for each player.

    Raises
    ------
    ValueError
        Raised if the function cannot find at least three suitable players
        or if the input lists are empty.

    Examples
    --------
    >>> player_names, player_leagues = identify_key_players(
    ...     'soccer',
    ...     ['Premier League', 'La Liga', 'Serie A']
    >>> )
    (['Lionel Messi', 'Cristiano Ronaldo', 'Neymar Jr.'], ['Premier League', 'La
    Liga', 'Serie A'])

    >>> names, leagues = identify_key_players(
    ...     'basketball',
    ...     ['NBA', 'EuroLeague']
    >>> )
    (['LeBron James', 'Kevin Durant', 'Stephen Curry'], ['NBA', 'NBA', 'NBA'])

    """
    sport: str = identify_sport_input.selected_sport
    leagues: List[str] = list_major_leagues_input.league_names
    
    validated_inputs: bool = validate_inputs(sport=sport, leagues=leagues)
    if not validated_inputs:
        raise ValueError("Input lists are empty or invalid")
    
    top_players_data: List[dict] = fetch_top_players_for_sport(sport=sport, target_count=5)
    
    filtered_players: List[dict] = filter_active_players(players_data=top_players_data)
    
    players_with_leagues: List[dict] = map_players_to_leagues(players=filtered_players, available_leagues=leagues)
    
    final_selection: List[dict] = select_best_players(players_with_leagues=players_with_leagues, min_count=3, max_count=5)
    
    if len(final_selection) < 3:
        raise ValueError("Cannot find at least three suitable players")
    
    player_names: List[str] = extract_player_names(player_data=final_selection)
    player_leagues: List[str] = extract_player_leagues(player_data=final_selection)
    
    return IdentifyKeyPlayersOutput(
        player_names=player_names,
        player_leagues=player_leagues
    )