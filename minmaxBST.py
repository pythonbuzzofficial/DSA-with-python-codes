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
    
    def find_min(self):
        current = self.root
        while current and current.left:
            current = current.left
        if current:
            return current.value
        else:
            return None
    def find_max(self):
        current = self.root
        while current and current.right:
            current = current.right
        if current:
            return current.value
        else:
            return None


bst = BST()
for val in [60,75,10,90,170,30,40]:
    bst.insert(val)

print("minimum value in BST:",bst.find_min())
print("maximum value in BST:",bst.find_max())


