'''
Created on 2014-4-16

@author: ezonghu
'''  
class Node(object):
    def __init__(self, Name, Attr):
        self.name = Name
        self.attr = Attr
        self.children = []
        

        


def setNodeTree(Parent, Nodes):
    if len(Nodes) == 1:
        for child in Parent.children:
            if Nodes[0] == child.name and child.attr == "d":
                return 0
        n = Node(Nodes[0], "d")
        Parent.children.append(n)
        return 1
    
    for child in Parent.children:
        if Nodes[0] == child.name and child.attr == "d":
            return setNodeTree(child, Nodes[1:])
    n = Node(Nodes[0], "d")
    Parent.children.append(n)
    return setNodeTree(n, Nodes[1:])+1

f=open('C:\Users\ezonghu\Downloads\A-large-practice.in')

first_line = f.readline()
Cases = int(first_line)
CaseId = 0
Line=0

for l in f:

    [N, M] = [int(i) for i in l.split()]
    root = Node("/", "d")
    for i in range(N):
        for l in f:
            setNodeTree(root, l.strip().split("/")[1:])
            break
    res = 0    
    for i in range(M):
        for l in f:
            res += setNodeTree(root, l.strip().split("/")[1:])
            break        
    CaseId += 1
    
    print "Case #%d: %d" % (CaseId, res)
    if Cases == CaseId:
        break
f.close()
    

    
        
            