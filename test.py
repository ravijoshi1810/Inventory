#!/usr/bin/env python3
import base64
import requests
url = 'https://raw.githubusercontent.com/ravijoshi1810/Inventory/master/input.csv'
req = requests.get(url)
if req.status_code == requests.codes.ok:
    req = req.json()  # the response is a JSON
    # req is now a dict with keys: name, encoding, url, size ...
    # and content. But it is encoded with base64.
    content = base64.decodestring(req['content'])
else:
    print('Content was not found.')
