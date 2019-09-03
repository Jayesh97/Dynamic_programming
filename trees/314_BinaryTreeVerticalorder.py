class TreeNode():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def verticalorder(root):
    res = {}
    queue = [(root,0)]
    for node,depth in queue:
        if node:
            res[depth]=res.get(depth,[])+[node.value]
            queue.append((node.left,depth-1))
            queue.append((node.right,depth+1))
    return [res[i] for i in sorted(res.keys())]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(verticalorder(root))
