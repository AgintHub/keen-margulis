def extract_economic_insights(economic_analysis: str) -> str:
    """
    Generates a concise, human‑readable summary of economic factors from an
    AnalyzeEconomicInfluencesOutput instance.

    Parameters
    ----------
    economic_analysis : AnalyzeEconomicInfluencesOutput
        Pydantic model instance containing details of an economic factor
        analysis.

    Returns
    -------
    str
        A single string summarizing the economic factor name, impact,
        evidence, impact strength, time period, and consensus status.

    Raises
    ------
    ValueError
        Raised when required fields in the input model are missing or empty.
    TypeError
        Raised when the input is not an instance of
        AnalyzeEconomicInfluencesOutput.

    Examples
    --------
    >>> economic_data =
    AnalyzeEconomicInfluencesOutput(economic_factor_name='Industrial
    Production', impact_summary='Increase in production led to inflation',
    evidence_sources='Data from 1920 Census', impact_strength=0.8,
    time_period_affected='1920-1925', is_consensus=True)
    >>> print(extract_economic_insights(economic_analysis=economic_data))
    "Economic Factor: Industrial Production; Impact: Increase in production led
    to inflation; Evidence: Data from 1920 Census; Impact Strength: 0.8; Time
    Period: 1920-1925; Consensus: Yes"

    >>> economic_data =
    AnalyzeEconomicInfluencesOutput(economic_factor_name='Trade Imbalance',
    impact_summary='Exports outpaced imports', evidence_sources='World Bank
    2000', impact_strength=0.6, time_period_affected='2000-2005',
    is_consensus=False)
    >>> print(extract_economic_insights(economic_analysis=economic_data))
    "Economic Factor: Trade Imbalance; Impact: Exports outpaced imports;
    Evidence: World Bank 2000; Impact Strength: 0.6; Time Period: 2000-2005;
    Consensus: No"

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")