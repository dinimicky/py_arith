#!/usr/bin/env python

'''
create a shell file or run the command:

cleartool setview -exec /home/ezonghu/ct.py ezonghu_mgc_pdb
'''
def run_cmd(cmd):
    print( cmd)
    import subprocess
    proc = subprocess.Popen([cmd], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return proc.communicate()
cmd = 'cleartool lsview ezonghu*'

print(run_cmd(cmd))

cmd = 'cleartool catcs'
print(run_cmd(cmd))

cmd = 'cleartool lshistory'
print(run_cmd(cmd))

cmd = 'ls -l'
print(run_cmd(cmd))

cmd = 'pwd'
print(run_cmd(cmd))


import os

for r, ds, fs in os.walk("."):
    for d in ds:
        print(r+d)



