from homeassistant.const import REQUIRED_PYTHON_VER

from custom_components.hass_diagnostics import *
from custom_components.hass_diagnostics.config_flow import *
from custom_components.hass_diagnostics.diagnostics import *
from custom_components.hass_diagnostics.sensor import *


def test_backward():
    # https://github.com/home-assistant/core/blob/2023.2.0/homeassistant/const.py
    assert REQUIRED_PYTHON_VER >= (3, 10, 0)

    assert async_setup_entry, async_unload_entry
    assert FlowHandler, OptionsFlowHandler
    assert async_get_config_entry_diagnostics
    assert SmartLog, StartTime
