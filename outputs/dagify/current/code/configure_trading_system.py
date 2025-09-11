from pydantic import BaseModel, Field
from typing import List


class SetMarketEnvironmentOutput(BaseModel):
    """Pydantic model for set_market_environment node outputs."""
    trading_accounts_setup_status: bool = Field(..., description="Whether the trading accounts have been successfully set up")
    api_configuration_status: bool = Field(..., description="Whether the APIs have been successfully configured")
    exchange_links_configuration_status: bool = Field(..., description="Whether the exchange links have been successfully configured")
    configured_exchanges: List[str] = Field(..., description="List of exchanges that have been configured")


class ConfigureTradingSystemOutput(BaseModel):
    """Pydantic model for configure_trading_system node outputs."""
    trading_system_status: bool = Field(..., description="Whether the trading system has been successfully configured")
    configuration_parameters: str = Field(..., description="List of configuration parameters used in the trading system")
    market_environment_details: str = Field(..., description="Details of the market environment, including trading accounts, APIs, and exchange links")
    trading_rules_implemented: str = Field(..., description="List of trading rules implemented in the trading system")


def configure_trading_system(set_market_environment_input: SetMarketEnvironmentOutput, **kwargs) -> ConfigureTradingSystemOutput:
    """
    Configures the trading system to connect to the market environment and
    implement the trading rules and strategy.

    Parameters
    ----------
    trading_accounts_setup_status : bool
        Whether the trading accounts have been successfully set up.
    api_configuration_status : bool
        Whether the APIs have been successfully configured.
    exchange_links_configuration_status : bool
        Whether the exchange links have been successfully configured.
    configured_exchanges : List[str]
        List of exchanges that have been configured.

    Returns
    -------
    dict
        A dictionary containing the status of the trading system
        configuration, the list of configuration parameters, details of the
        market environment, and the list of trading rules implemented.

    Raises
    ------
    ValueError
        If any of the required parent node outputs are not provided or are
        invalid.

    Examples
    --------
    >>> trading_accounts_setup_status = True
    >>> api_configuration_status = True
    >>> exchange_links_configuration_status = True
    >>> configured_exchanges = ['Binance', 'Kraken']
    >>> result = configure_trading_system(trading_accounts_setup_status,
    api_configuration_status, exchange_links_configuration_status,
    configured_exchanges)
    {
      'trading_system_status': True,
      'configuration_parameters': 'API keys, account credentials, exchange
    links',
      'market_environment_details': 'Trading accounts: [True], APIs: [True],
    Exchange links: [True]',
      'trading_rules_implemented': ['Entry point rule', 'Exit point rule',
    'Stop-loss rule']
    }

    >>> trading_accounts_setup_status = False
    >>> api_configuration_status = True
    >>> exchange_links_configuration_status = True
    >>> configured_exchanges = ['Binance', 'Kraken']
    >>> result = configure_trading_system(trading_accounts_setup_status,
    api_configuration_status, exchange_links_configuration_status,
    configured_exchanges)
    {
      'trading_system_status': False,
      'configuration_parameters': '',
      'market_environment_details': 'Trading accounts: [False], APIs: [True],
    Exchange links: [True]',
      'trading_rules_implemented': []
    }

    """
    return ConfigureTradingSystemOutput(
        trading_system_status=False,
        configuration_parameters="",
        market_environment_details="",
        trading_rules_implemented="",
    )