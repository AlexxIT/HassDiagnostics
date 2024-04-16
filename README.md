# Hass Diagnostics

## Smart Log

- combining issues by integration, category, and device IP address
- displaying short text of problem
- displaying where possible:
  - integration name
  - python library name
  - issue category
  - IP address of the device
  - link to github sources

<img src="https://raw.githubusercontent.com/AlexxIT/HassDiagnostics/master/smart_log.png" width="480">

**Markdown card - version 1**

```markdown
[diagnostics](/config/integrations/integration/hass_diagnostics) | [log](/config/logs) | total: {{ states('sensor.smart_log') }} items

{% for i in state_attr('sensor.smart_log', 'records') -%}
---
<details>
<summary>
  <b>{{i.get('domain') or i.get('package') or i.name}}</b> ({{i.count}}) {{i.get('category','')}} {{i.get('host','')}}
  <br>&nbsp; &nbsp;<i>{{i.short}}</i>
</summary>
<table>
  <tr><td><b>{{i.name}}</b></td></tr>
  <tr><td>{{i.message|replace('\n',' ')}}</td></tr>
  <tr><td>{{i.source|join(', ')}}{{', <a href="%s">github</a>'%i.github if 'github' in i}}</td></tr>
</table>
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
