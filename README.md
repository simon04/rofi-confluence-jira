# rofi-confluence-jira

Loads the most recently modified [Confluence](https://www.atlassian.com/software/confluence) pages and the most recently updated [JIRA](https://www.atlassian.com/software/jira) issues via their REST APIs, and displays those in a [rofi](https://github.com/davatorium/rofi) menu to quickly access them.

## Dependencies

- [Python 3](https://www.python.org/)
- [PyXDG](https://freedesktop.org/wiki/Software/pyxdg/)
- [rofi](https://github.com/davatorium/rofi)

## Configuration

This script reads the configuration from `$XDG_CONFIG_HOME/rofi-confluence-jira.cfg`.

```ini
; .config/rofi-confluence-jira.cfg
[confluence]
URL = https://confluence.example.com
USER = username
PASS = password

[jira]
URL = https://jira.example.com
USER = username
PASS = password
```

## Author and License

- Author: [simon04](https://github.com/simon04)
- License: [GPL v3](https://github.com/simon04/bldrwnsch/blob/gh-pages/LICENSE)
