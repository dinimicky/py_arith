'''
Created on 2013-6-22

@author: ezonghu
'''
def iSort(List = []):
    if len(List) <=1:
        return List
    
    for j in range(1, len(List)):
        key = List[j]
        i = j - 1
        while i >= 0 and List[i] > key:
            List[i + 1] = List[i]
            i -= 1
        List[i + 1] = key
        
    return List

def iSort2(List = []):
    if len(List) <=1:
        return List
    
    for j in range(1, len(List)):
        key = List[j]
        i = j - 1
        while i >= 0 and List[i] < key:
            List[i + 1] = List[i]
            i -= 1
        List[i + 1] = key
        
    return List
    
print iSort([5,3,4,2,1])
print iSort2([5,3,4,2,1])