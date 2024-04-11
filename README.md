# Hass Diagnostics

## System Log

```
[diagnostics](/config/integrations/integration/hass_diagnostics) | [log](/config/logs) | total: {{ states('sensor.smart_log') }} items
{% for i in state_attr('sensor.smart_log', 'records') -%}
- **{{i.get('domain') or i.get('package') or i.name}}** [{{i.count}}] {{i.get('category') or ''}}
  *{{i.short}}*
{% endfor %}
```
