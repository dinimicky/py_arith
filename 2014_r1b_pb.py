'''
Created on 2014-5-3

@author: ezonghu
'''     
def getBit(num, i):
    return (num >> i) & 1
from functools import lru_cache
@lru_cache(maxsize = None)
def count(i, lessM, M):
    if i == -1:
        return lessM
    
    maxM = lessM or getBit(M, i) == 1
    
    res = count(i - 1, maxM, M)
    
    if maxM:
        res += count(i - 1, lessM, M)
    
    return res
print(count(31, False, 123456789))

@lru_cache(maxsize = None)
def countPairs(i, lessA, lessB, lessK, A, B, K):
    if i == -1:
        return lessA and lessB and lessK
    
    maxA = lessA or getBit(A, i) == 1
    maxB = lessB or getBit(B, i) == 1
    maxK = lessK or getBit(K, i) == 1
    
    count = countPairs(i - 1, maxA, maxB, maxK, A, B, K)
    if maxA:
        count += countPairs(i - 1, lessA, maxB, maxK, A, B, K)
    
    if maxB:
        count += countPairs(i - 1, maxA, lessB, maxK, A, B, K)
        
    if maxA and maxB and maxK:
        count += countPairs(i - 1, lessA, lessB, lessK, A, B, K)
        
    return count
        
@lru_cache(maxsize = None)
def f(A, B, K):
    if A == 0 or B == 0 or K == 0:
        return 0
    if A == B == 1:
        return 1
    return f((A+1)>>1, (B+1)>>1, (K+1)>>1) + \
           f((A+1)>>1, B>>1, (K+1)>>1) + \
           f(A>>1, (B+1)>>1, (K+1)>>1) + \
           f(A>>1, B>>1, K>>1)
                   
def solve2(A,B,K):
    if A < B:
        A, B = B, A
    
    res = 0
    for b in range(B):
        for a in range(b, A):
            if (a & b) < K:
                res += 1
                if a < B and b < A and a != b :
                    res += 1
                
    return res

def solve(A,B):
    res = []
    for a in range(A):
        for b in range(B):
            if (a & b) == 0:
                res.append((a,b))
    return res
                

def process():
    fn="C:/Users/ezonghu/Downloads/B-large-practice"
    fi=open(fn+'.in')
    fo=open(fn+'.out','w')
    Cases = int(fi.next())
    CaseId = 0
     
    for l in fi:
        [A,B,K] = [int(i) for i in l.split()]
        res2 = solve2(A,B,K)
        CaseId += 1
        Output = "Case #%d: %s" % (CaseId, res2)
        print(Output)
        fo.write(Output+'\n')
        if Cases == CaseId:
            break
    fi.close()
    fo.close()
    
# process()
print(solve2(3,4,1))