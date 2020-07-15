# rofi-confluence-jira

Loads the most recently modified [Confluence](https://www.atlassian.com/software/confluence) pages and the most recently updated [JIRA](https://www.atlassian.com/software/jira) issues via their REST APIs, and displays those in a [rofi](https://github.com/davatorium/rofi) menu to quickly access them.

## Dependencies

- [Python 3](https://www.python.org/)
- [PyXDG](https://freedesktop.org/wiki/Software/pyxdg/)
- [Requests](https://pypi.org/project/requests/)
- [rofi](https://github.com/davatorium/rofi)

## Configuration

This script reads the configuration from `"${XDG_CONFIG_HOME:-${HOME}/.config}/rofi-confluence-jira.cfg"`.

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

### Usage API Token

To use an API token instead of your regular password.

1. Retrieve an api token for your instance, if you are using public atlassian the link is: [`https://id.atlassian.com/manage-profile/security/api-tokens`](https://id.atlassian.com/manage-profile/security/api-tokens)
2. Set the token as `PASS` and your username or email address as `USER`

### Different browser

You can set the environment variable `BROWSER` to define a different browser.

`BROWSER=xdg-open ./rofi-confluence-jira.py`


## Author and License

- Author: [simon04](https://github.com/simon04)
- License: [GPL v3](https://github.com/simon04/bldrwnsch/blob/gh-pages/LICENSE)
