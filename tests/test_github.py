from homeassistant.const import __version__

from custom_components.hass_diagnostics.core.github import github_get_link


def fake_github_get_link(args: dict):
    record = type("LogRecord", (), args)()
    return github_get_link(record)


def test_homeassistant():
    entry = {
        "pathname": "/usr/src/homeassistant/homeassistant/components/yeelight/light.py",
        "lineno": 257,
    }
    actual = fake_github_get_link(entry)
    expected = f"https://github.com/home-assistant/core/blob/{__version__}/homeassistant/components/yeelight/light.py#L257"
    assert actual == expected


def test_adaptive_lighting():
    entry = {
        "pathname": "/config/custom_components/adaptive_lighting/hass_utils.py",
        "lineno": 62,
        "funcName": "service_func_proxy",
    }
    actual = fake_github_get_link(entry)
    expected = "https://github.com/search?q=path%3Acustom_components%2Fadaptive_lighting%2Fhass_utils.py+service_func_proxy&type=code#L62"
    assert actual == expected


def test_pychromecast():
    entry = {
        "pathname": "/usr/local/lib/python3.12/site-packages/pychromecast/dial.py",
        "lineno": 159,
        "funcName": "get_cast_type",
    }
    actual = fake_github_get_link(entry)
    expected = "https://github.com/search?q=path%3Apychromecast%2Fdial.py+get_cast_type&type=code#L159"
    assert actual == expected
