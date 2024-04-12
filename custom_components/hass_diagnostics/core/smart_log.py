import re
import traceback
from logging import LogRecord

RE_CUSTOM_DOMAIN = re.compile(r"\bcustom_components[/.]([0-9a-z_]+)")
RE_DOMAIN = re.compile(r"\bcomponents[/.]([0-9a-z_]+)")
RE_DEPRECATED = re.compile(r"will stop working in Home Assistant.+?[0-9.]+")
RE_SETUP = re.compile(r"^Setup of ([^ ]+) is taking over")
RE_UPDATING = re.compile(r"^Updating ([^ ]+) [^ ]+ took longer than")
RE_PACKAGE = re.compile(r"/site-packages/([^/]+)")
RE_TEMPLATE = re.compile(r"Template<template=\((.+?)\) renders=", flags=re.DOTALL)
RE_CONNECT_TO_HOST = re.compile(r"Cannot connect to host ([^ :]+)")
RE_CONNECT = re.compile(
    r"\b(connect|connection|disconnected|socket|timed out)\b", flags=re.IGNORECASE
)
RE_IP = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
RE_LOGIN = re.compile(r"^Login attempt or request [^(]+\(([^)]+)")
RE_LAST_LINE = re.compile(r"\n\S+Error: ([^\n]+)\n$")


def parse_log_record(record: LogRecord) -> dict:
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
    if m := RE_CONNECT_TO_HOST.search(text):
        entry["category"] = "connection"
        entry["host"] = m[1]
    elif RE_CONNECT.search(message) and (m := RE_IP.search(message)):
        entry["category"] = "connection"
        entry["host"] = m[0]
    elif m := RE_DEPRECATED.search(message):
        entry["category"] = "deprecated"
        short = "..." + m[0]
    elif m := RE_SETUP.search(message):
        entry["category"] = "performance"
        entry["domain"] = m[1]
    elif m := RE_UPDATING.search(message):
        entry["category"] = "performance"
        entry["domain"] = m[1]
    elif m := RE_TEMPLATE.search(message):
        entry["category"] = "template"
        short = m[1]
    elif m := RE_LOGIN.search(message):
        entry["category"] = "login"
        entry["host"] = m[1]
    elif m := RE_LAST_LINE.search(text):
        short = m[1]
        if RE_CONNECT.search(short) and (m := RE_IP.search(short)):
            entry["category"] = "connection"
            entry["host"] = m[0]

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
