import httpagentparser
import os, sys


def BrowserDetails(request):
    agent = request.environ.get('HTTP_USER_AGENT')
    browser = httpagentparser.detect(agent)
    if not browser:
        browser = agent.split('/')[0]
    else:
        browser_name = browser['browser']['name'] 
        browser_version = browser['browser']['version']
        browser = browser_name + " " + browser_version
    return browser
