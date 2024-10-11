#!/usr/bin/python3


import requests
from base64 import b64encode, b64decode
from urllib.parse import urlencode


def main():
	payload = """<?xml  version="1.0" encoding="ISO-8859-1"?>
		<bugreport>
		<title>w</title>
		<cwe>s</cwe>
		<cvss>w</cvss>
		<reward>w</reward>
		</bugreport>
	"""
	payload = b64encode(payload.encode("UTF-8")).decode()
	
	data = urlencode({"data": payload})
	ress = requests.post(url="http://10.10.11.100/tracker_diRbPr00f314.php", data=data)
	print(ress.status_code)
	print(ress.text)


if __name__ == "__main__":
	main()
