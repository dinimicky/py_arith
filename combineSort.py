'''
Created on 2013-6-8

@author: Brilliant
'''
def combine2SortedLists(List1, List2):
    if len(List1)> 0 and len(List2)> 0:
        if List1[ 0]>List2[ 0]:
            return [List2[ 0]]+combine2SortedLists(List1, List2[ 1:])
        elif List1[ 0]<List2[ 0]:
            return [List1[ 0]]+combine2SortedLists(List1[ 1:], List2)
        else:
            return [List1[ 0], List2[ 0]]+combine2SortedLists(List1[ 1:], List2[ 1:])
    elif len(List2)== 0:
        return List1
    elif len(List1)== 0:
        return List2
       
def combineSort(List1):
    NewList1=[]
    for value in List1:
        NewList1.append([value])
    return do_combineSort(NewList1)
       
def do_combineSort(ListsOfList=[]):
    if len(ListsOfList) == 1:
        return ListsOfList[ 0]

    i = 1
    Result = []   
    while i < len(ListsOfList):
        Result.append(combine2SortedLists(ListsOfList[i- 1], ListsOfList[i]))
        i+= 2
    if len(ListsOfList) % 2 == 1 :
        Result.append(ListsOfList[- 1])
    return do_combineSort(Result)

print combine2SortedLists([1 ,2 ,3 ,4 ], [1 ,6 ,7 ,8 ])
print combineSort([6 ,5 ,4 ,3 ,2 ,1 ])

Seq=range(1,100)+range(300,400)+range(200,300)
Seq.reverse()
print combineSort(Seq)
