'''
Created on 2014-4-26

@author: ezonghu
'''
from itertools import combinations
class Node(object):
    def __init__(self, parent=None):
        self.node = None
        self.parent = parent
        self.childs = []

def buildTree2(d,r):
    tmp=[r]
    while d != {}:
        c = tmp.pop(0)
        for i in d[c.node]:
            if i == c.parent:
                continue
            tc = Node(c.node)
            tc.node = i
            c.childs.append(tc)
        del d[c.node]
        tmp.extend(c.childs)
        
        
        
def buildTree(d, r):
    if d=={}:
        return
    for i in d[r.node]:
        if i == r.parent:
            continue
        tc = Node(r.node)
        tc.node = i
        r.childs.append(tc)
    
    del d[r.node]
    for c in r.childs:
        buildTree(d, c)

def buildFullBinaryTree(node):
    if len(node.childs) <=1:
        return 1
    
    maxBT = 0
    for lc, rc in combinations(node.childs, 2):
        tmp=1+buildFullBinaryTree(lc)+buildFullBinaryTree(rc)
        maxBT=max(maxBT, tmp)
    
    return maxBT 


def solve(N, edges):
    d={}
    for i in range(1,N+1):
        d[i]=[]
        
    for p1, p2 in edges:
        d[p1].append(p2)
        d[p2].append(p1)
    
    deleted = N+1        
    for i in d:
        root = Node(None)
        root.node = i
        buildTree2(dict(d), root)
        deleted = min(deleted, N-buildFullBinaryTree(root))
    return deleted
        
import time
curr=time.clock()
fn="C:/Users/ezonghu/Downloads/B-large-practice"
fi=open(fn+'.in')
fo=open(fn+'.out','w')
first_line = fi.readline()
Cases = int(first_line)
CaseId = 0
  
for l in fi:
    N = int(l)
    Edges = []
    for i in range(N-1):
        e = [int(i) for i in fi.next().split()]
        Edges.append(e)
    res = solve(N, Edges)
    CaseId += 1
    Output = "Case #%d: %s" % (CaseId, res)
    print( Output)
    fo.write(Output+'\n')
    if Cases == CaseId:
        break
fi.close()
fo.close()
print( time.clock()-curr)