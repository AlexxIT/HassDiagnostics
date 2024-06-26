# Hass Diagnostics

Diagnostics entities for [Home Assistant](https://www.home-assistant.io/).

## Installation

[HACS](https://hacs.xyz/) custom repository: `AlexxIT/HassDiagnostics`.

[![](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=AlexxIT&repository=HassDiagnostics&category=Integration)

Or manually copy `hass_diagnostics` folder from [latest release](https://github.com/AlexxIT/HassDiagnostics/releases/latest) to `/config/custom_components` folder.

## Configuration

Add integration via Home Assistant UI.

[![](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=hass_diagnostics)

## Smart Log

Creates a sensor whose data can be displayed with a [Markdown card](https://www.home-assistant.io/dashboards/markdown/).

- combining issues by integration, category, and device IP address
- displaying short text of problem
- displaying where possible:
  - integration name
  - python library name
  - issue category
  - IP address of the device
  - link to github sources

<img src="https://raw.githubusercontent.com/AlexxIT/HassDiagnostics/101177ca7e4fcdc56242ab772e4a88224c9e162d/smart_log.png" width="480">

**Markdown card - version 1**

```markdown
[diagnostics](/config/integrations/integration/hass_diagnostics) | [log](/config/logs) | total: {{ states('sensor.smart_log') }} items

{% for i in state_attr('sensor.smart_log', 'records') or '' -%}
---
<details>
<summary>
  <b>{{i.get('domain') or i.get('package') or i.name}}</b> ({{i.count}}) {{i.get('category','')}} {{i.get('host','')}}
  <br>&nbsp; &nbsp;<i>{{i.short}}</i>
</summary>
<div><b>{{i.name}}</b></div>
<div>{{i.message|replace('\n',' ')|regex_replace('(http[^\s]+)', '<a href="\\1">\\1</a>')}}</div>
<div>{{i.source|join(', ')}}{{', <a href="%s">github</a>'%i.github if 'github' in i}}</div>
{{'<pre>'+i.exception+'</pre>' if 'exception' in i}}
</details>

{% endfor %}
```

**Markdown card - version 2**

```markdown
[diagnostics](/config/integrations/integration/hass_diagnostics) | [log](/config/logs) | total: {{ states('sensor.smart_log') }} items
{% for i in state_attr('sensor.smart_log', 'records') -%}
- **{{i.get('domain') or i.get('package') or i.name}}** ({{i.count}}) {{i.get('category','')}} {{i.get('host','')}}
  *{{i.short}}*
{% endfor %}
```

## Start Time

Creates a sensor, with Home Assistant start time from the logs.

```
2020-02-24 17:13:11 INFO (MainThread) [homeassistant.bootstrap] Home Assistant initialized in 25.5s
```
