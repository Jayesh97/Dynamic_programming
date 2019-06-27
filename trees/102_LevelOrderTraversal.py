class Node():
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
def level_order(root):
    if root != None:
        queue = [root]
    else:
        queue = []
    l = []
    while queue != []:
        l.append([node.value for node in queue if node!=None])
        queue = [node for i in queue for node in (i.left, i.right) if node]
    return l

tree = Node(3)
tree.left = Node(9)
tree.right = Node(20)
tree.right.left = Node(15)
tree.right.right = Node(7)
print(level_order(tree))