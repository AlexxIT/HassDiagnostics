from logging import LogRecord
from urllib.parse import urlencode

from homeassistant.const import __version__


def github_get_link(record: LogRecord) -> str | None:
    if record.pathname.startswith("/usr/src/homeassistant/"):
        base = f"https://github.com/home-assistant/core/blob"
        return f"{base}/{__version__}/{record.pathname[23:]}#L{record.lineno}"

    if record.pathname.startswith("/config/custom_components"):
        query = urlencode(
            {"q": f"path:{record.pathname[8:]} {record.funcName}", "type": "code"}
        )
        return f"https://github.com/search?{query}#L{record.lineno}"

    return None
