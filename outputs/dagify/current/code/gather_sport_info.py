from ._gather_sport_info.validate_sport_name import validate_sport_name
from ._gather_sport_info.fetch_sport_rules import fetch_sport_rules
from ._gather_sport_info.get_popular_leagues import get_popular_leagues
from ._gather_sport_info.get_major_tournaments import get_major_tournaments

from pydantic import BaseModel, Field
from typing import List


class IdentifySportOutput(BaseModel):
    """Pydantic model for identify_sport node outputs."""
    selected_sport: str = (
        Field(..., description = (
            "The name of the sport identified or specified by the user")
        )
    )


class GatherSportInfoOutput(BaseModel):
    """Pydantic model for gather_sport_info node outputs."""
    rules: List[str] = (
        Field(..., description="List of key rules governing the sport")
    )
    popular_leagues: List[str] = (
        Field(..., description = (
            "List of major professional leagues associated with the sport")
        )
    )
    major_tournaments: List[str] = (
        Field(..., description = (
            "List of major international tournaments or competitions for the sport")
        )
    )


def gather_sport_info(identify_sport_input: IdentifySportOutput, **kwargs) -> GatherSportInfoOutput:
    """
    Gather general information about the identified sport.

    Parameters
    ----------
    selected_sport : str
        The name of the sport identified by the user, e.g., 'soccer',
        'basketball', 'tennis'.

    Returns
    -------
    dict
        A dictionary with three keys:   * rules (List[str]) – key rules
        governing the sport.   * popular_leagues (List[str]) – major
        professional leagues.   * major_tournaments (List[str]) – major
        international tournaments.

    Raises
    ------
    ValueError
        If `selected_sport` is empty or not recognized in the knowledge
        base.

    Examples
    --------
    >>> gather_sport_info('soccer')
    {
      'rules': [
        'Players may not use their hands except the goalkeeper.',
        'Each team has 11 players on the field.',
        'A match lasts 90 minutes with two 45‑minute halves.'
      ],
      'popular_leagues': [
        'Premier League',
        'La Liga',
        'Bundesliga',
        'Serie A'
      ],
      'major_tournaments': [
        'FIFA World Cup',
        'UEFA Champions League',
        'Copa América'
      ]
    }

    >>> gather_sport_info('basketball')
    {
      'rules': [
        'Each team has five players on the court.',
        'The game is played in four 12‑minute quarters.',
        'Players must advance the ball by dribbling or passing.'
      ],
      'popular_leagues': [
        'NBA',
        'EuroLeague',
        'NBL'
      ],
      'major_tournaments': [
        'NBA Finals',
        'FIBA World Cup',
        'Olympic Games Basketball' 
      ]
    }

    """
    selected_sport: str = identify_sport_input.selected_sport
    
    validated_sport: str = validate_sport_name(sport_name=selected_sport)
    
    sport_rules: List[str] = fetch_sport_rules(sport=validated_sport)
    
    leagues_data: List[str] = get_popular_leagues(sport=validated_sport)
    
    tournaments_data: List[str] = get_major_tournaments(sport=validated_sport)
    
    return GatherSportInfoOutput(
        rules=sport_rules,
        popular_leagues=leagues_data,
        major_tournaments=tournaments_data
    )