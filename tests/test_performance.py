from . import parse_log_entry


def test_is_taking_over():
    entry = {
        "name": "homeassistant.setup",
        "message": ["Setup of dataplicity is taking over 10 seconds."],
        "level": "WARNING",
        "source": ["runner.py", 189],
        "timestamp": 1712755906.1509893,
        "exception": "",
        "count": 1,
        "first_occurred": 1712755906.1509893,
    }
    assert parse_log_entry(entry) == {
        "category": "performance",
        "domain": "dataplicity",
        "name": "homeassistant.setup",
        "short": "Setup of dataplicity is taking over 10 seconds.",
    }
