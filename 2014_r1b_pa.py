'''
Created on 2014-5-3

@author: ezonghu
'''

def distance(a,b):
    "Calculates the Levenshtein distance between a and b."
    a, b = " " + a, " " + b
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a,b = b,a
        n,m = m,n
    current = [0] + [float('+infinity')]*(n-1)
    for i in range(1, m):
        previous, current = current, [float('+infinity')] + [0]*(n-1)
        for j in range(1,n):
            add = previous[j]+1 if b[i] == a[j] else float('+infinity')
            delete = current[j-1]+1 if a[j] == b[i] else float('+infinity')
            change = previous[j-1] if a[j] == b[i] else float('+infinity')
            current[j] = min(add, delete, change)
    return current[n-1]

def maxSubStr(A,B):
    n = len(A)
    m = len(B)
    mss = ""
    
    if A[0] != B[0]:
        return "Fegla Won"
    i = j = 1
    mss += A[0]
    while i < n and j < m:
        if A[i] == B[j]:
            mss += A[i]
            i += 1
            j += 1
            continue
        if A[i - 1] == A[i]:
            i += 1
            continue
        if B[j - 1] == B[j]:
            j += 1
            continue
        return "Fegla Won"
    return mss

def compress(s):
    cs = [s[0]]
    cc = [1]
    for c in s[1:]:
        if c == cs[-1]:
            cc[-1] += 1
            continue
        cs.append(c)
        cc.append(1)
    return cs, cc
        

def solve3(Strs):
    cs, cc = compress(Strs[0])
    ccs = [cc]
    for s in Strs[1:]:
        ncs, ncc = compress(s)
        if ncs != cs:
            return "Fegla Won"
        ccs.append(ncc)
        
    ma = 0
    for ec in zip(*ccs):
        ave = sum(ec)/len(ec)
        ma += min(sum(abs(e - ave) for e in ec) for ave in range(min(ec),max(ec)+1))
            
    return ma
    

def solve2(Strs):
    [s1,s2]=Strs
    m1 = maxSubStr(s1, s2)
    m2 = maxSubStr(s1[::-1], s2[::-1])
    if m1 == "Fegla Won" or m2 == "Fegla Won":
        return "Fegla Won"
    return sum(abs(len(s)-len(m1)) for s in Strs)

    
def solve(Strs):
    res = distance(Strs[0],Strs[1])
    if res == float('+infinity'):
        return "Fegla Won"
    return res
    
def process():
    fn="C:/Users/ezonghu/Downloads/A-large-practice"
    fi=open(fn+'.in')
    fo=open(fn+'.out','w')
    Cases = int(fi.next())
    CaseId = 0
     
    for l in fi:
        N = int(l.strip())
        Strs = []
        for _i in range(N):
            Strs.append(fi.next().strip())

        res3 = solve3(Strs)
        CaseId += 1
        Output = "Case #%d: %s" % (CaseId, res3)
        print( Output)
        fo.write(Output+'\n')
        if Cases == CaseId:
            break
    fi.close()
    fo.close()
    
process()