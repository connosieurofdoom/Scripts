import re

import subprocess

out = subprocess.check_output(['xinput', 'list'], shell= True).strip()
for line in out.splitlines():
    
    print(line.decode())

t = input("Enter id:")

out = subprocess.check_output(['xinput', 'float', t], shell= True).strip()

for line in out.splitlines():
    
    print(line.decode())

import time

time.sleep(5)