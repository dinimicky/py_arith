'''
Created on 2013-6-8

@author: Brilliant
'''
import types
Seq=list()
Seq=range(1,100)+range(300,400)+range(200,300)
Seq.reverse()
LargeSeq=range(1000,1, -1)+range( 3000, 4000)+range( 200, 3000)
def partition(List=[]):
    if List == []:
        return [], None, []
    if len(List) == 1:
        return [], List[0], []
    
    Upper =[]
    Lower = []    
    
    Pivot = List[0]
    RestList = List[1:]
    for value in RestList:
        if value > Pivot:
            Upper.append(value)
        else:
            Lower.append(value)
            
    return Lower, Pivot, Upper  

def qSort(List=[]):
    Lower, Pivot, Upper = partition(List)
    if Pivot == None:
        return []
    
    return qSort(Lower)+[Pivot]+qSort(Upper)

          
def qSort2(List):
    Result = []
    Stack = []
    Lower, Pivot, Upper = partition(List)
    Stack.append(Upper)
    Stack.append(Pivot)
    Stack.append(Lower)
    while True:
        if Stack != []:
            Top = Stack.pop()
        else:
            break
        if types.ListType == type(Top):
            if Top == []:
                continue
            Lower, Pivot, Upper = partition(Top)
            Stack.append(Upper)
            Stack.append(Pivot)
            Stack.append(Lower)
        else:
            if Top != None:
                Result.append(Top)
                
    return Result
            
    
      
print Seq
print qSort(Seq)
print qSort2(Seq)
print len(LargeSeq)
print qSort2(LargeSeq)

