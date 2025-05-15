class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        self.root = self._insert(self.root,value)
    
    def _insert(self,root,value):
        if root is None:
           return Node(value)
        
        if value < root.value:
            root.left = self._insert(root.left,value)
        
        elif value > root.value:
            root.right = self._insert(root.right,value)

        return root  
    def search(self,target):
          return self._search(self.root,target)

    def _search(self,root,target):
         if root is None:
             return False
         if target == root.value:
             return True
         elif target < root.value:
             return self._search(root.left,target)
         else:
             return self._search(root.right,target)   
             
    def inorder(self,node):
       if node:
         self.inorder(node.left)
         print(node.value,end=" ")
         self.inorder(node.right)

    def preorder(self,node):
       if node:
         print(node.value,end=" ")
         self.preorder(node.left)
         self.preorder(node.right)
    
    def postorder(self,node):
       if node:  
         self.postorder(node.left)
         self.postorder(node.right)
         print(node.value,end=" ")

    def delete(self,value):
        self.root = self._delete(self.root,value)

    def _delete(self,root,value):
        if root is None:
            return root
        if value < root.value:
            root.left = self._delete(root.left,value)
        elif value>root.value:
             root.right = self._delete(root.right,value)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            min_node = self._min_value_node(root.right)
            root.value = min_node.value
            root.right = self._delete(root.right,min_node.value)

        return root

    def _min_value_node(self,node):
        current = node
        while current.left:
              current = current.left

        return current

 
  
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)
bst.inorder(bst.root)
print("\n")
# bst.preorder(bst.root)
# print("\n")
# bst.postorder(bst.root)
bst.delete(40)
bst.inorder(bst.root)


# result = bst.search(20)
# if result:
#     print("target Found")
# else:
#     print("target not found")


