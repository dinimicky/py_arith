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


def insertSort(L):
    for j in range(1, len(L)):
        key = L[j]
        for i in range(j, 0, -1):
            if key > L[i - 1]:
                L[i] = key
                break
            L[i] = L[i - 1]
    return L


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
            

def quickSort2(L):
    if len(L) < 2:
        return L
    Stack = [L]
    SL = []
    while Stack != []:
        e = Stack.pop(0)
        if isinstance(e, list):
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
        Stack = [small, pivot, big] + Stack
    return SL

def partition(L, s, e):
    pivot = L[e]
    i = s - 1
    for j in range(s, e):
        if L[j] < pivot:
            i += 1
            L[i], L[j] = L[j], L[i]
    
    L[e], L[i+1] = L[i+1], L[e]
    return i+1
    
def quickSort3(L, p, r):
    if p < r:
        q = partition(L, p, r)
        quickSort3(L, p, q - 1)
        quickSort3(L, q + 1, r)
    return L

def quickSort4(L):
    s = 0
    e = len(L) - 1
    Stack = [(s,e)]
    while Stack != []:
        (s,e) = Stack.pop(0)
        p = partition(L,s,e)
        if p + 1 < e:
            Stack.insert(0, (p + 1, e))
        if s < p - 1:
            Stack.insert(0, (s, p - 1))
    return L
    

def count_sort(A):
    k = max(A)
    C = [0] * (k + 1)
    B = [None] * len(A)
    for a in A:
        C[a] += 1
    
    i = 0
    for j in range(k + 1):
        if C[j] != 0:
            for _c in range(C[j]):
                B[i] = j
                i += 1

    return B

# print count_sort([1,5,3,3,2,6,99,7])
# print bubbleSort(list(TL))
# print insertSort(list(TL))
# print mergeSort(TL)
# print quickSort1(TL)
# print quickSort2(TL)                
# print quickSort3(list(TL), 0, len(TL)-1)
# print quickSort4(list(TL))