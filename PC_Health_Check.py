#!/usr/bin/env python

import shutil
import psutil
import socket
import requests


def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free

def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage

def check_localhost():
        localhost = socket.gethostbyname('localhost')
        if localhost == "127.0.0.1":
                return True

def check_connectivity():
        request = requests.get("http://www.google.com")
        response = request.status_code
        if response == 200:
                return True
