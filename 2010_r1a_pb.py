'''
Created on 2014-4-20

@author: ezonghu
'''
def solve2(D, I, m, data):
    n = len(data)
    tab = [0] * 256
    otab = [0] * 256
    for i in xrange(n):
        otab, tab = tab, otab
        for j in xrange(256):
            cur = otab[j] + D
            for k in xrange(256):
                new = otab[k] + abs(data[i] - j)
                if k != j:
                    if m == 0:
                        continue
                    new += (abs(k - j) - 1) // m * I
                cur = min(cur, new)
            tab[j] = cur
    return min(tab)


f=open('C:\Users\ezonghu\Downloads\B-small-practice.in')
 
first_line = f.readline()
Cases = int(first_line)
CaseId = 0
Line=0
import time
t1=time.time() 
for l in f:
 
    [D,I,M, N] = [int(i) for i in l.split()]
    for l in f:
        An = [ int(i) for i in l.split()]
        break
    An1=list(An)
    res2 = solve2(D,I,M,An)
    CaseId += 1
    
    print "Case #%d: %d" % (CaseId, res2)
    if Cases == CaseId:
        break
f.close()
print time.time()-t1    
        