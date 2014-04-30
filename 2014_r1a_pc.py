'''
Created on 2014-4-26

@author: ezonghu
'''
import random
def good(N):
    a=[0]*N
    for i in range(N):
        a[i]=i
        
    for k in range(N):
        p=random.randint(k,N-1)
        a[k], a[p] = a[p], a[k]
    return N,a
def bad(N):
    a=[0]*N
    for i in range(N):
        a[i]=i
        
    for k in range(N):
        p=random.randint(0,N-1)
        a[k], a[p] = a[p], a[k]
    return N,a

def solve(N,a):
    return 'BAD' if sum(i>a[i] for i in range(N)) < 484 else 'GOOD'
def test():
    for _i in range(1000):
        print "GOOD" == solve(*good(1000))
        print "BAD" == solve(*bad(1000))
def process():
    fn="C:\Users\ezonghu\Downloads\C-small-practice"
    fi=open(fn+'.in')
    fo=open(fn+'.out','w')
    first_line = fi.readline()
    Cases = int(first_line)
    CaseId = 0
  
    for l in fi:
        N = int(l.strip())
        a = [int(i) for i in fi.next().split()]
        res = solve(N, a)
        CaseId += 1
        Output = "Case #%d: %s" % (CaseId, res)
        print Output
        fo.write(Output+'\n')
        if Cases == CaseId:
            break
    fi.close()
    fo.close()

    
process()
# test()