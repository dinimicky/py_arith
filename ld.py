'''
Created on 2013-4-2

@author: ezonghu

Create Levenshtein distance algorithm.
'''
def try():
    pass

def ld(strS, strT):
    if "" == strS:
        return len(strT)
    
    if "" == strT:
        return len(strS)
    
    if strS[ -1] == strT[-1]:
        cost = 0
    else:
        cost = 1
        
    return min(ld(strS[0 :  -1], strT) + 1, 
               ld(strS, strT[0 : -1]) + 1,
               ld(strS[0 : -1], strT[0 : -1]) + cost)

def reverse_ld(strS, strT):
    if "" == strS:
        return len(strT)
    
    if "" == strT:
        return len(strS)
    
    if strS[0] == strT[0]:
        cost = 0
    else:
        cost = 1
        
    return min(reverse_ld(strS[1 : ], strT) + 1, 
               reverse_ld(strS, strT[1 : ]) + 1,
               reverse_ld(strS[1 : ], strT[1 : ]) + cost)  
               
def ld_wf(strS, strT):
    lenS = len(strS)
    lenT = len(strT)
    
    d = [[float('-infinity') for j in range(lenS+1)] for i in range(lenT+1)]
            
    for i in xrange(lenS+1):
        d[0][i] = i
        
    for j in xrange(lenT+1):
        d[j][0] = j
    
    for j in xrange(1, lenT+1):
        for i in xrange(1, lenS+1):
            cost = 0 if strS[i-1] == strT[j-1] else 1
            d[j][i] = min(d[j-1][i]+1, d[j][i-1]+1, d[j-1][i-1]+cost)
        
    return d[lenT][lenS], d

def distance(a,b):
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a,b = b,a
        n,m = m,n
        
    current = range(n+1)
    for i in range(1,m+1):
        previous, current = current, [i]+[0]*n
        for j in range(1,n+1):
            add, delete = previous[j]+1, current[j-1]+1
            change = previous[j-1]
            if a[j-1] != b[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)
            
    return current[n]


import time
def CalTimeElapse(strS, strT):
    StartTime=time.clock()
    print ld(strS, strT)
    EndTime=time.clock()
    print "elaspe time:%f" % (EndTime-StartTime)
    StartTime=time.clock()
    print reverse_ld(strS, strT)
    EndTime=time.clock()
    print "elaspe time:%f" % (EndTime-StartTime)         

#CalTimeElapse("kittenabcd", "sit")
#CalTimeElapse("kittenabcd", "sitnabcd")
#CalTimeElapse("kittenabcddfdsa", "sitnabcddfs")

if __name__ == '__main__' :
    print reverse_ld("kitten", "sitting")
    print ld("kitten", "sitting")
    print ld_wf("kitten", "sitting")
    print ld_wf("Sunday","Saturday")
    print reverse_ld("kittenabcd", "sitnabcd")
    print ld_wf("kittenabcd", "sitnabcd")
    print distance("Sunday","Saturday")
    print distance("kittenaf4wefifsdififadfefadasorgyeruifdafeawefadsfdgfgafeafefadfasdfdafdfafyuifhbcdab", 
                   "sitnabcdabdafdafefeadafdfdasfefdfdasfewfewafdfdddddddddddddddddddadfeeasdfdasdfdafdafdasffa")


    
    from timeit import Timer
    t1 = Timer("ld_wf(\"kittenabcd\", \"sitnabcd\")", "from __main__ import ld_wf")
    print sum(t1.repeat(10, 1))/10
    t1 = Timer("ld_wf(\"kittenabcda\", \"sitnabcd\")", "from __main__ import ld_wf")
    print sum(t1.repeat(10, 1))/10
    t1 = Timer("ld_wf(\"kittenabcd\", \"sitnabcda\")", "from __main__ import ld_wf")
    print sum(t1.repeat(10, 1))/10
    t1 = Timer("ld_wf(\"kittenabcda\", \"sitnabcda\")", "from __main__ import ld_wf")
    print sum(t1.repeat(10, 1))/10
    t1 = Timer("ld_wf(\"kittenabcdab\", \"sitnabcda\")", "from __main__ import ld_wf")
    print sum(t1.repeat(10, 1))/10
    t1 = Timer("ld_wf(\"kittenabcda\", \"sitnabcdab\")", "from __main__ import ld_wf")
    print sum(t1.repeat(10, 1))/10
    t1 = Timer("ld_wf(\"kittenaf4wefifsdififadfefadasorgyeruifdafeawefadsfdgfgafeafefadfasdfdafdfafyuifhbcdab\", \"sitnabcdabdafdafefeadafdfdasfefdfdasfewfewafdfdddddddddddddddddddadfeeasdfdasdfdafdafdasffa\")", "from __main__ import ld_wf")
    print sum(t1.repeat(100, 1))/100
    t1 = Timer("distance(\"kittenaf4wefifsdififadfefadasorgyeruifdafeawefadsfdgfgafeafefadfasdfdafdfafyuifhbcdab\", \"sitnabcdabdafdafefeadafdfdasfefdfdasfewfewafdfdddddddddddddddddddadfeeasdfdasdfdafdafdasffa\")", "from __main__ import distance")
    print sum(t1.repeat(100, 1))/100 
    
