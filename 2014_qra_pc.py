'''
Created on 2014-4-12

@author: ezonghu
'''
def solve(R,C,M):
    if R == 1:
        return 'c' + '.'*(C-M-1) + '*'*M
    if C == 1:
        return '\n'.join(['c'] + ['.']*(R-M-1) + ['*']*M)
    m = R*C - M
    res = [['*']*C for r in range(R)]
    if m == 1:
        return res
    for r in range(2, R+1):
        c = m // r
        z = m % r
        if c < 2 or c + (z>0) > C:
            continue
        if z == 1 and (r < 3 or c < 3):
            continue
        for x in range(r):
            for y in range(c):
                res[x][y] = '.'
        for y in range(z):
            res[y][c] = '.'
        if z == 1:
            res[z][c] = '.'
            res[r-1][c-1] = '*'
        return res
    return 
        
        
     
f=open('C:\Users\ezonghu\Downloads\C-small-attempt2.in')
 
first_line = f.readline()
Cases = int(first_line)
CaseId = 0
 
for l in f:
    CaseId += 1
    data =[int(i) for i in l.split()]
    print( "Case #%d: " % CaseId)
    Res  = solve(*data)
    if None == Res:
        print( "Impossible") 
    else:
        if type(Res)==type([]):
            Res[0][0]="c"
        for row in Res:
            for c in row:
                print( c, end = ' ')
            print
    if Cases == CaseId:
        break
f.close()