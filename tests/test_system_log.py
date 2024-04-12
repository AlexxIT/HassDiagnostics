from . import parse_log_entry


def test_script():
    entry = {
        "name": "homeassistant.components.script",
        "message": [
            "Script with alias 'toggle' has invalid object id and has been disabled: A script's object_id must not be one of reload, toggle, turn_off, turn_on. Got 'toggle'"
        ],
        "level": "ERROR",
        "source": ["components/script/config.py", 140],
        "timestamp": 1712755894.1904705,
        "exception": "",
        "count": 1,
        "first_occurred": 1712755894.1904705,
    }
    assert parse_log_entry(entry) == {
        "domain": "script",
        "name": "homeassistant.components.script",
        "short": "Script with alias 'toggle' has invalid object id and has be...",
    }


def test_rpi_power():
    entry = {
        "name": "homeassistant.components.rpi_power.binary_sensor",
        "message": [
            "Under-voltage was detected. Consider getting a uninterruptible power supply for your Raspberry Pi."
        ],
        "level": "WARNING",
        "source": ["components/rpi_power/binary_sensor.py", 56],
        "timestamp": 1712755969.323869,
        "exception": "",
        "count": 1,
        "first_occurred": 1712755969.323869,
    }
    assert parse_log_entry(entry) == {
        "domain": "rpi_power",
        "name": "homeassistant.components.rpi_power.binary_sensor",
        "short": "Under-voltage was detected. Consider getting a uninterrupti...",
    }


def test_miio():
    entry = {
        "name": "homeassistant.components.xiaomi_miio",
        "message": [
            "Unexpected error fetching zhimi.airpurifier.ma2 data: byte indices must be integers or slices, not str"
        ],
        "level": "ERROR",
        "source": ["helpers/update_coordinator.py", 315],
        "timestamp": 1712800756.920274,
        "exception": 'Traceback (most recent call last):\n  File "/usr/src/homeassistant/homeassistant/helpers/update_coordinator.py", line 315, in _async_refresh\n    self.data = await self._async_update_data()\n                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/helpers/update_coordinator.py", line 271, in _async_update_data\n    return await self.update_method()\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/xiaomi_miio/__init__.py", line 185, in update\n    return await _async_fetch_data()\n           ^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/xiaomi_miio/__init__.py", line 180, in _async_fetch_data\n    state = await hass.async_add_executor_job(device.status)\n            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/concurrent/futures/thread.py", line 58, in run\n    result = self.fn(*self.args, **self.kwargs)\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/miio/click_common.py", line 184, in _wrap\n    return func(self, *args, **kwargs)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/miio/integrations/airpurifier/zhimi/airpurifier.py", line 391, in status\n    values = self.get_properties(properties, max_properties=15)\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/miio/device.py", line 240, in get_properties\n    values.extend(self.send(property_getter, _props[:max_properties]))\n                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/miio/device.py", line 107, in send\n    return self._protocol.send(\n           ^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/miio/miioprotocol.py", line 202, in send\n    self.__id = payload["id"]\n                ~~~~~~~^^^^^^\nTypeError: byte indices must be integers or slices, not str\n',
        "count": 1,
        "first_occurred": 1712800756.920274,
    }
    assert parse_log_entry(entry) == {
        "domain": "xiaomi_miio",
        "name": "homeassistant.components.xiaomi_miio",
        "short": "byte indices must be integers or slices, not str",
    }


def test_system_log():
    entry = {
        "name": "frontend.js.latest.202402071",
        "message": [
            "Uncaught error from Chrome 123.0.0.0 on Mac OS 10.15.7\nTypeError: Cannot read properties of undefined (reading '_leaflet_pos')\n_leaflet_pos (src/dom/DomUtil.js:247:11)\ngetPosition (src/map/Map.js:1488:9)\n_getMapPanePos (src/map/Map.js:1505:66)\n_getNewPixelOrigin (src/map/Map.js:1224:27)\n_move (src/map/Map.js:1726:7)"
        ],
        "level": "ERROR",
        "source": ["components/system_log/__init__.py", 306],
        "timestamp": 1712806870.5005805,
        "exception": "",
        "count": 2,
        "first_occurred": 1712806870.4994752,
    }
    assert parse_log_entry(entry) == {
        "name": "frontend.js.latest.202402071",
        "short": "Uncaught error from Chrome 123.0.0.0 on Mac OS 10.15.7 Type...",
    }


def test_zeroconf():
    entry = {
        "name": "zeroconf",
        "message": [
            "Error with socket 25 (('::', 5353, 0, 0))): [Errno 101] Network unreachable"
        ],
        "level": "WARNING",
        "source": ["/usr/local/lib/python3.12/site-packages/zeroconf/_logger.py", 86],
        "timestamp": 1712762496.2768898,
        "exception": 'Traceback (most recent call last):\n  File "/usr/local/lib/python3.12/asyncio/selector_events.py", line 1265, in sendto\n    self._sock.sendto(data, addr)\nOSError: [Errno 101] Network unreachable\n',
        "count": 1,
        "first_occurred": 1712762496.2768898,
    }
    assert parse_log_entry(entry) == {
        "name": "zeroconf",
        "package": "zeroconf",
        "short": "[Errno 101] Network unreachable",
    }


def test_dataplicity():
    entry = {
        "name": "agent",
        "message": [
            'unable to associate m2m identity ("m2m.associate"=-32603, "Internal error. device is offline")'
        ],
        "level": "ERROR",
        "source": [
            "/usr/local/lib/python3.12/site-packages/dataplicity/client.py",
            308,
        ],
        "timestamp": 1712791008.0606177,
        "exception": "",
        "count": 8,
        "first_occurred": 1712775585.3678474,
    }
    assert parse_log_entry(entry) == {
        "name": "agent",
        "package": "dataplicity",
        "short": 'unable to associate m2m identity ("m2m.associate"=-32603, "...',
    }

    entry = {
        "name": "agent",
        "message": [
            "disk poll failed unable to contact JSONRPC server 'https://api.dataplicity.com' (HTTP Error 503: Service Temporarily Unavailable)",
            "disk poll failed unable to contact JSONRPC server 'https://api.dataplicity.com' (HTTP Error 502: Bad Gateway)",
            "disk poll failed unable to contact JSONRPC server 'https://api.dataplicity.com' (HTTP Error 504: Gateway Time-out)",
        ],
        "level": "ERROR",
        "source": [
            "/usr/local/lib/python3.12/site-packages/dataplicity/client.py",
            169,
        ],
        "timestamp": 1712802958.1291404,
        "exception": "",
        "count": 8,
        "first_occurred": 1712773955.9478126,
    }
    assert parse_log_entry(entry) == {
        "name": "agent",
        "package": "dataplicity",
        "short": "disk poll failed unable to contact JSONRPC server 'https://...",
    }


def test_websocket_philips():
    entry = {
        "name": "homeassistant.components.websocket_api.http.connection",
        "message": ["[139961207849792] TV is not available"],
        "level": "ERROR",
        "source": ["components/websocket_api/commands.py", 239],
        "timestamp": 1712826115.5249946,
        "exception": 'Traceback (most recent call last):\n  File "/usr/src/homeassistant/homeassistant/components/websocket_api/commands.py", line 239, in handle_call_service\n    response = await hass.services.async_call(\n               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/core.py", line 2543, in async_call\n    response_data = await coro\n                    ^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/core.py", line 2580, in _execute_service\n    return await target(service_call)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/helpers/service.py", line 996, in entity_service_call\n    raise result from None\n  File "/usr/src/homeassistant/homeassistant/helpers/entity.py", line 1580, in async_request_call\n    return await coro\n           ^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/helpers/service.py", line 1043, in _handle_entity_call\n    result = await task\n             ^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/light/__init__.py", line 642, in async_handle_light_off_service\n    await light.async_turn_off(**filter_turn_off_params(light, params))\n  File "/usr/src/homeassistant/homeassistant/components/philips_js/light.py", line 374, in async_turn_off\n    raise HomeAssistantError("TV is not available")\nhomeassistant.exceptions.HomeAssistantError: TV is not available\n',
        "count": 1,
        "first_occurred": 1712826115.5249946,
    }
    assert parse_log_entry(entry) == {
        "domain": "philips_js",
        "name": "homeassistant.components.websocket_api.http.connection",
        "short": "TV is not available",
    }


def test_service_call_philips():
    entry = {
        "name": "homeassistant.core",
        "message": [
            "Error executing service: <ServiceCall light.turn_off (c:xxx): entity_id=['light.philips_tv_ambilight'], params=>"
        ],
        "level": "ERROR",
        "source": ["core.py", 2559],
        "timestamp": 1712848158.1559181,
        "exception": 'Traceback (most recent call last):\n  File "/usr/src/homeassistant/homeassistant/core.py", line 2559, in _run_service_call_catch_exceptions\n    await coro_or_task\n  File "/usr/src/homeassistant/homeassistant/core.py", line 2580, in _execute_service\n    return await target(service_call)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/helpers/service.py", line 971, in entity_service_call\n    single_response = await _handle_entity_call(\n                      ^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/helpers/service.py", line 1043, in _handle_entity_call\n    result = await task\n             ^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/light/__init__.py", line 642, in async_handle_light_off_service\n    await light.async_turn_off(**filter_turn_off_params(light, params))\n  File "/usr/src/homeassistant/homeassistant/components/philips_js/light.py", line 374, in async_turn_off\n    raise HomeAssistantError("TV is not available")\nhomeassistant.exceptions.HomeAssistantError: TV is not available\n',
        "count": 1,
        "first_occurred": 1712848158.1559181,
    }
    assert parse_log_entry(entry) == {
        "domain": "philips_js",
        "name": "homeassistant.core",
        "short": "TV is not available",
    }


def test_telegram_bad_gateway():
    entry = {
        "name": "telegram.ext.Updater",
        "message": ["Error while getting Updates: Bad Gateway"],
        "level": "ERROR",
        "source": ["runner.py", 189],
        "timestamp": 1712884285.4835799,
        "exception": "",
        "count": 2,
        "first_occurred": 1712884284.3447855,
    }
    assert parse_log_entry(entry) == {
        "name": "telegram.ext.Updater",
        "short": "Error while getting Updates: Bad Gateway",
    }

    entry = {
        "name": "telegram.ext.Updater",
        "message": ["Exception happened while polling for updates."],
        "level": "ERROR",
        "source": [
            "/usr/local/lib/python3.12/site-packages/telegram/ext/_updater.py",
            411,
        ],
        "timestamp": 1712884285.4848557,
        "exception": 'Traceback (most recent call last):\n  File "/usr/local/lib/python3.12/site-packages/telegram/ext/_updater.py", line 742, in _network_loop_retry\n    if not await do_action():\n           ^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/telegram/ext/_updater.py", line 736, in do_action\n    return action_cb_task.result()\n           ^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/telegram/ext/_updater.py", line 387, in polling_action_cb\n    raise exc\n  File "/usr/local/lib/python3.12/site-packages/telegram/ext/_updater.py", line 376, in polling_action_cb\n    updates = await self.bot.get_updates(\n              ^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/telegram/_bot.py", line 541, in decorator\n    result = await func(self, *args, **kwargs)\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/telegram/_bot.py", line 4177, in get_updates\n    await self._post(\n  File "/usr/local/lib/python3.12/site-packages/telegram/_bot.py", line 629, in _post\n    return await self._do_post(\n           ^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/telegram/_bot.py", line 657, in _do_post\n    return await request.post(\n           ^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/telegram/request/_baserequest.py", line 200, in post\n    result = await self._request_wrapper(\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/telegram/request/_baserequest.py", line 383, in _request_wrapper\n    raise NetworkError(description or "Bad Gateway")\ntelegram.error.NetworkError: Bad Gateway\n',
        "count": 2,
        "first_occurred": 1712884284.3461096,
    }
    assert parse_log_entry(entry) == {
        "name": "telegram.ext.Updater",
        "package": "telegram",
        "short": "Bad Gateway",
    }
