class Node():
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

def serialize(root):
    def re_serialize(root,string):
        if root == None:
            string = string + 'None,'
        else:
            string = string + str(root.value)+','
            string = re_serialize(root.left,string)
            string = re_serialize(root.right,string)
        return string
    return re_serialize(root,"")

def deserialize(data):
    def re_deserialize(data_list):
        if data_list[0]=="None":
            data_list.pop(0)
            return None
        root = Node(data_list[0])
        data_list.pop(0)
        root.left = re_deserialize(data_list)
        root.right = re_deserialize(data_list)
        return root
    data_list = data.split(',')
    print(data_list)
    root = re_deserialize(data_list)
    return root
    
    
tree = Node(1)
tree.left = Node(2)
tree.right = Node(5)
tree.left.left = Node(3)
tree.left.right = Node(4)

print(serialize(tree))
print(deserialize(serialize(tree)))