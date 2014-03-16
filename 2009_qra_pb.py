'''
Created on 2014-3-16

@author: ezonghu
'''
Label = 'a'
def filledBasinsWithoutLabel(Basins, Basin, LastLabel):
    if Basin == None:
        global Label
        Label = chr(ord(LastLabel)+1)
        return Label
    h,w = Basin
    NextBasin = Basins[h][w][1]
    Lab = Basins[h][w][2]
    if Lab == "":
        CurrLabel = filledBasinsWithoutLabel(Basins, NextBasin, LastLabel)
        Basins[h][w][2]=CurrLabel
        return CurrLabel
    else:
        return Lab
def filledBasins(Basins, Basin, label):
    if Basin == None:
        return
    h,w=Basin
    NextBasin = Basins[h][w][1] 
    Basins[h][w][2]=label
    return filledBasins(Basins, NextBasin, label)
def generateBasinRelationship(H,W, basins):
    for h in range(H):
        for w in range(W):
            North=(h-1, w) if h>=1 else None
            South=(h+1, w) if h<=H-2 else None
            East=(h, w+1) if w<=W-2 else None
            West=(h, w-1) if w>=1 else None
            Surrounding = [i for i in [North, West, East, South] if i != None]
            minLat = basins[h][w][0]
            for (sh,sw) in Surrounding:
                if basins[sh][sw][0] < minLat:
                    minLat = basins[sh][sw][0] 
                    basins[h][w][1]=(sh,sw)
    
    global Label
    Label = 'a'
    for h in range(H):
        for w in range(W):
            NextBasin = basins[h][w][1]
            CurrLabel = basins[h][w][2]
            
            if CurrLabel == '':
                filledBasinsWithoutLabel(basins, (h,w), Label)
            else:
                filledBasins(basins, NextBasin, CurrLabel)
            
            
            
            
f=open('B-large-practice.in')
first_line = f.readline()
Cases = int(first_line)
CaseNo = 0
for l in f:
    [H,W]=[int(i) for i in l.split()]
    basins = []
    tmp = 0
    for h in f:
        basins.append([[int(i), None, ""] for i in h.split()])
        tmp+=1
        if H==tmp:
            break
        
    basins[0][0][2]="a"
    CaseNo += 1
    print "Case #%d:" % (CaseNo)
    generateBasinRelationship(H,W, basins)    
    for h in range(H):
        for w in range(W):
            print basins[h][w][2],
        print
    print
        

f.close()