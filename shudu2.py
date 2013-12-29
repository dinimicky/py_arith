'''
Created on 2013-12-28

@author: ezonghu
'''
'''
Created on 2013-12-5

@author: ezonghu
'''
SDStr =  ["005000600080701040700060003090205060008040900060109080500090002040308010006000700",
          "800000000003600000070090200050007000000045700000100030001000068008500010090000400",
          "003279000020501009000080003000060500690003000005000000000000064700600080060920007",
          "142000387003040201080132005090000106000520704000004000608200009020000000001070000",
          "041020000000000007080005200610080000000010460000490050006000000437009106102000090",
          "000000100096200800800000600100082003000140060760050000600400901004020000950001000",
          "600000803040700000000000000000504070300200000106000000020000050000080600000010000"]                 
class Shudu(object):
    defaultRange = set(range(1,10))
    defaultPositions = [(i % 9, i //9)for i in xrange(81)]
    
    def __init__(self, SDL):
        self.sdList = [int(i) for i in SDL]
        
    def getColumn(self, C):
        ColSet = set()
        for i in xrange(9):
            element = self.sdList[i*9+C]
            if 0 != element:
                ColSet.add(element)
        return ColSet
    
    def getRow(self, R):
        RowSet = set()
        for i in xrange(9):
            element = self.sdList[R*9+i]
            if 0 != element:
                RowSet.add(element)
        return RowSet
    
    def getArea(self, X, Y):
        AreaSet = set()
        X1 = X // 3 * 3
        X2 = (X // 3+1) * 3
        Y1 = Y // 3 * 3
        Y2 = (Y // 3 + 1) * 3
        for i in xrange(Y1, Y2):
            for j in xrange(X1, X2):
                element = self.sdList[i * 9 + j]
                if 0 != element:
                    AreaSet.add(element)
        return AreaSet
    
    def exclusion(self, P):
        (posX, posY) = self.defaultPositions[P]
        r_s = self.getRow(posY)
        c_s = self.getColumn(posX)
        a_s = self.getArea(posX, posY)
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
                        
def evaluatePerformance():
    import cProfile
    global SDStr
    cProfile.run("Shudu(\"%s\").scanSDL()" % SDStr[-1])
    t=Shudu(SDStr[-1])
    t.scanSDL()
    for i in range(0,81,9):
        print t.sdList[i:i+9]        
           
def evaluateRunTime():
    global SDStr
    from timeit import Timer
    for SDL in SDStr:     
        print SDL
        t1 = Timer("Shudu(\"%s\").scanSDL()" % SDL, "from __main__ import Shudu")
        print sum(t1.repeat(10, 1))/10
    
if __name__ == '__main__' :
    evaluatePerformance()
    evaluateRunTime()        