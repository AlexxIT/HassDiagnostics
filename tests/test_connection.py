from . import parse_log_entry


def test_aiohttp_server():
    entry = {
        "name": "aiohttp.server",
        "message": ["Error handling request"],
        "level": "ERROR",
        "source": [
            "/usr/local/lib/python3.12/site-packages/aiohttp/web_protocol.py",
            421,
        ],
        "timestamp": 1712756321.8393567,
        "exception": 'Traceback (most recent call last):\n  File "/usr/local/lib/python3.12/site-packages/aiohttp/connector.py", line 992, in _wrap_create_connection\n    return await self._loop.create_connection(*args, **kwargs)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/asyncio/base_events.py", line 1119, in create_connection\n    raise exceptions[0]\n  File "/usr/local/lib/python3.12/asyncio/base_events.py", line 1101, in create_connection\n    sock = await self._connect_sock(\n           ^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/asyncio/base_events.py", line 1004, in _connect_sock\n    await self.sock_connect(sock, address)\n  File "/usr/local/lib/python3.12/asyncio/selector_events.py", line 637, in sock_connect\n    return await fut\n           ^^^^^^^^^\n  File "/usr/local/lib/python3.12/asyncio/selector_events.py", line 677, in _sock_connect_cb\n    raise OSError(err, f\'Connect call failed {address}\')\nConnectionRefusedError: [Errno 111] Connect call failed (\'127.0.0.1\', 443)\n\nThe above exception was the direct cause of the following exception:\n\nTraceback (most recent call last):\n  File "/usr/local/lib/python3.12/site-packages/aiohttp/web_protocol.py", line 452, in _handle_request\n    resp = await request_handler(request)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/aiohttp/web_app.py", line 543, in _handle\n    resp = await handler(request)\n           ^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/aiohttp/web_middlewares.py", line 114, in impl\n    return await handler(request)\n           ^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/http/security_filter.py", line 91, in security_filter_middleware\n    return await handler(request)\n           ^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/http/forwarded.py", line 100, in forwarded_middleware\n    return await handler(request)\n           ^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/http/request_context.py", line 28, in request_context_middleware\n    return await handler(request)\n           ^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/http/ban.py", line 80, in ban_middleware\n    return await handler(request)\n           ^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/http/auth.py", line 235, in auth_middleware\n    return await handler(request)\n           ^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/http/headers.py", line 31, in headers_middleware\n    response = await handler(request)\n               ^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/http/view.py", line 149, in handle\n    result = await handler(request, **request.match_info)\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/media_player/__init__.py", line 1255, in get\n    data, content_type = await player.async_get_media_image()\n                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/media_player/__init__.py", line 655, in async_get_media_image\n    return await self._async_fetch_image_from_cache(url)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/media_player/__init__.py", line 1174, in _async_fetch_image_from_cache\n    (content, content_type) = await self._async_fetch_image(url)\n                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/media_player/__init__.py", line 1185, in _async_fetch_image\n    return await async_fetch_image(_LOGGER, self.hass, url)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/media_player/__init__.py", line 1350, in async_fetch_image\n    response = await websession.get(url)\n               ^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/aiohttp/client.py", line 578, in _request\n    conn = await self._connector.connect(\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/aiohttp/connector.py", line 544, in connect\n    proto = await self._create_connection(req, traces, timeout)\n            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/aiohttp/connector.py", line 911, in _create_connection\n    _, proto = await self._create_direct_connection(req, traces, timeout)\n               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/aiohttp/connector.py", line 1235, in _create_direct_connection\n    raise last_exc\n  File "/usr/local/lib/python3.12/site-packages/aiohttp/connector.py", line 1204, in _create_direct_connection\n    transp, proto = await self._wrap_create_connection(\n                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/aiohttp/connector.py", line 1000, in _wrap_create_connection\n    raise client_error(req.connection_key, exc) from exc\naiohttp.client_exceptions.ClientConnectorError: Cannot connect to host graph.facebook.com:443 ssl:default [Connect call failed (\'127.0.0.1\', 443)]\n',
        "count": 3,
        "first_occurred": 1712756321.6496823,
    }
    assert parse_log_entry(entry) == {
        "category": "connection",
        "domain": "media_player",
        "host": "graph.facebook.com",
        "name": "aiohttp.server",
        "package": "aiohttp",
        "short": "Error handling request",
    }


def test_yandex_smart_home():
    entry = {
        "name": "custom_components.yandex_smart_home.smart_home",
        "message": [
            "INTERNAL_ERROR: Failed to execute action for instance on (devices.capabilities.on_off) of light.kids_lamp: HomeAssistantError('Error when calling _async_turn_on for bulb Yeelight Ceiling6 0x80xxxxx at 192.168.1.123: The write socket is closed')"
        ],
        "level": "ERROR",
        "source": ["custom_components/yandex_smart_home/smart_home.py", 151],
        "timestamp": 1712762773.383661,
        "exception": "",
        "count": 1,
        "first_occurred": 1712762773.383661,
    }
    assert parse_log_entry(entry) == {
        "category": "connection",
        "domain": "yandex_smart_home",
        "host": "192.168.1.123",
        "name": "custom_components.yandex_smart_home.smart_home",
        "short": "INTERNAL_ERROR: Failed to execute action for instance on (d...",
    }


def test_pychromecast():
    entry = {
        "name": "pychromecast.socket_client",
        "message": [
            "[MIBOX4(192.168.1.123):8009] Heartbeat timeout, resetting connection",
        ],
        "level": "WARNING",
        "source": [
            "/usr/local/lib/python3.12/site-packages/pychromecast/socket_client.py",
            664,
        ],
        "timestamp": 1712806799.5915406,
        "exception": "",
        "count": 14,
        "first_occurred": 1712762147.9811645,
    }
    assert parse_log_entry(entry) == {
        "category": "connection",
        "host": "192.168.1.123",
        "name": "pychromecast.socket_client",
        "package": "pychromecast",
        "short": "[MIBOX4(192.168.1.123):8009] Heartbeat timeout, resetting c...",
    }

    entry = {
        "name": "pychromecast.socket_client",
        "message": ["[All(192.168.1.123):32156] Error reading from socket."],
        "level": "ERROR",
        "source": [
            "/usr/local/lib/python3.12/site-packages/pychromecast/socket_client.py",
            616,
        ],
        "timestamp": 1712806815.509437,
        "exception": "",
        "count": 4,
        "first_occurred": 1712799203.7723434,
    }
    assert parse_log_entry(entry) == {
        "category": "connection",
        "host": "192.168.1.123",
        "name": "pychromecast.socket_client",
        "package": "pychromecast",
        "short": "[All(192.168.1.123):32156] Error reading from socket.",
    }

    entry = {
        "name": "pychromecast.socket_client",
        "message": [
            "[All(192.168.1.123):32156] Error communicating with socket, resetting connection"
        ],
        "level": "WARNING",
        "source": [
            "/usr/local/lib/python3.12/site-packages/pychromecast/socket_client.py",
            655,
        ],
        "timestamp": 1712806815.5136075,
        "exception": "",
        "count": 4,
        "first_occurred": 1712799203.7767339,
    }
    assert parse_log_entry(entry) == {
        "category": "connection",
        "host": "192.168.1.123",
        "name": "pychromecast.socket_client",
        "package": "pychromecast",
        "short": "[All(192.168.1.123):32156] Error communicating with socket,...",
    }

    entry = {
        "name": "pychromecast.socket_client",
        "message": [
            "[All(192.168.1.123):32156] Failed to connect to service HostServiceInfo(host='192.168.1.123', port=32156), retrying in 5.0s",
        ],
        "level": "ERROR",
        "source": [
            "/usr/local/lib/python3.12/site-packages/pychromecast/socket_client.py",
            412,
        ],
        "timestamp": 1712806818.2968147,
        "exception": "",
        "count": 16,
        "first_occurred": 1712762177.9957035,
    }
    assert parse_log_entry(entry) == {
        "category": "connection",
        "host": "192.168.1.123",
        "name": "pychromecast.socket_client",
        "package": "pychromecast",
        "short": "[All(192.168.1.123):32156] Failed to connect to service Hos...",
    }


def test_service_call_yeelight():
    entry = {
        "name": "homeassistant.core",
        "message": [
            "Error executing service: <ServiceCall light.turn_on (c:xxx): entity_id=['light.kids_lamp'], params=transition=45.0, brightness=255, color_temp=257, color_temp_kelvin=3885>",
            "Error executing service: <ServiceCall light.turn_off (c:xxx): entity_id=['light.kids_lamp'], params=>",
        ],
        "level": "ERROR",
        "source": ["core.py", 2559],
        "timestamp": 1712848188.1388695,
        "exception": 'Traceback (most recent call last):\n  File "/usr/local/lib/python3.12/site-packages/yeelight/aio.py", line 101, in async_send_command\n    response = await future\n               ^^^^^^^^^^^^\nasyncio.exceptions.CancelledError\n\nThe above exception was the direct cause of the following exception:\n\nTraceback (most recent call last):\n  File "/usr/src/homeassistant/homeassistant/components/yeelight/light.py", line 257, in _async_wrap\n    return await func(self, *args, **kwargs)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/yeelight/light.py", line 705, in async_set_colortemp\n    await self._bulb.async_set_color_temp(\n  File "/usr/local/lib/python3.12/site-packages/yeelight/aio.py", line 45, in wrapper\n    cmd = await self.async_send_command(\n          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/yeelight/aio.py", line 100, in async_send_command\n    async with asyncio_timeout(TIMEOUT):\n  File "/usr/local/lib/python3.12/asyncio/timeouts.py", line 115, in __aexit__\n    raise TimeoutError from exc_val\nTimeoutError\n\nThe above exception was the direct cause of the following exception:\n\nTraceback (most recent call last):\n  File "/usr/src/homeassistant/homeassistant/core.py", line 2559, in _run_service_call_catch_exceptions\n    await coro_or_task\n  File "/usr/src/homeassistant/homeassistant/core.py", line 2580, in _execute_service\n    return await target(service_call)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/config/custom_components/adaptive_lighting/hass_utils.py", line 62, in service_func_proxy\n    await existing_service.job.target(call)\n  File "/usr/src/homeassistant/homeassistant/helpers/service.py", line 971, in entity_service_call\n    single_response = await _handle_entity_call(\n                      ^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/helpers/service.py", line 1043, in _handle_entity_call\n    result = await task\n             ^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/light/__init__.py", line 631, in async_handle_light_on_service\n    await light.async_turn_on(**filter_turn_on_params(light, params))\n  File "/usr/src/homeassistant/homeassistant/components/yeelight/light.py", line 803, in async_turn_on\n    await self.async_set_colortemp(colortemp, duration)\n  File "/usr/src/homeassistant/homeassistant/components/yeelight/light.py", line 263, in _async_wrap\n    raise HomeAssistantError(\nhomeassistant.exceptions.HomeAssistantError: Timed out when calling async_set_colortemp for bulb Yeelight Ceiling6 0x8xxxxxx at 192.168.1.123: <class \'TimeoutError\'>\n',
        "count": 2,
        "first_occurred": 1712848151.0284944,
    }
    assert parse_log_entry(entry) == {
        "category": "connection",
        "domain": "adaptive_lighting",
        "host": "192.168.1.123",
        "name": "homeassistant.core",
        "short": "Timed out when calling async_set_colortemp for bulb Yeeligh...",
    }


def test_disconnected_from():
    entry = {
        "name": "homeassistant.components.androidtv_remote",
        "message": ["Disconnected from MIBOX4 at 192.168.1.123"],
        "level": "WARNING",
        "source": ["components/androidtv_remote/__init__.py", 39],
        "timestamp": 1712885169.0774295,
        "exception": "",
        "count": 5,
        "first_occurred": 1712849441.482956,
    }
    assert parse_log_entry(entry) == {
        "category": "connection",
        "domain": "androidtv_remote",
        "host": "192.168.1.123",
        "name": "homeassistant.components.androidtv_remote",
        "short": "Disconnected from MIBOX4 at 192.168.1.123",
    }


def test_sonoff_cloud():
    entry = {
        "name": "custom_components.sonoff.core.ewelink.cloud",
        "message": [
            "Cloud WS Connection error: Cannot connect to host eu-dispa.coolkit.cc:443 ssl:default [Connect call failed ('18.159.168.104', 443)]"
        ],
        "level": "WARNING",
        "source": ["custom_components/sonoff/core/ewelink/cloud.py", 360],
        "timestamp": 1712896573.0078208,
        "exception": "",
        "count": 1,
        "first_occurred": 1712896573.0078208,
    }
    assert parse_log_entry(entry) == {
        "category": "connection",
        "domain": "sonoff",
        "host": "eu-dispa.coolkit.cc",
        "name": "custom_components.sonoff.core.ewelink.cloud",
        "short": "Cloud WS Connection error: Cannot connect to host eu-dispa....",
    }
