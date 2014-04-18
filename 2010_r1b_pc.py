'''
Created on 2014-4-16

@author: ezonghu
'''
g_tab = {1:[1], 2:[1]}
import operator
def c(n,k):
    if n == 0:
        return 1
    if k == 0 or k==n:
        return 1
    return  reduce(operator.mul, range(n - k + 1, n + 1)) /reduce(operator.mul, range(1, k +1))
     

def getNumCombinations(K, N):
    AvailableNum = N-1-K
    res = []
        
    for i in range(1, K):
        Positions = K-1-i
        if AvailableNum >= Positions >= 0:
            res.append(c(AvailableNum, Positions))
            continue
        res.append(0)
    if res == []:
        return [1]
    return res
            
        
def solve(N):
    global g_tab
    if N in g_tab:
        return g_tab[N]
    res = []
    for i in range(1, N):
        if i in g_tab:
            tmp = g_tab[i]
        else:
            tmp = solve(i)
            
        res.append(sum([kv * c % 100003 for kv, c in zip(tmp,getNumCombinations(i, N))]))
    
    g_tab[N]=res
    return res

f=open('C:\Users\ezonghu\Downloads\C-large-practice.in')

import time
print time.time() 
first_line = f.readline()
Cases = int(first_line)
CaseId = 0

for l in f:
    n = int(l)
    res = sum(solve(n)) % 100003
    CaseId += 1
    print "Case #%d: %s" % (CaseId, res)
    if Cases == CaseId:
        break
f.close()
      
print time.time()
    
        
            