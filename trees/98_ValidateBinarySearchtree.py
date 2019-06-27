class Node():
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
def validate(root,left,right):
    if not root:
        return True
    value = root.value
    if value <= left or value >= right:
        return False
    if validate(root.left,left,value)==False:
        return False
    if validate(root.right,value,right)==False:
        return False
    return True

tree = Node(5)
tree.left = Node(2)
tree.right = Node(6)
tree.left.left = Node(0)
tree.left.right = Node(7)
tree.right.left = Node(10)
print(validate(tree,-float('inf'),float('inf')))