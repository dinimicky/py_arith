'''
Created on 2013-6-8

@author: Brilliant
'''
class heap(object):
    def __init__(self, A):
        A.insert( 0, None)
        self.List=A
        self.length=len(A)-1
        self.heap_len=len(A)-1
    def getList(self):
        if self.length==0:
            return None
        return self.List[1:]
    def getHeap(self):
        if self.heap_len==0:
            return None
        return self.List[1:self.heap_len+1 ]
    def setList(self, A):
        self.__init__(A)
    def left(self, i):
        return 2*i
    def right(self, i):
        return 2*i+ 1
    def parent(self, i):
        return i// 2
   
class minHeap(heap):
    def min_heapify(self, i):
        if i<= 0:
            return False
       
        l= self.left(i)
        r= self.right(i)
       
        if l<= self.heap_len and self.List[i]>self.List[l]:
            smallest=l
        else:
            smallest=i
           
        if r<= self.heap_len and self.List[r]<self.List[smallest]:
            smallest=r
           
        if smallest==i:
            return True
        else:
            tmp= self.List[i]
            self.List[i]=self .List[smallest]
            self.List[smallest]=tmp
            self.min_heapify(smallest)
           
    def build_min_heap(self):
        if self.heap_len==0:
            return None
        i= self.heap_len//2
       
        while i>= 1:
            self.min_heapify(i)
            i-= 1
           
    def sort(self):
        if self.heap_len <= 1:
            return
        mini = self.List[1]
        self.List[1 ]=self.List[ self.heap_len]
        self.List[self.heap_len]=mini
        self.heap_len-=1
        self.min_heapify(1 )
        self.sort()
       
class maxHeap(heap):
    def max_heapify(self, i):
        if i <= 0:
            return False
        l= self.left(i)
        r= self.right(i)
        if l <= self.heap_len and self.List[l] >= self.List[i]:
            largest=l
        else:
            largest=i
           
        if r <= self.heap_len and self.List[r] >= self.List[largest]:
            largest=r
           
        if largest == i:
            return True
        else:
            tmp= self.List[largest]
            self.List[largest]=self .List[i]
            self.List[i]=tmp
            return self.max_heapify(largest)

    def build_max_heap(self):
        if self.heap_len==0:
            return None
       
        i= self.heap_len//2
        while i >= 1:
            self.max_heapify(i)
            i-= 1
   
    def sort(self):
        if self.heap_len<=1:
            return
       
        largest = self.List[1]
        self.List[1 ]=self.List[ self.heap_len]
        self.List[self.heap_len]=largest
        self.heap_len-=1
        self.max_heapify(1 )
        self.sort()


class minPriorityQueue(minHeap):
    def heap_minimum(self):
        return self.List[1]
   
    def heap_extract_min(self):
        if self.heap_len<1:
            return None
       
        Result= self.List[1]
       
        self.List[1 ]=self.List[ self.heap_len]
        self.List[self.heap_len]=float( "+infinity")
        self.heap_len-=1
        self.min_heapify(1 )
        return Result
   
    def decrease_key(self, i, k):
        if i<= 0:
            return False
        if self.List[i]>k:
            return False
       
        self.List[i]=k
        while i> 1 and self.List[self .parent(i)]>self.List[i]:
            tmp= self.List[i]
            self.List[i]=self .List[self.parent(i)]
            self.List[self .parent(i)]=tmp
            i= self.parent(i)
           
        return True
       
    def insert(self, x):
        self.heap_len+=1
        self.List[self.heap_len]=float( "+infinity")
        self.decrease_key( self.heap_len, x)

class maxPriorityQueue(maxHeap):
    def heap_maximum(self):
        return self.List[1]
    def heap_extract_max(self):
        if self.heap_len < 1:
            return None
       
        Result= self.List[1]
       
        self.List[1 ]=self.List[ self.heap_len]
        self.List[self.heap_len]=float( "-infinity")
        self.heap_len-=1
        self.max_heapify(1 )
        return Result
    def increase_key(self, i, k):
        if i<= 0:
            return False
        if k< self.List[i]:
            return False
       
        self.List[i]=k
        while i> 1 and self.List[self .parent(i)]<self.List[i]:
            tmp= self.List[i]
            self.List[i]=self .List[self.parent(i)]
            self.List[self .parent(i)]=tmp
            i= self.parent(i)
        return True
       
        self.max_heapify(i)
    def insert(self, x):
        self.heap_len+=1
        self.List[self.heap_len]=float( "-infinity")
        self.increase_key(self.heap_len, x)


def test():
    print "========================================="
    A=minHeap([5,4,3,2,1])
    A.build_min_heap()
    A.sort()
    print A.getList()
    A=maxHeap([1,2,3,4,5])
    A.build_max_heap()
    A.sort()
    print A.getList()

    A=minHeap([5])
    A.build_min_heap()
    A.sort()
    print A.getList()
    A=maxHeap([1])
    A.build_max_heap()
    A.sort()
    print A.getList()

    A=minHeap([])
    A.build_min_heap()
    A.sort()
    print A.getList()
    A=maxHeap([])
    A.build_max_heap()
    A.sort()
    print A.getList()   
   
    A=maxPriorityQueue([ 1, 3, 4, 5, 6, 7])
    A.build_max_heap()
    print A.getList()
    A.increase_key(5, 9)
    print A.getList()
    print A.heap_extract_max()
    print A.getList()
    print A.List
    print "========================================="
   

test()
  
