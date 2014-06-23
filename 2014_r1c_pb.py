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
    
    if res == 2 and s1[0] * (len(s1)+len(s2)) == s1+s2:
        return 3
    return res

import math
from itertools import combinations
def solve2(Strs):
    Strs = {i:v for i, v in enumerate(Strs)}
    res3 = {}
    for i, j in combinations(Strs, 2):
        if checkValid(Strs[i], Strs[j]) == 3:
            c = Strs[i][0]
            if c not in res3:
                res3[c] = [i, j]
            else:
                if i not in res3[c]:
                    res3[c].append(i)
                if j not in res3[c]:
                    res3[c].append(j)
    
    for indexes in res3.itervalues():
        for i in indexes:
            del Strs[i]
    res = 0
    return res % 1000000007

    

# print solve2(["aa", "aa", "bcc", "cc"])
        
def solve(Strs):
    res = 0
    Strs = [compress(ss) for ss in Strs]
    for ss in permutations(Strs, len(Strs)):
        tmp = compress(''.join(ss))

        if check(tmp):
            res +=1
    return res % 1000000007

fn="C:/Users/ezonghu/Downloads/B-small-practice"
fi=open(fn+'.in')
fo=open(fn+'.out','w')
Cases = int(fi.next())
CaseId = 0
     
for l in fi:
    N = int(l.strip())
    strs = fi.next().split()
    res2 = solve2(strs)
    res = solve(strs)
    CaseId += 1
    Output = "Case #%d: %s %s" % (CaseId, res, res2)
    print(Output)
    fo.write(Output+'\n')
    if Cases == CaseId:
        break
fi.close()
fo.close()