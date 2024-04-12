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
        "short": "TypeError: byte indices must be integers or slices, not str",
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
        "short": "OSError: [Errno 101] Network unreachable",
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
        "short": "HomeAssistantError: TV is not available",
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
        "short": "HomeAssistantError: TV is not available",
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
        "short": "NetworkError: Bad Gateway",
    }


def test_mikrotik():
    entry = {
        "name": "custom_components.mikrotik_router.coordinator",
        "message": [
            "Mikrotik 192.168.88.1 duplicate Mangle rule change-mss,tcp:any, entity will be unavailable."
        ],
        "level": "ERROR",
        "source": ["custom_components/mikrotik_router/coordinator.py", 1131],
        "timestamp": 1712919756.6597452,
        "exception": "",
        "count": 2,
        "first_occurred": 1712919756.6596253,
    }
    assert parse_log_entry(entry) == {
        "domain": "mikrotik_router",
        "host": "192.168.88.1",
        "name": "custom_components.mikrotik_router.coordinator",
        "short": "Mikrotik 192.168.88.1 duplicate Mangle rule change-mss,tcp:...",
    }


def test_setup_matrix():
    entry = {
        "name": "homeassistant.setup",
        "message": ["Error during setup of component matrix"],
        "level": "ERROR",
        "source": ["setup.py", 398],
        "timestamp": 1712919752.8565288,
        "exception": 'Traceback (most recent call last):\n  File "/usr/src/homeassistant/homeassistant/setup.py", line 398, in _async_setup_component\n    result = await task\n             ^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/matrix/__init__.py", line 138, in async_setup\n    config = config[DOMAIN]\n             ~~~~~~^^^^^^^^\nKeyError: \'matrix\'\n',
        "count": 1,
        "first_occurred": 1712919752.8565288,
    }
    assert parse_log_entry(entry) == {
        "domain": "matrix",
        "name": "homeassistant.setup",
        "short": "KeyError: 'matrix'",
    }


def test_xbox():
    entry = {
        "name": "homeassistant.config_entries",
        "message": ["Error setting up entry Home Assistant Cloud for xbox"],
        "level": "ERROR",
        "source": ["config_entries.py", 551],
        "timestamp": 1712919761.4121366,
        "exception": 'Traceback (most recent call last):\n  File "/usr/src/homeassistant/homeassistant/config_entries.py", line 551, in async_setup\n    result = await component.async_setup_entry(hass, self)\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/xbox/__init__.py", line 61, in async_setup_entry\n    consoles: SmartglassConsoleList = await client.smartglass.get_console_list()\n                                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/xbox/webapi/api/provider/smartglass/__init__.py", line 54, in get_console_list\n    resp = await self._fetch_list("devices", params, **kwargs)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/xbox/webapi/api/provider/smartglass/__init__.py", line 359, in _fetch_list\n    resp = await self.client.session.get(\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/xbox/webapi/api/client.py", line 86, in get\n    return await self.request(hdrs.METH_GET, url, **kwargs)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/xbox/webapi/api/client.py", line 60, in request\n    await self._auth_mgr.refresh_tokens()\n  File "/usr/src/homeassistant/homeassistant/components/xbox/api.py", line 28, in refresh_tokens\n    await self._oauth_session.async_ensure_token_valid()\n  File "/usr/src/homeassistant/homeassistant/helpers/config_entry_oauth2_flow.py", line 523, in async_ensure_token_valid\n    new_token = await self.implementation.async_refresh_token(self.token)\n                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/helpers/config_entry_oauth2_flow.py", line 94, in async_refresh_token\n    new_token = await self._async_refresh_token(token)\n                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/cloud/account_link.py", line 140, in _async_refresh_token\n    new_token = await account_link.async_fetch_access_token(\n                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/hass_nabucasa/account_link.py", line 121, in async_fetch_access_token\n    resp.raise_for_status()\n  File "/usr/local/lib/python3.12/site-packages/aiohttp/client_reqrep.py", line 1060, in raise_for_status\n    raise ClientResponseError(\naiohttp.client_exceptions.ClientResponseError: 500, message=\'Internal Server Error\', url=URL(\'https://account-link.nabucasa.com/refresh_token/xbox\')\n',
        "count": 1,
        "first_occurred": 1712919761.4121366,
    }
    assert parse_log_entry(entry) == {
        "domain": "cloud",
        "name": "homeassistant.config_entries",
        "short": "ClientResponseError: 500, message='Internal Server Error', ...",
    }

    entry = {
        "name": "homeassistant.util.logging",
        "message": [
            "Exception in <function _process_media_source_platform at 0x7f634c77bb00> when processing platform 'media_source': (<HomeAssistant NOT_RUNNING>, 'xbox', <module 'homeassistant.components.xbox.media_source' from '/usr/src/homeassistant/homeassistant/components/xbox/media_source.py'>)\nTraceback (most recent call last):\n  File \"/usr/src/homeassistant/homeassistant/components/media_source/__init__.py\", line 93, in _process_media_source_platform\n    hass.data[DOMAIN][domain] = await platform.async_get_media_source(hass)\n                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/src/homeassistant/homeassistant/components/xbox/media_source.py\", line 42, in async_get_media_source\n    client = hass.data[DOMAIN][entry.entry_id][\"client\"]\n             ~~~~~~~~~^^^^^^^^\nKeyError: 'xbox'\n"
        ],
        "level": "ERROR",
        "source": ["util/logging.py", 103],
        "timestamp": 1712919762.2007668,
        "exception": "",
        "count": 1,
        "first_occurred": 1712919762.2007668,
    }
    assert parse_log_entry(entry) == {
        "domain": "xbox",
        "name": "homeassistant.util.logging",
        "short": "KeyError: 'xbox'",
    }


def test_xiaomi_miot():
    entry = {
        "name": "homeassistant.components.sensor",
        "message": [
            "Platform xiaomi_miot does not generate unique IDs. ID xxx-magnet_sensor-2.illumination-1 is already used by sensor.isa_dw2hl_31cf_illumination - ignoring sensor.isa_dw2hl_31cf_illumination",
        ],
        "level": "ERROR",
        "source": ["helpers/entity_platform.py", 744],
        "timestamp": 1712919784.493696,
        "exception": "",
        "count": 11,
        "first_occurred": 1712919784.3675585,
    }
    assert parse_log_entry(entry) == {
        "domain": "xiaomi_miot",
        "name": "homeassistant.components.sensor",
        "short": "Platform xiaomi_miot does not generate unique IDs. ID xxx-m...",
    }


def test_requirements():
    entry = {
        "name": "homeassistant",
        "message": ["Error doing job: Task exception was never retrieved"],
        "level": "ERROR",
        "source": ["requirements.py", 318],
        "timestamp": 1712919903.9594476,
        "exception": 'Traceback (most recent call last):\n  File "/usr/src/homeassistant/homeassistant/helpers/discovery_flow.py", line 107, in _async_start\n    await gather_with_limited_concurrency(FLOW_INIT_LIMIT, *init_coros)\n  File "/usr/src/homeassistant/homeassistant/util/async_.py", line 207, in gather_with_limited_concurrency\n    return await gather(\n           ^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/util/async_.py", line 205, in sem_task\n    return await task\n           ^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/config_entries.py", line 1155, in async_init\n    flow, result = await self._async_init(flow_id, handler, context, data)\n                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/config_entries.py", line 1175, in _async_init\n    flow = await self.async_create_flow(handler, context=context, data=data)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/config_entries.py", line 1312, in async_create_flow\n    handler = await _async_get_flow_handler(\n              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/config_entries.py", line 2608, in _async_get_flow_handler\n    await _load_integration(hass, domain, hass_config)\n  File "/usr/src/homeassistant/homeassistant/config_entries.py", line 2585, in _load_integration\n    await async_process_deps_reqs(hass, hass_config, integration)\n  File "/usr/src/homeassistant/homeassistant/setup.py", line 551, in async_process_deps_reqs\n    await requirements.async_get_integration_with_requirements(\n  File "/usr/src/homeassistant/homeassistant/requirements.py", line 53, in async_get_integration_with_requirements\n    return await manager.async_get_integration_with_requirements(domain)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/requirements.py", line 176, in async_get_integration_with_requirements\n    await self._async_process_integration(integration, done)\n  File "/usr/src/homeassistant/homeassistant/requirements.py", line 193, in _async_process_integration\n    await self.async_process_requirements(\n  File "/usr/src/homeassistant/homeassistant/requirements.py", line 280, in async_process_requirements\n    await self._async_process_requirements(name, missing)\n  File "/usr/src/homeassistant/homeassistant/requirements.py", line 318, in _async_process_requirements\n    raise RequirementsNotFound(name, list(failures))\nhomeassistant.requirements.RequirementsNotFound: Requirements for tuya_ble not found: [\'pycountry==22.3.5\'].\n',
        "count": 1,
        "first_occurred": 1712919903.9594476,
    }
    assert parse_log_entry(entry) == {
        "domain": "tuya_ble",
        "name": "homeassistant",
        "short": "Requirements for tuya_ble not found: ['pycountry==22.3.5'].",
    }
