from homeassistant.components.system_log import DOMAIN as SYSTEM_LOG
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, config_entry: ConfigEntry
):
    return {"records": [i.to_dict() for i in hass.data[SYSTEM_LOG].records.values()]}
