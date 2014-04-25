'''
Created on Apr 25, 2014

@author: ezonghu
'''

def solve(r,t):
    import math
    n=(math.sqrt((2*r-1)**2+8*t)-(2*r-1))/4
    return long(n)
# print solve(1,9)
# print solve(1,10)
# print solve(3,40)
# print solve(1, 1000000000000000000)
# print solve(10000000000000000, 1000000000000000000)
fn="C:\Users\ezonghu\Downloads\A-large-practice"
fi=open(fn+'.in')
fo=open(fn+'.out','w')
first_line = fi.readline()
Cases = int(first_line)
CaseId = 0
 
for l in fi:
    [r, t] = [long(i) for i in l.split()]
    res = solve(r, t)
    CaseId += 1
    Output = "Case #%d: %s" % (CaseId, res)
    print Output
    fo.write(Output+'\n')
    if Cases == CaseId:
        break
fi.close()
fo.close()