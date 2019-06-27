class Node:
    def __init__(self,val,left=None,right=None,next=None):
        val = self.value
        left = self.left
        right = self.right
        next = self.next

def connect(root):
    if root == None:
        return None
    if root.left!=None and root.right!=None:
        connect(root.left)
        connect(root.right)
        l = root.left
        r = root.right
        while l:
            l.next = r
            l = l.right
            r = r.left
    return root

tree = Node(3)
tree.left = Node(5)
tree.right = Node(1)
tree.right.left = Node(0)
tree.right.right = Node(8)
tree.left.left = Node(6)
tree.left.right = Node(2)
tree.left.right.left = Node(7)
tree.left.right.right = Node(4)

print(connect(tree))