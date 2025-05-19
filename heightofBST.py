class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root, value):
        if root is None:
            return Node(value)
        if value < root.value:
            root.left = self._insert(root.left, value)
        else:
            root.right = self._insert(root.right, value)
        return root

    def height(self):
        
        return self._height(self.root)
    
    def _height(self,node):

        if node is None:
            return 0
        
        left_height = self._height(node.left)
        right_height = self._height(node.right)

        return 1+max(left_height,right_height)


bst = BST()
for val in [15,10,20,8,12,17,25,6]:
    bst.insert(val)

print("Height of bst (in terms of nodes):",bst.height())






