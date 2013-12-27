'''
Created on 2013-12-5

@author: ezonghu
'''
class Position(object):
    def __init__(self, *Pos):
        if len(Pos) == 1:
            self.pos = Pos[0]
            self.x = self.pos % 9
            self.y = self.pos // 9 
        elif len(Pos) == 2:
            self.x = Pos[0]
            self.y = Pos[1]
            self.pos = self.x + self.y * 9
        else:
            raise TypeError("only accept the number of the arguments <=2")
        self.areaX = self.x // 3
        self.areaY = self.y // 3
        self.area = self.areaX + self.areaY * 3

class Area(object):
    def __init__(self, ShuduList, *Pos):
        if len(Pos) == 1:
            self.areaPos = Pos[0]
            self.areaX = self.areaPos % 3
            self.areaY = self.areaPos // 3 
        elif len(Pos) == 2:
            self.areaX = Pos[0]
            self.areaY = Pos[1]
            self.areaPos = self.areaX + self.areaY * 3
        else:
            raise TypeError("only accept the number of the arguments <=2")    
        
        self.area = set()
        self.areaStart = (self.areaX*3, self.areaY*3)
        self.areaStop = (self.areaX*3+2, self.areaY*3+2)
        for Row in range(self.areaY*3, (self.areaY+1)*3):
            for Col in range(self.areaX*3, (self.areaX+1)*3):
                p = Position(Col, Row)
                if ShuduList[p.pos] != 0:
                    self.area.add(ShuduList[p.pos])
class Column(object):
    def __init__(self, ShuduList, Col):
        self.column = set()
        for i in range(9):
            p = Position(Col, i)
            if ShuduList[p.pos] != 0:
                self.column.add(ShuduList[p.pos])
    
class Row(object):
    def __init__(self, ShuduList, R):
        self.row = set()
        for i in range(9):
            p = Position(i, R)
            if ShuduList[p.pos] != 0:
                self.row.add(ShuduList[p.pos])
                
class Shudu(object):
    defaultRange = set(range(1,10))
    def __init__(self, SDL):
        self.sdList = [int(i) for i in SDL]
        
    def getColumn(self, C):
        return Column(self.sdList, C)
    
    def getRow(self, R):
        return Row(self.sdList, R)
    
    def getArea(self, A):
        return Area(self.sdList, A)
    
    def exclusion(self, P):
        pos = Position(P)
        r_s = self.getRow(pos.y).row
        c_s = self.getColumn(pos.x).column
        a_s = self.getArea(pos.area).area
        tmp = self.defaultRange - (r_s|c_s|a_s)
        return tmp

             
    
    def scanSDLOnce(self):
        changeFlag = False
        sdListRightOrNot = True
        for i in xrange(81):
            tmp = self.sdList[i]
            if 0 == tmp:
                res = self.exclusion(i)
                if 0 == len(res):
                    sdListRightOrNot = False
                    return changeFlag, sdListRightOrNot
                
                if 1 == len(res):
                    self.sdList[i] = res.pop()
                    changeFlag = True
            
        return changeFlag, sdListRightOrNot
    
    #return -1: Can't find the value that can change
    #return -2: the current Shudu List is wrong
    #return 0: get the final result
    def scanSDLWithGuess(self):
        while (0 in self.sdList):
            changeFlag, sdListRightOrNot = self.scanSDLOnce()
            
            if False == changeFlag:
                return -1
            
            if False == sdListRightOrNot:
                return -2
        
        return 0                  
    
    def scanSDL(self):
#         print self.sdList
        res = self.scanSDLWithGuess()
        if -1 == res:
            tmpSDL = list(self.sdList)
            minSet = self.defaultRange
            pos = -1
            #do assumption
            for i in xrange(81):
                if 0 == self.sdList[i]:
                    tmp = self.exclusion(i)
                    if 0 == len(tmp):
                        return -2
                    if len(minSet)>len(tmp):
                        minSet = tmp
                        pos = i
                        
            for assumption in minSet:
                self.sdList[pos]=assumption
                if self.scanSDL() < 0 :
                    self.sdList = tmpSDL
                else:
                    return 0
                
        
        if -2 == res:
            #return False
            return res
        
        return res                
                        
        
           
                    

    
if __name__ == '__main__' :
    SDStr = []
    SDStr =  ["005000600080701040700060003090205060008040900060109080500090002040308010006000700",
              "800000000003600000070090200050007000000045700000100030001000068008500010090000400",
              "003279000020501009000080003000060500690003000005000000000000064700600080060920007",
              "142000387003040201080132005090000106000520704000004000608200009020000000001070000",
              "041020000000000007080005200610080000000010460000490050006000000437009106102000090",
              "000000100096200800800000600100082003000140060760050000600400901004020000950001000"]                    
    
    t = Shudu(SDStr[2])
    t.scanSDL()
    for i in range(0,81,9):
        print t.sdList[i:i+9]   
    from timeit import Timer
    for SDL in SDStr:     
        print SDL
        t1 = Timer("print Shudu(\"%s\").scanSDL() == 0" % SDL, "from __main__ import Shudu")
        print sum(t1.repeat(10, 1))/10      

        