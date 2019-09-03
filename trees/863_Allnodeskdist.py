from collections import deque
class TreeNode(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    

def dfs(node,par=None):
    if node:
        node.par=par
        dfs(node.left,node)
        dfs(node.right,node)
    
def distance(root,target,k):
    dfs(root)
    queue = deque([(target,0)]) #list of tuples
    seen = {target}
    while queue:
        if queue[0][1]==k:
            return [i.value for i,dist in queue]
        node,dist=queue.popleft()
        for neigh in (node.par,node.right,node.left):
            if neigh!=None and neigh not in seen:
                #print(neigh.value)
                seen.add(neigh)
                queue.append((neigh,dist+1))
    return []



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

target = root.left
k=3

print(distance(root,target,k))
