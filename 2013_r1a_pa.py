'''
Created on Apr 25, 2014

@author: ezonghu
'''
def inks(r,n):
    return 2*n**2+(2*r-1)*n

def solve(r,t):
    import math
    n=(math.sqrt((2*r-1)**2+8*t)-(2*r-1))/4
    return int(n)
def solve2(r,t):
    res, lo, hi = 0, 1, t
    while lo <= hi:
        mid = (lo + hi) / 2
        if inks(r, mid) > t:
            hi = mid - 1
        else:
            lo, res = mid + 1, mid
            
    return res
    
# print solve2(1,9)
# print solve2(1,10)
# print solve2(3,40)
# print solve2(1, 1000000000000000000)
# print solve2(10000000000000000, 1000000000000000000)

def process():
    fn="C:\Users\ezonghu\Downloads\A-large-practice"
    fi=open(fn+'.in')
    fo=open(fn+'.out','w')
    first_line = fi.readline()
    Cases = int(first_line)
    CaseId = 0
     
    for l in fi:
        [r, t] = [long(i) for i in l.split()]
        res = solve2(r, t)
        CaseId += 1
        Output = "Case #%d: %s" % (CaseId, res)
        print Output
        fo.write(Output+'\n')
        if Cases == CaseId:
            break
    fi.close()
    fo.close()
    
process()