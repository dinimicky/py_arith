'''
Created on 2014-3-11

@author: ezonghu
'''
fp = open('B-large-practice.in')

def checkX(CF, X):
    Malted, UnMalted=CF
    if UnMalted != []:
        for T in UnMalted:
            if 0 == X[T]:
                return True
    if Malted != None:
        if 1 == X[Malted]:
            return True
    return False

def initX(Types):
    return {i:0 for i in xrange(1,Types+1)}
            
def checkXModification(PreCFs, X):
    for CF in PreCFs:
        if not checkX(CF, X):
            return False
    return True

def tryX(CustomersFlavors, X):
    for i in xrange(len(CustomersFlavors)):
        CF = CustomersFlavors[i]
        if checkX(CF,X):
            continue
        Malted, Umalted = CF
        if Malted == None and Umalted != []:
            return False
        
        if Malted != None:
            X[Malted]=1
            return tryX(CustomersFlavors, X)
        
    return X  

first_line = True
CaseNum = 0
CaseItem = 0
CaseLine = 0
for line in fp:
    if first_line:
        CaseNum = int(line)
        first_line = False
        continue
    if CaseLine == 0:
        CaseLine +=1
        CaseItem +=1
        Types = int(line)
        continue
    if CaseLine == 1:
        CaseLine +=1
        Customers = int(line)
        CustomersFlavors = []
        continue
    if CaseLine >= 2:
        CaseLine += 1
        Customers -= 1
        OneCustomerFlavor = [int(i) for i in line.split()]
        Ts = []
        Tm = None
        for i in xrange(OneCustomerFlavor[0]):
            T = OneCustomerFlavor[i*2+1]
            M = OneCustomerFlavor[i*2+2]
            if 1==M:
                Tm=T
                continue
            Ts.append(T)
        CustomersFlavors.append((Tm, Ts))
        
        if Customers == 0:
            CaseLine = 0
            
            Str = 'Case #%d: %s'
            if CaseItem==2:
                pass
            Res2 = tryX(CustomersFlavors, initX(Types))
            def printRes(Res):
                if Res==False: 
                    print Str % (CaseItem, 'IMPOSSIBLE')
                else:
                    ResStr=''
                    for i in xrange(1,Types+1):
                        ResStr +=' %d' % Res[i]
                    print Str % (CaseItem, ResStr)
            printRes(Res2)
            CustomersFlavors=[]

