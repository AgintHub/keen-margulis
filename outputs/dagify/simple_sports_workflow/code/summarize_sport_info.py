from pydantic import BaseModel, Field
from typing import List


class GatherSportInfoOutput(BaseModel):
    """Pydantic model for gather_sport_info node outputs."""
    rules: List[str] = (
        Field(..., description="List of key rules governing the sport")
    )
    popular_leagues: List[str] = (
        Field(..., description="List of major professional leagues associated with the sport")
    )
    major_tournaments: List[str] = (
        Field(..., description="List of major international tournaments or competitions for the sport")
    )


class DetermineSportTypeOutput(BaseModel):
    """Pydantic model for determine_sport_type node outputs."""
    sport_type: str = (
        Field(..., description="Whether the sport is team-based or individual")
    )
    rationale: str = (
        Field(..., description="One-sentence explanation for the classification")
    )


class ListMajorLeaguesOutput(BaseModel):
    """Pydantic model for list_major_leagues node outputs."""
    league_names: List[str] = (
        Field(..., description="List of major professional leagues for the identified sport")
    )


class IdentifyKeyPlayersOutput(BaseModel):
    """Pydantic model for identify_key_players node outputs."""
    player_names: List[str] = (
        Field(..., description="Names of the 3-5 key players")
    )
    player_leagues: List[str] = (
        Field(..., description="Leagues corresponding to each player")
    )


class SummarizeSportInfoOutput(BaseModel):
    """Pydantic model for summarize_sport_info node outputs."""
    sport_type: str = (
        Field(..., description="Whether the sport is team-based or individual.")
    )
    major_leagues: List[str] = (
        Field(..., description="List of major professional leagues associated with the sport.")
    )
    key_players: List[str] = (
        Field(..., description="List of 3-5 key players currently active in the sport and their respective leagues.")
    )
    summary: str = (
        Field(..., description="Concise summary of the sport, not exceeding 200 words.")
    )
    word_count: int = Field(..., description="Number of words in the summary.")


def summarize_sport_info(gather_sport_info_input: GatherSportInfoOutput, determine_sport_type_input: DetermineSportTypeOutput, list_major_leagues_input: ListMajorLeaguesOutput, identify_key_players_input: IdentifyKeyPlayersOutput, **kwargs) -> SummarizeSportInfoOutput:
    """
    Generate a concise summary of a sport and return a structured dictionary
    with metadata.

    Parameters
    ----------
    sport_type : str
        Classification of the sport, e.g., "team-based" or "individual".
    major_leagues : List[str]
        Names of the major professional leagues for the sport.
    key_players : List[str]
        A list of 3–5 active players and their leagues (formatted as "Player
        – League").

    Returns
    -------
    Dict[str, Any]
        Dictionary containing sport_type (str), major_leagues (List[str]),
        key_players (List[str]), summary (str), and word_count (int).

    Raises
    ------
    ValueError
        If the constructed summary exceeds 200 words.
    TypeError
        If any input parameter is of an unexpected type.

    Examples
    --------
    >>> result = summarize_sport_info(
    ...     sport_type='team-based',
    ...     major_leagues=['NBA', 'EuroLeague'],
    ...     key_players=['LeBron James – NBA', 'Giannis Antetokounmpo – NBA']
    >>> )
    >>> print(result['summary'])
    "Basketball is a team-based sport played worldwide, with major leagues such
    as the NBA and EuroLeague showcasing elite talent. Key players include
    LeBron James and Giannis Antetokounmpo, both stars of the NBA."
    "word_count: 27"

    >>> summary_data = summarize_sport_info(
    ...     sport_type='team-based',
    ...     major_leagues=['Premier League', 'La Liga', 'Serie A'],
    ...     key_players=['Lionel Messi – La Liga', 'Cristiano Ronaldo – Serie
    A', 'Kevin De Bruyne – Premier League']
    >>> )
    >>> print(summary_data['summary'])
    "Football (soccer) is a team-based sport with premier competitions including
    the Premier League, La Liga, and Serie A. Notable players feature Lionel
    Messi and Cristiano Ronaldo in top European clubs, along with Kevin De
    Bruyne."
    "word_count: 31"

    """
    return SummarizeSportInfoOutput(
        sport_type="",
        major_leagues=[],
        key_players=[],
        summary="",
        word_count=0,
    )