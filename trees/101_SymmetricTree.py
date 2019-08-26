class TreeNode(object):
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
    
def ismirror(t1,t2):
    if t1==None and t2==None:
        return True
    if t1==None or t2==None:
        return False
    return t1.value==t2.value and ismirror(t1.right,t2.left) and ismirror(t1.left,t2.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(ismirror(root,root))