'''
Created on 2014-5-11

@author: ezonghu
'''
TL = [1,3,2,4,6,5]
def bubbleSort(L):
    for j in range(len(L), 1,-1):
        for i in range(1, j):
            if L[i] < L[i - 1]:
                L[i], L[i - 1] = L[i - 1], L[i]
    
    return L

print bubbleSort(TL)

def insertSort(L):
    for j in range(1, len(L)):
        key = L[j]
        for i in range(j, 0, -1):
            if key > L[i - 1]:
                L[i] = key
                break
            L[i] = L[i - 1]
    return L

print insertSort(TL)

def mergeSort(L):
    def merge(L1, L2):
        i = j = 0
        SL = []
        while i < len(L1) and j < len(L2):
            if L1[i] < L2[j]:
                SL.append(L1[i])
                i += 1
            else:
                SL.append(L2[j])
                j += 1
        if i < len(L1):
            SL += L1[i:]
        if j < len(L2):
            SL += L2[j:]
        return SL
    
    Queue = [[i] for i in L]
    while len(Queue) > 1:
        Queue.append(merge(Queue.pop(0), Queue.pop(0)))
    return Queue[0]

print mergeSort(TL)

def quickSort1(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    small = []
    big = []
    for i in L[1:]:
        if i < pivot:
            small.append(i)
        else:
            big.append(i)
    return quickSort1(small) + [pivot] + quickSort1(big)
            
print quickSort1(TL)

def quickSort2(L):
    if len(L) < 2:
        return L
    import types
    Stack = [L]
    SL = []
    while Stack != []:
        e = Stack.pop(0)
        if type(e) != types.ListType:
            SL.append(e)
            continue
        if e == []:
            continue
        small = []
        big = []
        pivot = e[0]
        for i in e[1:]:
            if i > pivot:
                big.append(i)
            else:
                small.append(i)
        Stack.extend([small, pivot, big])
    return SL
print quickSort2(TL)        
        