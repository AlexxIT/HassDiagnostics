import logging

from homeassistant.components.sensor import SensorEntity, SensorStateClass
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall

from . import DOMAIN
from .core.github import github_get_link
from .core.smart_log import convert_log_entry_to_record, parse_log_record


async def async_setup_entry(
    hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities
):
    smart_log = SmartLog()

    # import log records from global system_log
    system_log = hass.data["system_log"]
    for log_entry in system_log.records.values():
        dict_entry = log_entry.to_dict()
        record = convert_log_entry_to_record(dict_entry)
        smart_log.emit(record, dict_entry["count"])

    # store for diagnostics.py
    data = hass.data.setdefault(DOMAIN, {})
    data["smart_log"] = smart_log

    async_add_entities([smart_log], False)

    async def send_command(call: ServiceCall):
        for dict_entry in call.data["system_log"]:
            record = convert_log_entry_to_record(dict_entry)
            smart_log.emit(record, dict_entry["count"])

    hass.services.async_register(DOMAIN, "send_command", send_command)


class SmartLog(SensorEntity):
    _attr_icon = "mdi:math-log"
    _attr_name = "Smart Log"
    _attr_native_value = 0
    _attr_native_unit_of_measurement = "items"
    _attr_should_poll = False
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_unique_id = "smart_log"
    _unrecorded_attributes = {"records"}

    def __init__(self):
        self.records: dict[tuple, dict] = {}

        handler = logging.Handler(logging.WARNING)
        handler.emit = self.emit
        logging.root.addHandler(handler)

    def emit(self, record: logging.LogRecord, count: int = 1):
        entry = parse_log_record(record)
        key = (
            entry.get("domain"),
            entry.get("package"),
            entry.get("category"),
            entry.get("host"),
        )
        if item := self.records.get(key):
            item["count"] += count
        else:
            if github := github_get_link(record):
                entry["github"] = github
            entry["count"] = count
            self.records[key] = entry

        self._attr_native_value += count
        if self.hass and self.entity_id:
            self._async_write_ha_state()

    @property
    def extra_state_attributes(self):
        # fix JSON serialization
        return {"records": list(self.records.values())}
