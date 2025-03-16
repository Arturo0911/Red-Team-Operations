# Web Requests

```bash
1) To get the flag, start the above exercise, then use cURL to download the file returned by '/download.php' in the server shown above.

❯ curl -s "http://94.237.53.146:58508/download.php"
HTB{64$!c_cURL_u$3r}

2) What is the HTTP method used while intercepting the request? (case-sensitive)
Get

3) Send a GET request to the above server, and read the response headers to find the version of Apache running on the server, then submit it as the answer. (answer format: X.Y.ZZ)

❯ curl -s -X GET "http://94.237.53.146:58508/download.php" -I | grep "Server"
Server: Apache/2.4.41 (Ubuntu)

4) The server above loads the flag after the page is loaded. Use the Network tab in the browser devtools to see what requests are made by the page, and find the request to the flag.

  echo "after searching in the network dev tools I found this"
  http://94.237.55.96:59333/flag_327a6c4304ad5938eaf0efb6cc3e53dc.txt

❯ curl -s -X GET "http://94.237.55.96:59333/flag_327a6c4304ad5938eaf0efb6cc3e53dc.txt"
HTB{p493_r3qu3$t$_m0n!t0r}


5)  The exercise above seems to be broken, as it returns incorrect results. Use the browser devtools to see what is the request it is sending when we search, and use cURL to search for 'flag' and obtain the flag.

curl -s -X GET "http://94.237.59.30:50250/search.php?search=flag" -H "Authorization: Basic YWRtaW46YWRtaW4=" | html2text
flag: HTB{curl_g3773r}


6) Obtain a session cookie through a valid login, and then use the cookie with cURL to search for the flag through a JSON POST request to '/search.php'
["flag: HTB{p0$t_r3p34t3r}"]%
❯ curl -s -X POST "http://94.237.59.176:54649/" -d 'username=admin&password=admin' | html2text
[                    ]
Type a city name and hit Enter
❯ curl -s -X POST "http://94.237.59.176:54649/search.php" -b 'PHPSESSID=vjsev7ugpjh3gn5b64a44ij9jk' -H "Content-Type: application/json" -d '{"search":"flag"}'
["flag: HTB{p0$t_r3p34t3r}"]

7) 

curl -s -X GET "http://94.237.55.96:50942/api.php/city" | jq ".[].city_name" | grep -v "flag" | tr -d '"' | while read line; do curl -s -X DELETE "http://94.237.55.96:50942/api.php/city/$line"; done 

❯ curl -s -X GET "http://94.237.55.96:50942/api.php/city" | jq
[
  {
    "city_name": "flag",
    "country_name": "HTB{crud_4p!_m4n!pul4t0r}"
  },
  <snip>
]
```
