'''
Created on 2014-7-30

@author: ezonghu
'''

def BFS(G, s):
    color = {}
    pai = {}
    d = {}
    
    for v in G:
        color[v] = 0
        pai[v] = None
        d[v] = float('+inf')
        
    q = []
    
    q.append(s)
    color[s] = 1
    d[s] = 0
    pai[s] = None
    
    while not q:
        p = q.pop(0)
        for c in G[p]:
            if color[c] == 0:
                color[c] = 1
                pai[c] = p
                d[c] = d[p] + 1
                q.append(c)
        
        color[p] = 2
        
    return pai,color,d
        
    
    