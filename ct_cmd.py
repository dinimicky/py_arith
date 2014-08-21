#!/usr/bin/env python

'''
create a shell file or run the command:

cleartool setview -exec /home/ezonghu/ct.py ezonghu_mgc_pdb
'''

time_str0 = '20070523.101629'
time_str1 = '20070623.101629'
time_fmt = "%Y%m%d.%H%M%S"
get_datetime = lambda time_str : datetime.datetime.strptime(time_str, time_fmt)
import datetime
dt = get_datetime(time_str0)
dt2 = get_datetime(time_str1)
print(dt)
delta = dt2-dt
print(delta)
print(delta.total_seconds())
print(datetime.datetime.now())
def run_cmd(cmd):
    print(cmd)
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




