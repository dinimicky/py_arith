'''
Created on 2014-3-15

@author: ezonghu
'''
def parseWord(S):
    Letters=[]
    flag=None
    tmp=[]
    for i in S:
        if i=="(":
            flag="("
            tmp=[]
            continue
        if i==')':
            flag = None
            Letters.append(tmp)
            tmp=[]
            continue
        if flag =="(":
            tmp.append(i)
            continue
        Letters.append([i])
        
    return Letters

def getDict(Word, WDict):
    if len(Word)==0:
        return WDict
    if Word[0] not in WDict:
        WDict[Word[0]]=getDict(Word[1:], {})
    else:
        getDict(Word[1:], WDict[Word[0]])
    
    return WDict
def WordsCounter(Word, WDict, Counter=0):
    if Word==[]:
        return Counter+1
    Letters = Word[0]
    for l in Letters:
        if l in WDict:
            Counter = WordsCounter(Word[1:], WDict[l], Counter)
            
    return Counter
            
        
f=open("A-large-practice.in")
first_line=f.readline()
[L,D,N]=[int(i) for i in first_line.split()]

AList=[]
WDict = {}
for _i in range(D):
    Word = f.readline().strip()
    AList.append(Word)
    getDict(Word, WDict)

# print WDict
CaseNo = 0
for line in f:
    CaseNo +=1
    Word = parseWord(line.strip())  
    print( 'Case #%d: %d' % (CaseNo, WordsCounter(Word, WDict, 0)))
    
    

        