class Node():
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder(root):
    if root!=None:
        if root.left!=None:
            inorder(root.left)
        inorder.l.append(root.value)
        if root.right!=None:
            inorder(root.right)
    return inorder.l


tree = Node(5)
tree.left = Node(3)
tree.right = Node(6)
tree.left.left = Node(2)
tree.left.right = Node(4)
tree.right.right = Node(7)
inorder.l = []
k = 3

print(inorder(tree)[k-1])