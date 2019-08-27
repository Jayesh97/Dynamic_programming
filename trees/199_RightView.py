class TreeNode(object):
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

def rightview(root):
    #{depth-->rightmostvalue}
    rightmost_dict = {}
    max_depth = -1
    stack = [(root,0)]
    while stack:
        node,depth=stack.pop()
        if node!=None:
            max_depth=max(max_depth,depth)
            if depth not in rightmost_dict:
                rightmost_dict[depth]=node.value
            stack.append((node.right,depth+1))
            stack.append((node.left,depth+1))
    return(rightmost_dict.values())