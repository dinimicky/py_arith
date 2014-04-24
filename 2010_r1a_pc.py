'''
Created on 2014-4-25

@author: ezonghu
'''

import math

    
def solve3(A1,A2,B1,B2):
    phi = (1+5**.5)/2
    tot = 0
    for a in range(A1,A2+1):
        phihigh = math.ceil(phi*a)
        philow = math.floor(a/phi)
        tot += max(0,min(philow,B2)-B1+1)
        tot += max(0,B2-max(B1,phihigh)+1)
    return tot
def iswin(a,b):
    m = min(a, b)
    n = max(a, b)
    if m == n:
        return False
    if n/m >= 2:
        return True
    if n%m == 0:
        return True
    if n/m == 1:
        return not iswin(n-m, m)

def win(a,b):
    from math import sqrt
    return max(a,b)>= (1+sqrt(5))/2*min(a,b)    
def WinAB(a, b):
    if a == b:
        return False
    
    big = max(a,b)
    small = min(a,b)
    y = big % small
    s = big // small
    if y == 0:
        return True
    
    if s != 1:
        big1 = small+y
        small1 = small
        result = not WinAB(big1, small1)
        if result:
            return True      
    
    big2 = small
    small2 = y
    result = not WinAB(big2, small2)
    
    return result

def solve(A1,A2,B1,B2):
    counter = 0
    cache = []
    for i in xrange(A1,A2+1):
        for j in xrange(B1, B2+1):
            if (max(i,j), min(i,j)) in cache:
                counter +=1
                continue
            if WinAB(i,j):
                cache.append((max(i,j), min(i,j)))
                counter+=1
    return counter     
def solve2(A1,A2,B1,B2):
    counter = 0
    for i in xrange(A1,A2+1):
        for j in xrange(B1, B2+1):
            if win(i,j):
                counter+=1
    return counter              
f=open('C:\Users\ezonghu\Downloads\C-large-practice.in')
 
first_line = f.readline()
Cases = int(first_line)
CaseId = 0
Line=0
import time
t1=time.time() 
for l in f:
    data = [int(i) for i in l.split()]
    CaseId+=1
    print "Case #%d: %d" % (CaseId, solve3(*data))
    if Cases == CaseId:
        break
f.close()