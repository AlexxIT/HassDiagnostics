from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from . import DOMAIN


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, config_entry: ConfigEntry
):
    info = {}

    # internal system_log
    if log := hass.data.get(DOMAIN, {}).get("system_log"):
        info["system_log"] = [i for i in log.records.values()]

    # global system_log
    if log := hass.data.get("system_log"):
        info["hass_system_log"] = [i.to_dict() for i in log.records.values()]

    return info
