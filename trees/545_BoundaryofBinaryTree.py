class Node():
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

def boundary(root):

    #no left and no right adds in the leaves thats y we have return in both dfs_l,r
    def dfs_left(node):
        if node==None or node.left==None and node.right==None:
            return
        result.append(node.value)
        if node.left!=None:
            dfs_left(node.left)
        else:
            dfs_left(node.right)

    def dfs_right(node):
        if node==None or node.left==None and node.right==None:
            return
        if node.right!=None:
            dfs_right(node.right)
        else:
            dfs_right(node.left)
        result.append(node.value)

    def dfs_leaves(node):
        if node==None:
            return
        dfs_leaves(node.left)
        if node!=None and node.left==None and node.right==None:
            result.append(node.value)
        dfs_leaves(node.right)
        

    if not root:
        return []
    result = [root.value]
    dfs_left(root.left)
    dfs_leaves(root)
    dfs_right(root.right)
    return result



    
