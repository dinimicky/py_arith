'''
Created on 2014-4-26

@author: ezonghu
'''
'''
Created on Apr 25, 2014

@author: ezonghu
'''
from itertools import permutations
def compress(ss):
    res = ss[0]
    for c in ss[1:]:
        if c == res[-1]:
            continue
        res += c
    return res
def check(ss):
    res = [ss[0]]
    for c in ss[1:]:
        if c == res[-1]:
            continue
        if c not in res:
            res.append(c)
            continue
        return False
    return True

def checkValid(s1, s2):
    res = 1
    for c in s2:
        if c in s1:
            if c == s1[-1]:
                res = 2
            else:
                return 0
    return res

import math
def solve2(Strs):
    res = []
    for s1, s2 in permutations(Strs, 2):
        if checkValid(s1, s2) == 2:
            res.append((s1, s2))
    
    if res == []:
        return math.factorial(len(Strs))
    
    NStrs = [list(Strs)]
    for s1, s2 in res:
        for strs in NStrs:
            if s1 in NStrs and s2 in NStrs:
                NStrs.remove(s1)
                NStrs.remove(s2)
                NStrs.append(s1+s2)
                continue
            if s1 not in NStrs:
                NStrs
            
    return sum(total)
        
    

    

# print solve2([compress(ss) for ss in ["aa", "aa", "bcc", "cc"]])
        
def solve(Strs):
    res = 0
    Strs = [compress(ss) for ss in Strs]
    for ss in permutations(Strs, len(Strs)):
        tmp = compress(''.join(ss))

        if check(tmp):
            res +=1
    return res % 1000000007

# fn="C:/Users/ezonghu/Downloads/B-small-practice"
# fi=open(fn+'.in')
# fo=open(fn+'.out','w')
# Cases = int(fi.next())
# CaseId = 0
#     
# for l in fi:
#     N = int(l.strip())
#     strs = fi.next().split()
#     res = solve(strs)
#     CaseId += 1
#     Output = "Case #%d: %s" % (CaseId, res)
#     print Output
#     fo.write(Output+'\n')
#     if Cases == CaseId:
#         break
# fi.close()
# fo.close()