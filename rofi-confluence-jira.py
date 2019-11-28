#!/bin/env python3
from rofi import Rofi
from xdg import BaseDirectory
import configparser
import requests
import webbrowser

config = configparser.ConfigParser()
config.read(BaseDirectory.load_config_paths('rofi-confluence-jira.cfg'))

CONFLUENCE_URL = config['confluence']['URL']
CONFLUENCE_AUTH = (config['confluence']['USER'],
                   config['confluence']['PASS'])
confluence = requests.get(
    f'{CONFLUENCE_URL}/rest/api/content/search',
    params={
        'cql': 'type=page order by lastmodified desc',
        'limit': 500,
        'start': 0,
    },
    headers={'Content-Type': 'application/json'},
    auth=CONFLUENCE_AUTH)
pages = confluence.json()['results']
for page in pages:
    space = page['_expandable']['space'].split('/')[-1]
    title = page['title']
    url = page['_links']['webui']
    page['url'] = f'{CONFLUENCE_URL}/{url}'
    page['label'] = f'[{space}] {title}'

JIRA_URL = config['jira']['URL']
JIRA_AUTH = (config['jira']['USER'],
             config['jira']['PASS'])
jira = requests.get(
    f'{JIRA_URL}/rest/api/2/search',
    params={
        'jql': 'ORDER BY updated',
        'fields': 'summary',
        'maxResults': 1000,
        'startAt': 0,
    },
    headers={'Content-Type': 'application/json'},
    auth=JIRA_AUTH)
issues = jira.json()['issues']
for issue in issues:
    key = issue['key']
    summary = issue['fields']['summary']
    issue['url'] = f'{JIRA_URL}/browse/{key}'
    issue['label'] = f'[{key}] {summary}'

items = pages + issues

r = Rofi()
index, key = r.select('Confluence/JIRA', [i['label'] for i in items])
if key >= 0:
    webbrowser.open_new_tab(items[index]['url'])
