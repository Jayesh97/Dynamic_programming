class Node():
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
def inorder(root,l):
    if root!=None:
        if root.left!=None:
            inorder(root.left,l)
        l.append(root.value)
        if root.right!=None:
            inorder(root.right,l)
    return l

tree = Node(5)
tree.left = Node(2)
tree.right = Node(6)
tree.left.left = Node(0)
tree.right.left = Node(10)
l = []
print(inorder(tree,l))