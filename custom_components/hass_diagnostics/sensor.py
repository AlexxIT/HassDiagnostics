import logging
import re

from aioesphomeapi import SensorStateClass
from homeassistant.components.sensor import SensorEntity
from homeassistant.components.system_log import DOMAIN as SYSTEM_LOG, LogEntry
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant


async def async_setup_entry(
    hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities
):
    records = hass.data[SYSTEM_LOG].records
    async_add_entities([SystemLogSensor(records)], False)


class SystemLogSensor(SensorEntity):
    _attr_icon = "mdi:math-log"
    _attr_name = "System Log"
    _attr_native_value = 0
    _attr_native_unit_of_measurement = "items"
    _attr_should_poll = False
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_unique_id = SYSTEM_LOG
    _unrecorded_attributes = {"records"}

    def __init__(self, records: dict):
        self.system_log_records = records
        self.records = []

        self._attr_extra_state_attributes = {"records": self.records}

        handler = logging.Handler(logging.WARNING)
        handler.emit = self.update
        logging.root.addHandler(handler)

    def update(self, *args):
        self.records.clear()

        for entry in self.system_log_records.values():
            self.records.append(parse_log_entry(entry))

        self._attr_native_value = len(self.records)

        if self.hass and self.entity_id:
            self._async_write_ha_state()


RE_CUSTOM_NAME = re.compile(r"\bcustom_components[/.]([0-9a-z_]+)")
RE_NAME = re.compile(r"\bcomponents[/.]([0-9a-z_]+)")
RE_CONNECTION = re.compile(r"(disconnected|not available)", flags=re.IGNORECASE)
RE_DEPRECATED = re.compile(r"will stop working in Home Assistant.+?[0-9.]+")
RE_SETUP = re.compile(r"Setup of (.+?) is taking over")


def parse_log_entry(entry: LogEntry) -> dict:
    record = {
        "name": entry.name,
        "level": entry.level,
        "timestamp": entry.timestamp,
        "count": entry.count,
        "first_occurred": entry.first_occurred,
    }

    text = f"{entry.name}\n{entry.message}\n{entry.exception}"
    if domains := (RE_CUSTOM_NAME.findall(text) or RE_NAME.findall(text)):
        record["domains"] = sorted(set(domains))

    message = entry.message[0]
    text = str(entry.message)

    if "Cannot connect to host" in text:
        record["category"] = "internet"
    elif RE_CONNECTION.search(text):
        record["category"] = "connection"
    elif m := RE_DEPRECATED.search(text):
        record["category"] = "deprecated"
        message = "..." + m[0]
    elif m := RE_SETUP.findall(text):
        record["category"] = "performance"
        record["domains"] = m

    if len(message) > 62:
        message = message[:59] + "..."

    record["message"] = message

    return record
