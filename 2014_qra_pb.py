'''
Created on 2014-4-12

@author: ezonghu
'''

def solve(C,F,X):
    S=2
    T=0
    while True:
        T1 = X/S
        T2 = X/(S+F)+C/S
        if T1 <= T2:
            return "%.7f" % (T1+T)
        
        T += C/S
        S += F
        
f=open('C:\Users\ezonghu\Downloads\B-large.in')

first_line = f.readline()
Cases = int(first_line)
CaseId = 0

for l in f:
    CaseId += 1
    data =[float(i) for i in l.split()]
    print "Case #%d: %s" % (CaseId, solve(*data))
    if Cases == CaseId:
        break
f.close()