from . import parse_log_entry


def test_template():
    entry = {
        "name": "homeassistant.helpers.event",
        "message": [
            "Error while processing template: Template<template=({% for i in state_attr('sensor.system_log', 'records') -%}\n- **{{i.domains|join(\" \") if \"domains\" in i else i.name}}** {{i.count}} {{i.get('category','')}}\n  *{{i.message}}*\n{% endfor %}) renders=2>"
        ],
        "level": "ERROR",
        "source": ["helpers/template.py", 588],
        "timestamp": 1712810148.7572696,
        "exception": 'Traceback (most recent call last):\n  File "/usr/src/homeassistant/homeassistant/helpers/template.py", line 586, in async_render\n    render_result = _render_with_context(self.template, compiled, **kwargs)\n                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/helpers/template.py", line 2545, in _render_with_context\n    return template.render(**kwargs)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/jinja2/environment.py", line 1301, in render\n    self.environment.handle_exception()\n  File "/usr/local/lib/python3.12/site-packages/jinja2/environment.py", line 936, in handle_exception\n    raise rewrite_traceback_stack(source=source)\n  File "<template>", line 1, in top-level template code\nTypeError: \'NoneType\' object is not iterable\n\nThe above exception was the direct cause of the following exception:\n\nTraceback (most recent call last):\n  File "/usr/src/homeassistant/homeassistant/helpers/template.py", line 712, in async_render_to_info\n    render_info._result = self.async_render(\n                          ^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/helpers/template.py", line 588, in async_render\n    raise TemplateError(err) from err\nhomeassistant.exceptions.TemplateError: TypeError: \'NoneType\' object is not iterable\n',
        "count": 1,
        "first_occurred": 1712810148.7572696,
    }
    assert parse_log_entry(entry) == {
        "category": "template",
        "name": "homeassistant.helpers.event",
        "short": "{% for i in state_attr('sensor.system_log', 'records') -%} ...",
    }
