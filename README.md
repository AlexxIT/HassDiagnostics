# Hass Diagnostics

## Smart Log

**Version 1**

```markdown
[diagnostics](/config/integrations/integration/hass_diagnostics) | [log](/config/logs) | total: {{ states('sensor.smart_log') }} items
{% for i in state_attr('sensor.smart_log', 'records') -%}
<details>
<summary>
<b>{{i.get('domain') or i.get('package') or i.name}}</b> [{{i.count}}] {{i.get('category','')}} {{i.get('host','')}} {{"[github]("+i.github+")" if 'github' in i}}
<br>&nbsp; &nbsp;<i>{{i.short}}</i>
</summary>
{{i.message|replace('\n',' ')}}
</details>
{% endfor %}
```

**Version 2**

```markdown
[diagnostics](/config/integrations/integration/hass_diagnostics) | [log](/config/logs) | total: {{ states('sensor.smart_log') }} items
{% for i in state_attr('sensor.smart_log', 'records') -%}
- **{{i.get('domain') or i.get('package') or i.name}}** [{{i.count}}] {{i.get('category','')}} {{i.get('host','')}} {{"[github]("+i.github+")" if 'github' in i}}
  *{{i.short}}*
{% endfor %}
```
