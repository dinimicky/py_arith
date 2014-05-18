'''
Created on 2014-3-21

@author: ezonghu
'''


def CounterWorst(L,P,C):
    if L*C >=P:
        return 0
    if L*C*C >= P :
        return 1
    
    import math
    N=(math.log(P)-math.log(L))/math.log(C)
    N=math.ceil(N)
    X=L*math.pow(C,N//2)
    return 1+max( CounterWorst(L,X,C), CounterWorst(X,P,C))
 
f = open('B-large-practice.in')
first_line = f.readline()
Cases = int(first_line)
CaseNo = 0
 
for l in f:
    CaseNo += 1
    [L,P,C]=[int(i)for i in l.split()]
    print( "Case #%d: %d" % (CaseNo, CounterWorst(L,P,C)))