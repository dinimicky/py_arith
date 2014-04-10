'''
Created on 2014-3-22

@author: ezonghu
'''
def analysisHex(H):
    filters = [8,4,2,1]
    bits = []
    for f in filters:
        if H & f != 0:
            bits.append(1)
        else:
            bits.append(-1)
    return bits

def Squares(Bark):
    Rows = len(Bark)
    squares = []
    for r in Bark:
        squares.append([])
        for _c in r:
            squares[-1].append(0)

    for rid in xrange(Rows):
        r = Bark[rid]
        for cid in xrange(len(r)):
            if rid == 0 and Bark[rid][cid] != 0:
                squares[rid][cid]= 1
                continue
            if cid == 0 and Bark[rid][cid] != 0:
                squares[rid][cid]= 1
                continue
           
            if (Bark[rid][cid] * Bark[rid-1][cid-1] == 1 and
                Bark[rid][cid] * Bark[rid][cid-1] == -1 and
                Bark[rid][cid] * Bark[rid-1][cid]) == -1 :
                squares[rid][cid] = 1 + min( squares[rid-1][cid-1],
                                              squares[rid-1][cid],
                                              squares[rid][cid-1] )
            elif Bark[rid][cid] == 0:
                squares[rid][cid] = 0
            else:
                squares[rid][cid] = 1
    return squares
def checkSquares(max_size, Squares, s_rid, s_cid):
    for rid, cid in Squares:
        deltar=abs(s_rid-rid)
        deltac=abs(s_cid-cid)
        if deltar>=max_size or deltac>=max_size:
            continue
        else:
            return False
    return True

def getLargestSquares(squares):
    sizes = {}
    for rid in xrange(len(squares)):
        for cid in xrange(len(squares[rid])):
            sz = squares[rid][cid]
            if sz not in sizes:
                sizes[sz] = [[rid,cid]]
                continue
            
            sizes[sz].append([rid,cid])
    
    max_size = max(sizes.keys())        
    max_squares = sizes[max_size]
#    print max_squares
    OkSquares = []

    for rid,cid in max_squares:
        if checkSquares(max_size, OkSquares, rid, cid):
            OkSquares.append([rid,cid])
            
    return max_size, OkSquares
        
def updateRows(size, squares, rows):
    for rid, cid in squares:
        for r in xrange(rid-size+1, rid+1):
            for c in xrange(cid-size+1, cid+1):
                rows[r][c]=0
#    printRows(rows)            
    return rows        
def printRows(rows):
    for r in rows:
        print r
                                       
f = open('C-large-practice.in')
first_line = f.readline()
Cases = int(first_line)
CaseNo = 0
           
for l in f:
    CaseNo += 1
    [M, N] = [int(i) for i in l.split()]
    total_grid = M * N
#     print M,N
    rows = []
    for r in f:
        M -= 1
        tmp = []
        for c in r.strip():
            tmp.extend(analysisHex(int(c, 16)))
           
        rows.append(tmp)
        if M == 0:
            break

    res = []

    def checkRows(rows):
        for r in rows:
            for c in r:
                if c !=0:
                    return True
        return False
    while sum([sz*sz*num for sz, num in res]) < total_grid:
        
        s, sqs = getLargestSquares(Squares(rows))
        updateRows(s,sqs, rows)
        res.append([s, len(sqs)])

    print 'Case #%d: %d' % (CaseNo, len(res))
    
    for sz, num in res:
        print sz,num
    if CaseNo==Cases:
        break

f.close()    
