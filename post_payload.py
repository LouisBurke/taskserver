from json import dumps

from furl import furl
from requests import (get, post)

f = furl('http://127.0.0.1:8000')
f.path.segments = ['tasks', 'handler']

task = {
    'command': 'python3',
    'arguments': ["-c", "print('hello')"],
    'environment': {
        "PATH": "/usr/local/bin/python3"
    },
    "working_directory": "/Users/louis"
}

resp = post(f.url, data=dumps(task))

print(resp.content.decode('utf8'))
