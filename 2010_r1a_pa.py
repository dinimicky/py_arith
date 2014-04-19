'''
Created on 2014-4-19

@author: ezonghu
'''
slot={".":0, "R":1, "B":2}
rslot=[".", "R", "B"]
def clockwise90(board):
    def r(l):
        l.reverse()
        return l
    return [r(list(l)) for l in zip(*board)]

def anticlockwise90(board):
    newboard = [list(l) for l in zip(*board)]
    newboard.reverse()
    return newboard

def gravity(board):
    newboard = [[0 for _e in r] for r in board]
    
    c = 0
    for col in zip(*board):
        col_len = len(col)
        tmp = []
        for e in col:
            if e != 0:
                tmp.append(e)
        tmp.reverse()
        
        for r in xrange(len(tmp)):
            newboard[col_len-1-r][c]=tmp[r]
            
        c+=1
    
    return newboard
        
def printBoard(board):
    for r in board:
        for e in r:
            print e,
        print
        
def scanRow(board, K, Wins):
    for r in board:
        preflag = r[0]
        count = 1
        for e in r[1:]:
            if e == preflag:
                count += 1
            else:
                preflag = e
                count = 1
            
            if K == count:
                if preflag not in Wins:
                    Wins[preflag] = 1
                else:
                    Wins[preflag] += 1             
    return Wins

def scanCol(board, K, Wins):
    for c in zip(*board):
        preflag = c[0]
        count = 1
        for e in c[1:]:
            if e == preflag:
                count += 1
            else:
                preflag = e
                count = 1
            if K == count:
                if preflag not in Wins:
                    Wins[preflag] = 1
                else:
                    Wins[preflag] += 1
    return Wins
def scanDiagonal(board, K, Wins):
    rs = len(board)
    cs = len(board[0])
    bigboard1 = [ [ 0 for _j in range(rs+cs-1)] for _i in range(rs)]
    bigboard2 = [ [ 0 for _j in range(rs+cs-1)] for _i in range(rs)]
    
    for i in range(rs):
        bigboard1[i][i:]=board[i][:]+bigboard1[i][cs+i:]
        bigboard2[i][rs-1-i:]=board[i][:]+bigboard2[i][cs+rs-1-i:]
        
    Wins = scanCol(bigboard1, K, Wins)
    Wins = scanCol(bigboard2, K, Wins)
    return Wins

def read(board):
    newboard = []
    for r in board:
        tmp = []
        for e in r:
            tmp.append(slot[e])
        newboard.append(tmp)
    return newboard
def write(board):
    newboard = []
    for r in board:
        tmp = []
        for e in r:
            tmp.append(rslot[e])
        newboard.append(tmp)
    return newboard

def whoWin(board, K):
    newboard = read(board)
    T = gravity(clockwise90(newboard))
    w = scanRow(T, K, {})
    w = scanCol(T, K, w)
    w = scanDiagonal(T, K, w)
    if 0 in w:
        del w[0]
    if len(w) == 2:
        return "Both"
    if len(w) == 0:
        return "Neither"
    for k in w.keys():
        if k == 1:
            return 'Red'
        if k == 2:
            return 'Blue'
    
    
f=open('C:\Users\ezonghu\Downloads\A-large-practice.in')

first_line = f.readline()
Cases = int(first_line)
CaseId = 0

for l in f:
    [N, K] = [int(i) for i in l.split()]
    board = []
    for r in range(N):
        for l in f:
            board.append(l.strip())
            break
    
    res = whoWin(board, K)
    CaseId += 1
    print "Case #%d: %s" % (CaseId, res)
    if Cases == CaseId:
        break
f.close()
    

    
        
            
        
        