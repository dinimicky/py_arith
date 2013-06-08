'''
Created on 2013-6-8

@author: Brilliant
'''
class Node(object):
    def __init__(self, key= None):
        self.parent=None
        self.key=key
        self.ltree=None
        self.rtree=None
      
class BinarySearchTree(object):
    def __init__(self):
        self.TreeRootNode=None
      
    def tree_insert(self, node):
        y= None
        x= self.TreeRootNode
        while x != None :
            y=x
            if node.key<y.key:
                x=y.ltree
            else:
                x=y.rtree
      
        node.parent=y
      
        if y== None:
            self.TreeRootNode=node
        elif node.key < y.key:
            y.ltree=node
        else:
            y.rtree=node
          
    def inorder_tree_walk(self):
        self.__inorder_tree_walk(self.TreeRootNode)
      
    def __inorder_tree_walk(self, node):
        if node!= None:
            self.__inorder_tree_walk(node.ltree)
            print node.key
            self.__inorder_tree_walk(node.rtree)
  
    def tree_search(self, key):
        x= self.TreeRootNode
       
        if x== None:
            return None
       
        while x != None :
            if x.key == key:
                return x
            elif key < x.key:
                x=x.ltree
            else:
                x=x.rtree
               
        return None
       

       
    def tree_search_closest(self, key):
        x= self.TreeRootNode
        Result= None
        Delta=float( "infinity")
        if x== None:
            return None
       
        while x != None :
            NewDelta=abs(key-x.key)
            if NewDelta < Delta:
                Result=x
                Delta=NewDelta
            if key < x.key:
                x=x.ltree
            elif key==x.key:
                return (0 , x)
            else:
                x=x.rtree
        return (Delta, Result, Result.key)
   
    def tree_max(self):
        x= self.TreeRootNode
        while x != None :
            x=x.rtree
           
        return x
   
    def tree_min(self):
        x= self.TreeRootNode
        while x != None :
            x=x.ltree
           
        return x
   
   
           
           

          
      
          
def test():
    tree=BinarySearchTree()
    for i in [6,7,1,2,5,4.5]:
        tree.tree_insert(Node(i))
    tree.inorder_tree_walk()
    print tree.tree_search( 1).key
    print tree.tree_search_closest( 4.9)
  
  


test()
