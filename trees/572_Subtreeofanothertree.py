class TreeNode():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def subtreeofanother():
    

root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


child = TreeNode(4)
child.left = TreeNode(1)
child.right = TreeNode(2)