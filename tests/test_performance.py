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


def test_took_longer():
    entry = {
        "name": "homeassistant.components.media_player",
        "message": [
            "Updating samsungtv media_player took longer than the scheduled update interval 0:00:10"
        ],
        "level": "WARNING",
        "source": ["helpers/entity_platform.py", 1010],
        "timestamp": 1712901964.4957683,
        "exception": "",
        "count": 2,
        "first_occurred": 1712901954.4951386,
    }
    assert parse_log_entry(entry) == {
        "category": "performance",
        "domain": "samsungtv",
        "name": "homeassistant.components.media_player",
        "short": "Updating samsungtv media_player took longer than the schedu...",
    }
