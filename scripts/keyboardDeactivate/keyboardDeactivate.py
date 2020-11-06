import re
import time
import subprocess

out = subprocess.check_output(['xinput', 'list'], shell= True).strip()
for line in out.splitlines():
    
    print(line.decode())

t = input("Enter id:")

try:
    subprocess.check_call('xinput float {}'.format(t), shell= True)
    out = subprocess.check_output(['xinput', 'list'], shell= True).strip()
    for line in out.splitlines():
        
        print(line.decode())

except Exception as e:
    print('\n',e,'\n',"Exiting in 5 seconds")
    time.sleep(5)





time.sleep(5)