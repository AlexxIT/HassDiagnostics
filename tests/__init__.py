from custom_components.hass_diagnostics.sensor import (
    convert_log_entry_to_record,
    parse_log_record,
)


def parse_log_entry(entry: dict) -> dict:
    record = convert_log_entry_to_record(entry)
    p = parse_log_record(record)
    return {
        k: v
        for k, v in p.items()
        if k in ("name", "category", "domain", "package", "short")
    }
