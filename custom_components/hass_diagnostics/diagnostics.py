from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from . import DOMAIN


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, config_entry: ConfigEntry
):
    info = {}

    # internal system_log
    if smart_log := hass.data.get(DOMAIN, {}).get("smart_log"):
        info["smart_log"] = [i for i in smart_log.records.values()]

    # global system_log
    if system_log := hass.data["system_log"]:
        info["system_log"] = [i.to_dict() for i in system_log.records.values()]

    return info
