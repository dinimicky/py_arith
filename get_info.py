'''
Created on 2013-9-1

@author: ezonghu
'''

'''
ssh  root@10.175.168.51 "cmw-repository-list |grep ' Used'"
ssh -p 2024 expert@10.175.168.12 "show ManagedElement 1 Equipment 1 Shelf 0"
ssh -p 2024 expert@10.175.168.12 "request ManagedElement 1 DmxFunctions 1 SoftwareManagement 1 get_sw_inventory"
'''
import subprocess

P=subprocess.Popen(["ssh  root@10.175.168.51 \"cmw-repository-list |grep ' Used'\""], shell=True,stdin=subprocess.PIPE)
P.communicate("rootroot\n")

def test(a):
    print( a)
    
test(1,2)