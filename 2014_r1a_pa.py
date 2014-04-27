'''
Created on 2014-4-26

@author: ezonghu
'''
'''
Created on Apr 25, 2014

@author: ezonghu
'''

def solve(L, A,B):
    ans = L+1
    for i in B:
        if sorted(A[0]^i^j for j in A) == B:
            ans = min(ans, bin(A[0] ^ i).count('1'))
        
    if ans == L+1:
        return "NOT POSSIBLE"
    return ans
        
        

fn="C:/Users/ezonghu/Downloads/A-large-practice"
fi=open(fn+'.in')
fo=open(fn+'.out','w')
Cases = int(fi.next())
CaseId = 0
 
for l in fi:
    [N, L] = [int(i) for i in l.split()]
    A=sorted(int(i,2) for i in fi.next().split())
    B=sorted(int(i,2) for i in fi.next().split())
    res = solve(L,A,B)
    CaseId += 1
    Output = "Case #%d: %s" % (CaseId, res)
    print Output
    fo.write(Output+'\n')
    if Cases == CaseId:
        break
fi.close()
fo.close()