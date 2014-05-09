'''
Created on 2014-5-3

@author: ezonghu
'''     
def solve2(A,B,K):
    if A < B:
        A, B = B, A
    
    res = 0
    for b in xrange(B):
        for a in xrange(b, A):
            if (a & b) < K:
                res += 1
                if a < B and b < A and a !=b :
                    res += 1
                
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
        print Output
        fo.write(Output+'\n')
        if Cases == CaseId:
            break
    fi.close()
    fo.close()
    
process()