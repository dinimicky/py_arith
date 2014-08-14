'''
Created on 2014-8-14

@author: ezonghu
'''
class cfg(object):
    OAM_IP = '1.1.1.1'
    LOCAL_NODE = 'client@10.170.9.122'
    TRAF_IP = '2.2.2.2'
TestString = '''
{sisNetconf, {"$OAM_IP$", 830, "expert", "expert"}}.
{sisSftp, {"$OAM_IP$", 22, "root", "tre,14"}}.
{mgcName, "mgc2_slot7"}.
{localNode, "$LOCAL_NODE$"}.
{remoteNode, [{server, {"$TRAF_IP$", 22, "root","mgcroot"}},
                 {nodeName, "remote@10.170.9.123"},
                 {srcPath, "/home/ewagyae/MGC_AUTO_ST/MGC_ST/src"}]}.
'''

import re

p = re.compile('\$([a-zA-Z0-9_]+)\$')

l = [ i.group(1) for i in p.finditer(TestString)]
res = [ getattr(cfg, i.group(1)) for i in p.finditer(TestString)]


print(p.sub('%s', TestString))
print(p.sub('%s', TestString) % tuple(res))

import importlib

m = importlib.import_module("test_env")
res = [getattr(m, i.group(1)) for i in p.finditer(TestString)]
print(p.sub('%s', TestString) % tuple(res))