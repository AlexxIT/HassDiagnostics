# Hass Diagnostics

## System Log

```
[Hass Diagnostics](/config/integrations/integration/hass_diagnostics) [System log](/config/logs): {{ states('sensor.system_log') }} items
{% for i in state_attr('sensor.system_log', 'records') -%}
- **{{i.get('domain') or i.get('package') or i.name}}** [{{i.count}}] {{i.get('category') or ''}}
  *{{i.short}}*
{% endfor %}
```
