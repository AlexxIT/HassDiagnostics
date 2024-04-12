from . import parse_log_entry


def test_hacs():
    entry = {
        "name": "homeassistant.helpers.frame",
        "message": [
            "Detected that custom integration 'hacs' accesses hass.components.frontend. This is deprecated and will stop working in Home Assistant 2024.9, it should be updated to import functions used from frontend directly at custom_components/hacs/frontend.py, line 68: hass.components.frontend.async_register_built_in_panel(, please create a bug report at https://github.com/hacs/integration/issues"
        ],
        "level": "WARNING",
        "source": ["helpers/frame.py", 188],
        "timestamp": 1712755125.5083797,
        "exception": "",
        "count": 1,
        "first_occurred": 1712755125.5083797,
    }
    assert parse_log_entry(entry) == {
        "category": "deprecated",
        "domain": "hacs",
        "name": "homeassistant.helpers.frame",
        "short": "Detected that custom integration 'hacs' accesses hass.compo...",
    }


def test_light_deprecation():
    entry = {
        "name": "homeassistant.components.light",
        "message": [
            "sonoff.xxx (<class 'custom_components.sonoff.switch.XSwitches'>) does not set supported color modes, this will stop working in Home Assistant Core 2025.3, please create a bug report at https://github.com/AlexxIT/SonoffLAN/issues",
            "sonoff.xxx (<class 'custom_components.sonoff.switch.XSwitch'>) does not set supported color modes, this will stop working in Home Assistant Core 2025.3, please create a bug report at https://github.com/AlexxIT/SonoffLAN/issues",
            "ergomotion.xxx (<class 'custom_components.ergomotion.light.XScene'>) does not set supported color modes, this will stop working in Home Assistant Core 2025.3, please create a bug report at https://github.com/AlexxIT/Ergomotion/issues",
            "ergomotion.xxx (<class 'custom_components.ergomotion.light.XLed'>) does not set supported color modes, this will stop working in Home Assistant Core 2025.3, please create a bug report at https://github.com/AlexxIT/Ergomotion/issues",
        ],
        "level": "WARNING",
        "source": ["components/light/__init__.py", 1272],
        "timestamp": 1712755126.123485,
        "exception": "",
        "count": 11,
        "first_occurred": 1712755125.336377,
    }
    assert parse_log_entry(entry) == {
        "category": "deprecated",
        "domain": "sonoff",
        "name": "homeassistant.components.light",
        "short": "sonoff.xxx (<class 'custom_components.sonoff.switch.XSwitch...",
    }


def test_configuration_yaml():
    entry = {
        "name": "homeassistant.helpers.config_validation",
        "message": [
            "The 'exclude' option near /config/configuration.yaml:69 is deprecated, please remove it from your configuration"
        ],
        "level": "WARNING",
        "source": ["helpers/config_validation.py", 924],
        "timestamp": 1712919751.101808,
        "exception": "",
        "count": 1,
        "first_occurred": 1712919751.101808,
    }
    assert parse_log_entry(entry) == {
        "category": "deprecated",
        "name": "homeassistant.helpers.config_validation",
        "short": "The 'exclude' option near /config/configuration.yaml:69 is ...",
    }


def test_const():
    entry = {
        "name": "homeassistant.const",
        "message": [
            "TEMP_CELSIUS was used from gismeteo, this is a deprecated constant which will be removed in HA Core 2025.1. Use UnitOfTemperature.CELSIUS instead, please report it to the author of the 'gismeteo' custom integration",
            "LENGTH_KILOMETERS was used from blitzortung, this is a deprecated constant which will be removed in HA Core 2025.1. Use UnitOfLength.KILOMETERS instead, please report it to the author of the 'blitzortung' custom integration",
            "LENGTH_MILES was used from blitzortung, this is a deprecated constant which will be removed in HA Core 2025.1. Use UnitOfLength.MILES instead, please report it to the author of the 'blitzortung' custom integration",
            "PRESSURE_MMHG was used from gismeteo, this is a deprecated constant which will be removed in HA Core 2025.1. Use UnitOfPressure.MMHG instead, please report it to the author of the 'gismeteo' custom integration",
            "SPEED_KILOMETERS_PER_HOUR was used from gismeteo, this is a deprecated constant which will be removed in HA Core 2025.1. Use UnitOfSpeed.KILOMETERS_PER_HOUR instead, please report it to the author of the 'gismeteo' custom integration",
        ],
        "level": "WARNING",
        "source": ["helpers/deprecation.py", 206],
        "timestamp": 1712919760.4818387,
        "exception": "",
        "count": 15,
        "first_occurred": 1712919755.8094475,
    }
    assert parse_log_entry(entry) == {
        "category": "deprecated",
        "domain": "gismeteo",
        "name": "homeassistant.const",
        "short": "TEMP_CELSIUS was used from gismeteo, this is a deprecated c...",
    }
