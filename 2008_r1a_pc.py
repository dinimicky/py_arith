'''
Created on 2014-3-14

@author: ezonghu
'''

fn="C-large-practice.in"

fp=open(fn)

CaseNum = int(fp.readline())
def multi(M1,M2):
    return [[sum(map(lambda x:x[0]*x[1] % 10000, zip(i,j))) for j in zip(*M2)]for i in M1]

def fast_exp(A, n):
    if n == 1:
        return A
    if n % 2 == 0:
        A1=fast_exp(A, n/2)
        return multi(A1,A1)
    return multi(A, fast_exp(A,n-1))

def solve(n):
    A = [[6,-4],[1,0]]
    X = [[28],[6]]
    if n ==0:
        return 2
    if n==1:
        return 6
    if n==2:
        return 28
    return multi(fast_exp(A,n-2), X)[0][0] %1000
# print CaseNum
CaseItem=0
for line in fp:
    CaseItem += 1
    print( 'Case #%d: %03d' % (CaseItem, (solve(int(line))+999)%1000))
