'''
Created on 2014-4-16

@author: ezonghu
'''
'''
Created on 2014-4-16

@author: ezonghu
'''  
def solve(N,K,B,T, Cs):
    Ts = []
    for i in range(N):
        [x,v]=Cs[i]
        T1=(B-x)/v
        if T1 <= T:
            Ts.insert(0, i)
    if len(Ts) < K:
        return "IMPOSSIBLE"
    if len(Ts) == K and K==0:
        return 0

    swap = 0

    for i in Ts:
        if K == 0:
            return swap
        for j in range(i+1,N):
            if j not in Ts:
                swap +=1
            
        K-=1
            
                    
    return swap
        
        


f=open('C:\Users\ezonghu\Downloads\B-large-practice.in')

first_line = f.readline()
Cases = int(first_line)
CaseId = 0

for l in f:
    [N, K, B, T] = [int(i) for i in l.split()]
    Line=0
    for l in f:
        Line +=1
        if Line == 1:
            X = [float(i) for i in l.split()]
        if Line == 2:
            V = [float(i) for i in l.split()]
            break
    
    Cs=[]
    for x, v in zip(X,V):
        Cs.append([x, v])
        
    res = solve(N,K,B,T, Cs)
    CaseId += 1
    print "Case #%d: %s" % (CaseId, res)
    if Cases == CaseId:
        break
f.close()
    

    
        
            