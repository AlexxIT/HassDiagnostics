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
    smart_log = SmartLog()

    # import log records from global system_log
    if system_log := hass.data["system_log"]:
        for entry in system_log.records.values():
            entry = entry.to_dict()
            record = convert_log_entry_to_record(entry)
            smart_log.emit(record, entry["count"])

    data = hass.data.setdefault(DOMAIN, {})
    data["smart_log"] = smart_log

    async_add_entities([smart_log], False)


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
        if record := self.records.get(key):
            record["count"] += count
        else:
            entry["count"] = count
            self.records[key] = entry

        self._attr_native_value += count
        if self.hass and self.entity_id:
            self._async_write_ha_state()

    @property
    def extra_state_attributes(self):
        # fix JSON serialization
        return {"records": list(self.records.values())}


RE_CUSTOM_DOMAIN = re.compile(r"\bcustom_components[/.]([0-9a-z_]+)")
RE_DOMAIN = re.compile(r"\bcomponents[/.]([0-9a-z_]+)")
RE_CONNECTION = re.compile(r"(disconnected|not available)", flags=re.IGNORECASE)
RE_DEPRECATED = re.compile(r"will stop working in Home Assistant.+?[0-9.]+")
RE_SETUP = re.compile(r"Setup of (.+?) is taking over")
# RE_ERROR = re.compile(r"\('(.+?)'\)")
RE_PACKAGE = re.compile(r"/site-packages/([^/]+)")
RE_TEMPLATE = re.compile(r"Template<template=\((.+?)\) renders=", flags=re.DOTALL)
RE_CONNECT_TO_HOST = re.compile(r"Cannot connect to host ([^ :]+)")
RE_CONNECT = re.compile(
    r"\b(connect|connection|disconnected|socket|timed out)\b", flags=re.IGNORECASE
)
RE_IP = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
RE_LAST_LINE = re.compile(r"\n\S+Error: ([^\n]+)\n$")


def parse_log_record(record: logging.LogRecord) -> dict:
    message = short = record.message or record.getMessage()

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
    if RE_CONNECT.search(message) and (m := RE_IP.search(message)):
        entry["category"] = "connection"
        entry["host"] = m[0]
    elif m := RE_DEPRECATED.search(message):
        entry["category"] = "deprecated"
        short = "..." + m[0]
    elif m := RE_SETUP.search(message):
        entry["category"] = "performance"
        entry["domain"] = m[1]
    elif m := RE_TEMPLATE.search(message):
        entry["category"] = "template"
        short = m[1]
    elif m := RE_LAST_LINE.search(text):
        short = m[1]
        if m := RE_CONNECT_TO_HOST.search(short):
            entry["category"] = "connection"
            entry["host"] = m[1]
        elif RE_CONNECT.search(short) and (m := RE_IP.search(short)):
            entry["host"] = m[0]
            entry["category"] = "connection"

    if record.name == "homeassistant.components.websocket_api.http.connection":
        short = short.lstrip("[0123456789] ")

    if len(short) > 62:
        short = short[:59] + "..."

    entry["short"] = short.replace("\n", " ")

    return entry


def convert_log_entry_to_record(entry: dict):
    args = {
        "name": entry["name"],
        "levelname": entry["level"],
        "created": entry["timestamp"],
        "pathname": entry["source"][0],
        "message": entry["message"][0],
        "exc_info": entry["exception"] != "",
        "exc_text": entry["exception"],
    }
    return type("LogRecord", (), args)()
