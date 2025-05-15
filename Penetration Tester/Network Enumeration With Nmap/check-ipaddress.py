#!/usr/bin/python3

import os
import subprocess
import time
import sys


def check_tun0_interface():
    try:
        result = subprocess.run(["ip", "addr", "show", "tun0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode != 0:
            print("tun0 interface not found or not connected")
            sys.exit(1)


        for line in result.stdout.splitlines():
            if "inet" in line:
                ipaddr = line.strip().split()[1].split("/")[0]
                return ipaddr
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    print(check_tun0_interface())

