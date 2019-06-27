class Node():
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
def lca(root,p,q):
    stack = [root]
    parent = {root:None}
    while p not in parent or q not in parent:
        node = stack.pop()
        if node.left!=None:
            parent[node.left]=node
            stack.append(node.left)
        if node.right!=None:
            parent[node.right]=node
            stack.append(node.right)
    ancestors = set()
    while p!=None:
        ancestors.add(p)
        p = parent[p]
    while q not in ancestors:
        q = parent[q]
    return q

tree = Node(3)
tree.left = Node(5)
tree.right = Node(1)
tree.right.left = Node(0)
tree.right.right = Node(8)
tree.left.left = Node(6)
tree.left.right = Node(2)
tree.left.right.left = Node(7)
tree.left.right.right = Node(4)

print(lca(tree,tree.left.left,tree.left.right))