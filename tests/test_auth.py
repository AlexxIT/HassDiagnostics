from . import parse_log_entry


def test_ban():
    entry = {
        "name": "homeassistant.components.http.ban",
        "message": [
            "Login attempt or request with invalid authentication from MACM1 (192.168.1.123). Requested URL: '/api/websocket'. (Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36)"
        ],
        "level": "WARNING",
        "source": [
            "C:\\venv\\hass-py312\\Lib\\site-packages\\homeassistant\\components\\http\\ban.py",
            138,
        ],
        "timestamp": 1712904723.8199923,
        "exception": "",
        "count": 2,
        "first_occurred": 1712904722.8587666,
    }
    assert parse_log_entry(entry) == {
        "category": "login",
        "domain": "http",
        "host": "192.168.1.123",
        "name": "homeassistant.components.http.ban",
        "short": "Login attempt or request with invalid authentication from M...",
    }
