class Node():
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

def serialize(root,string):
    if root == None:
        string = string + 'None,'
    else:
        string = string + str(root.value)+','
        string = serialize(root.left,string)
        string = serialize(root.right,string)
    return string

def deserialize(data):
    if data[0]=="None":
        data.pop(0)
        return None
    root = Node(data[0])
    data.pop(0)
    root.left = deserialize(data)
    root.right = deserialize(data)
    return root


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.right.left = Node(4)
tree.right.right = Node(5)

print(serialize(tree,""))