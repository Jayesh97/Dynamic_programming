class TreeNode():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def mindepth(root):
    if not root:
        return 0
    if root.left==None and root.right==None:
        return 1
    #if there is null on one of the child then we cant go that way
    depth=float("inf")#to invalidate right child which has null
    child = [root.left,root.right]
    for c in child:
        if c:
            depth=min(mindepth(c),depth)
    return depth+1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(mindepth(root))