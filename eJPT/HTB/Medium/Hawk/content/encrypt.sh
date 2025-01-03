#!/bin/bash

for cipher in $(cat cipher-list.txt); do
	for lenght in $(ls | grep "^[0-9]\?[0-9]\?[0-9]\?$"); do
		openssl enc $cipher -e -in $lenght -out $lenght$cipher.enc -k PleaseSubscribe
	done
done
