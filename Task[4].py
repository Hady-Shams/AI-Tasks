class Node:
    
   def __init__(self, data):    # Construvtor
      self.left = None
      self.right = None
      self.data = data

   def insert(self, data):
# Compare the new value with the parent
      if self.data:
         if data < self.data:
             if self.left is None:
                 self.left = Node(data)     # Parent
             else:
                 self.left.insert(data)     # Child
         elif data > self.data:
             if self.right is None:
                 self.right = Node(data)
             else:
                 self.right.insert(data)
      else:
         self.data = data
         
      
   # def PrintTree(self):
   #    print(self.data)
      
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

# Print from the last child in the left up to the root then go th right
root.PrintTree()
#########################################################
print('#########################################################\n')

from binarytree import build
  
nodes =[3, 6, 8, 2, 11, None, 13]
  
binary_tree = build(nodes)

print('Binary tree from list :\n', binary_tree)
  
print('\nList from binary tree :', binary_tree.values)
