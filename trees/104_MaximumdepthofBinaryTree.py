class TreeNode():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def maxdepth(root):
    if not root:
        return 0
    depth = max(1+maxdepth(root.left),1+maxdepth(root.right))
    return depth

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(maxdepth(root))