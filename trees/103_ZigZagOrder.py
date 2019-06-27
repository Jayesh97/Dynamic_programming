class Node():
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

def zigzag(root):
    if not root:
        return []
    queue = [root]
    l = []
    level = 1
    while queue:
        temp = [node.value for node in queue if node!=None]
        queue = [node for i in queue for node in (i.left,i.right) if node]
        if level%2==0:
            l.append(temp[::-1])
        else:
            l.append(temp)
    return l
    

tree = Node(3)
tree.left = Node(9)
tree.right = Node(20)
tree.right.left = Node(15)
tree.right.right = Node(7)
print(zigzag(tree))