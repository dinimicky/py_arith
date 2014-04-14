'''
Created on 2014-4-12

@author: ezonghu
'''
'''
Created on 2014-4-12

@author: ezonghu
''' 
def getBiggerThanNCW(NCW, KSBS):
    for i in range(len(KSBS)):
        if KSBS[i] > NCW:
            KSBS.pop(i)
            return True
    return False
def War(BN,NSBS, KSBS):
    if BN == 1:
        return 1 if NSBS[0]>KSBS[0] else 0
    
    while NSBS != []:
        NCW = NSBS.pop(0)
        if not getBiggerThanNCW(NCW, KSBS):
            return len(NSBS)+1
    return 0

def DWar(BN, NSBS, KSBS):
    if BN == 1:
        return 1 if NSBS[0]>KSBS[0] else 0
    
    NW = 0
    while NSBS != []:
        NCW = NSBS.pop(0)
        if NCW > KSBS[0]:
            KSBS.pop(0)
            NW +=1
        else:
            KSBS.pop()
        if KSBS != [] and NCW > KSBS[-1]:
            return len(NSBS)+NW
        
    return NW

def solve(BN, NBS, KBS):
    NBS.sort()
    KBS.sort()
    NBS2=list(NBS)
    KBS2=list(KBS)
    z = War(BN, NBS, KBS)
    y = DWar(BN, NBS2, KBS2)
    
    return y,z
        

f=open('C:\Users\ezonghu\Downloads\D-large.in')
 
first_line = f.readline()
Cases = int(first_line)
CaseId = 0
Line=0
 
for l in f:
     
 
    if Line == 0:
        block_num = int(l)
    elif Line ==1:
        N_Blocks=[float(i) for i in l.split()]
    elif Line == 2:
        K_Blocks=[float(i) for i in l.split()]
        CaseId +=1
        Line = 0
        
        y,z = solve(block_num, N_Blocks, K_Blocks) 
        print "Case #%d: %d %d" % (CaseId,  y, z)
        continue
 
         
    Line += 1        
     
    if Cases == CaseId:
        break
f.close()