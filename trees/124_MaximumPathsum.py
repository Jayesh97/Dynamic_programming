# maxValue is the value which recording whether this current root is the final root, so we use left + right + node.val.
# But to the upper layer(after return statement), we cannot choose both left and right brunches, 
# so we need to select the larger one, so we use max(left, right) + node.val to prune the lower brunch

class TreeNode():
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder(root,l):
    if root.left != None:
        inorder(root.left,l)
    l.append(root.value)
    if root.right != None:
        inorder(root.right,l)

def maxpath(root):
    def helper(root):
        if root==None:
            return 0
        left = max(helper(root.left),0)
        right = max(helper(root.right),0)
        helper.maxx = max(helper.maxx,root.value+left+right)
        return root.value + max(left,right)
    helper.maxx = -float('inf')
    helper(root)
    return helper.maxx

tree = TreeNode(-10)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

print(maxpath(tree))