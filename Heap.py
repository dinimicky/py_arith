def parent(i):
    return i // 2

def left(i):
    return i * 2

def right(i):
    return i * 2 + 1

def max_heapify1(Heap, i):
    heap_len = Heap[0]
    l = left(i)
    r = right(i)
    
    if l <= heap_len and Heap[i] <= Heap[l]:
        largest = l
    else:
        largest = i
        
    if r <= heap_len and Heap[largest] <= Heap[r]:
        largest = r
        
    if largest != i:
        Heap[i], Heap[largest] = Heap[largest], Heap[i]
        max_heapify1(Heap, largest)
        
def max_heapify2(Heap, i):
    heap_len = Heap[0]
    
    while i < heap_len:
        r = right(i)
        l = left(i)
        
        if l <= heap_len and Heap[i] <= Heap[l]:
            largest = l
        else:
            largest = i
            
        if r <= heap_len and Heap[largest] <= Heap[r]:
            largest = r
            
        if largest == i:
            break
        
        Heap[i], Heap[largest] = Heap[largest], Heap[i]
        i = largest
        
def build_max_heap(L):
    Heap = list(L)
    heap_len = len(Heap)
    Heap.insert(0, heap_len)
    
    for i in range(heap_len // 2, 0, -1):
        max_heapify2(Heap, i)
        
    return Heap

def heap_sort(L):
    Heap = build_max_heap(L)
    
    while Heap[0] >= 2:
        Heap[1], Heap[Heap[0]] = Heap[Heap[0]], Heap[1]
        Heap[0] -= 1
        max_heapify2(Heap, 1)
    return Heap[1:]

#Priority Queue
def heap_maximum(Heap):
    return Heap[1]

def heap_extract_max(Heap):
    if Heap[0] < 1:
        return 
    Max = Heap[1]
    Heap[1], Heap[Heap[0]] = Heap[Heap[0]], Heap[1]
    Heap[0] -= 1
    max_heapify2(Heap, 1)
    return Max

def heap_increase_key(Heap, i, key):
    if Heap[i] > key:
        return False
    
    Heap[i] = key
    while i > 1 and Heap[parent(i)] < Heap[i]:
        p = parent(i)
        Heap[i], Heap[p] = Heap[p], Heap[i]
        i = p

    return True

def max_heap_insert1(Heap, key):
    Heap[0] += 1
    if Heap[0] > len(Heap) - 1:
        Heap.append(float('-inf'))
    else:
        Heap[Heap[0]] = float('-inf')
    heap_increase_key(Heap, Heap[0], key)
    
def max_heap_insert2(Heap, key):
    Heap[0] += 1
    if Heap[0] > len(Heap) - 1:
        Heap.append(key)
    else:
        Heap[Heap[0]] = key
    i = Heap[0]
    while i > 1 and Heap[parent(i)] < Heap[i]:
        p = parent(i)
        Heap[i], Heap[p] = Heap[p], Heap[i]
        i = p
        
def max_heap_delete(Heap, i):
    Heap[i] = float('-inf')
    max_heapify2(Heap, i)
    Heap[0] -= 1
    
