'''
Created on 2013-6-8

@author: Brilliant
'''
import copy

QueensList=[]
Queens=[]
def Position(row, col):
    return row*8+col

def checkColumn(Queens, row, col):
    r=row
    while r >= 0:
        r -= 1
        if r>= 0:
            if Position(r, col) in Queens:
                return False
        else:
            return True
       
def checkLeftOblique(Queens, row, col):
    r=row
    c=col
    while r>= 0 and c>= 0:
        c-= 1
        r-= 1
        if r>= 0 and c>= 0:
            if Position(r, c) in Queens:
                return False
        else:
            return True
       
def checkRightOblique(Queens, row, col):
    r=row
    c=col
    while r>= 0 and c<= 7:
        c+= 1
        r-= 1
        if r>= 0 and c<= 7:
            if Position(r, c) in Queens:
                return False
        else:
            return True

def getQueens(Queens, row):
    if row==8:
        global QueensList
        QueensList.append(copy.deepcopy(Queens))
        return
   
    for c in range(8):
        if (checkColumn(Queens, row, c)
            and checkLeftOblique(Queens, row, c)
            and checkRightOblique(Queens, row, c)):
            Queens.append(Position(row, c))
            getQueens(Queens, row+ 1)
            Queens.pop()
    return          

getQueens([], 0)
print( len(QueensList))
print( QueensList)
