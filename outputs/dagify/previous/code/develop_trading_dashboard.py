from pydantic import BaseModel, Field
from typing import List


class ConfigureTradingSystemOutput(BaseModel):
    """Pydantic model for configure_trading_system node outputs."""
    trading_system_status: bool = Field(..., description="Whether the trading system has been successfully configured")
    configuration_parameters: str = Field(..., description="List of configuration parameters used in the trading system")
    market_environment_details: str = Field(..., description="Details of the market environment, including trading accounts, APIs, and exchange links")
    trading_rules_implemented: str = Field(..., description="List of trading rules implemented in the trading system")


class DevelopTradingDashboardOutput(BaseModel):
    """Pydantic model for develop_trading_dashboard node outputs."""
    dashboard_name: str = Field(..., description="The name of the trading dashboard")
    metrics_used: List[str] = Field(..., description="A list of metrics used in the trading dashboard")
    data_feeds: List[str] = Field(..., description="A list of real-time data feeds used in the trading dashboard")
    analytics_tools: List[str] = Field(..., description="A list of analytics tools used in the trading dashboard")
    alert_system: bool = Field(..., description="Whether the trading dashboard has an alert system")
    dashboard_url: str = Field(..., description="The URL of the trading dashboard")


def develop_trading_dashboard(configure_trading_system_input: ConfigureTradingSystemOutput, **kwargs) -> DevelopTradingDashboardOutput:
    """
    Develop a trading dashboard to monitor the performance of the trading
    workflow.

    Parameters
    ----------
    trading_system_status : bool
        Whether the trading system has been successfully configured
    configuration_parameters : str
        List of configuration parameters used in the trading system
    market_environment_details : str
        Details of the market environment, including trading accounts, APIs,
        and exchange links
    trading_rules_implemented : List[str]
        List of trading rules implemented in the trading system

    Returns
    -------
    dict
        A dictionary containing the dashboard_name, metrics_used,
        data_feeds, analytics_tools, alert_system, and dashboard_url

    Raises
    ------
    ValueError
        If the trading system status is False or if the configuration
        parameters are invalid

    Examples
    --------
    >>> develop_trading_dashboard(trading_system_status=True,
    configuration_parameters='param1,param2',
    market_environment_details='market_env',
    trading_rules_implemented=['rule1','rule2'])
    {'dashboard_name': 'Trading Dashboard', 'metrics_used':
    ['metric1','metric2'], 'data_feeds': ['feed1','feed2'], 'analytics_tools':
    ['tool1','tool2'], 'alert_system': True, 'dashboard_url':
    'https://dashboard.com'}

    """
    return DevelopTradingDashboardOutput(
        dashboard_name="",
        metrics_used=[],
        data_feeds=[],
        analytics_tools=[],
        alert_system=False,
        dashboard_url="",
    )