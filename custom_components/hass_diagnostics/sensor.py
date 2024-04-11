import logging
import re
import traceback

from homeassistant.components.sensor import SensorEntity, SensorStateClass
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from . import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities
):
    data = hass.data.setdefault(DOMAIN, {})
    data["system_log"] = system_log = SystemLogSensor()
    async_add_entities([system_log], False)


class SystemLogSensor(SensorEntity):
    _attr_icon = "mdi:math-log"
    _attr_name = "System Log"
    _attr_native_value = 0
    _attr_native_unit_of_measurement = "items"
    _attr_should_poll = False
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_unique_id = "system_log"
    _unrecorded_attributes = {"records"}

    def __init__(self):
        self.records: dict[tuple, dict] = {}

        self._attr_extra_state_attributes = {"records": self.records.values()}

        handler = logging.Handler(logging.WARNING)
        handler.emit = self.emit
        logging.root.addHandler(handler)

    def emit(self, record: logging.LogRecord):
        entry = parse_log_record(record)
        key = (entry.get("domain"), entry.get("package"), entry.get("category"))
        if record := self.records.get(key):
            record["count"] += 1
        else:
            entry["count"] = 1
            self.records[key] = entry

        self.internal_update()

    def internal_update(self):
        self._attr_native_value = len(self.records)

        if self.hass and self.entity_id:
            self._async_write_ha_state()


RE_CUSTOM_DOMAIN = re.compile(r"\bcustom_components[/.]([0-9a-z_]+)")
RE_DOMAIN = re.compile(r"\bcomponents[/.]([0-9a-z_]+)")
RE_CONNECTION = re.compile(r"(disconnected|not available)", flags=re.IGNORECASE)
RE_DEPRECATED = re.compile(r"will stop working in Home Assistant.+?[0-9.]+")
RE_SETUP = re.compile(r"Setup of (.+?) is taking over")
# RE_ERROR = re.compile(r"\('(.+?)'\)")
RE_PACKAGE = re.compile(r"/site-packages/([^/]+)")
RE_TEMPLATE = re.compile(r"Template<template=\((.+?)\) renders=", flags=re.DOTALL)
RE_CONNECT_TO_HOST = re.compile(r"Cannot connect to host [^ ]+")
RE_CONNECT = re.compile(r"\b(connect|connection|socket)\b", flags=re.IGNORECASE)
RE_HOST = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")


def parse_log_record(record: logging.LogRecord) -> dict:
    message = record.message or record.getMessage()

    # base info
    entry = {
        "name": record.name,
        "level": record.levelname,
        "message": message,
        "timestamp": record.created,
    }

    # domain from name, message and exception
    text = f"{record.name}\n{message}\n"
    if record.exc_info:
        text += record.exc_text or str(traceback.format_exception(*record.exc_info))

    if m := RE_CUSTOM_DOMAIN.search(text):
        entry["domain"] = m[1]
    elif m := RE_DOMAIN.findall(text):
        entry["domain"] = m[-1]

    # package from pathname
    if m := RE_PACKAGE.search(record.pathname):
        entry["package"] = m[1]

    # short and category
    short = message

    if RE_CONNECT.search(message) and (m := RE_HOST.search(message)):
        entry["category"] = "connection"
        short = "Error connect to " + m[0]
    elif m := RE_DEPRECATED.search(message):
        entry["category"] = "deprecated"
        short = "..." + m[0]
    elif m := RE_SETUP.search(message):
        entry["category"] = "performance"
        entry["domain"] = m[1]
    elif m := RE_TEMPLATE.search(message):
        entry["category"] = "template"
        short = m[1]
    elif m := RE_CONNECT_TO_HOST.search(text):
        entry["category"] = "connection"
        short = m[0]

    if record.name == "homeassistant.components.websocket_api.http.connection":
        short = short.lstrip("[0123456789] ")

    if len(short) > 62:
        short = short[:59] + "..."

    entry["short"] = short.replace("\n", " ")

    return entry
