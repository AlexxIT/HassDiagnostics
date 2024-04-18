import logging

from custom_components.hass_diagnostics.core.smart_log import parse_log_record


def test_empty_record():
    store = []
    store_filter = logging.Filter()
    store_filter.filter = lambda record: store.append(record)

    logger = logging.getLogger(__name__)
    logger.addFilter(store_filter)
    logger.warning("test1")

    assert hasattr(store[-1], "message") is False

    entry = parse_log_record(store[-1])
    entry.pop("timestamp")
    assert entry == {
        "level": "WARNING",
        "message": "test1",
        "name": "tests.test_misc",
        "short": "test1",
    }

    logger.warning("test2", 1)

    entry = parse_log_record(store[-1])
    entry.pop("timestamp")
    assert entry == {
        "level": "WARNING",
        "message": "test2",
        "name": "tests.test_misc",
        "short": "test2",
    }
